# UX & UI Best Practices

> A living, principle-first reference for building interfaces people *love* to use — across mobile web, PWAs, online shops, desktop, web, and conversational/bot UIs.

This repo has **three pillars**:

1. **Guideline** — written, opinionated best practices distilled from real development experience → [`docs/`](docs/)
2. **Showcase** — runnable code that proves each idea, see/copy/adapt it → [`showcases/`](showcases/) + an interactive [`playground/`](playground/)
3. **Prototypes** — small *complete* React apps you can browse to pick a style/feel for a new project → [`prototypes/`](prototypes/)

The focus is on **principles**, not any single stack. Examples happen to use HTML/CSS/JS and React/Vite — but the *why* behind each technique outlives the tools.

It's built to be consumed by both **humans** (browse the docs, explore the playground) and **AI agents** (see [`AGENTS.md`](AGENTS.md) and [`llms.txt`](llms.txt)).

👉 **Every rule in one place:** open [`index.html`](index.html) in a browser — a searchable, filterable index of all entries, generated from their front-matter. Regenerate it with `python3 tools/build-index.py` after adding or editing an entry.

---

## Who this is for

| Audience | How to use it |
| --- | --- |
| 🧑‍💼 **Founders / builders** (incl. me) | Stop re-deciding solved problems. Grab a [checklist](docs/checklists/) before kicking off a project. |
| 👩‍💻 **Developers** | Study the [patterns](docs/patterns/) & [techniques](docs/techniques/), copy the [showcases](showcases/). |
| 🙋 **End users / reviewers** | Read the guidelines, try the demos, and [open feedback](../../issues). |
| 🤖 **AI / agents** | Structured, tagged Markdown designed to be parsed and learned from. |

---

## How it's organized

The reference works along **two axes** — *what* you're building × *where* it runs — plus craft topics and actionable lists:

| Area | Question it answers | Folder |
| --- | --- | --- |
| **Archetypes** | *What you're building* — consumer mobile, ops/admin panel, fancy app, e-commerce, bot, game | [`docs/archetypes/`](docs/archetypes/) |
| **Platforms** | *Where it runs* — mobile web, PWA, desktop, web | [`docs/platforms/`](docs/platforms/) |
| **Principles** | *Why* — the timeless laws behind good UX & UI | [`docs/principles/`](docs/principles/) |
| **UI craft** | *Look* — typography, color, spacing, motion, components | [`docs/ui/`](docs/ui/) |
| **Patterns** | *Behavior* — reusable solutions to recurring interaction problems | [`docs/patterns/`](docs/patterns/) |
| **Techniques** | *Feel* — modern tricks that make apps feel smooth & alive | [`docs/techniques/`](docs/techniques/) |
| **Checklists** | *Ship it* — actionable lists for reuse | [`docs/checklists/`](docs/checklists/) |
| **Showcases** | *Proof* — runnable single-technique demos | [`showcases/`](showcases/) |
| **Playground** | *Explore* — interactive React gallery of the demos | [`playground/`](playground/) |
| **Prototypes** | *Pick a style* — complete sample React apps | [`prototypes/`](prototypes/) |

Start at the [**docs index →**](docs/README.md)

---

## Trying the showcases

**Standalone demos** (most of them) need no build — just open the HTML file in a browser:

```bash
open showcases/skeleton-loading/index.html   # macOS
```

**Richer demos** live in the Vite + React [`playground/`](playground/):

```bash
cd playground
npm install
npm run dev
```

---

## Philosophy

- **Principle first, code second.** A technique without a reason is a fad.
- **Mobile is the default**, not the afterthought. Thumb reach, slow networks, small screens.
- **Perceived performance beats raw performance.** How fast it *feels* is what users judge.
- **Accessible by default.** If it doesn't work for everyone, it isn't done.
- **Show, don't just tell.** Every claim should be demonstrable.

---

## Status

🌱 **Living document.** This grows over time as I capture experiences, challenges, and proven solutions. Entries are tagged with a `status:` (`seed` · `draft` · `stable`) so you know how battle-tested each one is.

## Contributing & feedback

Ideas, corrections, and demos are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Found something wrong or have a better approach? [Open an issue](../../issues).

## License

- **Code** (showcases, playground, snippets): [MIT](LICENSE)
- **Written content** (guidelines, docs): [CC BY 4.0](LICENSE-CONTENT.md)

See [LICENSE](LICENSE) and [LICENSE-CONTENT.md](LICENSE-CONTENT.md) for details.
