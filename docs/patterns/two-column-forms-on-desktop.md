---
title: Two-column forms on desktop, one on mobile
summary: A desktop form laid out as a single narrow column wastes half the screen and pushes the submit button below the fold — pair short related fields side by side, and let long ones span.
category: pattern
tags: [forms, layout, responsive, desktop, modal, admin]
platforms: [web, mobile-web]
archetypes: [ops-admin-panel, saas-dashboard]
status: draft
related:
  - inline-form-validation.md
  - preview-modal-over-full-page.md
  - ../ui/spacing-and-layout.md
last_updated: 2026-08-05
---

# Two-column forms on desktop, one on mobile

> The single-column form is mobile advice that got promoted to a law. On a
> 1440px screen it leaves two thirds of the dialog empty and pushes the button
> that saves the work below the fold — so the person scrolls past what they just
> filled in to reach it.

## Why it matters

Single-column is right on a phone and is genuinely the safer default: one
decision per row, no ambiguity about reading order, no field pairs that only
make sense at one width. That is why it became the received wisdom.

But a form is read at the width it is shown at. On a desktop dialog, a strict
single column produces:

- **A scroll for something that fits.** Six controls that would occupy half a
  screen in two columns become a ladder taller than the dialog, and the primary
  action leaves the viewport.
- **A broken review pass.** Nobody submits without a last glance over what they
  entered. If that glance is a scroll, most people skip it.
- **A form that reads as longer than it is.** Perceived length is measured in
  screens, not in fields. The same eight fields feel like a chore in one column
  and like a small task in two.
- **Live context pushed out of view.** Anything the form *changes* — a preview,
  a computed total, a rendered result — ends up above the controls that change
  it, so the person cannot see the effect of the thing they are adjusting.

## The guideline

**Do**

- ✅ **One column on small screens, two from the tablet breakpoint up.** One
  grid, one breakpoint, no second layout to maintain.
- ✅ **Pair fields that are short and related** — a label and a status, a city
  and a postcode, a quantity and a unit.
- ✅ **Let long fields span both columns**: free text, a textarea, a repeating
  key/value editor, an explanatory toggle, an error message.
- ✅ Put a **live preview beside its controls**, not above them.
- ✅ Choose the span **per field, from what the field is** — not to make the
  grid come out even.
- ✅ Use the **same breakpoint** the overlay itself switches on (dialog ↔ sheet),
  so the layout and its container can never disagree.

**Don't**

- ❌ Split a **single logical decision** across two columns.
- ❌ Put fields side by side in a **narrow pane** — two halves of a 400px column
  are 190px cells, and a URL in one of them breaks mid-token.
- ❌ Order fields **down the left column then down the right**. Reading order is
  row by row; a form that reads in Z is a form filled in out of order.
- ❌ Go to **three columns** in a dialog. Beyond two, the eye stops tracking rows
  and every label gets truncated.
- ❌ Force a **two-column grid on a phone** to look consistent with desktop.

## Technique

One grid, one breakpoint, spans declared per field:

```html
<form class="grid grid-cols-1 gap-4 sm:grid-cols-2">
  <Field label="Name">…</Field>          <!-- short: pairs -->
  <Field label="Destination">…</Field>   <!-- short: pairs -->

  <div class="sm:col-span-2">           <!-- long: spans -->
    <Field label="Notes"><textarea …/></Field>
  </div>

  <div class="sm:col-span-2">           <!-- repeating rows: spans -->
    <ParamEditor …/>
  </div>
</form>
```

For a form with a live preview, the preview is the other column:

```html
<div class="grid grid-cols-1 items-start gap-4 sm:grid-cols-2">
  <Preview class="sm:sticky sm:top-0" />
  <div class="flex flex-col gap-4"><!-- controls --></div>
</div>
```

`items-start` matters: without it, a short column stretches to the tall one's
height and its contents float.

## Pitfalls & anti-patterns

- **Grid-driven spans.** Deciding a field spans because the row would otherwise
  be ragged. The span is a property of the field's content.
- **A breakpoint that disagrees with the container.** A two-column form inside a
  dialog that has already collapsed to a phone sheet.
- **Sticky preview with no height limit** — it scrolls out of its own column on
  a short viewport. Cap it.
- **Tab order surprises.** CSS grid does not change DOM order; keep the source
  order the same as the intended reading order and the two stay aligned.

## Notes from experience

The honest version of the rule: *single column is the default, and a desktop
dialog is the case where the default costs more than it saves.* The question to
ask per field is not "can this share a row?" but "does this field's content
survive half the width?" — a label does, a URL usually does not, a paragraph
never does.

## References

- Baymard Institute — form field layout and completion rates
- NN/g — single-column forms (the original advice, and its mobile context)
