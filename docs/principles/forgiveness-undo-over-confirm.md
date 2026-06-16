---
title: "Forgiveness: prefer undo over confirm"
summary: Let users act fast and recover from mistakes — favor reversible actions and undo over interruptive confirm dialogs.
category: principle
tags: [forgiveness, undo, error-prevention, trust, confirmation]
status: draft
related:
  - feedback-for-every-action.md
  - design-every-state.md
last_updated: 2026-06-16
---

# Forgiveness: prefer undo over confirm

> Good UX makes mistakes cheap to recover from rather than hard to make. A confirm dialog interrupts *everyone* to catch the rare misclick; undo lets everyone move fast and rescues the few who slip.

## Why it matters

Confirmation dialogs train users to click "Yes" reflexively — so they stop preventing the very mistakes they exist for, while taxing every correct action with friction. Reversibility is almost always the better design: act immediately, and offer a clear, time-boxed way back.

## The guideline

**Do**

- ✅ Default to **reversible actions** with an **Undo** (toast/snackbar) for deletes, archives, sends, bulk ops.
- ✅ Keep undo available long enough to notice (~5–10s) or until the next action.
- ✅ Make state changes feel safe: soft-delete first, hard-delete later/in background.
- ✅ Reserve **confirm dialogs** for the genuinely irreversible & high-stakes (permanent delete, money, data loss) — and state the consequence + the count.
- ✅ Support `Esc`/back to cancel, and never lose typed input.

**Don't**

- ❌ Block every action with "Are you sure?" — it becomes muscle-memory noise.
- ❌ Make destructive actions one-click *and* irreversible.
- ❌ Use a vague confirm ("Delete?") with no scope ("Delete 42 orders?").
- ❌ Hide whether an action can be undone.

## Confirm vs. Undo — quick rule

| Action | Pattern |
| --- | --- |
| Delete a row, archive, mark done, send message | **Undo** (do it, offer rollback) |
| Permanently delete account / wipe data / irreversible payment | **Confirm** (type-to-confirm for the worst cases) |

## Pitfalls & anti-patterns

- **Confirm fatigue** — too many dialogs = reflexive approval = no protection.
- **Fake undo** — offering undo for something you can't actually reverse.
- **Silent destruction** — deleting with neither confirm nor undo.

## Notes from experience

> *(draft — replace with your own)* Swapping "Are you sure?" dialogs for an undo toast almost always tests better: people feel the app is faster *and* safer. Keep the dialog only where reversal is truly impossible.

## References

- Aza Raskin — *Never Use a Warning When you Mean Undo*
- NN/g — *Confirmation Dialogs* guidance
