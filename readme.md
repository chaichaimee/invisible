# Invisible

**Hide or swap any words on websites — skip the repetitive, cut the clutter, keep only what matters**

![NVDA Add-on](https://img.shields.io/badge/NVDA-Add--on-blue?logo=nvaccess)
![License](https://img.shields.io/github/license/chaichaimee/invisible)
![Version](https://img.shields.io/github/v/release/chaichaimee/invisible?label=latest)

**Author:** chai chaimee  
**Repository:** https://github.com/chaichaimee/invisible

---

Invisible lets you **silence** or **replace** any word, phrase, or pattern that NVDA would normally speak — without changing the web page itself.  
Perfect for skipping ads, repetitive text, spoilers, profanity, or anything that distracts you.

### Features

- Completely hide words (NVDA simply skips them)  
- Replace words with custom text (e.g. "Advertisement"  "skip")  
- Clean up profanity (e.g. "fuck"  "\*\*\*")  
- Rules apply to a **single page** or an **entire domain**  
- Full **regular expression (regex)** support for advanced users  
- Each website has its own independent settings  
- Settings saved as simple `.json` files — easy to share or backup

### How to Use

1. Go to the web page you want to clean up.  
2. Press **`NVDA+Shift+W`**  the Invisible settings dialog opens.  
3. The current URL is detected automatically.  
4. Give the site a friendly name (e.g. `YouTube`, `News Site`).  
5. Choose the scope:  
   - **Single page only** – rules apply only to this exact URL  
   - **Whole website (domain)** – rules apply to every page on the same domain  
6. In the **Entries** section:  
   - Type the text you want to affect in **Pattern**  
   - (Optional) Type the replacement text in **Replacement**  
     - Leave blank  the text is silenced completely  
   - Tick **"Use as regular expression"** only if you know regex  
   - Click **Add** (or **Update** when editing)  
7. Click **OK** or **Close** — changes take effect immediately.

### Examples

| Pattern                 | Replacement | Regex? | Result when NVDA reads                     |
|-------------------------|-------------|--------|--------------------------------------------|
| Advertisement           | (blank)     | No     | Skipped completely                         |
| Sponsored               | skip        | No     | Says "skip" instead                        |
| [AD]                    | (blank)     | No     | Removed                                    |
| fuck                    | ***         | No     | Says "\*\*\*"                               |
| `^\d+ comments?$`       | (blank)     | Yes    | Removes "5 comments", "42 comments", etc.  |

### Where Settings Are Saved

Each site has its own small `.json` file located in:  
`%appdata%\nvda\invisible\`  
(or your portable NVDA config folder)

You can copy these files to share your rules with friends or back them up easily.

### Keyboard Shortcut

**`NVDA+Shift+W`** – Open Invisible settings from any web page.

### Important Notes

- Only affects **what NVDA speaks** — the actual web page remains unchanged.  
- Works with **Firefox**, **Chrome**, **Edge**, and any browser supported by NVDA.

---

**Enjoy a cleaner, quieter browsing experience!**

?? Made for the NVDA community – free and open source.
