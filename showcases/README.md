# Showcases — runnable proof

Each showcase demonstrates a guideline from [`docs/`](../docs/) with real, runnable code. Seeing and touching beats reading.

## How to run

**Standalone demos** (default): open the `index.html` directly — no build, no install.

```bash
open showcases/skeleton-loading/index.html      # macOS
# or just double-click the file
```

**Richer demos** that need state/components live in the Vite + React [`playground/`](../playground/).

## Demos

| Demo | Demonstrates | Doc |
| --- | --- | --- |
| [`skeleton-loading/`](skeleton-loading/) | Perceived performance: skeleton vs. spinner | [techniques/skeleton-loading](../docs/techniques/skeleton-loading.md) |
| [`back-friendly-modals/`](back-friendly-modals/) | Back button closes the modal, not the page (History API) | [patterns/back-friendly-modals](../docs/patterns/back-friendly-modals.md) |

## Conventions

- One folder per demo: `showcases/<kebab-name>/index.html`.
- Self-contained (inline CSS/JS) so it runs offline with zero setup.
- Mobile-first, accessible, and `prefers-reduced-motion`-aware.
- Link each demo to its guideline doc, and the doc back to the demo.
