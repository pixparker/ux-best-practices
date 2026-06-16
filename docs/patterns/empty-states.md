---
title: Empty states
summary: Turn "nothing here" into onboarding — explain what goes here, why it's empty, and the one action to fill it.
category: pattern
tags: [empty-state, onboarding, first-run, no-results, states]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../principles/design-every-state.md
last_updated: 2026-06-16
---

# Empty states

> The empty state is often a user's *first* impression of a feature. A blank screen says "broken"; a good empty state says "here's what this does and how to start."

## Why it matters

New users meet empty states constantly — empty inbox, no projects, zero results. Done well, they onboard and convert. Done badly (blank), they confuse and stall. Empty states are not edge cases; they are the front door.

## The three kinds (handle each differently)

| Kind | Trigger | Goal |
| --- | --- | --- |
| **First-run** | User has created nothing yet | Teach + invite the first action |
| **No-results** | Search/filter returns nothing | Explain why + help adjust |
| **Cleared / done** | User finished or emptied a list | Reassure (e.g., "All caught up ✅") |

## The guideline

**Do**

- ✅ State **what belongs here** and the **value** of adding it.
- ✅ Give **one clear primary action** ("Create your first invoice").
- ✅ For **no-results**, suggest a fix ("Clear filters", check spelling, broaden search).
- ✅ Keep it light — a short line + action beats a giant illustration with no CTA.
- ✅ Consider a subtle, optional illustration/icon for warmth — not as a replacement for guidance.

**Don't**

- ❌ Show a blank area or just "No data".
- ❌ Treat first-run and no-results the same (different messages, different actions).
- ❌ Bury the action or offer none.
- ❌ Over-design with huge graphics that push the CTA below the fold.

## Pitfalls & anti-patterns

- **Decorative-only** empty states with no next step.
- **Same copy everywhere** regardless of cause.
- **Guilt/empty-handed tone** instead of an inviting one.

## Notes from experience

> *(draft — replace with your own)* The first-run empty state is prime onboarding real estate that most MVPs waste. One sentence of "what + why" plus a single primary button measurably lifts activation.

## References

- NN/g — *Empty States*
- emptystat.es / pttrns — pattern galleries
