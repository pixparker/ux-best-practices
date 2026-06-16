---
title: Optimistic UI
summary: For high-confidence actions, update the UI instantly and reconcile with the server in the background — roll back on failure.
category: technique
tags: [perceived-performance, optimistic, responsiveness, state, feedback]
platforms: [mobile-web, pwa, desktop, web]
status: draft
related:
  - ../principles/feedback-for-every-action.md
  - skeleton-loading.md
last_updated: 2026-06-16
---

# Optimistic UI

> Don't make users wait for the server to confirm what will almost certainly succeed. Apply the change immediately, send the request in the background, and quietly fix things only if it fails.

## Why it matters

A like, a checkbox toggle, a reorder, adding to cart — these succeed ~99% of the time. Blocking the UI behind a spinner on each one makes a fast app feel sluggish. Optimistic updates make interactions feel **instant**, which is the single biggest perceived-speed lever after skeletons.

## The guideline

**Do**

- ✅ Use it for **high-confidence, low-stakes, easily-reversible** actions (toggles, likes, add-to-cart, reorder, inline edits).
- ✅ Apply the change to local state **immediately**; fire the request in the background.
- ✅ On failure, **roll back** to the previous state and tell the user (toast: "Couldn't save — retry").
- ✅ Keep an undo/retry path; preserve the user's intent.
- ✅ Reconcile with the server response (e.g., real IDs, server-computed fields) when it returns.

**Don't**

- ❌ Be optimistic about **destructive or irreversible** actions (payments, permanent deletes).
- ❌ Be optimistic when **failure is likely** or success depends on server validation you can't predict.
- ❌ Roll back silently — a value that snaps back with no explanation feels like a bug.
- ❌ Lose the user's input on rollback.

## Pattern shape

1. Snapshot current state.
2. Apply expected result locally → UI updates now.
3. Send request.
4. **Success:** reconcile with server data.
5. **Failure:** restore snapshot + surface a clear error/retry.

## Pitfalls & anti-patterns

- **Optimism everywhere** — using it for risky actions causes confusing reversals.
- **No rollback** — drift between UI and server state.
- **Silent failure** — the user thinks it saved; it didn't.

## Notes from experience

> *(draft — replace with your own)* Optimistic toggles + add-to-cart make an app feel "native fast" on the same backend. The discipline is the rollback path: the technique is only as good as how gracefully it handles the 1% failure.

## References

- Designing optimistic updates (TanStack Query / SWR docs)
- Optimistic UI patterns — various engineering write-ups
