---
title: Back-friendly modals & overlays
summary: Make Back (and Esc, scrim, ✕) close the open modal/sheet — not unload the whole page. Hook overlays into browser history.
category: pattern
tags: [modal, back-button, history, navigation, mobile, overlay, bottom-sheet]
platforms: [mobile-web, pwa, web]
archetypes: [consumer-mobile, ecommerce]
status: draft
related:
  - bottom-sheet-and-thumb-zone.md
  - lock-scroll-when-modal-open.md
  - ../principles/forgiveness-undo-over-confirm.md
  - ../principles/reload-returns-to-main-content.md
last_updated: 2026-06-16
---

# Back-friendly modals & overlays

> When a modal, sheet, or detail view is open, the **Back button/gesture should close it** — peeling one layer at a time — *not* navigate away from the page. On the web this doesn't happen for free: you have to hook overlays into browser history.

## Why it matters

On the web, the device/browser **Back** button (and the iOS swipe-back gesture) maps to browser **history**. If you open a modal by only toggling a CSS class, the history stack never changed — so when the user instinctively presses Back to dismiss the modal, the browser navigates *away from the whole page*.

On mobile this is brutal: the user is dumped out of the app and has to find their way back from scratch. For a QR-code restaurant menu, that means **re-scanning the code, re-opening the menu, and hunting for where they were** — every single time. Back is the most-used navigation control on the planet; if your overlays ignore it, you punish your most natural user behavior.

## The guideline

Treat **Back, Esc, scrim-tap, and the ✕ button as the same action: "dismiss the top layer."** Route them all through history so they stay consistent.

**Do**

- ✅ When you **open** an overlay, push a history entry (`history.pushState`).
- ✅ Listen for **`popstate`** (fired by Back/swipe-back) and **close the topmost overlay**.
- ✅ When the user closes via **✕ / scrim / Esc**, call **`history.back()`** so it goes through the *same* path (don't close the DOM directly — let `popstate` do it). One source of truth.
- ✅ Stack correctly: each open overlay = **one** history entry, so Back peels one layer at a time (nested sheet → parent modal → page).
- ✅ Preserve the underlying **scroll position & list state** so the user returns exactly where they were.
- ✅ For multi-step flows, let Back step **backward through steps** before closing.
- ✅ Ideally reflect deep state in the **URL** (e.g. `?item=123`) so refresh and sharing work.

**Don't**

- ❌ Let Back unload the entire page/app while an overlay is open.
- ❌ Push a history entry on open but forget to consume it on ✕-close → a "dead" Back press that does nothing.
- ❌ Push **multiple** entries for one overlay → user must press Back several times to escape.
- ❌ Trap Back so it does nothing — users expect it to close the modal, not freeze.
- ❌ Lose scroll position / re-fetch the list when the overlay closes.

## Minimal mechanic

```js
const stack = []; // open overlay ids, top = last

function openOverlay(id) {
  stack.push(id);
  history.pushState({ overlay: id, depth: stack.length }, '');
  render();
}

// ✕ button, scrim tap, and Esc all funnel here — mirror the Back button:
function dismiss() {
  if (stack.length) history.back();   // triggers popstate below
}

window.addEventListener('popstate', () => {
  if (stack.length) {                  // an overlay is open → close just the top one
    stack.pop();
    render();
  }                                    // else: nothing open → let the browser navigate (normal Back)
});

document.addEventListener('keydown', (e) => { if (e.key === 'Escape') dismiss(); });
```

## Showcase

- 👉 [`showcases/back-friendly-modals/`](../../showcases/back-friendly-modals/) — a mini QR-menu. Open an item, then press your **browser/phone Back button**: the detail closes and you stay on the menu. Includes a nested sheet so you can watch Back peel layers, plus an event log of `pushState`/`popstate`.

## Pitfalls & anti-patterns

- **Double-push** — adding two history entries for one overlay (e.g., open handler runs twice). Back then needs multiple presses.
- **Direct close + leftover history entry** — closing the DOM on ✕ without `history.back()` leaves a stale entry; the next Back does nothing.
- **iOS swipe-back** fires `popstate` too — the same handler covers it, but always test the gesture.
- **Refresh with overlay open** — without URL state the overlay is lost (acceptable); just make sure you land on a valid page, not a broken one.

## Notes from experience

> I was at a restaurant using their digital menu. I tapped an item to see details, then hit Back to return to the list — and it threw me *out of the menu entirely*, because "back" was just browser history. So I had to re-scan the QR code, re-open the menu, and find my place again. It happened over and over. Painful.
>
> Since then it's a rule in my designs: **Back and the close button must close the modal, not navigate history.** Whether the user taps ✕ or presses Back, they should land back on the page they were on — never get ejected.

## References

- MDN — History API (`pushState`, `popstate`)
- Material / iOS HIG — modal & sheet dismissal expectations
