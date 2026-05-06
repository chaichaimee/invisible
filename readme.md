<p align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</p>

# Invisible

<p align="center"><i>Silence the clutter. Shape the voice. Own your browsing experience.</i></p>

<p align="center">
  <strong>Author:</strong> Chai Chaimee<br>
  <strong>Repository:</strong> <a href="https://github.com/chaichaimee/invisible">github.com/chaichaimee/invisible</a>
</p>

---

## Why settle for noisy web pages?

Modern websites are full of repetition, sponsorship labels, cookie notices, comment counts, sidebars, and auto-generated fluff that screen readers must read aloud — again and again.

**Invisible** gives you back control.

Decide exactly which words, phrases or patterns NVDA should skip entirely — or quietly replace with something shorter, cleaner, or completely silent.

<br><br>

This is not just filtering. This is **personal audio curation** for the web.

## Powerful yet elegantly simple

*   Hide text completely — NVDA acts as if it never existed
*   Replace annoying labels with short placeholders (“Sponsored · Advertisement” → “skip”)
*   Apply rules to one page, an entire domain, or complex URL patterns (regex)
*   Full regular expression support for surgical precision
*   Instant effect — no page reload needed
*   Context-sensitive interface: double-tap gesture opens “Add Site” with current URL pre-filled
*   Right-click + Delete key support for fast management
*   Portable per-site .json files — easy to backup or share

## Get started in under 30 seconds

1.  Go to any page where NVDA reads something you want to silence or change.

2.  Press **NVDA + Shift + W**<br><br>
    → Single tap → opens main management window<br>
    → Double tap (quickly) → opens “Add New Site” dialog with current URL already filled in

3.  In the **Add Site** dialog:<br><br>
    • Keep or edit the display name<br>
    • Choose scope:<br>
    &nbsp;&nbsp;– Single page only<br>
    &nbsp;&nbsp;– Whole website (domain)<br>
    &nbsp;&nbsp;– Regular expression (advanced URL matching)<br><br>
    Click **Save**

4.  Now you’re inside the site’s rule manager:<br><br>
    • Type the pattern you want to target<br>
    • Enter replacement text — or leave blank for complete silence<br>
    • Tick “Use as regular expression” when needed<br>
    • Click **Add** (or **Update** when editing)<br><br>
    Changes apply instantly — go back to browsing and listen.

<br>

You can return anytime with **NVDA+Shift+W** (single tap) to edit, add more rules, remove entries, or switch between sites.

## Real-world examples that save time every day

| Target Pattern | Replacement | Regex? | What you hear instead |
| :--- | :--- | :--- | :--- |
| Advertisement | (blank) | No | — completely skipped — |
| Sponsored | skip | No | “skip” |
| · [0-9,]+ comments? | (blank) | Yes | — no comment counts — |
| Breaking News: | News: | No | Shorter & cleaner |
| ^Cookie notice.*accept | (blank) | Yes | Banner text silenced |

## Pro tips for power users

*   Right-click any site or entry → context menu with Edit / Remove
*   Press **Delete** key on selected item for instant removal
*   Use literal longest-first matching → avoids partial word problems
*   Import rules from another .json file directly into any site
*   Regex mode supports replacement groups — very powerful for dynamic content

<br><br>

## Support Me

If this tool has made your life easier, consider fueling the next update with a small donation.

<br>

[<img src="https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe" alt="Support me">](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Your support means the world. Let's build something great together.

<br>

<p align="center">© 2026 Chai Chaimee NVDA Add-on Released under GNU</p>