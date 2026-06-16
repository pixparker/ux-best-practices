---
title: Color, contrast & dark mode
summary: Use semantic color tokens, meet WCAG AA contrast, and design dark mode as its own theme — not an inverted afterthought.
category: ui
tags: [color, contrast, accessibility, dark-mode, design-tokens, theming]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../principles/visual-hierarchy.md
  - spacing-and-layout.md
last_updated: 2026-06-16
---

# Color, contrast & dark mode

> Color carries meaning, hierarchy, and brand — but it must stay readable for everyone and in every theme. Define color by *role*, not by raw hex, and contrast becomes a property of the system, not a per-screen gamble.

## Why it matters

Hardcoded hex values scattered through a codebase make theming impossible and contrast accidental. Low-contrast "clean" gray text excludes users with low vision and anyone in sunlight. Dark mode bolted on by inverting colors produces muddy, glaring results. Semantic tokens fix all three at once.

## The guideline

Define color by **semantic role**, then map roles to values per theme:

```css
:root {
  --color-bg: #ffffff;
  --color-surface: #f4f7fa;
  --color-text: #1b2330;
  --color-text-muted: #6b7689;
  --color-border: #e6ebf1;
  --color-primary: #3b82f6;
  --color-danger: #e5484d;
  --color-success: #2e9e5b;
}
[data-theme="dark"] {
  --color-bg: #0f141b;
  --color-surface: #1a212b;
  --color-text: #e8edf3;
  --color-text-muted: #9aa6b6;
  --color-border: #2a333f;
  --color-primary: #5b9bff;
}
```

**Do**

- ✅ Reference **tokens** (`var(--color-text)`), never raw hex, in components.
- ✅ Meet **WCAG AA**: 4.5:1 for body text, 3:1 for large text & UI/icons.
- ✅ Pair color meaning with a **second cue** (icon, label, shape) — never color alone.
- ✅ Treat **dark mode as a distinct theme**: softer surfaces, reduced pure-white, re-checked contrast (avoid pure `#000`/`#fff`).
- ✅ Respect `prefers-color-scheme` and offer a manual toggle.

**Don't**

- ❌ Use light-gray-on-white because it "looks minimal" — it usually fails AA.
- ❌ Convey status with color only (red/green) — color-blind users miss it.
- ❌ Invert light colors to fake dark mode (glare, muddy contrast).
- ❌ Use saturated, high-contrast brand colors as large background fills behind text.

## Pitfalls & anti-patterns

- **Pure black dark mode** (`#000`) with pure-white text causes halation/eye strain — use near-black/near-white.
- **Too many accent colors** dilute meaning; keep a small, role-based palette.
- **Untested contrast** on disabled/placeholder/muted text (the usual offenders).

## Notes from experience

> *(draft — replace with your own)* The two recurring fixes: muted text that fails contrast, and "minimal" gray UI that's actually unreadable. Tokenizing color first makes both auditable and makes dark mode a config, not a rewrite.

## References

- WCAG 2.2 — *Contrast (Minimum / Non-text)*
- Material 3 / Radix Colors — semantic color systems
