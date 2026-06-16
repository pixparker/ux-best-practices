---
title: Inline form validation
summary: Validate on blur with clear, adjacent messages — guide users to success instead of scolding them after submit.
category: pattern
tags: [forms, validation, input, feedback, errors]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../principles/feedback-for-every-action.md
  - ../principles/design-every-state.md
last_updated: 2026-06-16
---

# Inline form validation

> Tell users about a problem with a field **as they finish it**, right next to it — not in a red wall after they hit submit. Validation should feel like a helpful guide, not a gatekeeper.

## Why it matters

Submit-only validation makes users fill the whole form, get rejected, then hunt for what's wrong. Validating on every keystroke yells at people before they've finished typing. The sweet spot — **validate on blur, re-validate on change once an error exists** — catches problems early without nagging.

## The guideline

**Do**

- ✅ Validate a field **on blur** (when the user leaves it), not on every keystroke.
- ✅ Once a field is in an error state, **re-validate on input** so the error clears as soon as it's fixed.
- ✅ Put the message **adjacent to the field**, in plain language, saying how to fix it.
- ✅ Show **positive confirmation** for important fields (a check on a valid, unique username).
- ✅ Use the right input type/inputmode and `autocomplete` so fewer errors happen at all.
- ✅ On submit, focus and scroll to the **first invalid field**.

**Don't**

- ❌ Validate aggressively on first keystroke ("invalid email" while still typing).
- ❌ Surface all errors only after submit with no inline anchoring.
- ❌ Use vague messages ("Invalid input") — say *what* and *how to fix*.
- ❌ Rely on color alone (red border) — add text + icon for accessibility.
- ❌ Clear the user's entries on a failed submit.

## Accessibility

- Associate messages with inputs via `aria-describedby`; set `aria-invalid="true"` on error.
- Ensure error text meets contrast and isn't conveyed by color only.

## Pitfalls & anti-patterns

- **Premature validation** — erroring before the field is complete.
- **Disabled submit with no explanation** — users can't tell what's missing.
- **Generic messages** — "Error" teaches nothing.

## Notes from experience

> *(draft — replace with your own)* "Validate on blur, re-validate on change after the first error" is the rule that makes forms feel helpful instead of hostile. Pair it with correct `inputmode`/`autocomplete` and error rates drop before validation even fires.

## References

- NN/g — *Inline Validation in Web Forms*
- GOV.UK Design System — error messages & summaries
