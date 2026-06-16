---
title: Swipe to dismiss (drawers & sheets)
summary: Let an overlay be dismissed by swiping it back the way it came in — left drawer swipes left, right drawer swipes right, bottom sheet swipes down.
category: pattern
tags: [gesture, swipe, drawer, side-panel, bottom-sheet, modal, mobile, dismissal]
platforms: [mobile-web, pwa]
archetypes: [consumer-mobile, ecommerce]
status: draft
related:
  - back-friendly-modals.md
  - lock-scroll-when-modal-open.md
  - bottom-sheet-and-thumb-zone.md
last_updated: 2026-06-16
---

# Swipe to dismiss (drawers & sheets)

> An overlay that slides in should slide back out the same way. If a panel enters from the right, the natural way to close it is to **swipe it back to the right**. Matching the dismissal gesture to the entry direction makes overlays feel physical and obvious.

## Why it matters

Sliding panels imply direction. Users instinctively try to "push" a drawer back toward the edge it came from. When that gesture does nothing — and the only way out is a small ✕ in a far corner — the overlay feels stuck and unnatural, especially one-handed on mobile. Swipe-to-dismiss turns the obvious instinct into the action.

## The principle: dismiss in the direction it entered

| Overlay | Enters from | Swipe to dismiss |
| --- | --- | --- |
| Right drawer / side panel | right | swipe **right** |
| Left drawer / nav | left | swipe **left** |
| Bottom sheet | bottom | swipe **down** |
| Top notification / sheet | top | swipe **up** |

## The guideline

**Do**

- ✅ The panel **follows the finger** during the drag (1:1), so it feels physical.
- ✅ Commit the dismiss past a **distance threshold (~35–45% of size) OR a flick velocity**; otherwise **snap back**.
- ✅ Show an affordance — a drag handle/grabber — so the gesture is discoverable.
- ✅ Keep swipe as an **addition**, never the only exit: ✕, scrim tap, `Esc`, and Back must still work (see [back-friendly modals](back-friendly-modals.md)).
- ✅ Route the dismiss through the **same path** as the other closers (history-back / single source of truth) and keep [scroll locked](lock-scroll-when-modal-open.md) while open.
- ✅ Use `touch-action` to separate the swipe axis from content scroll (e.g. `pan-y` on a horizontally-dismissed drawer).

**Don't**

- ❌ Allow dragging the *wrong* way (a right drawer shouldn't pull further left into the screen).
- ❌ Dismiss on a tiny accidental drag — require threshold + velocity.
- ❌ Fight platform gestures: a **left-edge** swipe collides with the **iOS back gesture**; carousels/sliders inside the panel can hijack horizontal drags.
- ❌ Make swipe the *only* way to close (discoverability + accessibility fail).
- ❌ Skip the snap-back animation — a half-dragged panel that just freezes feels broken.

## Mechanic (sketch)

```js
// right-side drawer: only rightward drag closes it
let startX = 0, startT = 0, dx = 0, dragging = false;
el.style.touchAction = 'pan-y';                 // let vertical scroll, capture horizontal

el.addEventListener('pointerdown', (e) => {
  startX = e.clientX; startT = Date.now(); dx = 0; dragging = true;
  el.style.transition = 'none';
});
el.addEventListener('pointermove', (e) => {
  if (!dragging) return;
  dx = Math.max(0, e.clientX - startX);         // clamp to the "out" direction
  el.style.transform = `translateX(${dx}px)`;
});
el.addEventListener('pointerup', () => {
  dragging = false;
  el.style.transition = '';                      // re-enable animation
  const vel = dx / Math.max(1, Date.now() - startT);
  if (dx > el.offsetWidth * 0.4 || vel > 0.5) dismiss();   // same closer as Back/Esc/✕
  else el.style.transform = '';                  // snap back
});
```

## Showcase

- 👉 [`showcases/back-friendly-modals/`](../../showcases/back-friendly-modals/) — overlays enter from **all four sides** and each dismisses in the direction it came: dish-detail **bottom sheet → swipe down**, **🎉 Offers top sheet → swipe up**, **☰ Categories left drawer → swipe left**, **🛒 Cart right drawer → swipe right** — all with follow-the-finger drag, a distance/velocity threshold, and snap-back. Every overlay also still closes via ✕ / scrim / Esc / Back. One demo, the full modal family: history-back dismissal + scroll lock + swipe-to-dismiss.

## Pitfalls & anti-patterns

- **Axis bleed** — horizontal swipe stealing vertical scroll (or vice-versa); fix with `touch-action` + direction lock on first move.
- **iOS edge-back conflict** — avoid relying on a left-edge swipe to open/close.
- **No velocity check** — a slow short drag past threshold dismisses unexpectedly; combine distance OR flick.
- **Swipe-only** — fails keyboard and screen-reader users; always pair with a button.

## Notes from experience

> *(draft — add your own)* Pair this with the other modal rules: a drawer should close by the obvious swipe, by the ✕, by the scrim, by Esc, and by Back — all landing the user back where they were. Same intent, five doors out.

## References

- Material Design — *Navigation drawer* (swipe to open/close), *Bottom sheet* gestures
- iOS HIG — sheets & gesture dismissal
