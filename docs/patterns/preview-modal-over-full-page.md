---
title: "Preview-first: quick modal over full-page navigation"
summary: In data grids (esp. ops panels), open a fast preview modal with quick actions on row click; escalate to a full page only when the task is heavy — and never lose the filtered list.
category: pattern
tags: [ops-panel, admin, grid, table, modal, preview, navigation, productivity]
platforms: [web, desktop, mobile-web]
archetypes: [ops-admin-panel]
status: draft
related:
  - back-friendly-modals.md
  - lock-scroll-when-modal-open.md
  - responsive-tables-on-mobile.md
  - ../principles/reload-returns-to-main-content.md
  - ../archetypes/ops-admin-panel.md
last_updated: 2026-06-16
---

# Preview-first: quick modal over full-page navigation

> In a high-throughput ops panel, the user filters a grid, clicks a row to check or action an item, then goes back to the next one — dozens of times. If every click is a **full-page navigation**, each round-trip is slow *and* Back dumps them out of their filtered list, so they re-filter and hunt for their place again and again. Open a **preview** instead.

## Why it matters

Ops/admin users optimize for speed across many items. A full page per click costs them twice: the **load delay** to open it, and the **lost context** when they return (filters, sort, scroll, selection all reset). The result is the soul-crushing "filter → click → wait → back → re-filter → find my place → repeat" loop. A preview modal makes the common case instant and keeps the list exactly where they left it.

## The rule

**On row click → fast preview** (overview + quick actions). **Escalate to a full page only when there's substantial work there.** Otherwise the user acts and closes, still on their filtered list.

```
filter ──▶ click row ──▶ PREVIEW (overview + quick actions)
                              │
              ┌───────────────┼────────────────┐
        do a quick         need more?      next item (← / →)
        action & close   "Open full view"   without leaving
              │               │
              ▼               ▼
     back on the list   full page (heavy work) ──back──▶ preview ──back──▶ same list
```

## The guideline

**Do**

- ✅ Default the row click to a **preview modal**: status, key fields, and the **quick actions** that handle the common case (approve, mark paid, assign, change status).
- ✅ **Preserve list state** — filters, sort, search, page, scroll position, and selection — so closing the preview (or returning from full view) lands them exactly where they were.
- ✅ Offer an explicit **"Open full view / maximize"** to escalate when the task is heavy (editing, multi-step, lots of detail).
- ✅ Support **prev/next** within the preview (and keyboard ← / →, ↑/↓, Enter, Esc) so users can rip through items without returning to the grid each time.
- ✅ Make quick actions **optimistic** and reflected in the list immediately (see [optimistic UI](../techniques/optimistic-ui.md)).
- ✅ Reuse solid modal behavior: [Back closes the preview](back-friendly-modals.md), [background scroll is locked](lock-scroll-when-modal-open.md).
- ✅ Keep the **preview ephemeral** (no URL) but give the **full view its own URL** (`?item=…`) — so a reload restores the *enlarged item*, while a reload with only the preview open returns to the list. See [a reload lands on the main content](../principles/reload-returns-to-main-content.md).

**Don't**

- ❌ Make full-page navigation the *only* way to see an item.
- ❌ Reset filters/scroll when the user returns from an item (the #1 complaint).
- ❌ Cram a heavy, full editing workflow into a tiny preview — that's when you *do* route to a page.
- ❌ Force a page load just to flip one status or read two fields.

## When to go full-page anyway

Escalate (or skip the preview) when the task genuinely needs the room: multi-tab editing, long forms, related records, audit history, bulk sub-items. Heuristic: **preview for "look & quick action," full page for "sit down and work."**

## Showcase

- 👉 [`showcases/ops-panel/`](../../showcases/ops-panel/) — a filterable Orders grid. Click a row → instant preview with quick actions (Mark paid / Refund) and prev/next; "Open full view ⤢" escalates to the heavy page; Back/close returns to the **same filter and scroll position** (shown live in the context line). Keyboard: ↑/↓ select, Enter preview, ←/→ next/prev, Esc close.

## Pitfalls & anti-patterns

- **Context loss on Back** — re-running the filter and scrolling to find the row every time.
- **Preview that's secretly a full page** — slow and heavy, defeating the point.
- **No escalation path** — users stuck doing real work in a cramped modal.
- **Quick actions that navigate away** — breaking the "stay in the flow" promise.

## Notes from experience

> The ops panels that frustrated me routed to a new page on every row click — slow to open, and pressing Back lost my filters so I had to find my place again, over and over. My rule now: **don't open a full page unless there's a lot of work there.** On click, show a quick modal with useful info and useful actions; if they need the full page they can open it, otherwise they do the quick action, close, and move to the next item — never losing the list.

## References

- NN/g — *Modal vs. non-modal* and detail-on-demand in data tables
- Common admin frameworks (Retool/Forest/Django admin) — row preview/drawer patterns
