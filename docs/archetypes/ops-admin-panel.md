---
title: "Archetype: Ops / admin panel"
summary: For technical users managing a platform — optimize for density, speed, and bulk control, not hand-holding.
category: archetype
tags: [admin, dashboard, tables, power-user, productivity]
platforms: [desktop, web]
archetypes: [ops-panel]
status: draft
related:
  - ../patterns/README.md
  - consumer-mobile-app.md
last_updated: 2026-06-16
---

# Archetype: Ops / admin panel

> Built for people who use it **all day** to run a platform. They want power and speed, not a friendly tour. Density is a feature; every extra click is a tax.

## Who it's for

Internal operators, support agents, store managers, moderators — **technical or trained** users on **desktop**, repeating tasks dozens of times an hour. They'll learn shortcuts and tolerate complexity *if it makes them faster*.

This is the mirror image of the [consumer mobile app](consumer-mobile-app.md): there you optimize for the first-time, low-attention user; here you optimize for the expert, high-frequency user.

## Must do ✅

- **Data tables that work hard** — sortable columns, sticky header, column resize/show-hide, and **bulk actions** (select-all, multi-row operations).
- **Powerful filtering & search** — combinable filters, saved views/segments, and instant text search. Operators live in filtered subsets.
- **Quick navigation** — a **command palette** (`Cmd/Ctrl-K`) to jump anywhere or run any action without the mouse.
- **Keyboard-first** — shortcuts for the top actions, `j/k` row movement, `Enter` to open, `Esc` to close. Show a `?` shortcuts cheat-sheet.
- **Inline & side-panel editing** — edit a row in place or in a slide-over; don't force a full page navigation for a one-field change.
- **Density control** — comfortable/compact row toggle; default compact for power users.
- **Non-blocking feedback** — optimistic updates with undo, toasts for results. Never freeze the whole screen for one row's save.
- **Deep-linkable state** — filters, sort, and the open record live in the URL so views can be shared and bookmarked.
- **Destructive-action safety** — confirm or (better) **undo** for deletes and bulk operations; show exactly *how many* records are affected.
- **Pagination or virtualization** for large datasets — never render 10k DOM rows.

## Should avoid ❌

- ❌ **Mobile-style minimalism** — hiding columns and actions behind taps wastes the screen and slows experts.
- ❌ **Modal overload** — stacked modals trap power users; prefer slide-over panels and inline editing.
- ❌ **Full-page reloads** for every filter or edit — keep state client-side and the URL in sync.
- ❌ **Forcing the mouse** — if a frequent action has no keyboard path, it's a productivity bug.
- ❌ **Mystery bulk actions** — never run a bulk operation without stating the count and offering undo.
- ❌ **Over-animation** — operators repeat actions hundreds of times; long transitions become friction. Keep motion fast (<150ms) or off.
- ❌ **Infinite scroll for records you must audit** — operators need stable, addressable positions (page/cursor), not a shifting feed.

## Patterns that matter most here

- Data tables (sort / filter / bulk) · Command palette / quick nav · Slide-over panels · Inline validation · Undo-instead-of-confirm · Saved views · Empty & no-results states

## Pitfalls & anti-patterns

- **Designing it like the consumer app.** The same team often builds both and copies the friendly, sparse mobile UI into the admin tool — and operators hate it.
- **Death by clicks.** A task that takes 6 clicks × 200 times/day is the real cost. Measure clicks-per-task, not screens.
- **No bulk path.** If editing 50 records means opening 50 pages, the tool fails at its one job.

## Notes from experience

> The fastest win on any admin panel is `Cmd-K` + keyboard row navigation + bulk select. Operators stop touching the mouse and their throughput jumps. The second win is putting filter/sort state in the URL — suddenly people share "the exact view" in chat instead of writing paragraphs of instructions.

## References

- Refactoring UI — dashboards & data density
- Linear / Stripe Dashboard / Retool — reference points for keyboard-first ops UX
