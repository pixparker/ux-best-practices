---
title: Accessibility (a11y) checklist
summary: A pragmatic baseline to make any UI usable by keyboard, screen reader, and low-vision users — run before shipping.
category: checklist
tags: [accessibility, a11y, wcag, keyboard, screen-reader, inclusive]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../ui/color-contrast-and-dark-mode.md
  - ../principles/feedback-for-every-action.md
last_updated: 2026-06-16
---

# Accessibility (a11y) checklist

> Accessibility isn't a separate feature — it's whether your app works for everyone. This is a pragmatic baseline (roughly WCAG 2.2 AA) that catches the issues that matter most, fastest.

## Semantics & structure
- [ ] Use **semantic HTML** (`button`, `a`, `nav`, `main`, headings) before reaching for ARIA.
- [ ] One logical **heading order** (`h1` → `h2` …), not chosen for size.
- [ ] Buttons do actions; links navigate — don't swap them.
- [ ] Every form control has an associated **`<label>`**.

## Keyboard
- [ ] Everything interactive is **reachable and operable by keyboard** (Tab/Shift-Tab/Enter/Space/Esc).
- [ ] **Visible focus** indicator on all focusable elements (never `outline: none` with no replacement).
- [ ] Logical **focus order**; no keyboard traps.
- [ ] Modals/sheets trap focus while open and **return focus** to the trigger on close.

## Screen reader
- [ ] Images have meaningful `alt` (or `alt=""` if decorative).
- [ ] Icon-only controls have an **accessible name** (`aria-label`).
- [ ] Dynamic updates (toasts, validation, loading) use **live regions** (`aria-live`).
- [ ] State exposed: `aria-invalid`, `aria-expanded`, `aria-pressed`, etc.

## Visual
- [ ] Text contrast meets **AA** (4.5:1 body / 3:1 large & UI) — [color & contrast](../ui/color-contrast-and-dark-mode.md).
- [ ] **Never color-only** signals — pair with text/icon/shape.
- [ ] Layout works at **200% zoom** and reflows without horizontal scroll.
- [ ] Respects `prefers-reduced-motion` and `prefers-color-scheme`.

## Touch & input
- [ ] Touch targets **≥ 44×44px** with spacing.
- [ ] Input `font-size ≥ 16px`; correct `inputmode`/`autocomplete`.
- [ ] No essential action depends on **hover** or fine pointer precision.

## Quick test pass
- [ ] Tab through the whole screen with no mouse.
- [ ] Run an automated check (axe / Lighthouse).
- [ ] Try a screen reader on the primary flow (VoiceOver / NVDA).
- [ ] Zoom to 200% and check reflow.

## Notes from experience

> *(draft — replace with your own)* Three fixes clear the majority of real issues: keep visible focus, give icon-only buttons names, and stop signaling state with color alone. Bake them into the component library so they're free on every screen.

## References

- WCAG 2.2 AA · WAI-ARIA Authoring Practices
- axe DevTools · Lighthouse accessibility audit
