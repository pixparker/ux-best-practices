# 💢 Pains — *what actually went wrong*

The registry of real UX pain points we have hit, and the best answer we currently have for each.

Every other folder in this repo tells you **what to do**. This one tells you **what breaks** — which is the part that survives when frameworks, fashions and our own opinions change.

---

## 🔒 The rule that makes this useful

> **The pain is binding. The solution is a reference, not a mandate.**

A design may address a pain any way it likes — a different mechanism, a different framework, a different interaction model, or by removing the surface that causes it. What it may **not** do is ship something that leaves the pain in place.

So review does not ask *"did you follow the pattern?"* It asks:

> **"Which pains does this surface expose, and how does your design address each one?"**

If you solve one better than we did, that is not a deviation — **it is the new entry.** Update the pain with your approach and result, and say why it beats the old one.

## How each entry is shaped

Four sections, always in this order:

| Section | Answers |
|---|---|
| **1. Pain point** | What a real person experienced, and why it hurt. Written so it stays true in ten years. |
| **2. Approach / solution** | What we did about it. One reference implementation — not the only legal answer. |
| **3. The result** | What actually changed. Honest: including where it only half-worked. |
| **4. Best practice** | The durable rule this produced, and how it is enforced today. |

Copy [`_TEMPLATE.md`](_TEMPLATE.md).

## The registry

| ID | Pain — *the one-liner* | Archetypes | Status | Enforcement |
|---|---|---|---|---|
| [PAIN-001](PAIN-001-back-button-exits-the-app.md) | Back closes the **app** instead of the open overlay | consumer-mobile · ecommerce · ops | ✅ solved | 🟢 code + check |
| [PAIN-002](PAIN-002-every-row-click-loses-your-place.md) | Opening a row loses the filtered list you spent effort building | ops-admin-panel | ✅ solved | 🟡 check |
| [PAIN-003](PAIN-003-full-height-sections-jump-mid-scroll.md) | Full-height sections resize and jump as the mobile address bar hides | consumer-mobile · ecommerce | ✅ solved | 🔴 prose |

**Status:** ✅ solved · 🟡 mitigated (works, with known holes) · 🔴 open (no good answer yet — say so).
**Enforcement** ([why this column exists](#enforcement)): 🟢 code · 🟡 check · 🔴 prose.

## Enforcement

A rule becomes real in three forms, in this order — **code**, then **a check**, then **prose**:

- 🟢 **code** — a primitive makes the wrong thing hard to write (a `Sheet` that is back-friendly by construction)
- 🟡 **check** — a lint, grep-gate or test fails when someone regresses it
- 🔴 **prose** — this entry, and nothing else

Prose is the weakest form and is where every pain starts. **A pain sitting at 🔴 for a long time is a backlog item, not a finished job.** PAIN-001 is 🟢 and has never regressed since; that is the target state, not a luxury.

## Adding a pain

You do not need a solution to file one. **A pain with no answer is still worth recording** — set `status: open`, write sections 1 and 3 (what it cost), and leave 2 and 4 as `TBD`. That is a research brief for whoever picks it up.

The fastest path: describe the pain in one sentence to an agent working in this repo — *"user opens a modal, presses back, and the whole page unloads"* — and let it research the landscape, draft the entry, and build the sample. See [`CLAUDE.md`](../../CLAUDE.md) for the authoring workflow.

## Using this at design time

Before designing a surface, filter this registry by its **archetype** and **platform**, then run [the pain review](../checklists/pain-review.md). Each applicable pain gets one of three answers: *addressed* (how), *not applicable* (why), or *accepted* (a conscious, recorded trade-off).

That is the whole point of the registry: **the next dev inherits our scars instead of re-earning them.**
