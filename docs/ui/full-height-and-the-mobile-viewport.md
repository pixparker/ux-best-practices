---
title: Full-height sections & the mobile viewport (the 100vh trap)
summary: On mobile, 100vh isn't the visible area — the address bar shows/hides and changes it. Size full-height heroes with a STATIC viewport unit (or a frozen measurement) so they never resize mid-scroll.
category: ui
tags: [mobile, viewport, 100vh, svh, dvh, hero, layout, scroll-jump]
platforms: [mobile-web, pwa]
archetypes: [fancy-app, ecommerce, consumer-mobile]
status: draft
related:
  - spacing-and-layout.md
  - tap-and-touch-feedback.md
  - ../platforms/README.md
last_updated: 2026-06-16
---

# Full-height sections & the mobile viewport (the 100vh trap)

> A full-height hero (`height: 100vh`) looks perfect on desktop and in the design tool — then on a phone it either gets cut off behind the address bar, or **resizes the moment the bar hides and jerks the whole page**. On mobile, `100vh` does *not* mean "the height I can see."

## Why it matters

Mobile browsers grow and shrink the visible area as you scroll: the address bar is shown at the top, then collapses once you scroll down. That changes the viewport height by ~60–100px mid-interaction. If your hero is tied to that changing height, it resizes live — and because it's the **first** thing on the page, every element below it shifts, so the user's scroll position jumps. That's the bad UX you saw on the Luna hero (and it'll hit any full-height section).

## Know the four units

| Unit | Equals | Behavior |
| --- | --- | --- |
| `svh` | **S**mall viewport — address bar **shown** | Static. Fits the visible area even with the bar; never grows → **no jump** |
| `lvh` | **L**arge viewport — address bar **hidden** | Static. Fills when the bar is gone; bottom hidden behind bar initially |
| `dvh` | **D**ynamic — the live viewport | **Changes as the bar shows/hides** → resize + scroll jump on big sections |
| `vh`  | ≈ large viewport in modern browsers | Static-ish; same trade-off as `lvh` |

## The guideline

**Do**

- ✅ Size full-height sections with a **static** unit so they don't resize mid-scroll. **`100svh` is the safe default** — it fits with the bar shown, so there's no cut-off and no jump.
- ✅ Provide a fallback for older browsers: declare `100vh` first, then `100svh`.
- ✅ Choose the trade-off deliberately: **no-jump & no-cutoff** (`svh`) vs **fills the screen when the bar hides** (`lvh`/`vh`, accepting slight initial overflow).
- ✅ If you must support browsers without the new units, **measure `innerHeight` once and freeze it** in a CSS variable — update only on `orientationchange`, never on scroll.
- ✅ Test on a real phone with the address bar visible.

**Don't**

- ❌ Use `100dvh` for a large hero if you don't want it to resize — `dvh` tracks the live viewport and causes the reflow/jump. (`dvh` is fine for *small* UI like a sticky bottom bar.)
- ❌ Recompute and reapply height on every `scroll`/`resize` event — that's literally what produces the jump.
- ❌ Assume `100vh` = the area the user can see on mobile.
- ❌ Pin critical content (a CTA) to the very bottom of a `100vh`/`lvh` hero — it can sit behind the address bar on first paint.

## Copy-paste

```css
/* Modern, CSS-only, no jump: */
.hero {
  min-height: 100vh;    /* fallback for browsers without the new units */
  min-height: 100svh;   /* fits with the address bar shown; stays put when it hides */
}
/* AVOID for big heroes:  .hero { height: 100dvh; }  ← resizes as the bar toggles */
```

Legacy precision — *measure once, then freeze* (your instinct, in code):

```js
function setAppHeight() {
  // capture the height NOW and don't touch it again on scroll
  document.documentElement.style.setProperty('--app-h', window.innerHeight + 'px');
}
setAppHeight();
window.addEventListener('orientationchange', () => setTimeout(setAppHeight, 200));
// note: intentionally NOT listening to 'scroll' or 'resize' — that's what caused the jump
```
```css
.hero { height: var(--app-h, 100vh); }
```

## Showcase

- 👉 [`showcases/full-height-hero/`](../../showcases/full-height-hero/) — open **on your phone**, scroll so the address bar collapses, and watch the live height readout. Switch between `vh` / `svh` / `lvh` / `dvh` / *JS-frozen*: `dvh` resizes (and jumps); `svh`/`lvh`/frozen stay rock-steady.

## Pitfalls & anti-patterns

- **`dvh` everywhere** — looks smooth in isolation but reflows big sections during the bar transition.
- **`resize`/`scroll` height recalculation** — thrashing layout and fighting the browser.
- **No fallback** — `svh` silently does nothing on older engines; keep the `100vh` line above it.
- **Forgetting the bar exists** — the bug never appears in desktop preview.

## Notes from experience

> I hit this on the **Luna** template's full-height hero (and it'll affect any full-height hero). It opens with the address bar visible; as you scroll, the browser hides the bar, the window height changes, and the hero re-sizes to match — which makes the scroll position jump. Jarring. The fix is exactly *"calculate once and don't change the hero height after it's shown"* — these days that's a static unit like `100svh`, with the measure-once-and-freeze JS as the fallback for old browsers.

## References

- MDN — *Viewport units: `svh`, `lvh`, `dvh`*
- web.dev — *The large, small, and dynamic viewport units*
- CSS-Tricks — *The trick to viewport units on mobile*
