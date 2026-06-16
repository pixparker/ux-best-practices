---
title: Design every state
summary: A screen isn't done until its empty, loading, error, and partial states are designed — not just the happy path.
category: principle
tags: [states, empty-state, error-handling, loading, robustness]
status: draft
related:
  - feedback-for-every-action.md
  - ../techniques/skeleton-loading.md
  - ../patterns/empty-states.md
last_updated: 2026-06-16
---

# Design every state

> The demo always shows the happy path with perfect data. Real users hit empty accounts, slow networks, and failures first. If those states aren't designed, your app *looks broken* exactly when trust matters most.

## Why it matters

Every screen that loads or shows data has at least four states, not one. Teams design the "full of perfect content" state, ship it, and the first real user — with no data yet, on a train, with an expired token — sees a blank screen or a raw error. The happy path is the *exception*; the other states are the everyday experience of onboarding and edge conditions.

## The guideline

For any data-driven view, deliberately design these states:

| State | When | What to show |
| --- | --- | --- |
| **Empty** | No data yet (first-run, no results, cleared) | What this is, why it's empty, the one action to fill it |
| **Loading** | Fetching | Skeleton (preferred) or progress — never a blank screen |
| **Partial** | Some data, more coming / some failed | Show what you have; indicate the rest |
| **Error** | Request failed | Plain-language cause + a way to recover (retry/back) |
| **Ideal** | Full, healthy data | The happy path |

**Do**

- ✅ Treat empty/loading/error as **first-class deliverables**, designed alongside the happy path.
- ✅ Distinguish **first-run empty** ("Let's add your first…") from **no-results empty** ("No matches — try clearing filters").
- ✅ Make every error **actionable**: what happened + what to do next.
- ✅ Preserve user input on error (don't wipe the form).

**Don't**

- ❌ Ship a screen tested only with seeded "perfect" data.
- ❌ Show a blank white screen while loading.
- ❌ Surface raw error codes/stack traces to users.
- ❌ Use one generic "Something went wrong" for every failure with no recovery.

## Pitfalls & anti-patterns

- **Empty = blank.** An empty state is an *opportunity to onboard*, not a void.
- **Spinner-for-everything** instead of skeletons → see [skeleton loading](../techniques/skeleton-loading.md).
- **Dead-end errors** with no retry trap the user.

## Notes from experience

> *(draft — replace with your own)* The single most common "bug" in an MVP review isn't a crash — it's a screen that looks broken because it was only ever tested with the founder's own fully-populated account. Add a checklist gate: no screen ships without its empty + error states.

## References

- Nielsen Norman Group — *Empty States*
- Maze / design-systems writing on UI states
