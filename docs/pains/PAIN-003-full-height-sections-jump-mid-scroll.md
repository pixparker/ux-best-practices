---
id: PAIN-003
title: Full-height sections resize and jerk the page mid-scroll
pain: A 100vh hero looks perfect in the design tool, then on a phone it resizes the instant the address bar hides — and the whole page jumps under the user's finger.
category: pain
tags: [mobile, viewport, 100vh, svh, dvh, hero, layout, scroll-jump]
platforms: [mobile-web, pwa, tablet]
archetypes: [consumer-mobile, ecommerce, fancy-app]
severity: friction
status: solved
enforcement: prose
enforced-by: ""
solution: ../ui/full-height-and-the-mobile-viewport.md
showcase: ../../showcases/full-height-hero/
first-seen: 2026-06-22
last_updated: 2026-07-29
---

# PAIN-003 — Full-height sections resize and jerk the page mid-scroll

> **The pain.** A full-height hero is built with `height: 100vh`. It is flawless on desktop and in the design tool. On a real phone it either sits partly hidden behind the address bar, or — worse — **resizes the moment the bar collapses, yanking the page under the user's thumb.**

## 1. Pain point

Mobile browsers change the visible area *while you scroll*. The address bar is shown when the page loads, then collapses once you scroll down, changing viewport height by roughly 60–100px mid-gesture.

If the first section on the page is tied to that changing height, it resizes live. Because everything below it shifts by the same amount, **the user's scroll position jumps** — mid-swipe, with their finger still on the glass. It reads as the page fighting them.

This one is particularly nasty for three reasons:

- **It is invisible where it is built.** Desktop browsers have no collapsing address bar, and device emulators usually don't simulate one. The bug does not exist until a real phone touches it.
- **It hits the hero** — the first impression, the most design-attention-per-pixel surface on the site.
- **It looks like a performance problem.** The jump is easily misread as jank or a slow image, sending people to optimise the wrong thing entirely.

**Why it happens:** `100vh` does not mean "the height I can see." It is one of four different viewport units with genuinely different behaviours, and the intuitive-sounding one is the wrong default. `dvh` — the unit whose name suggests it adapts correctly — is the one that guarantees the jump on large sections.

## 2. Approach / solution

Size large sections with a **static** viewport unit, so the box never changes while the user scrolls.

- Use **`100svh`** (small viewport — as if the address bar is always shown) for full-height sections, with `100vh` as the fallback for older engines. It fits the visible area on load and **never grows**, so there is nothing to jump.
- **Avoid `dvh` for big sections.** It is the live viewport, so it resizes exactly when the user is mid-scroll. Keep it for small chrome — a sticky bar — where a resize is imperceptible.
- If you need the *initial* height precisely, freeze a measurement of `innerHeight` on load and use that; don't track it.
- Respect `env(safe-area-inset-*)` so content clears notches and home indicators.

**Rejected — and why:**
- *`100dvh`.* The name is a trap. It resizes by design; that is the whole pain.
- *JS resize listeners that re-measure and re-apply height.* This makes the resize a scripted animation instead of a browser one — the jump is still there, now with jank on top.
- *`lvh`.* Static, so no jump, but the bottom of the section starts hidden behind the address bar — you trade a jump for a crop.

> 🔒 Binding: **a full-height section must not change size while the user scrolls.** `svh` is our answer; a frozen measurement or a fixed-height design satisfies it just as well.

## 3. The result

The hero stopped moving. The section is very slightly shorter than the absolute maximum screen area — the cost of `svh` — and that trade is invisible to users, whereas the jump was not.

**What it did not fix:** anything that has to fill the *live* viewport exactly (a fullscreen media player, a canvas) still needs the dynamic unit and must handle resizing deliberately rather than pretending it won't happen.

**The broader lesson:** this class of bug is only findable on a real device. It is the strongest argument in this repo for **testing on an actual phone before calling a surface done** — no emulator surfaced it, and no amount of design review would have.

## 4. Best practice

**Rule:** Size full-height sections with a static viewport unit (`svh`, fallback `vh`). Never `dvh` for anything large enough that a resize is visible.

**Do**
- ✅ `min-height: 100vh; min-height: 100svh;` — fallback first, then the modern unit.
- ✅ Reserve `dvh` for small chrome where a resize cannot be perceived.
- ✅ Add `env(safe-area-inset-*)` padding for notches and home indicators.
- ✅ **Verify on a real phone**, scrolling until the address bar collapses.

**Don't**
- ❌ Use `100dvh` on a hero or any full-height section.
- ❌ Re-apply height from a JS resize listener.
- ❌ Trust a desktop browser or an emulator to reveal this.

**How it is enforced today**
- [ ] 🟢 code — *not yet: a layout primitive could own full-height sizing*
- [ ] 🟡 check — *not yet: a stylelint rule banning `dvh` on large sections is straightforward and unwritten*
- [x] 🔴 prose — this entry

> 🔴 This pain is **prose-only**, which means it is one careless `100vh` away from returning. The lint rule is the obvious next step.

**Full write-up:** [full-height sections & the mobile viewport](../ui/full-height-and-the-mobile-viewport.md) · **Sample design:** [`showcases/full-height-hero/`](../../showcases/full-height-hero/)

## Related pains

- Companion craft: [spacing & layout](../ui/spacing-and-layout.md), [tap & touch feedback](../ui/tap-and-touch-feedback.md) — the other two "only visible on a real device" categories.
