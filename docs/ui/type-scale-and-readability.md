---
title: Type scale & readability
summary: Use a small, consistent type scale and readable defaults — text is 90% of most UIs.
category: ui
tags: [typography, readability, hierarchy, accessibility]
platforms: [mobile-web, pwa, desktop, web]
status: draft
last_updated: 2026-06-16
---

# Type scale & readability

> Most of your UI is text. Get a handful of type decisions right and the whole product looks designed.

## Why it matters

Typography carries hierarchy, tone, and legibility. Inconsistent, too-small, or too-tight text makes an app feel amateur and excludes people with lower vision — regardless of how nice the rest of the UI is.

## The guideline

**Do**

- ✅ Define a **limited type scale** (e.g. 12 · 14 · 16 · 20 · 24 · 32 · 40) and use only those sizes.
- ✅ Set **body text ≥ 16px** on mobile (smaller triggers iOS zoom-on-focus and hurts readability).
- ✅ Keep line length around **45–75 characters** for comfortable reading.
- ✅ Use **line-height ~1.5** for body, tighter (~1.1–1.25) for large headings.
- ✅ Limit to **2 font families** (often 1). Use weight and size for hierarchy, not many fonts.
- ✅ Ensure contrast meets **WCAG AA** (4.5:1 for body, 3:1 for large text).
- ✅ Use relative units (`rem`) so the system scales with user font-size preferences.

**Don't**

- ❌ Sprinkle arbitrary one-off sizes (`13px` here, `15px` there).
- ❌ Set body text below 16px on mobile.
- ❌ Use light-gray text on white "because it looks clean" — it fails contrast.
- ❌ Justify text on narrow mobile columns (rivers of whitespace).

## A starting scale (copy me)

```css
:root {
  --text-xs:  0.75rem;  /* 12px — captions, metadata */
  --text-sm:  0.875rem; /* 14px — secondary text */
  --text-base:1rem;     /* 16px — body (mobile minimum) */
  --text-lg:  1.25rem;  /* 20px — lead, subheads */
  --text-xl:  1.5rem;   /* 24px — section titles */
  --text-2xl: 2rem;     /* 32px — page titles */
  --text-3xl: 2.5rem;   /* 40px — hero */
  --leading-body: 1.5;
  --leading-tight: 1.15;
}
```

## Pitfalls & anti-patterns

- **Too many sizes** — a 14px vs 15px difference is invisible but doubles your scale.
- **Tight line-height on long body text** hurts readability more than small size does.
- **Decorative fonts for UI text** — save them for the logo or a hero, never controls.

## Notes from experience

> The fastest way to make a rushed MVP look intentional: delete every ad-hoc font size, snap everything to a 6–7 step scale, and bump body to 16px. It takes an hour and the app instantly looks "designed."

## References

- Practical Typography — Butterick
- WCAG 2.2 — Contrast (Minimum)
