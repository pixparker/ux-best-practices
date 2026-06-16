---
title: Lock background scroll when a modal is open
summary: While an overlay is open, freeze the page behind it (and stop scroll-chaining) — but keep the modal's own content scrollable.
category: pattern
tags: [modal, scroll-lock, overlay, mobile, scroll, bottom-sheet, ios]
platforms: [mobile-web, pwa, web]
archetypes: [consumer-mobile, ecommerce]
status: draft
related:
  - back-friendly-modals.md
  - bottom-sheet-and-thumb-zone.md
last_updated: 2026-06-16
---

# Lock background scroll when a modal is open

> A modal is supposed to be *the* focus. If the page keeps scrolling behind it, the user loses their place, scrolls the wrong layer, and the overlay feels broken. Freeze the background while the overlay is open — then restore exactly where they were.

## Why it matters

When a modal/sheet is open and the user scrolls (or fat-fingers the background), one of two bad things happens: the **page behind moves** — so when they close the modal they're somewhere else — or, on mobile, scrolling past the end of the modal **chains** into the body. Both break the illusion that the modal is a focused, self-contained context. Locking scroll keeps attention where it belongs and preserves the user's position.

## The guideline

**Do**

- ✅ **Lock the background** (page/body) from scrolling while any overlay is open.
- ✅ Keep the **modal's own content scrollable** if it overflows — lock the page, not the dialog.
- ✅ Stop **scroll-chaining** with `overscroll-behavior: contain` on the scrollable modal.
- ✅ **Preserve & restore** the exact scroll position on close (avoid the iOS "jump to top").
- ✅ Avoid the **layout shift** when the scrollbar disappears (`scrollbar-gutter: stable` or compensate with padding).
- ✅ **Reference-count** for stacked overlays — only unlock when the *last* layer closes.
- ✅ Restore on **every** close path (Back, Esc, scrim, ✕) — see [back-friendly modals](back-friendly-modals.md).

**Don't**

- ❌ Leave the page scrollable behind the modal.
- ❌ Lock the modal's *own* scroll so long content becomes unreachable.
- ❌ Rely only on `body { overflow: hidden }` on **iOS Safari** — it leaks; the background still scrolls.
- ❌ Forget to unlock on one close path → page stuck frozen.
- ❌ Cause a horizontal content "jump" when the scrollbar vanishes.

## Technique

CSS (desktop + chaining):

```css
/* applied while a modal is open */
html.is-locked, body.is-locked { overflow: hidden; }
html { scrollbar-gutter: stable; }     /* no layout shift when scrollbar hides */
.sheet, .modal__content { overscroll-behavior: contain; }  /* no scroll-chaining */
```

JS (robust, incl. iOS — position-fixed trick with scroll restore + reference count):

```js
let locks = 0, savedY = 0;
function lockScroll() {
  if (locks++ > 0) return;             // already locked (stacked overlay)
  savedY = window.scrollY;
  document.body.style.position = 'fixed';
  document.body.style.top = `-${savedY}px`;
  document.body.style.width = '100%';  // prevent reflow when leaving normal flow
}
function unlockScroll() {
  if (--locks > 0) return;             // other overlays still open
  locks = 0;
  document.body.style.position = '';
  document.body.style.top = '';
  document.body.style.width = '';
  window.scrollTo(0, savedY);          // restore exact position
}
```

> The native `<dialog>` element (with `showModal()`) locks background interaction and provides `::backdrop` for free — a good baseline when you can use it. You still want `overscroll-behavior: contain` on scrollable content.

## Showcase

- 👉 [`showcases/back-friendly-modals/`](../../showcases/back-friendly-modals/) — the same QR-menu demo also **locks the page scroll** while a sheet is open and restores your position on close.

## Pitfalls & anti-patterns

- **iOS leak** — `overflow: hidden` alone doesn't hold; use the position-fixed + restore approach.
- **Lost position** — forgetting to restore `scrollY` dumps the user at the top on close.
- **Double lock / early unlock** — stacked overlays without reference counting unlock too soon.
- **Scrollbar jump** — content shifts horizontally when the scrollbar is removed.

## Notes from experience

> *(draft — refine in your words)* This goes hand-in-hand with [back-friendly modals](back-friendly-modals.md): the modal should own the screen. Locking the page behind it — and giving the user back their exact scroll spot on close — is what makes an overlay feel solid instead of slippery.

## References

- MDN — `overscroll-behavior`, `scrollbar-gutter`, `<dialog>`
- Common body-scroll-lock implementations (the iOS position-fixed pattern)
