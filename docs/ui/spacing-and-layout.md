---
title: Spacing & layout (the 8-pt grid)
summary: Snap all spacing to one scale (multiples of 4/8px) — consistent rhythm is the fastest path to a "designed" look.
category: ui
tags: [spacing, layout, grid, rhythm, consistency, design-tokens]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - type-scale-and-readability.md
  - ../principles/visual-hierarchy.md
last_updated: 2026-06-16
---

# Spacing & layout (the 8-pt grid)

> Inconsistent gaps are what make a UI feel "off" even when colors and fonts are fine. Pick one spacing scale and use *only* it. This single discipline makes a rushed build look intentional.

## Why it matters

Spacing creates rhythm and groups related things (proximity). When every margin is a random number — 13px here, 7px there — the eye senses the inconsistency as sloppiness. A shared scale produces visual harmony and makes layouts predictable to build and maintain.

## The guideline

Use a **4/8-based scale** and snap everything (margins, padding, gaps) to it.

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;   /* base unit */
  --space-5: 24px;
  --space-6: 32px;
  --space-8: 48px;
  --space-10: 64px;
}
```

**Do**

- ✅ Use scale values **only** — no arbitrary one-off spacing.
- ✅ Apply **proximity**: more space *between* groups than *within* a group.
- ✅ Be consistent: the same component has the same internal padding everywhere.
- ✅ Use a layout system (flex/grid + gap) instead of manual margins where possible.
- ✅ Keep generous touch spacing on mobile (avoid mis-taps).

**Don't**

- ❌ Eyeball pixels (`margin: 13px`) — it compounds into visual noise.
- ❌ Use equal spacing within and between groups (kills grouping).
- ❌ Fight the box model with negative margins as a default tool.
- ❌ Cram content edge-to-edge with no padding.

## Layout basics

- Establish a **max content width** for readability on large screens (don't stretch text full-width).
- Use a consistent **page gutter** (e.g., 16px mobile, 24–32px desktop).
- Prefer **responsive** layout (flex-wrap, grid `auto-fit`) over fixed pixel columns.

## Pitfalls & anti-patterns

- **Too many scale steps** — 4/8/12/16/24/32/48/64 is plenty.
- **Inconsistent component padding** — cards with different insets read as broken.
- **No proximity logic** — uniform gaps make everything feel unrelated.

## Notes from experience

> *(draft — replace with your own)* Tokenizing spacing and deleting every off-scale value is one of the highest visual-ROI hours you can spend on an MVP — it instantly reads as "designed" without touching features.

## References

- Refactoring UI — *Spacing & layout*
- Material Design — 8dp grid
