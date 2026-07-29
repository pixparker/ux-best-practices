---
id: PAIN-002
title: Every row click loses the filtered list you built
pain: An operator filters a long grid, opens a row, comes back — and the filters, sort, scroll and selection are all gone.
category: pain
tags: [ops-panel, admin, grid, table, navigation, productivity, context-loss]
platforms: [desktop, tablet, web, mobile-web]
archetypes: [ops-panel]
severity: friction
status: solved
enforcement: check
enforced-by: "preview-first is the default for opt-in lists; full-page navigation needs a stated reason at review"
solution: ../patterns/preview-modal-over-full-page.md
showcase: ../../showcases/ops-panel/
first-seen: 2026-06-28
last_updated: 2026-07-29
---

# PAIN-002 — Every row click loses the filtered list you built

> **The pain.** An operator narrows a few hundred rows down to the eight they care about, clicks the first one, deals with it, presses Back — and lands on an unfiltered list at the top. Then does it again. And again.

## 1. Pain point

Ops work is **high-throughput and repetitive**: filter, scan, act, next. The filtered list is not scenery — it is the operator's working set, and they paid for it with several deliberate actions (a search term, two filters, a sort, and scrolling to row 40).

When a row click is a full-page navigation, every round-trip charges them twice:

1. **The wait** — a full page load to see three fields they could have read in a tooltip.
2. **The loss** — Back returns to the *route*, not the *state*. Filters reset, sort resets, scroll jumps to the top, selection clears.

So the loop becomes *filter → click → wait → back → re-filter → find my place → repeat*, dozens of times a day. Each individual instance is only mildly annoying, which is exactly why it survives review — the cost is invisible in any single interaction and brutal in aggregate. It is the kind of friction operators stop reporting and start silently routing around, usually by keeping ten browser tabs open.

**Why it happens:** the grid treats "look at this row" and "do heavy work on this entity" as the same action, and gives both the most expensive affordance available — a route change. Meanwhile the list's state lives in component memory rather than anywhere navigation can restore it.

## 2. Approach / solution

Split the two intents, and make the common one cheap.

- **A plain row tap opens a preview** — a modal on desktop, a bottom sheet on mobile — showing the key fields and the two or three actions that cover most visits. The list stays mounted underneath, so nothing is lost because nothing was left.
- **Escalate deliberately.** The full page is still reachable — via an explicit "open full view", the expand affordance, a kebab item, and Cmd/Ctrl-click or middle-click, which must keep working as real link behaviour.
- **Preview is ephemeral: no URL.** A reload lands on the list, not on a modal over it.
- **Page within the preview** — prev/next through the filtered set with the keyboard, so the operator can work the whole working set without returning to the grid at all.
- **Opt-in per list**, so migrating one grid never regresses another.

**Rejected — and why:**
- *Keep full-page navigation, restore state on Back.* Fixes the loss but not the wait, and state restoration across routes is fragile in a way preview simply isn't.
- *Inline row expansion.* Fine for two or three fields; it reflows the grid and fights fixed columns as soon as there is real content.
- *Preview in the URL.* Would make reload restore a modal over a list — see [PAIN-001](PAIN-001-back-button-exits-the-app.md) and [reload lands on main content](../principles/reload-returns-to-main-content.md).

> 🔒 Binding: **a routine look at a row must not cost the operator their working set.** Preview is our answer, not the only one — a master-detail split view or a virtualised drawer would also satisfy it.

## 3. The result

The common case became instant, and the working set stopped evaporating. Prev/next paging turned out to matter more than expected: operators work a filtered batch end to end without touching the grid, which was never possible before.

**What it did not fix:** heavy work — anything with its own modals, multi-step forms or nested tables — still belongs on the full page. Trying to cram those into the preview made it a worse version of the page. The preview earns its keep by staying small; the moment it grows tabs, it has become the thing it replaced.

**A trap we hit:** the preview is only the *default* for lists that opt in. Un-migrated grids still full-page navigate, so the panel behaves inconsistently until every list migrates. Partial adoption is its own small pain — worth finishing rather than leaving half-done.

## 4. Best practice

**Rule:** In a data grid, a row tap opens a preview that preserves the list; full-page navigation is an escalation the user chooses, never the default.

**Do**
- ✅ Show, in the preview, the fields and the 2–3 actions that cover the routine visit.
- ✅ Keep the list mounted — filters, sort, scroll and selection intact.
- ✅ Offer prev/next through the filtered set, keyboard-driven.
- ✅ Keep Cmd/Ctrl-click and middle-click working as genuine link behaviour.
- ✅ Give the full page a real URL; keep the preview out of the URL.

**Don't**
- ❌ Make a full page load the price of reading three fields.
- ❌ Let Back return to a reset list.
- ❌ Grow the preview into a second detail page with tabs.

**How it is enforced today**
- [ ] 🟢 code — *not yet: the kit provides the primitive, but a list can still be built the old way*
- [x] 🟡 check — preview-first is the reviewed default; full-page-on-row-click needs a stated reason
- [x] 🔴 prose — this entry

**Full pattern:** [preview-first: quick modal over full-page navigation](../patterns/preview-modal-over-full-page.md) · **Sample design:** [`showcases/ops-panel/`](../../showcases/ops-panel/)

## Related pains

- [PAIN-001](PAIN-001-back-button-exits-the-app.md) — the same disease (navigation discarding user-built context) on the overlay layer.
- Companion patterns: [responsive tables on mobile](../patterns/responsive-tables-on-mobile.md), [ops-admin-panel archetype](../archetypes/ops-admin-panel.md).
