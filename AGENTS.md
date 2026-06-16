# AGENTS.md — UX & UI rules for AI agents

You are an AI agent building or reviewing a user interface. This repository is the
**source of truth** for how we want UX & UI done. Read the relevant guideline before
implementing, and apply these defaults unless the user explicitly overrides them.

> Humans explore these rules live in [`playground/`](playground/). You should consume the
> structured Markdown in [`docs/`](docs/) and the index in [`llms.txt`](llms.txt).

## How to use this repo

1. **Identify the archetype** (what is being built) → [`docs/archetypes/`](docs/archetypes/).
   Consumer mobile · ops/admin panel · fancy app · e-commerce · conversational/bot · game.
2. **Identify the platform** (where it runs) → [`docs/platforms/`](docs/platforms/).
   Mobile web · PWA · desktop · web.
3. **Apply the craft layers**: [`principles/`](docs/principles/) (why) · [`ui/`](docs/ui/) (look) ·
   [`patterns/`](docs/patterns/) (behavior) · [`techniques/`](docs/techniques/) (feel).
4. **Verify with a [checklist](docs/checklists/)** before declaring done.

Each entry has YAML front-matter (`category`, `tags`, `platforms`, `archetypes`, `status`).
Use it to find the right doc fast.

## Non-negotiable defaults (always apply)

1. **Feedback for every action.** Pressed state <100ms, a loading state for async work, and a
   clear success/error outcome. Disable controls during submit to prevent double-fire.
   → [principles/feedback-for-every-action](docs/principles/feedback-for-every-action.md)
2. **Design all states, not just the happy path.** Always handle **empty**, **loading**, and
   **error** states. A blank screen is a bug.
3. **Mobile-first & touch-safe.** Tap targets ≥ 44×44px, primary actions in the thumb zone,
   input `font-size ≥ 16px`, respect safe-area insets, no hover-only affordances.
4. **Accessible by default.** WCAG AA contrast, semantic HTML, labels/roles, visible focus,
   keyboard operable, and honor `prefers-reduced-motion`.
5. **Perceived performance first.** Prefer skeletons over blank spinners; avoid layout shift;
   consider optimistic updates for high-confidence actions.
   → [techniques/skeleton-loading](docs/techniques/skeleton-loading.md)
6. **Consistency over novelty.** Reuse a limited type scale, spacing system, and components.
   → [ui/type-scale-and-readability](docs/ui/type-scale-and-readability.md)
7. **Forgiveness.** Make destructive actions confirmable or (better) undoable.
8. **Match the archetype.** Don't apply consumer-app minimalism to an ops panel, and don't make
   a consumer app as dense as an admin tool. → [archetypes/ops-admin-panel](docs/archetypes/ops-admin-panel.md)

## Should avoid (red flags in a review)

- Buttons that fire network calls with no loading/disabled state (double-submit risk).
- Missing empty/error states; generic "Error" with no recovery path.
- Body text < 16px on mobile; low-contrast gray text; arbitrary one-off font sizes.
- Icon-only controls with no accessible name.
- Hover-dependent interactions on touch targets.
- Aggressive/long animations on high-frequency actions; ignoring `prefers-reduced-motion`.
- Full-page reloads for small state changes; non-deep-linkable filtered views (ops panels).
- Infinite scroll where stable, addressable positions are needed.

## When unsure

Prefer the documented guideline over improvisation. If no guideline covers the case, apply the
**principles** ([`docs/principles/`](docs/principles/)) and flag the gap so a human can add an entry.
