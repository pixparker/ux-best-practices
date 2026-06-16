---
title: Bottom sheets & the thumb zone
summary: On mobile, put primary actions and surfaces within easy thumb reach — anchor them to the bottom, not the top.
category: pattern
tags: [mobile, bottom-sheet, thumb-zone, navigation, reachability, touch]
platforms: [mobile-web, pwa]
archetypes: [consumer-mobile, ecommerce, fancy-app]
status: draft
related:
  - ../platforms/README.md
  - ../principles/visual-hierarchy.md
last_updated: 2026-06-16
---

# Bottom sheets & the thumb zone

> Phones are big and held one-handed. The top of the screen is the hardest place to reach and the bottom is the easiest — yet apps keep putting key actions in the top corners. Design for the thumb.

## Why it matters

Most phone use is one-handed, with the thumb pivoting from the bottom. The top corners are a stretch (or a hand-shuffle that risks dropping the phone). Placing primary actions and interactive surfaces in the bottom **thumb zone** makes the app faster, safer, and more comfortable — especially on today's tall screens.

## The guideline

**Do**

- ✅ Anchor the **primary action** to the bottom (bottom bar/button) within thumb reach.
- ✅ Use **bottom sheets** for menus, filters, pickers, and contextual actions instead of top dropdowns or full-screen modals.
- ✅ Make sheets **dismissible** by swipe-down and tap-outside; show a drag handle.
- ✅ Support partial (peek) and expanded heights for content-heavy sheets.
- ✅ Keep destructive/rare actions **out** of the easy zone to avoid accidental taps.
- ✅ Respect safe areas (`env(safe-area-inset-bottom)`) so controls clear the home indicator.

**Don't**

- ❌ Put the main CTA in a top-right corner on mobile.
- ❌ Use a tiny top "kebab" menu as the only path to important actions.
- ❌ Build sheets that can't be swiped away or that trap focus.
- ❌ Place a delete button right next to the most-tapped action.

## Reach map (right-handed, one hand)

```
┌─────────────┐
│  hard  ✦    │  ← top: avoid critical/primary actions
│             │
│   ok        │
│             │
│  easy  ★    │  ← bottom: primary actions, sheets, nav
└─────────────┘
```

## Pitfalls & anti-patterns

- **Bottom-sheet overload** — nesting sheets or using them for full workflows that deserve a page.
- **No dismissal affordance** — users get stuck.
- **Ignoring safe areas** — controls hidden behind the home indicator.

## Notes from experience

> *(draft — replace with your own)* Moving the primary action to a bottom-anchored button and converting top dropdowns into bottom sheets is one of the most-felt mobile improvements — users stop reaching and the app feels built *for the phone*.

## References

- Material Design — *Bottom sheets*
- Steven Hoober — research on one-handed phone use & thumb zones
