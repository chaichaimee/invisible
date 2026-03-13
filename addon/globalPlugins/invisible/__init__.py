# __init__.py
# Copyright (C) 2026 Chai Chaimee
# Licensed under GNU General Public License. See COPYING.txt for details.

import addonHandler
import globalPluginHandler
import api
import ui
import time
import wx
import re
import speech
from scriptHandler import script
from logHandler import log
import gui as nvdaGui
from .manager import InvisibleConfig
from .gui import MainDialog, AddSiteDialog

addonHandler.initTranslation()

DOUBLE_TAP_THRESHOLD = 0.4

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Invisible")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.config = InvisibleConfig()
		self._last_tap_time = 0
		self._tap_count = 0

		# Store the original processText function
		if hasattr(speech, "speech"):
			self.original_process_text = speech.speech.processText
			speech.speech.processText = self.process_text
		else:
			self.original_process_text = speech.processText
			speech.processText = self.process_text

	def terminate(self):
		"""Clean up when addon is terminated"""
		if hasattr(speech, "speech"):
			speech.speech.processText = self.original_process_text
		else:
			speech.processText = self.original_process_text

	def process_text(self, locale, text, symbolLevel=None, **kwargs):
		"""Process text to skip/replace words for current URL.
		Any error is logged and the original text is returned unchanged.
		"""
		result_text = text  # start with original
		try:
			current_url = self.get_current_url()
			if current_url:
				site_data = self.config.get_site_by_url(current_url)
				if site_data:
					words_data = site_data.get("words", [])
					literal_entries = []   # (value, replacement)
					regex_patterns = []    # (pattern, replacement)

					for word_data in words_data:
						value = word_data.get("value")
						is_regex = word_data.get("is_regex", False)
						replacement = word_data.get("replacement", "")
						if value:
							if is_regex:
								regex_patterns.append((value, replacement))
							else:
								literal_entries.append((value, replacement))

					# Literal replacements (longest first)
					literal_entries_sorted = sorted(literal_entries, key=lambda x: len(x[0]), reverse=True)
					for word, repl in literal_entries_sorted:
						result_text = result_text.replace(word, repl)

					for pattern, repl in regex_patterns:
						try:
							result_text = re.sub(pattern, repl, result_text)
						except re.error as e:
							log.error(f"Invalid regex pattern skipped: '{pattern}'. Error: {e}")
		except Exception as e:
			log.error(f"Invisible addon: unexpected error in process_text: {e}", exc_info=True)

		# Always call the original speech function with the (possibly modified) text
		return self.original_process_text(locale, result_text, symbolLevel, **kwargs)

	def get_current_url(self):
		"""Get current URL from focused browser"""
		try:
			focus = api.getFocusObject()
			if hasattr(focus, 'treeInterceptor') and focus.treeInterceptor is not None:
				ti = focus.treeInterceptor
				if hasattr(ti, 'documentConstantIdentifier'):
					url = ti.documentConstantIdentifier
					if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
						return url
			if hasattr(focus, 'IAccessibleObject'):
				try:
					url = focus.IAccessibleObject.accValue(0)
					if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
						return url
				except:
					pass
			if hasattr(focus, 'UIAElement'):
				try:
					url = focus.UIAElement.CurrentValue
					if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
						return url
				except:
					pass
			if hasattr(focus, 'windowText'):
				window_text = focus.windowText
				url_pattern = r'https?://[^\s]+|file:///[^\s]+'
				match = re.search(url_pattern, window_text)
				if match:
					return match.group(0)
			return None
		except Exception as e:
			log.debug(f"Error getting current URL: {e}")
			return None

	@script(
		description=_("Open Invisible settings (single tap) or Add new site (double tap)"),
		gesture="kb:NVDA+shift+W",
		category=_("Invisible")
	)
	def script_openSettings(self, gesture):
		current_time = time.time()
		if current_time - self._last_tap_time > DOUBLE_TAP_THRESHOLD:
			self._tap_count = 0
		self._tap_count += 1
		self._last_tap_time = current_time

		def execute_action():
			if self._tap_count == 1:
				# Single tap: open main dialog
				current_url = self.get_current_url()
				nvdaGui.mainFrame.popupSettingsDialog(MainDialog, current_url, self.config)
			elif self._tap_count >= 2:
				# Double tap: open Add Site dialog with current URL pre‑filled
				current_url = self.get_current_url()
				if not current_url:
					ui.message(_("Cannot capture URL. Make sure you are in a browser."))
				else:
					nvdaGui.mainFrame.popupSettingsDialog(AddSiteDialog, self.config, current_url)
			self._tap_count = 0

		wx.CallLater(int(DOUBLE_TAP_THRESHOLD * 1000), execute_action)