# manager.py

import os
import json
import re
import shutil
import globalVars
import addonHandler
from logHandler import log

addonHandler.initTranslation()

WORD_VALUE = "value"
WORD_IS_REGEX = "is_regex"
WORD_REPLACEMENT = "replacement"

class InvisibleConfig:
	"""Configuration manager for invisible addon with per-site JSON files"""

	def __init__(self):
		self.sites = {}
		self.config_dir = os.path.join(globalVars.appArgs.configPath, "ChaiChaimee", "invisible")
		self._ensure_config_dir()
		self._migrate_old_config()
		self._load_all_sites()

	def _ensure_config_dir(self):
		if not os.path.exists(self.config_dir):
			os.makedirs(self.config_dir)

	def _get_unique_backup_path(self, directory, base_name):
		counter = 1
		path = os.path.join(directory, base_name)
		while os.path.exists(path):
			path = os.path.join(directory, f"{base_name}_{counter}")
			counter += 1
		return path

	def _migrate_old_config(self):
		old_dir = os.path.join(globalVars.appArgs.configPath, "invisible")
		if os.path.exists(old_dir) and os.path.isdir(old_dir) and old_dir != self.config_dir:
			base_chai_dir = os.path.join(globalVars.appArgs.configPath, "ChaiChaimee")
			if not os.path.exists(base_chai_dir):
				os.makedirs(base_chai_dir)

			if os.path.exists(self.config_dir):
				try:
					if not os.listdir(self.config_dir):
						os.rmdir(self.config_dir)
						log.info("Invisible addon: Removed empty destination folder before migration.")
					else:
						backup_dir = self._get_unique_backup_path(base_chai_dir, "invisible_old")
						shutil.move(self.config_dir, backup_dir)
						log.info(f"Invisible addon: Existing non-empty config folder moved to backup: {backup_dir}")
				except Exception as e:
					log.error(f"Invisible addon: Error handling existing destination folder: {e}")
					return

			try:
				shutil.move(old_dir, self.config_dir)
				log.info("Invisible addon: Migrated entire 'invisible' folder to new location.")
			except Exception as e:
				log.error(f"Invisible addon: Error migrating old folder: {e}")
				return

			try:
				for item in os.listdir(self.config_dir):
					if not item.endswith('.json'):
						file_path = os.path.join(self.config_dir, item)
						if os.path.isfile(file_path):
							os.remove(file_path)
							log.info(f"Invisible addon: Removed unwanted file during migration: {item}")
			except Exception as e:
				log.error(f"Invisible addon: Error cleaning up migrated folder: {e}")

	def _safe_filename(self, name):
		name = re.sub(r'[\\/*?:"<>|]', "_", name)
		if len(name) > 100:
			name = name[:100]
		return name + ".json"

	def _load_all_sites(self):
		self.sites = {}
		try:
			if os.path.exists(self.config_dir):
				for filename in os.listdir(self.config_dir):
					if filename.endswith('.json'):
						filepath = os.path.join(self.config_dir, filename)
						try:
							with open(filepath, 'r', encoding='utf-8') as f:
								site_data = json.load(f)
								if "url" in site_data and "display_name" in site_data:
									words = site_data.get("words", [])
									for i, word_data in enumerate(words):
										if isinstance(word_data, str):
											words[i] = {WORD_VALUE: word_data, WORD_IS_REGEX: False, WORD_REPLACEMENT: ""}
										elif isinstance(word_data, dict):
											if WORD_REPLACEMENT not in word_data:
												word_data[WORD_REPLACEMENT] = ""
									if "mode" not in site_data:
										site_data["mode"] = "single"
									site_id = site_data["display_name"]
									self.sites[site_id] = site_data
						except Exception as e:
							log.error(f"Error loading site config {filename}: {e}")
		except Exception as e:
			log.error(f"Error reading config directory: {e}")

	def _save_site(self, site_id):
		if site_id in self.sites:
			site_data = self.sites[site_id]
			filename = self._safe_filename(site_id)
			filepath = os.path.join(self.config_dir, filename)
			try:
				with open(filepath, 'w', encoding='utf-8') as f:
					json.dump(site_data, f, ensure_ascii=False, indent=2)
				return True
			except Exception as e:
				log.error(f"Error saving site config {site_id}: {e}")
				return False
		return False

	def _delete_site_file(self, site_id):
		if site_id in self.sites:
			filename = self._safe_filename(site_id)
			filepath = os.path.join(self.config_dir, filename)
			try:
				if os.path.exists(filepath):
					os.remove(filepath)
					return True
			except Exception as e:
				log.error(f"Error deleting site config {site_id}: {e}")
		return False

	def _extract_domain(self, url):
		try:
			if "://" in url:
				url = url.split("://", 1)[1]
			domain = url.split("/")[0]
			domain = domain.split(":")[0]
			return domain.lower()
		except:
			return None

	def _extract_base_domain(self, domain):
		if not domain:
			return None
		parts = domain.split('.')
		if len(parts) >= 2:
			return '.'.join(parts[-2:])
		return domain

	def get_site_by_url(self, url):
		if not url:
			return None
		domain = self._extract_domain(url)
		for site_data in self.sites.values():
			site_url = site_data.get("url", "")
			mode = site_data.get("mode", "single")
			if mode == "single" and url == site_url:
				return site_data
			elif mode == "whole":
				current_base = self._extract_base_domain(domain) if domain else None
				site_base = self._extract_base_domain(self._extract_domain(site_url))
				if current_base and site_base and current_base == site_base:
					return site_data
			elif mode == "prefix":
				norm_site_url = site_url.rstrip('/')
				if url.lower().startswith(norm_site_url.lower()):
					return site_data
			elif mode == "regex":
				try:
					if re.match(site_url, url):
						return site_data
				except re.error:
					continue
		return None

	def get_site_by_id(self, site_id):
		return self.sites.get(site_id)

	def add_site(self, url, display_name, mode="single"):
		if not url or not display_name:
			return False
		if display_name in self.sites:
			counter = 1
			while f"{display_name} ({counter})" in self.sites:
				counter += 1
			display_name = f"{display_name} ({counter})"
		site_data = {
			"url": url,
			"display_name": display_name,
			"mode": mode,
			"words": []
		}
		self.sites[display_name] = site_data
		return self._save_site(display_name)

	def update_site(self, old_site_id, new_display_name=None, new_url=None, new_mode=None):
		if old_site_id not in self.sites:
			return False
		site_data = self.sites[old_site_id]
		changed = False
		if new_display_name and new_display_name != old_site_id:
			if new_display_name in self.sites and new_display_name != old_site_id:
				return False
			self.sites[new_display_name] = site_data
			del self.sites[old_site_id]
			site_data["display_name"] = new_display_name
			old_site_id = new_display_name
			changed = True
		if new_url and new_url != site_data.get("url"):
			site_data["url"] = new_url
			changed = True
		if new_mode and new_mode != site_data.get("mode"):
			site_data["mode"] = new_mode
			changed = True
		if changed:
			if new_display_name and new_display_name != old_site_id:
				self._delete_site_file(old_site_id)
			return self._save_site(old_site_id)
		return True

	def remove_site(self, site_id):
		if site_id in self.sites:
			if self._delete_site_file(site_id):
				del self.sites[site_id]
				return True
		return False

	def _get_display_word(self, word_data):
		value = word_data.get(WORD_VALUE, "")
		is_regex = word_data.get(WORD_IS_REGEX, False)
		replacement = word_data.get(WORD_REPLACEMENT, "")
		if is_regex:
			if replacement:
				return f"{value} -> {replacement} [{_('Regex')}]"
			else:
				return f"{value} [{_('Regex')}]"
		else:
			if replacement:
				return f"{value} -> {replacement}"
			else:
				return value

	def get_words_for_site(self, site_id):
		site_data = self.get_site_by_id(site_id)
		if site_data:
			return site_data.get("words", [])
		return []

	def add_word(self, site_id, word, is_regex, replacement=""):
		if site_id not in self.sites:
			raise ValueError(_("Site not found"))
		new_word_data = {WORD_VALUE: word, WORD_IS_REGEX: is_regex, WORD_REPLACEMENT: replacement}
		words_list = self.sites[site_id]["words"]
		if any(d[WORD_VALUE] == word and d[WORD_IS_REGEX] == is_regex for d in words_list):
			raise ValueError(_("This pattern/regex combination already exists"))
		words_list.append(new_word_data)
		words_list.sort(key=lambda x: x[WORD_VALUE].lower())
		if not self._save_site(site_id):
			raise ValueError(_("Failed to save configuration (permission or disk error)"))
		return True

	def update_word(self, site_id, old_word_data, new_word, new_is_regex, new_replacement=""):
		if site_id not in self.sites:
			raise ValueError(_("Site not found"))
		words_list = self.sites[site_id]["words"]
		index = -1
		for i, d in enumerate(words_list):
			if d[WORD_VALUE] == old_word_data[WORD_VALUE] and d[WORD_IS_REGEX] == old_word_data[WORD_IS_REGEX]:
				index = i
				break
		if index == -1:
			raise ValueError(_("Original entry not found"))
		for i, d in enumerate(words_list):
			if i != index and d[WORD_VALUE] == new_word and d[WORD_IS_REGEX] == new_is_regex:
				raise ValueError(_("This pattern/regex combination already exists"))
		new_word_data = {WORD_VALUE: new_word, WORD_IS_REGEX: new_is_regex, WORD_REPLACEMENT: new_replacement}
		words_list[index] = new_word_data
		words_list.sort(key=lambda x: x[WORD_VALUE].lower())
		if not self._save_site(site_id):
			raise ValueError(_("Failed to save configuration (permission or disk error)"))
		return True

	def remove_word(self, site_id, word_data):
		if site_id in self.sites:
			words_list = self.sites[site_id]["words"]
			try:
				words_list.remove(word_data)
				return self._save_site(site_id)
			except ValueError:
				log.error("Invisible Config: Word data not found for removal.")
		return False

	def get_all_sites(self):
		result = []
		for site_id, site_data in self.sites.items():
			result.append((site_id, site_data.get("display_name", site_id)))
		result.sort(key=lambda x: x[1].lower())
		return result