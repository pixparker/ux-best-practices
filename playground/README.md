# Playground — explore best practices live

An interactive **human UI playground**: a Vite + React gallery to browse and *feel* the best practices, not just read them. It's the human counterpart to the AI-facing docs ([`AGENTS.md`](../AGENTS.md), [`llms.txt`](../llms.txt)).

## Run it

```bash
cd playground
npm install
npm run dev
```

Opens at `http://localhost:5173`. Pick a demo from the sidebar; it renders live.

## How it works

- **Shell** ([`src/App.jsx`](src/App.jsx)) — sidebar grouped by area + a live stage. Mobile-friendly.
- **Registry** ([`src/registry.js`](src/registry.js)) — the single list of demos. The sidebar and routing are generated from it.
- **Demos** ([`src/demos/`](src/demos/)) — one React component per demo.

## Add a demo (2 steps)

1. Create `src/demos/MyDemo.jsx` exporting a default component.
2. Register it in [`src/registry.js`](src/registry.js):

```js
import MyDemo from './demos/MyDemo.jsx'

export const demos = [
  // ...existing
  {
    id: 'my-demo',
    title: 'My Demo',
    area: 'Patterns',          // groups it in the sidebar
    summary: 'One-line description.',
    doc: 'docs/patterns/my-demo.md', // optional link to the guideline
    Component: MyDemo,
  },
]
```

That's it — no routing or layout code to touch.

## When to use the playground vs. a standalone showcase

- **Standalone** ([`../showcases/`](../showcases/)) — a single self-contained HTML file, zero install, great for a focused demo or embedding.
- **Playground** (here) — stateful/interactive demos that benefit from React, browsed together in one place.
