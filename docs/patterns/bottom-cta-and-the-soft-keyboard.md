---
title: Bottom CTAs & the soft keyboard — the content budget
summary: When the keyboard opens it takes half the screen; guarantee the content region keeps a minimum share of what's left (≈45%) and make the header and the CTA bar yield to pay for it. The bar belongs in the shell's flex flow — not position:fixed, not position:sticky.
category: pattern
tags: [mobile, keyboard, visualviewport, cta, forms, viewport, layout, app-shell]
platforms: [mobile-web, pwa]
archetypes: [consumer-mobile, ecommerce, fancy-app]
status: draft
related:
  - bottom-sheet-and-thumb-zone.md
  - inline-form-validation.md
  - ../ui/full-height-and-the-mobile-viewport.md
  - ../pains/PAIN-004-keyboard-crushes-the-form.md
last_updated: 2026-07-30
---

# Bottom CTAs & the soft keyboard — the content budget

> A bottom-anchored CTA is the right call at rest. Then the keyboard opens, takes 40–62% of the screen, and **nothing in the layout gives anything back** — so the form collapses into a sliver between a header that kept its full height and a button the user doesn't need yet.
>
> *"Sticky" here means bottom-anchored, not `position: sticky` — which, as it turns out, is one of the two ways to get this wrong.*

## Why it matters

The soft keyboard is the single largest layout event on mobile, and it is the one CSS cannot see. The chrome is sized for a screen that no longer exists, and the squeeze comes from both directions at once:

- the field's **label and hint scroll out of view** while the user is typing into it — they are answering a question they can no longer read
- the **next field and any validation error** sit behind the CTA
- on a multi-step form this repeats on **every step**

The fix is not "remove the CTA." It is to decide, in advance, **how little content is acceptable** — and make the chrome the thing that pays.

## The guideline

**Rule:** the scrollable content region must never fall below **45% of the visible viewport**. Chrome yields until that holds.

**Do**

- ✅ Measure the keyboard with `window.visualViewport` and publish it as a CSS variable. There is no CSS-only signal.
- ✅ Make the bar a **flex row of the app shell** — a sibling of the scroll region — not `position: fixed` and not `position: sticky`. See *Where to put the bar* below.
- ✅ Define a **degradation ladder** and run it in order until the budget is met, re-measuring between rungs so you only give up what you must:
  - **L0** — full size. The CTA is a pinned row of the shell. This is the keyboard-closed state, and the keyboard-open state whenever there is room to spare.
  - **L1** — **the CTA leaves the shell.** It moves into the scroll region and flows to the end of the form, where the user reaches it by scrolling. **Spend this first:** it is the biggest single saving (the whole bar) and the cheapest, because while the keyboard is open its job is already done by the keyboard's own *next/done* key. It comes back the instant the keyboard closes.
  - **L2** — the header compacts as well: drop the subtitle, the step *labels* (keep the bars), the section tab, shrink the logo. **Spend this last** — knowing which step you are on is worth more than a button you can scroll to.
- ✅ **Pin the page at `scrollY = 0`** while the shell is fixed. iOS scrolls the *layout* viewport to reveal the focused input, dragging the shell — and its bottom row — off screen.
- ✅ On focus, wait for the keyboard animation to settle (~250 ms), re-measure, then `scrollIntoView({ block: 'center' })`. A preserved region is useless if the focused field isn't in it.
- ✅ Keep the field's **label, hint and error** in the same scroll-into-view unit as the input — those are what the user needs while typing.
- ✅ Verify on a **real phone**, both platforms. See the platform note below.

**Don't**

- ❌ Size the app shell with `100vh` / `100dvh` / `100svh` and expect the keyboard to be accounted for. Those units track the *layout* viewport, which iOS Safari does not shrink for the keyboard.
- ❌ Use `position: fixed; bottom: 0` for the CTA. On Android it rides up and crushes the content; on iOS it is displaced by the page scroll the keyboard triggers, so the button appears and disappears depending on scroll position.
- ❌ Reach for `position: sticky` as the safe alternative. It is still an overlay — it hides content behind it, and whether it is pinned depends on scroll position and on the scroll container behaving. A shell row is unconditional.
- ❌ **Transition any property the budget measures** (`bottom`, heights, paddings). The first measurement then reads the *pre-keyboard* layout, the ladder concludes there is plenty of room, and it silently never escalates — the exact failure this pattern exists to prevent. See *The measurement trap* below.
- ❌ Hide the whole header on focus as a reflex. Losing the step indicator mid-form is its own confusion — compact it first, remove it only if the budget still fails.
- ❌ Ship a `min-height` on the page and call it done. It restores *scrollability*, but the CTA still covers the focused field.

## Measuring the keyboard

```js
const vv = window.visualViewport;
const kb = Math.max(0, window.innerHeight - vv.height - vv.offsetTop);
document.documentElement.style.setProperty('--kb', kb + 'px');
if (window.scrollY !== 0) window.scrollTo(0, 0);   // iOS drags the fixed shell — pin it
```

## Where to put the bar

Three candidates, and the usual two are both wrong:

| | Behaviour | Verdict |
|---|---|---|
| `position: fixed; bottom: 0` | anchored to the layout viewport, which the keyboard doesn't change on iOS | ❌ displaced by iOS's scroll-to-input; rides up and crushes content on Android |
| `position: sticky; bottom: 0` | pinned only while its natural position is below the fold; still an overlay | ❌ visibility depends on scroll position; hides content behind it |
| **a flex row of the shell** | real layout: takes its own space, above the scroll region | ✅ always visible, never covers anything |

```css
.app    { position: absolute; inset: 0; bottom: var(--kb, 0px);   /* = the visible viewport */
          display: flex; flex-direction: column; min-height: 0; }
.appbar { flex: none; }
.scroll { flex: 1 1 auto; min-height: 0; overflow-y: auto; }
.ctabar { flex: none; }
```

Because the scroll region is sized to *exclude* the bar, `scroll.clientHeight` **is** the readable content region — no arithmetic, nothing hidden behind anything. And "leave the shell" at L3 becomes moving one node:

```js
(level === 3 ? scroll : app).appendChild(ctabar);
```

## Enforcing the budget

One measurement per rung, because chrome height is only knowable after layout:

```js
const visible = stage - kb;
const min = Math.max(130, visible * 0.45);
for (level = 0; level < 2; level++) {
  root.dataset.level = level;
  placeCta(level);                    // level >= 1 → CTA moves into the scroller
  if (scroll.clientHeight >= min) break;
}
root.dataset.level = level;           // falls through to 2 → the header compacts too
placeCta(level);
```

If the loop exits at 2 and the budget *still* is not met, that is a real signal: the surface needs fewer fields or a different flow, not a fourth rung. Say so in the log rather than pretending.

## The measurement trap

This ladder measures layout synchronously and then decides. That makes it fragile in one specific way, and it is worth stating on its own because it fails **silently**:

```css
.app { bottom: var(--kb); transition: bottom .18s ease; }   /* ← poison */
```

With that transition, `scroll.clientHeight` right after `--kb` changes returns the height the shell had *before* the keyboard opened. The budget compares a stale, generous number against the new, smaller viewport, concludes L0 is fine, and never escalates. The readout gives it away — content larger than the viewport it is supposed to fit inside, and a **negative** chrome height.

**Never animate a property the budget measures.** You do not need to: the keyboard's own animation is the transition. `visualViewport` fires `resize` continuously while the keyboard slides, so an untransitioned shell tracks it frame by frame and looks smooth for free. If you must animate something, animate a property outside the measurement chain (opacity, transform) — or defer the measurement to `transitionend`, which is strictly more code for a worse result.

## Platform note

The same code fails differently, which is why one-device testing misses it:

| | Layout viewport on keyboard open | What breaks |
|---|---|---|
| **Android / Chrome** (default `resizes-visual`) | unchanged; visual viewport shrinks | `position: fixed` CTA rides above the keyboard and crushes content |
| **iOS Safari** | unchanged; the page is scrolled instead | the page scroll drags a fixed shell up, so the CTA slides off screen — it appears or disappears depending on scroll position |
| **`interactive-widget=resizes-content`** (viewport meta, Chromium) | shrinks | consistent, but not universally supported — treat it as an enhancement, not the mechanism |

`window.visualViewport` is the one signal that behaves the same everywhere, which is why the budget is computed from it rather than from viewport units.

## Trade-offs

**Un-pinning the CTA is the first rung, not the last.** The instinct is to protect the button and shave the chrome around it — it was pinned for a reason. But while the keyboard is open the button is the one piece of chrome whose job is already covered: the keyboard's *next/done* key advances the form. So it is both the largest saving and the cheapest, and it should be spent before anything the user is actually reading. It returns the moment the keyboard closes, so the at-rest design — the reason it is pinned at all — is untouched.

**A CTA you scroll to is not a lost CTA.** The form is scrollable anyway; the button sits at its end, which is where a form's submit button has always lived. What you give up is *one tap away* becoming *a scroll and a tap away*, and only while typing.

**45% is a starting number, not a law.** What it encodes is "the focused field plus its label plus one line of hint, and evidence there is more form below." If your fields are taller, your budget is bigger.

**The chrome now changes shape on focus.** That is movement, and movement is a cost. Keep it small, transition it, and make it fully reversible — a user who focuses and blurs repeatedly will otherwise watch the header breathe.

## Sample design

- [`showcases/keyboard-content-budget/`](../../showcases/keyboard-content-budget/) — a five-step form with a `broken ⇄ budget` toggle, a live readout of the content share, and a simulated keyboard so it can be inspected on a desktop browser. On a phone it drives off the real `visualViewport`.

## Related

- [PAIN-004 — the keyboard opens and the form is crushed](../pains/PAIN-004-keyboard-crushes-the-form.md)
- [Bottom sheets & the thumb zone](bottom-sheet-and-thumb-zone.md) — why the CTA is down there in the first place
- [Full-height sections & the mobile viewport](../ui/full-height-and-the-mobile-viewport.md) — the other half of the viewport-units problem
- [Inline form validation](inline-form-validation.md) — the error message is part of what the budget protects
