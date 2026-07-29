---
id: PAIN-000
title: Short, specific — name the pain, not the fix
pain: One sentence a busy reader grasps in five seconds. This is the durable part.
category: pain
tags: [tag-one, tag-two]
platforms: [mobile-web, pwa, tablet, desktop, web]   # where it bites; omit if universal
archetypes: [consumer-mobile, ops-panel, ecommerce, fancy-app, conversational-bot, game]
severity: friction            # friction | error | abandonment | data-loss
status: open                  # open | mitigated | solved
enforcement: prose            # prose | check | code
enforced-by: ""               # what enforces it, when not prose
solution: ../patterns/example.md      # the full how-to, if one exists
showcase: ../../showcases/example/    # runnable sample design
first-seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# PAIN-000 — Title

> **The pain.** One or two sentences. Written so it is still true in ten years — describe what the *person* experienced, not the framework that caused it.

## 1. Pain point

The story. A real person, doing a real thing, hitting the wall.

Cover:
- **Who** and what they were trying to do
- **What they expected** (this is usually the whole bug — a broken expectation)
- **What happened instead**, and what it cost them: re-work, lost state, lost trust, abandonment
- **Why it happens** — the underlying cause, not the symptom. Usually a default nobody chose.

Be specific about the cost. *"Annoying"* is not a cost. *"Re-scan the QR code and hunt for their place, every time"* is.

## 2. Approach / solution

What we did about it — **one reference implementation, not the only legal answer.**

- The mechanism, concretely enough to build from
- **What we rejected and why** — usually more useful than what we picked
- Where this approach has limits

> 🔒 A design may address this pain differently. What it may not do is leave it in place. If your answer is better, replace this section and say why.

## 3. The result

What actually changed after shipping. Be honest — including the parts that only half-worked.

- What improved, measured if you can
- What it did **not** fix
- Any new problem the fix introduced

## 4. Best practice

The durable rule this produced.

**Rule:** one sentence, imperative, checkable.

**Do**
- ✅ Concrete and copyable.

**Don't**
- ❌ The mistake that produced this entry.

**How it is enforced today**
- [ ] 🟢 code — a primitive makes the wrong thing hard
- [ ] 🟡 check — a lint / grep-gate / test fails on regression
- [x] 🔴 prose — this entry

**Full pattern:** `../patterns/<name>.md` · **Sample design:** `../../showcases/<name>/`

## Related pains

- `PAIN-NNN` — name the pain and how they interact
