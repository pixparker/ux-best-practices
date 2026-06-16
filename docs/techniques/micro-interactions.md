---
title: Micro-interactions
summary: Small, purposeful, sub-300ms animations that confirm actions and add life — used with restraint and reduced-motion support.
category: technique
tags: [motion, animation, feedback, delight, micro-interaction]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../principles/feedback-for-every-action.md
  - ../ui/color-contrast-and-dark-mode.md
last_updated: 2026-06-16
---

# Micro-interactions

> Tiny moments of motion — a button that depresses, a heart that pops, a toggle that slides — make an interface feel responsive and alive. The key word is *micro*: fast, purposeful, and never in the way.

## Why it matters

Motion is feedback the brain reads instantly. A well-timed micro-interaction confirms "that worked," shows relationships (where a thing came from / went), and adds personality. Overdone, motion becomes lag and annoyance. The craft is using just enough.

## The guideline

**Do**

- ✅ Keep durations short: **~150–250ms** for UI feedback (longer feels sluggish).
- ✅ Use **ease-out** for entrances, **ease-in** for exits; avoid linear for UI.
- ✅ Animate to **confirm an action** (press, success check, add-to-cart fly), **show state change** (toggle, expand), or **guide attention**.
- ✅ Animate **transform & opacity** (GPU-friendly) rather than layout properties.
- ✅ Always honor `prefers-reduced-motion` — provide a reduced/!no-motion path.
- ✅ Make motion **interruptible** — don't lock input during an animation.

**Don't**

- ❌ Add motion with no purpose ("because it looks cool").
- ❌ Use long/elaborate animations on **high-frequency** actions (they become friction).
- ❌ Animate `width/height/top/left` where `transform` would do (jank).
- ❌ Block the UI until an animation finishes.
- ❌ Ignore reduced-motion — it can trigger discomfort/vestibular issues.

```css
.btn { transition: transform .15s ease, background .15s ease; }
.btn:active { transform: scale(.96); }
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: .01ms !important; transition-duration: .01ms !important; }
}
```

## Pitfalls & anti-patterns

- **Motion as decoration** that slows real tasks.
- **Same flourish on a 200×/day action** — delightful once, infuriating by lunch.
- **Forgetting reduced-motion** — an accessibility and comfort failure.

## Notes from experience

> *(draft — replace with your own)* A press-state scale and a smooth toggle do more for "feels premium" than any big hero animation. Spend motion budget on the moments users repeat, keep it under ~250ms, and always wire up reduced-motion.

## References

- Val Head — *Designing Interface Animation*
- WCAG — *Animation from Interactions* / reduced motion
