---
title: Responsive tables on mobile (don't let borders clip the data)
summary: Wide data tables don't fit phones — reflow rows into cards (label:value), prioritize key columns, or use a sticky-column horizontal scroll. Never just shrink until content is cut off.
category: pattern
tags: [table, mobile, responsive, ops-panel, data-grid, cards, layout]
platforms: [mobile-web, pwa, web]
archetypes: [ops-admin-panel, ecommerce]
status: draft
related:
  - preview-modal-over-full-page.md
  - ../ui/spacing-and-layout.md
  - ../archetypes/ops-admin-panel.md
last_updated: 2026-06-16
---

# Responsive tables on mobile (don't let borders clip the data)

> A multi-column table is built for wide screens. Drop it onto a phone untouched and the columns squeeze until text wraps into shreds or gets **cut off by the cell borders** — rich rows become unreadable. Tables need a real small-screen strategy, not just shrinking.

## Why it matters

Ops panels lean on dense tables. On a phone there isn't room for 6 columns, so the naive result is clipped, truncated, horizontally-scrolling-everything mess where users can't read a single row cleanly. Choose a deliberate reflow so each record stays legible on a narrow screen.

## Pick a strategy (by table shape)

| Strategy | Best when | How |
| --- | --- | --- |
| **Cards (stacked label:value)** | Few rows, rich fields | Each row becomes a card; every cell shows its column label beside the value |
| **Prioritize columns** | Many columns, one or two matter | Show the key column(s) + status; tuck the rest into the preview/expand |
| **Sticky first column + h-scroll** | Genuinely tabular comparison | Freeze the identifier column, horizontally scroll the rest |
| **Row → preview** | Lots of detail per row | Show minimal columns; tap the row for the full record ([preview pattern](preview-modal-over-full-page.md)) |

## The guideline

**Do**

- ✅ Reflow rows into **cards** on narrow screens — each value carries its **label** so nothing is ambiguous.
- ✅ Keep the **identifier + status** always visible; demote secondary fields.
- ✅ If you must keep a grid, **freeze the first column** and scroll the rest horizontally (don't scroll the whole page sideways).
- ✅ Let a tap open the **[preview modal](preview-modal-over-full-page.md)** for the complete record.
- ✅ Keep tap targets ≥ 44px and rows comfortably spaced.

**Don't**

- ❌ Shrink a desktop table until text wraps/clips against borders.
- ❌ Make the whole page scroll horizontally to read one row.
- ❌ Hide columns with no way to reach the hidden data.
- ❌ Use tiny font sizes to force columns to fit.

## Technique (CSS-only card reflow)

```css
@media (max-width: 640px) {
  thead { display: none; }                 /* headers move into each cell */
  table, tbody, tr, td { display: block; width: 100%; }
  tr { border: 1px solid var(--line); border-radius: 12px; margin-bottom: 10px; }
  td { display: flex; justify-content: space-between; gap: 14px; padding: 8px 14px; }
  td::before { content: attr(data-label); color: var(--muted); font-weight: 600; }
}
```
```html
<td data-label="Customer">Aria Mostafavi</td>  <!-- label shows on mobile -->
```

## Showcase

- 👉 [`showcases/ops-panel/`](../../showcases/ops-panel/) — the Orders grid is a real table on desktop and **reflows into labelled cards under 640px** so no field is clipped. Tap any card to open the full record in a preview.

## Pitfalls & anti-patterns

- **Clipped cells** — the default outcome of an unhandled table on mobile.
- **Sideways-scrolling page** — disorienting; scroll a *container*, not the page.
- **Unreachable hidden columns** — pair column-hiding with a preview/expand.

## Notes from experience

> The other ops-panel pain on mobile: table rows just can't show rich info — the content gets cut by the table borders. Reflowing rows into labelled cards (and letting a tap open the full record) makes dense data readable on a phone without losing anything.

## References

- CSS-Tricks — *Responsive data tables* (the label/card reflow)
- MDN — `position: sticky` for frozen columns
