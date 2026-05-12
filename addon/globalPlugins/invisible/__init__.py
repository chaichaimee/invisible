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
		self._pending_action = None
		self._cached_url = None
		self._cache_time = 0

		self._patch_speech_processor()

	def _patch_speech_processor(self):
		"""Patch speech processing with fallback for NVDA 2025/2026."""
		try:
			import speech
			self.original_process_text = None
			self._patch_target = None
			self._patch_name = None

			# NVDA 2025.x
			if hasattr(speech, 'speech') and hasattr(speech.speech, 'processText'):
				self.original_process_text = speech.speech.processText
				speech.speech.processText = self.process_text
				self._patch_target = speech.speech
				self._patch_name = 'processText'
			elif hasattr(speech, 'processText'):
				self.original_process_text = speech.processText
				speech.processText = self.process_text
				self._patch_target = speech
				self._patch_name = 'processText'
			# NVDA 2026.x (beta)
			elif hasattr(speech, '_processText'):
				self.original_process_text = speech._processText
				speech._processText = self.process_text
				self._patch_target = speech
				self._patch_name = '_processText'
			else:
				log.error("Invisible: Cannot locate speech processing function")
		except Exception as e:
			log.error(f"Invisible: Speech patch failed: {e}")

	def terminate(self):
		"""Restore original speech processor."""
		if self._patch_target and self._patch_name and self.original_process_text:
			try:
				setattr(self._patch_target, self._patch_name, self.original_process_text)
			except Exception as e:
				log.error(f"Invisible: Failed to restore speech processor: {e}")

	def process_text(self, *args, **kwargs):
		"""Intercept and modify speech text before speaking."""
		# Locate the text argument
		text_arg = None
		if len(args) >= 2:
			text_arg = args[1]
		elif 'text' in kwargs:
			text_arg = kwargs['text']
		elif len(args) >= 1 and isinstance(args[0], str):
			# Some NVDA versions pass text as first argument
			text_arg = args[0]

		if text_arg and isinstance(text_arg, str):
			modified_text = self._apply_word_replacements(text_arg)
			# Replace text in the original call signature
			if len(args) >= 2:
				args_list = list(args)
				args_list[1] = modified_text
				args = tuple(args_list)
			elif 'text' in kwargs:
				kwargs['text'] = modified_text
			elif len(args) >= 1 and isinstance(args[0], str):
				args_list = list(args)
				args_list[0] = modified_text
				args = tuple(args_list)

		try:
			if self.original_process_text:
				return self.original_process_text(*args, **kwargs)
			else:
				# Fallback: call default speech (should not happen)
				return None
		except Exception as e:
			log.error(f"Invisible: Error in original speech processor: {e}")
			# Still try to speak original text to avoid complete silence
			if self.original_process_text:
				return self.original_process_text(*args, **kwargs)
			return None

	def _apply_word_replacements(self, text):
		"""Apply literal and regex replacements with timeout protection."""
		if not text or len(text) > 20000:  # Skip extremely long text for performance
			return text

		try:
			current_url = self.get_current_url()
			if not current_url:
				return text

			site_data = self.config.get_site_by_url(current_url)
			if not site_data:
				return text

			words_data = site_data.get("words", [])
			if not words_data:
				return text

			result_text = text

			# Separate literal and regex entries
			literal_entries = []
			regex_patterns = []
			for word_data in words_data:
				value = word_data.get("value")
				is_regex = word_data.get("is_regex", False)
				replacement = word_data.get("replacement", "")
				if value:
					if is_regex:
						regex_patterns.append((value, replacement))
					else:
						literal_entries.append((value, replacement))

			# Literal replacements (longest first) - unlimited count
			if literal_entries:
				literal_entries_sorted = sorted(literal_entries, key=lambda x: len(x[0]), reverse=True)
				for word, repl in literal_entries_sorted:
					result_text = result_text.replace(word, repl)

			# Regex replacements with per-pattern timeout (max 0.3 seconds each)
			for pattern, repl in regex_patterns:
				try:
					start_time = time.time()
					result_text = re.sub(pattern, repl, result_text)
					elapsed = time.time() - start_time
					if elapsed > 0.3:
						log.warning(f"Invisible: Slow regex pattern ({elapsed:.2f}s): {pattern[:50]}")
				except re.error as e:
					log.error(f"Invisible: Invalid regex skipped: {pattern[:50]} - {e}")
				except Exception as e:
					log.error(f"Invisible: Regex execution error: {e}")

			return result_text

		except Exception as e:
			log.error(f"Invisible: Error in word replacements: {e}", exc_info=True)
			return text

	def get_current_url(self):
		"""Get current URL from focused browser with timeout/crash protection."""
		# Use cached URL for 0.2 seconds to reduce repeated calls
		current_time = time.time()
		if hasattr(self, '_cached_url') and self._cached_url:
			if current_time - self._cache_time < 0.2:
				return self._cached_url

		try:
			focus = api.getFocusObject()
			if not focus:
				return None

			url = None

			# 1. TreeInterceptor (safest)
			try:
				if hasattr(focus, 'treeInterceptor') and focus.treeInterceptor is not None:
					ti = focus.treeInterceptor
					if hasattr(ti, 'documentConstantIdentifier'):
						url = ti.documentConstantIdentifier
						if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
							self._cached_url = url
							self._cache_time = current_time
							return url
			except Exception:
				pass

			# 2. UIA Element (moderately safe)
			try:
				if hasattr(focus, 'UIAElement'):
					url = focus.UIAElement.CurrentValue
					if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
						self._cached_url = url
						self._cache_time = current_time
						return url
			except Exception:
				pass

			# 3. IAccessible accValue (can be slow but usually safe)
			try:
				if hasattr(focus, 'IAccessibleObject'):
					url = focus.IAccessibleObject.accValue(0)
					if url and (url.startswith('http') or url.startswith('https') or url.startswith('file')):
						self._cached_url = url
						self._cache_time = current_time
						return url
			except Exception:
				pass

			# 4. Window text (most dangerous, use last resort with extra try/except)
			try:
				if hasattr(focus, 'windowText'):
					window_text = focus.windowText
					if window_text:
						url_pattern = r'https?://[^\s]+|file:///[^\s]+'
						match = re.search(url_pattern, window_text)
						if match:
							url = match.group(0)
							self._cached_url = url
							self._cache_time = current_time
							return url
			except Exception:
				pass

			return None

		except Exception as e:
			log.debug(f"Invisible: Error getting URL: {e}")
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

		# Cancel any pending execution to prevent multiple dialogs
		if self._pending_action:
			try:
				self._pending_action.Stop()
			except Exception:
				pass
			self._pending_action = None

		def execute_action():
			try:
				if self._tap_count == 1:
					current_url = self.get_current_url()
					nvdaGui.mainFrame.popupSettingsDialog(MainDialog, current_url, self.config)
				elif self._tap_count >= 2:
					current_url = self.get_current_url()
					if not current_url:
						ui.message(_("Cannot capture URL. Make sure you are in a browser."))
					else:
						nvdaGui.mainFrame.popupSettingsDialog(AddSiteDialog, self.config, current_url)
			except Exception as e:
				log.error(f"Invisible: Error in settings dialog: {e}")
			finally:
				self._tap_count = 0
				self._pending_action = None

		self._pending_action = wx.CallLater(int(DOUBLE_TAP_THRESHOLD * 1000), execute_action)