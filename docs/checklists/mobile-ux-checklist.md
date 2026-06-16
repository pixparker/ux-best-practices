---
title: Mobile UX checklist
summary: A pre-ship pass for any mobile-facing screen — touch, feedback, performance, accessibility.
category: checklist
tags: [mobile, checklist, pre-launch, accessibility]
platforms: [mobile-web, pwa]
status: draft
last_updated: 2026-06-16
---

# Mobile UX checklist

> Run this before shipping any mobile screen. If a box is unchecked, you have a known UX bug — decide consciously, don't ship by accident.

## Touch & layout
- [ ] Primary actions are reachable in the **thumb zone** (bottom third).
- [ ] Tap targets are **≥ 44×44px** with enough spacing to avoid mis-taps.
- [ ] No critical action depends on **hover** (there is none on touch).
- [ ] Layout respects **safe areas** (notch, home indicator) via `env(safe-area-inset-*)`.
- [ ] Content reflows for small/large text and landscape; nothing is cut off.

## Feedback & states
- [ ] Every tappable element has a **pressed state** (within 100ms).
- [ ] Async actions show a **loading state**; buttons disable to prevent double-submit.
- [ ] Every async action has a clear **success** and **error + recovery** path.
- [ ] **Empty states** are designed (first-run, no-results, error) — not blank.
- [ ] Loading uses **skeletons** over blank spinners where the layout is predictable.

## Input & forms
- [ ] Inputs use the right **keyboard/type** (`email`, `tel`, `numeric`, etc.).
- [ ] Input `font-size ≥ 16px` to avoid iOS zoom-on-focus.
- [ ] Validation is **inline** and on blur, with helpful messages.
- [ ] Autofill, autocomplete, and sane defaults are enabled.

## Performance (perceived)
- [ ] First meaningful paint feels fast on a **mid-range device / 3G-ish** network.
- [ ] No layout shift as content/images load (reserve space).
- [ ] Images are sized/lazy-loaded; no giant payloads.
- [ ] Interactions stay responsive (no jank on scroll/tap).

## Accessibility
- [ ] Text contrast meets **WCAG AA** (4.5:1 body / 3:1 large).
- [ ] Works with **screen reader** basics (labels, roles, focus order).
- [ ] Respects `prefers-reduced-motion`.
- [ ] Focus is visible and not trapped; modals return focus on close.

## Trust & polish
- [ ] Destructive actions are confirmable or **undoable**.
- [ ] Copy is clear, concise, and jargon-free for the audience.
- [ ] Icons have labels or accessible names; nothing is icon-only-and-ambiguous.

## Notes from experience

> The two boxes that catch the most real bugs in MVPs: **"buttons disable to prevent double-submit"** and **"empty states are designed."** Both are invisible in the happy-path demo and very visible the moment a real user hits a slow network or an empty account.
