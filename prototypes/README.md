# Prototypes — pick-a-style sample apps

Small but **complete** React apps, each demonstrating a whole style/archetype end-to-end. Where a [showcase](../showcases/) proves *one technique*, a prototype shows what a *finished product* in a given style feels like.

> **Why this exists:** for a new project, a customer can browse these prototypes and point to the one whose style and feel matches what they want. That turns a vague brief into a concrete starting point — and gives us a proven base to build from.

## The three pillars (where this fits)

1. **Guideline** — [`docs/`](../docs/): the written best practices.
2. **Showcase** — [`showcases/`](../showcases/) + [`playground/`](../playground/): focused proof of a single technique.
3. **Prototypes** — *(here)*: complete sample apps to pick a style from.

## Prototypes map to archetypes

Each prototype is an instance of an [archetype](../docs/archetypes/) in a particular visual style. Picking a prototype tells us which playbook to follow.

| Planned prototype | Archetype | Style direction |
| --- | --- | --- |
| Weather app | [Fancy app](../docs/archetypes/fancy-app.md) | Bold, motion-rich, eye-catching |
| Habit / fitness tracker | [Fancy app](../docs/archetypes/fancy-app.md) | Clean, playful, rewarding |
| Admin dashboard | [Ops / admin panel](../docs/archetypes/ops-admin-panel.md) | Dense, keyboard-first, data-heavy |
| Mini storefront | [E-commerce](../docs/archetypes/ecommerce.md) | Trust-forward, conversion-focused |
| Assistant chat | [Conversational / bot](../docs/archetypes/conversational-bot.md) | Friendly, guided, streaming |
| Simple utility app | [Consumer mobile](../docs/archetypes/consumer-mobile-app.md) | Minimal, obvious, forgiving |

## Convention

- **Stack:** React + Vite (our default — quick to build, easy for customers to run).
- **Layout:** one self-contained app per folder — `prototypes/<kebab-name>/`.
- Each prototype has its own `README.md` stating the **archetype**, the **style direction**, and a screenshot/gif.
- Keep them **runnable in isolation** (`npm install && npm run dev`) so a customer can try a single one.
- Reuse the best practices from [`docs/`](../docs/) — prototypes should *exemplify* the guidelines, not contradict them.

## Add a prototype

1. Scaffold a Vite + React app in `prototypes/<name>/` (mirror [`playground/`](../playground/)'s setup).
2. Build a small but complete experience for one archetype + style.
3. Add a `README.md` (archetype, style, how to run, screenshot) and list it in the table above.

> 🚧 **Status:** pillar scaffolded; first prototype coming next.
