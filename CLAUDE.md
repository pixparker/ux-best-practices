# ux-best-practices — agent guide

The UX/UI standard for Aradvision's web apps (mobile · tablet · desktop). It is consumed by every product as a git submodule at `standards/ux/`.

**Two different jobs use two different files:**

- **Applying the standard** while building someone's UI → [`AGENTS.md`](AGENTS.md). That is the operating rule set.
- **Working on this repo** — adding entries, showcases, prototypes → this file.

## What this repo is

Three pillars: **guidelines** (`docs/`), **runnable proof** (`showcases/`, `playground/`), **style references** (`prototypes/`).

Organised on two axes plus two cross-cutting layers:

```
   WHAT you're building  →  docs/archetypes/
   WHERE it runs         →  docs/platforms/
                             ×
   craft   →  docs/principles/ · ui/ · patterns/ · techniques/
   evidence →  docs/pains/        ← why we believe any of it
   action  →  docs/checklists/
```

🔒 **The public repo rule.** This is public, MIT (code) / CC-BY (content). **Never commit internal specifics** — customer names, private architecture, credentials, revenue figures, internal file paths. Write pains generically: *"an ops panel over a few hundred rows"*, not the product's internals.

## `docs/pains/` — the important one

The registry of real failures. Every other folder says *what to do*; this says *what broke*, which is the part that survives when frameworks and opinions change.

🔒 **The pain is binding. The solution is a reference, not a mandate.** A design may address a pain any way it likes; it may not leave the pain in place. If someone solves one better than we did, that becomes the new §2.

Four sections, always in this order — see [`docs/pains/_TEMPLATE.md`](docs/pains/_TEMPLATE.md):

1. **Pain point** — the story, the broken expectation, the real cost, the root cause
2. **Approach / solution** — one reference implementation, plus what was rejected and why
3. **The result** — what changed, honestly, including what it did *not* fix
4. **Best practice** — the durable rule, and how it is enforced today

## Authoring a pain from one sentence

The founder describes a pain in a sentence. Your job is to turn it into an entry. Example input:

> *"user opens a modal then presses back, expects the previous page, but back closes the whole page — SPA problem"*

**Do this:**

1. **Interrogate the pain before solving it.** What did the person *expect*? What did they get? What did it actually cost — rework, lost state, lost trust, abandonment? What is the *root cause*, not the symptom? Ask the founder if any of this is unclear; a vague pain produces a useless entry.
2. **Research the landscape.** How do good apps solve this? Native platforms? What do the specs and WCAG say? Bring back options, not one answer.
3. **Propose a solution and name what you rejected.** The rejected options are usually more useful than the chosen one — they encode why the obvious approach fails.
4. **Build a sample.** A self-contained `showcases/<name>/index.html`, no build step, opens in a browser. Richer demos go in `playground/`. **A pain without a runnable sample is half-written.**
5. **Write the entry.** Next free `PAIN-NNN`, accurate front-matter, all four sections. Set `status: open` honestly if there is no good answer yet — a research brief is a legitimate entry.
6. **Wire it up:** add a row to [`docs/pains/README.md`](docs/pains/README.md), a row to [`docs/checklists/pain-review.md`](docs/checklists/pain-review.md), cross-links to related pains, and a line in `llms.txt`.

**Do not:**
- ❌ Invent a cost. If you don't know what it cost, ask or leave it qualitative.
- ❌ Write a pain that is really a bug report. A pain is a *class* of failure that will recur across products.
- ❌ Duplicate an existing pattern doc. The pain links to it; the how-to lives there.
- ❌ Claim enforcement that doesn't exist. `enforcement: code` means code exists, today.

## Adding other entries

- Guideline → copy `docs/_TEMPLATE.md` into the right bucket, keep the front-matter accurate (it powers search and AI parsing), link it from that bucket's `README.md`.
- Showcase → `showcases/<name>/index.html`, self-contained. Link it from its guideline and back.
- Every entry carries `status: seed | draft | stable`. Be honest — `seed` means "we think so", `stable` means "we have shipped this and it held."

## Enforcement ladder

A rule becomes real as **🟢 code**, then **🟡 a check**, then **🔴 prose**. Prose is weakest and is where everything starts. Each pain records where it sits; a pain stuck at 🔴 is a backlog item, not a finished job.

When you add or edit a pain, ask: *could this be a primitive that makes the wrong thing hard, or a lint that fails on regression?* If yes, say so in §4 even if you don't build it.

## Conventions

- Markdown with YAML front-matter, `kebab-case-title.md` (pains: `PAIN-NNN-kebab-title.md`).
- Showcases are dependency-free HTML; the playground is Vite + React.
- Persian is **not** used here — the standard is English so it can be public and forkable. Products localise.
- 🔒 **Do not commit until the founder approves the approach** for each scenario. Explicit paths only, never `git add -A`.
