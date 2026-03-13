<div align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</div>

# Invisible

*Silence the clutter. Shape the voice. Own your browsing experience.*

**Author:** Chai Chaimee  
**Repository:** [github.com/chaichaimee/invisible](https://github.com/chaichaimee/invisible)

---

## Why settle for noisy web pages?

Modern websites are full of repetition, sponsorship labels, cookie notices, comment counts, sidebars, and auto-generated fluff that screen readers must read aloud — again and again.

**Invisible** gives you back control.

Decide exactly which words, phrases or patterns NVDA should skip entirely — or quietly replace with something shorter, cleaner, or completely silent.

This is not just filtering. This is **personal audio curation** for the web.

## Powerful yet elegantly simple

- Hide text completely — NVDA acts as if it never existed
- Replace annoying labels with short placeholders (“Sponsored · Advertisement” → “skip”)
- Apply rules to one page, an entire domain, or complex URL patterns (regex)
- Full regular expression support for surgical precision
- Instant effect — no page reload needed
- Context-sensitive interface: double-tap gesture opens “Add Site” with current URL pre-filled
- Right-click + Delete key support for fast management
- Portable per-site .json files — easy to backup or share

## Get started in under 30 seconds

1. Go to any page where NVDA reads something you want to silence or change.

2. Press **NVDA + Shift + W**  
   - Single tap → opens main management window  
   - Double tap (quickly) → opens “Add New Site” dialog with current URL already filled in

3. In the **Add Site** dialog:  
   - Keep or edit the display name  
   - Choose scope:  
     - Single page only  
     - Whole website (domain)  
     - Regular expression (advanced URL matching)  
   - Click **Save**

4. Now you’re inside the site’s rule manager:  
   - Type the pattern you want to target  
   - Enter replacement text — or leave blank for complete silence  
   - Tick “Use as regular expression” when needed  
   - Click **Add** (or **Update** when editing)  
   Changes apply instantly — go back to browsing and listen.

You can return anytime with **NVDA+Shift+W** (single tap) to edit, add more rules, remove entries, or switch between sites.

## Real-world examples that save time every day

| Target Pattern              | Replacement   | Regex? | What you hear instead          |
|-----------------------------|---------------|--------|--------------------------------|
| Advertisement               | (blank)       | No     | — completely skipped —         |
| Sponsored                   | skip          | No     | “skip”                         |
| · [0-9,]+ comments?         | (blank)       | Yes    | — no comment counts —          |
| Breaking News:              | News:         | No     | Shorter & cleaner              |
| ^Cookie notice.*accept      | (blank)       | Yes    | Banner text silenced           |

## Pro tips for power users

- Right-click any site or entry → context menu with Edit / Remove
- Press **Delete** key on selected item for instant removal
- Use literal longest-first matching → avoids partial word problems
- Import rules from another .json file directly into any site
- Regex mode supports replacement groups — very powerful for dynamic content

## Support the project

If Invisible has improved your daily browsing experience, consider supporting its continued development.

[**Donate via GitHub Sponsors**](https://github.com/chaichaimee)

---

© 2026 Chai Chaimee · Invisible NVDA Add-on · Released under GNU GPL v2+