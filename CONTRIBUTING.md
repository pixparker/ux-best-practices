# Contributing

Thanks for wanting to make this better. This is a living reference, so contributions of all sizes are welcome — a typo fix, a sharper explanation, a new pattern, or a runnable demo.

## Ways to contribute

- **Feedback / disagreement** — [open an issue](../../issues). Real-world counterexamples are gold.
- **A new guideline** — add a Markdown entry (see below).
- **A showcase** — add a runnable demo proving a technique.
- **An improvement** — refine wording, add references, fix a bug in a demo.

## Adding a guideline entry

1. Pick the right bucket:
   - [`docs/principles/`](docs/principles/) — a timeless *why*.
   - [`docs/ui/`](docs/ui/) — visual craft (type, color, spacing, motion).
   - [`docs/patterns/`](docs/patterns/) — a reusable interaction solution.
   - [`docs/techniques/`](docs/techniques/) — a modern "feel-good" technique.
   - [`docs/archetypes/`](docs/archetypes/) — a playbook for a product type.
   - [`docs/platforms/`](docs/platforms/) — guidance for a delivery context.
   - [`docs/checklists/`](docs/checklists/) — an actionable list.
   - [`docs/pains/`](docs/pains/) — **a real failure we hit.** Use [`docs/pains/_TEMPLATE.md`](docs/pains/_TEMPLATE.md) (pain point → approach → result → best practice) and name it `PAIN-NNN-kebab-title.md`. You do not need a solution to file one — `status: open` is a valid entry.
2. Copy [`docs/_TEMPLATE.md`](docs/_TEMPLATE.md) into that folder, rename it `kebab-case-title.md`.
3. Fill in the front-matter and sections. Keep the **front-matter accurate** — it powers search, tagging, and AI parsing.
4. Add a link to it from that bucket's `README.md`.

## Adding a showcase

- **Simple demo (preferred):** create `showcases/<name>/index.html` — fully self-contained, no build, opens in a browser.
- **Richer demo:** add it to the Vite + React [`playground/`](playground/).
- Link the showcase from its related guideline entry, and vice-versa.

## Style

- Write for a smart reader in a hurry. Lead with the takeaway.
- Prefer **do / don't** pairs over abstract advice.
- Every claim should be demonstrable or referenced.
- Mobile-first and accessible by default.

## Conventions

- File & folder names: `kebab-case`.
- One idea per file.
- Mark maturity with `status:` front-matter (`seed` → `draft` → `stable`).
