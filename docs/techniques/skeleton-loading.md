---
title: Skeleton loading
summary: Show a gray placeholder of the upcoming layout instead of a blank screen or spinner — the app feels faster.
category: technique
tags: [perceived-performance, loading, states, motion]
platforms: [mobile-web, pwa, desktop, web]
status: stable
related:
  - ../principles/feedback-for-every-action.md
last_updated: 2026-06-16
---

# Skeleton loading

> Replace blank screens and spinners with a soft preview of the content's shape. Users perceive the wait as shorter and the app as faster — even when load time is identical.

## Why it matters

A spinner says "wait" but communicates nothing. A blank screen feels broken. A **skeleton** shows the structure that's about to appear, so the brain starts processing layout immediately and the perceived wait drops. It also prevents jarring layout shift when content pops in.

## The guideline

**Do**

- ✅ Mirror the **real layout** — skeleton blocks should match the size/position of the content they replace.
- ✅ Add a subtle **shimmer/pulse** so it reads as "loading," not "broken."
- ✅ Use skeletons for **content you can predict** (lists, cards, profiles, tables).
- ✅ Keep the transition to real content smooth (fade, no layout jump).
- ✅ Respect `prefers-reduced-motion` — drop the shimmer for users who opt out.

**Don't**

- ❌ Use a skeleton for **sub-300ms** loads — the flash is worse than nothing.
- ❌ Build a skeleton that looks nothing like the final layout (causes a jump).
- ❌ Animate aggressively — the shimmer should be calm, not strobing.
- ❌ Use skeletons for unpredictable content where you can't approximate the shape.

## Showcase

- 👉 [`showcases/skeleton-loading/`](../../showcases/skeleton-loading/) — open `index.html`. Toggle the load to compare **spinner vs. skeleton** and feel the difference. Honors `prefers-reduced-motion`.

## Minimal CSS

```css
.skeleton {
  background: linear-gradient(90deg, #e9edf2 25%, #f4f7fa 37%, #e9edf2 63%);
  background-size: 400% 100%;
  animation: shimmer 1.4s ease infinite;
  border-radius: 8px;
}
@keyframes shimmer { 0% { background-position: 100% 0; } 100% { background-position: -100% 0; } }
@media (prefers-reduced-motion: reduce) { .skeleton { animation: none; } }
```

## Pitfalls & anti-patterns

- **Skeleton everything forever** — if data routinely takes >10s, a skeleton becomes a lie; show progress or a message.
- **Mismatched shape** — the #1 mistake; the page jumps when real content arrives.
- **Over-engineering** — for tiny waits, an optimistic update or instant cache is better than any loader.

## Notes from experience

> Skeletons are the highest-ROI perceived-performance trick in an MVP. Same backend, same latency — but swapping a centered spinner for a content-shaped skeleton makes testers describe the app as "snappy." It's almost free and it changes how people *feel* about the product.

## References

- Nielsen Norman Group — *Skeleton Screens*
- Luke Wroblewski — perceived performance writing
