---
title: Intentional tap & touch feedback (no default blue flash)
summary: Mobile browsers add their own tap highlight, long-press menu, and selection on touch — replace these defaults with your own feedback, but keep keyboard focus accessible.
category: ui
tags: [mobile, touch, tap-highlight, focus, accessibility, polish, webkit]
platforms: [mobile-web, pwa]
status: draft
related:
  - ../principles/feedback-for-every-action.md
  - ../techniques/micro-interactions.md
  - ../platforms/README.md
last_updated: 2026-06-16
---

# Intentional tap & touch feedback (no default blue flash)

> You design a beautiful UI, deploy it, open it on your phone — and every tap flashes an ugly blue/grey rectangle you never added. That's the browser's **default tap highlight**. The fix is to take control of touch feedback: remove the defaults you don't want, and replace them with your *own* intentional press states — without breaking accessibility.

## Why it matters

Mobile browsers apply their own interaction chrome that's **invisible on desktop**: a tap-highlight rectangle (`-webkit-tap-highlight-color`), a long-press callout menu, text selection on UI labels, and a 300ms tap delay / double-tap zoom. Left as-is, a polished design suddenly looks cheap and unbranded on a real device. But naively stripping *all* of it (e.g. killing focus outlines) breaks keyboard and screen-reader users. The goal is **intentional** feedback.

## The guideline

**Do**

- ✅ Remove the tap-highlight flash with `-webkit-tap-highlight-color: transparent`. That removal **is** the fix.
- ✅ Add your own `:active` feedback (scale/opacity/background) where useful — **recommended but not mandatory** ([when to skip it](#is-a-custom-press-effect-required)).
- ✅ Keep keyboard focus visible with **`:focus-visible`** (shows a ring for keyboard, not for mouse/touch).
- ✅ Use `touch-action: manipulation` on tappable controls to drop the 300ms delay & double-tap zoom.
- ✅ Disable selection/callout on **non-text UI** (`user-select: none`, `-webkit-touch-callout: none`) — but keep selection on real content.
- ✅ **Test on a real device early** — these defaults don't show in desktop preview.

**Don't**

- ❌ Blanket-remove focus (`*:focus { outline: none }`) — that's an accessibility regression.
- ❌ Remove the highlight from an element that has **no other feedback** and add nothing — taps feel dead. (If the action already responds visibly, a press effect is optional.)
- ❌ Disable text selection on actual paragraphs/content.
- ❌ Assume "looks great on my laptop" means it looks great on a phone.

## Is a custom press effect required?

No — **removing the default flash is the only must**. A replacement `:active` effect is *recommended but optional*, judged by whether the tap already produces immediate feedback:

- **You can skip it** when the tap visibly does something right away — navigates, opens a sheet/modal, toggles a switch, expands a row. The result *is* the feedback.
- **Add it** when the result is delayed, off-screen, or subtle (a network call, a far-away change) so the tap still feels acknowledged.
- Either way, **keep accessible focus** (`:focus-visible`) — that part is never optional.

## Copy-paste baseline

```css
/* 1) Take control of touch defaults on interactive elements */
button, a, [role="button"], .tappable {
  -webkit-tap-highlight-color: transparent; /* no blue/grey flash on tap */
  -webkit-touch-callout: none;              /* no iOS long-press menu on UI */
  touch-action: manipulation;               /* no 300ms delay / double-tap zoom */
  user-select: none;                        /* UI chrome shouldn't be selectable */
}

/* 2) Replace it with YOUR OWN press feedback */
button:active, .tappable:active { transform: scale(.97); opacity: .92; }

/* 3) Keep focus visible for keyboard users only */
:focus-visible { outline: 2px solid var(--focus, #3b82f6); outline-offset: 2px; }
:focus:not(:focus-visible) { outline: none; }

/* 4) But DO let people select real text */
p, h1, h2, h3, li, .selectable { user-select: text; }

@media (prefers-reduced-motion: reduce) {
  button:active, .tappable:active { transform: none; }
}
```

## Showcase

- 👉 [`showcases/tap-feedback/`](../../showcases/tap-feedback/) — open it **on your phone**. Toggle **Default** to see the browser's blue/grey tap flash; toggle **Polished** to see it gone and replaced with a crisp press. Press <kbd>Tab</kbd> to confirm the keyboard focus ring is preserved.

## Pitfalls & anti-patterns

- **Killing all focus outlines** to "clean up" — invisible-but-critical accessibility break.
- **Transparent highlight + no `:active`** — feedback disappears entirely; taps feel unresponsive.
- **`user-select: none` on the whole `body`** — users can't copy real content.
- **Desktop-only testing** — the #1 reason this bug ships.

## Notes from experience

> I built a UI I was proud of, deployed it, opened it on my phone — and every single tap flashed a blue rectangle I never designed. It was Chrome's default tap highlight. I asked the designer to kill that effect 🙂 — but the real lesson is to bake it into the **CSS baseline** so nobody has to chase it per-screen: `-webkit-tap-highlight-color: transparent` + your own `:active` feedback, applied to all tappable elements from the start. And: **test on a real device early** — this never shows on desktop.

## References

- MDN — `-webkit-tap-highlight-color`, `touch-action`, `:focus-visible`, `user-select`
- web.dev — *Use `:focus-visible`* and removing the 300ms tap delay
