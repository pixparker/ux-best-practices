---
title: Pain review — before you design a surface
summary: Filter the pain registry to your archetype and platform, then give every applicable pain one of three answers: addressed, not applicable, or accepted.
category: checklist
tags: [design-review, pains, kickoff, qa]
status: draft
related:
  - ../pains/README.md
  - new-project-kickoff.md
  - mobile-ux-checklist.md
last_updated: 2026-07-29
---

# Pain review — before you design a surface

> Run this **at design time**, not at QA. A pain caught in a mock costs minutes; the same pain caught after build costs a rewrite of the thing that caused it.

## The rule 🔒

> **The pain is binding. The solution is a reference.**

You are not being asked to copy our patterns. You are being asked to make sure a user of *your* surface will not hit a wall we already know about.

## The three legal answers

Every applicable pain gets exactly one:

| Answer | Means | Must record |
|---|---|---|
| ✅ **Addressed** | The design handles it | *how* — one line is enough |
| ➖ **Not applicable** | This surface can't hit it | *why* — "no overlays on this page" |
| ⚠️ **Accepted** | It can happen, and we ship anyway | *what* the user will experience, and *why* it's worth it |

**"Accepted" is legitimate** — deadlines are real. What is not legitimate is *silent* acceptance. A recorded trade-off gets revisited; an unrecorded one becomes a permanent defect nobody remembers choosing.

## The review

**1. Scope it**
- [ ] Name the **archetype** — consumer-mobile · ops-panel · ecommerce · fancy-app · conversational-bot · game
- [ ] Name the **platforms** — mobile-web · pwa · tablet · desktop · web
- [ ] Filter [the pain registry](../pains/README.md) to those two. That is your list.

**2. Answer each pain**

| Pain | Answer | How / why |
|---|---|---|
| PAIN-001 Back exits the app | | |
| PAIN-002 Row click loses the list | | |
| PAIN-003 Full-height sections jump | | |
| PAIN-004 Keyboard crushes the form | | |

**3. Look for the pain you're about to create**
- [ ] What does this surface do that **no existing pain covers**? Overlays, long lists, live-updating data, money, destructive actions, anything that holds unsaved state — these are where pains come from.
- [ ] If you find one, **file it now** with `status: open`. A pain with no solution is still worth recording.

**4. Close the loop**
- [ ] Any ⚠️ accepted trade-offs are written into the surface's spec, not just this checklist.
- [ ] If you solved a pain **better than the registry's approach**, update that pain's §2 and §3 and say why yours wins. That is a contribution, not a deviation.

## Where this plugs into delivery

If you use the Arad delivery method, this maps cleanly:

- **Stage 3 (architect)** — the pain review runs as the epic's *expected behaviours* are written. Every ✅ addressed answer should show up as an EB, so QA can actually verify it.
- **Stage 5 (QA)** — any refinement that is a *pattern* rather than a one-off bug becomes a new pain entry. This is the intake pipe that keeps the registry fed from work you are already doing.

## The point

The registry only pays off if it is consulted **before** the design exists. Read at design time, it costs ten minutes and removes a class of defect. Read at QA time, it is a list of things you now have to go back and change.
