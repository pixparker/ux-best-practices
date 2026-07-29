---
id: PAIN-001
title: Back closes the app instead of the open overlay
pain: A user opens a modal, presses Back expecting to close it, and the browser unloads the whole page instead.
category: pain
tags: [modal, back-button, history, navigation, mobile, overlay, spa]
platforms: [mobile-web, pwa, tablet, web]
archetypes: [consumer-mobile, ecommerce, ops-panel, fancy-app]
severity: abandonment
status: solved
enforcement: code
enforced-by: "a single popstate owner (BackStack) + useBackHandler; grep-gated in tests"
solution: ../patterns/back-friendly-modals.md
showcase: ../../showcases/back-friendly-modals/
first-seen: 2026-06-08
last_updated: 2026-07-29
---

# PAIN-001 — Back closes the app instead of the open overlay

> **The pain.** The user opens a modal, sheet or drawer, then presses Back expecting to return to what was underneath. Instead the browser leaves the page entirely and they are thrown out of the app.

## 1. Pain point

Back is the most-used navigation control on earth, and on mobile it is often a *gesture* — a swipe from the screen edge — so it gets used reflexively, without a decision.

In a single-page app, opening an overlay usually just flips a boolean and renders a `<div>`. The browser's history stack never changed. So when the user presses Back to dismiss the overlay, the browser does the only thing it knows: **it navigates away from the page.**

**The expectation that breaks:** *"Back undoes the last thing I did."* The user's last action was *open this modal*. The browser's last recorded action was *load this page*. Those two disagree, and the user loses.

The cost is not "annoying" — it is **task abandonment**. On a QR-code menu, being thrown out means re-scanning the physical code, waiting for the page again, and hunting for where they were. On a form, it can mean losing typed input. Users who get burned once start avoiding overlays entirely, or they stop using Back and get stranded inside flows with no way out.

**Why it happens:** the overlay is a *visual* layer with no *navigational* existence. Nothing told the browser that a new state was entered, so nothing can take the user back out of it.

## 2. Approach / solution

Give every overlay a real presence in history, and route every way of closing it through one path.

- On **open**, push a history entry. On `popstate` (Back / swipe-back), close the **topmost** overlay only — so Back peels one layer at a time.
- **Close buttons, scrim taps and Esc call `history.back()`** rather than closing the DOM directly. One source of truth, so all four dismissal routes behave identically and the history stack never desynchronises.
- **Exactly one `popstate` listener for the whole app.** This is the load-bearing constraint (see §3).
- Preserve the underlying scroll and list state so the user lands exactly where they were.
- Keep ephemeral overlays **out of the URL**; give a URL only to destinations worth sharing or reloading into.

**Rejected — and why:**
- *Each overlay manages its own `popstate`.* This is the obvious first implementation and it is the trap. It produced four competing listeners that fought over a single Back press.
- *Intercepting Back to block navigation.* Fights the platform and breaks the legitimate case of leaving the page.
- *Putting every overlay in the URL.* Reload then restores a modal over a page the user never chose, which violates [reload lands on main content](../principles/reload-returns-to-main-content.md).

> 🔒 The mechanism is a reference, not a mandate. A router with real modal routes, or a native shell, may satisfy this differently. What is binding: **Back must dismiss the top layer, never the app.**

## 3. The result

The overlay layer stopped being a trap. Back, Esc, scrim and ✕ became genuinely interchangeable, and nested flows (sheet → modal → page) unwind one step at a time as users expect.

**The real lesson was about ownership, not history.** The first version let each component hook `popstate` itself. With four listeners live, one Back press could close two overlays, or none, depending on mount order — a bug that was intermittent, device-dependent and nearly impossible to reproduce on demand. Collapsing them into **one owner with a LIFO stack** is what actually fixed it. The history API was never the hard part; *coordination* was.

**Not fixed:** it does nothing for a hard reload while an overlay is open (by design — see the rejected options), and an overlay opened from a `<form>` submit still needs care so Back doesn't resubmit.

**A cost worth naming:** every new overlay primitive must go through the shared owner. That is a small, permanent tax, and it is why this pain is enforced by a grep-gate rather than a code review habit.

## 4. Best practice

**Rule:** Back, Esc, scrim-tap and ✕ are the same action — *dismiss the top layer* — and exactly one module in the app owns `popstate`.

**Do**
- ✅ Push one history entry per opened overlay; pop one per dismissal.
- ✅ Route ✕ / scrim / Esc through `history.back()` so all paths converge.
- ✅ Keep a single app-wide `popstate` owner with a LIFO stack.
- ✅ Restore scroll and list state underneath.
- ✅ In multi-step flows, let Back walk *backwards through steps* before closing.

**Don't**
- ❌ Let a component add its own `popstate` listener.
- ❌ Close the overlay's DOM directly from a close button — the stack desyncs.
- ❌ Put ephemeral overlays in the URL just to make Back work.

**How it is enforced today**
- [x] 🟢 code — `BackStack` + `useBackHandler` / `usePageBackGuard`; overlay primitives are back-friendly by construction
- [x] 🟡 check — a grep-gate fails the build on any `addEventListener('popstate')` outside the owner
- [x] 🔴 prose — this entry

**Full pattern:** [back-friendly modals & overlays](../patterns/back-friendly-modals.md) · **Sample design:** [`showcases/back-friendly-modals/`](../../showcases/back-friendly-modals/)

## Related pains

- [PAIN-002](PAIN-002-every-row-click-loses-your-place.md) — same root cause, different surface: navigation that discards context the user built.
- Companion patterns: [lock scroll when a modal is open](../patterns/lock-scroll-when-modal-open.md), [swipe to dismiss](../patterns/swipe-to-dismiss-drawers.md).
