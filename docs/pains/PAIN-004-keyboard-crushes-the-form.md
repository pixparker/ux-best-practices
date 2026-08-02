---
id: PAIN-004
title: The keyboard opens and the bottom CTA crushes the form
pain: A sticky bottom CTA is perfect at rest; the moment the soft keyboard takes half the screen, the header and the CTA keep every pixel and the form collapses to a sliver — the user types into a field whose label has scrolled away.
category: pain
tags: [mobile, keyboard, visualviewport, bottom-cta, forms, viewport, layout, app-shell]
platforms: [mobile-web, pwa]
archetypes: [consumer-mobile, ecommerce, fancy-app]
severity: friction
status: mitigated
enforcement: prose
enforced-by: ""
solution: ../patterns/bottom-cta-and-the-soft-keyboard.md
showcase: ../../showcases/keyboard-content-budget/
first-seen: 2026-07-30
last_updated: 2026-07-30
---

# PAIN-004 — The keyboard opens and the bottom CTA crushes the form

> **The pain.** We put the primary action in a sticky bottom bar so it is always thumb-reachable. Then the user taps a text field, the soft keyboard takes 40–62% of the screen — and **nothing in the layout gives anything up.** The header keeps its full height, the CTA keeps its full height, and what is left for the actual form is about one and a half fields.

## 1. Pain point

A five-step lead-capture form on a phone. Step 1 asks for name, business and mobile number. At rest it reads well: brand row, step indicator, a section title, a line of explanation, three labelled fields, and a sticky **Continue** button parked at the bottom where the thumb is.

The user taps the first field.

The keyboard slides up and claims roughly half the screen. What remains is shared between:

- the sticky header — brand row + 5-step indicator, unchanged
- the bottom CTA — a tall bar, generous padding, a full-width button, unchanged
- whatever content survives in between

The content is what loses. In the state we captured, the visible form was **one field and a clipped fragment of the next**. The section title and the explanatory line — the text that says *what this step is for* — were gone. The user was answering a question they could no longer see, in a viewport whose largest single element was a button they would not need until they had finished typing.

**What they expected:** *"the keyboard covers the bottom of the screen, so the top of the screen is still mine."* Instead the keyboard took from the bottom **and** the chrome kept its full share, so the content was squeezed from both directions at once.

**What it costs:**

- **Typing blind.** The label, the hint and any validation error are off-screen or behind the CTA. The user cannot tell what format is wanted, and cannot see why *Continue* is disabled — which reads as the form being broken rather than incomplete.
- **It repeats.** On a five-step form this is not one bad moment, it is five. And it lands hardest on step 1, where abandonment is cheapest for the user and most expensive for us.
- **Loss of orientation.** With the step indicator squeezed or scrolled away, the user loses the "3 more steps" context that was the reason for putting a stepper there.

**Why it happens — the actual cause.** Three things compound:

1. **CSS cannot see the keyboard.** `100vh`, `100dvh`, `100svh` and `position: fixed` are anchored to the **layout** viewport. iOS Safari does not shrink the layout viewport when the keyboard opens — it scrolls the page instead. Chrome's default (`interactive-widget=resizes-visual`) also leaves it unchanged. So a layout built from viewport units has no idea the keyboard exists.
2. **The failure is platform-specific**, which is why one device does not find it. On Android the fixed CTA rides up above the keyboard and crushes the content. On iOS the same bar can end up *under* the keyboard, floating mid-screen, or covering the focused input. Same code, two different bugs.
3. **Nothing in the layout is marked optional.** Every element in the chrome claims its pixels unconditionally. No rule anywhere says *"these are the pixels to give back when space runs out."*

The first cause is a footgun. The third is the design mistake, and it is the one worth fixing.

## 2. Approach / solution

**Declare a content budget and make the chrome pay for it.**

The invariant: **the scrollable content region never falls below 45% of the visible viewport.** Everything else is negotiable.

Two mechanisms:

**a) Measure the keyboard.** The only signal that behaves the same on both platforms is `window.visualViewport`:

```js
const kb = Math.max(0, innerHeight - visualViewport.height - visualViewport.offsetTop);
```

Publish it as a CSS variable, size the app shell to `bottom: var(--kb)`, and the rest is plain CSS.

**b) Degrade the chrome in a defined order** until the budget holds — one rung at a time, re-measuring after each, because chrome height is only knowable after layout:

- **L0** — everything full size, CTA pinned to the shell. Keyboard closed, or open with room to spare.
- **L1** — **the CTA leaves the shell** and flows to the end of the form, reached by scrolling. This rung is spent *first*: it is the largest saving (the whole bar) and the cheapest, because while the keyboard is open the button's job is already done by the keyboard's own *next/done* key. It returns the moment the keyboard closes.
- **L2** — the header compacts as well: subtitle drops, step *labels* drop (the progress bars stay), section tab drops, logo shrinks. Spent last, because knowing which step you are on is worth more than a button you can scroll to.

Two things the budget does not do by itself:

- **Bring the field into the region.** On focus, wait for the keyboard animation to settle, re-measure, then scroll the focused field to the **centre** of the preserved region — with its label and hint. A guaranteed content region is worthless if the field lands outside it.
- **Pin the page.** iOS scrolls the *layout* viewport to reveal the focused input. Since the app shell is fixed to that viewport, the page scroll drags the shell — and its bottom row — off screen. Keep the page at `scrollY = 0`; the shell owns its own scrolling.

**Where the bar lives is the load-bearing decision.** Not `position: fixed` (iOS displaces it; Android rides it up over the content) and not `position: sticky` (still an overlay, and whether it is pinned depends on scroll position). The CTA is a **flex row of the app shell**, a sibling of the scroll region. It is then always visible regardless of scroll, it never covers content — the scroll region is sized to exclude it — and `scroll.clientHeight` *is* the readable region, with no arithmetic. "Leave the shell" at L1 is then just moving that one node into the scroller.

**Rejected — and why:**

- ***A `min-height` on the page, with the CTA left pinned.*** The original instinct, and **most of it survived** — "guarantee the content a minimum height, and let the CTA sit at the end of a scrollable page" is exactly L1, and it turned out to be the rung that does the most work. What does *not* survive is doing the min-height **alone**: if the bar stays pinned, the page scrolls but the button still covers the focused field, and the user still cannot see what they are typing into. The un-pinning is the load-bearing half; the minimum height is what makes the un-pinned button reachable.
- ***`position: fixed; bottom: 0` for the CTA.*** The obvious construction and the source of the bug. It is anchored to the layout viewport, which the keyboard does not change on iOS — so when Safari scrolls the page to reveal the focused input, the whole shell is dragged up and the bar slides off screen.
- ***`position: sticky; bottom: 0` inside the scroll container.*** Our own first attempt, and it failed in review: the bar became **visible or hidden depending on scroll position**, which is worse than either alternative because it is intermittent. Sticky is still an overlay — it hides content behind it — and being pinned at all depends on the element's natural position relative to the fold. **A shell row is unconditional; that is the whole advantage.**
- ***Compacting the chrome before un-pinning the CTA.*** Our own first ladder did this — shave the header, then shrink the button, and only un-pin as a last resort, on the theory that a button that disappears reads as broken. Measured, it is backwards: un-pinning returns ~84px for a cost the soft keyboard already covers (its *next/done* key advances the form), while compacting the header returns ~39px and takes away the step indicator, which is orientation the user cannot reconstruct. **Spend the button first; spend what the user is reading last.**
- ***Hide the entire header when a field gets focus.*** Cheap and effective on pixels, but it removes the step indicator mid-form — trading one disorientation for another. Compacting recovers most of the height at none of the cost; full removal is available at L2 if it is ever needed.
- ***`interactive-widget=resizes-content` in the viewport meta.*** Genuinely useful — it makes the layout viewport shrink so `dvh` becomes keyboard-aware — but support is not universal. It is an enhancement layered on top, not the mechanism.
- ***`env(keyboard-inset-height)` via the VirtualKeyboard API.*** The cleanest API by far, and Chromium-only. Same verdict: enhancement, not mechanism.
- ***Fixed pixel budget (e.g. "content ≥ 220px").*** Breaks on small phones, where 220px may be more than the visible viewport has to give. A percentage with a small floor degrades sensibly on every screen.
- ***Never pin the CTA at all — always put the button at the end of the form.*** Solves the pain outright, and is a defensible choice. It is L1 applied unconditionally, and it gives up the at-rest thumb-reachability that put the bar there in the first place. Keep it conditional: pinned while the keyboard is closed, in-flow while it is open.

> 🔒 Binding: **when the keyboard is open, the readable content region must keep a usable share of the visible viewport.** Our answer is a 45% budget with a three-rung ladder. A design that gets there by another route — a shorter chrome, a one-field-per-screen flow, a full-screen field editor — satisfies this just as well.

## 3. The result

Measured in the showcase on a 720px screen, same form, same keyboard:

| Keyboard | Broken | With the budget | Rung reached |
|---|---|---|---|
| 45% | 119px readable (**30%**) | 202px (**51%**) | L1 — CTA leaves the shell, header untouched |
| 55% | 47px (**15%**) | 203px (**63%**) | L2 — header compacts too |
| 62% | **0px (0%)** | 153px (**56%**) | L2 |

At 30% the user sees a heading and a clipped field label. At 15% they see the heading and nothing else. At 62% — a keyboard with a suggestion strip and a toolbar, which is an ordinary configuration, not an edge case — **the form is gone entirely**: the screen is a header, a debug line and a button. With the budget, all three cases show the heading, the field, its label *and* its hint, with evidence that more form follows. Chrome drops from 277px to 194px at 45% — and note what that buys: at 45% the **entire header survives intact**, subtitle, step labels and all. Un-pinning the CTA alone was enough. The CTA returns to full size the moment the keyboard closes, so the at-rest design — the reason the bar is down there at all — is unchanged.

**Be honest about the maturity:** the numbers above are measured in the showcase against a *simulated* keyboard. The two rejected constructions below were caught on a real phone; **the current one has not yet been re-confirmed there**, and it has not been through a ship-and-watch cycle on either platform. That is why the status is `mitigated`, not `solved`. Update this section when it has.

**What the build itself taught us.** Three drafts, three different ways to be wrong, and none of them were caught by reading the code:

1. **`position: fixed`** made the CTA's visibility conditional on iOS's page scroll.
2. **`position: sticky`** made it conditional on scroll position inside the form. Both were found by someone simply opening the keyboard and scrolling. The fix — make the bar a real row of the shell — is less clever than either and has no conditions at all. **When a bar promises "always visible" but is built from a mechanism that cannot keep that promise, the promise is what breaks.**
3. **A `transition: bottom` on the shell** meant the budget measured the *pre-keyboard* height, decided nothing needed to change, and stayed at L0 — reproducing the original pain in code that reported success. It was invisible on page load (no transition runs) and only appeared when a human toggled the keyboard. **A rule that measures its own layout must not animate what it measures**, and it needs a visible readout, because a silent wrong answer looks exactly like a right one.

All three were found the same way: by a person opening the keyboard and looking, not by review. That is an argument for the demo, and against trusting the ladder until it prints its numbers on screen.

**What it does not fix:**

- **Landscape on a small phone.** With the keyboard open in landscape there may be no arrangement that satisfies the budget. At that point the honest answer is a different flow — a full-screen field editor, or one question per screen — not a smarter ladder.
- **Tall single inputs.** A textarea or a rich editor can exceed the whole budget by itself. Those need the field to own the viewport, not to be one item in a scrolling form.
- **Third-party keyboards** with suggestion strips, clipboard bars and toolbars take more than the system keyboard. The measurement handles it; the ladder may simply run out of rungs.

**A new problem it introduces:** the chrome now changes shape when a field is focused. That is movement, and movement is a cost. It is kept small (a subtitle and some labels), it is transitioned, and it is reversible — but a user who focuses and blurs repeatedly will see the header breathe. Worth watching in real use.

## 4. Best practice

**Rule:** When the soft keyboard is open, the readable content region must keep at least **45% of the visible viewport** — measured from `window.visualViewport`, paid for by compacting the chrome and, if needed, un-sticking the CTA.

**Do**

- ✅ Compute the keyboard inset from `window.visualViewport` and publish it as a CSS variable. It is the only cross-platform signal.
- ✅ Make the bottom bar a **flex row of the app shell**, so its visibility has no conditions attached.
- ✅ Write down the ladder before you need it, and order it by *cost to the user*, not by what looks expendable: the pinned CTA goes first, the header's orientation cues go last.
- ✅ Keep the measurement synchronous and honest — see the anti-pattern below.
- ✅ Pin the page at `scrollY = 0` when the shell is fixed to the layout viewport.
- ✅ After focus, let the keyboard settle, re-measure, then scroll the field **and its label and hint** into the centre of the preserved region.
- ✅ Test on a **real iOS device and a real Android device**, and **scroll while the keyboard is open** — that is the gesture that exposes it.

**Don't**

- ❌ Assume `100vh` / `100dvh` / `100svh` account for the keyboard. They do not.
- ❌ Use `position: fixed; bottom: 0` for the CTA — nor `position: sticky` as the "safe" alternative. Both make visibility conditional on scroll position.
- ❌ **Transition a property the budget measures** (`bottom`, heights, paddings). The first measurement then reads the pre-keyboard layout and the ladder silently never escalates — you get the original pain back with code that believes it is working.
- ❌ Fix this with a page `min-height` alone — that restores scrolling, not visibility.
- ❌ Budget in fixed pixels; small phones cannot pay.

**How it is enforced today**

- [ ] 🟢 code — *not yet: a `KeyboardAwareScreen` shell that owns the measurement and the ladder is the obvious primitive, and would make the wrong layout hard to write*
- [ ] 🟡 check — *not yet: a lint could flag `position: fixed` + `bottom: 0` on any element inside a form surface*
- [x] 🔴 prose — this entry

> 🔴 Prose-only, and this one is a strong candidate for 🟢: every form we ship needs the same shell, and hand-rolling the `visualViewport` maths per product is exactly how this regresses.

**Full write-up:** [bottom CTAs & the soft keyboard](../patterns/bottom-cta-and-the-soft-keyboard.md) · **Sample design:** [`showcases/keyboard-content-budget/`](../../showcases/keyboard-content-budget/)

## Related pains

- [PAIN-003](PAIN-003-full-height-sections-jump-mid-scroll.md) — the other half of the viewport problem. Both come from the same root cause: **CSS viewport units describe a viewport the user is not looking at.** PAIN-003 is the address bar, this is the keyboard.
- Companion craft: [bottom sheets & the thumb zone](../patterns/bottom-sheet-and-thumb-zone.md) — why the CTA is at the bottom to begin with; [inline form validation](../patterns/inline-form-validation.md) — the error message is part of what the budget must protect.
