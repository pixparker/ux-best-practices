---
title: Visual hierarchy guides the eye
summary: Use size, weight, color, and spacing so the most important thing is obviously the most important.
category: principle
tags: [hierarchy, layout, attention, emphasis, scanning]
status: draft
related:
  - ../ui/type-scale-and-readability.md
  - ../ui/spacing-and-layout.md
last_updated: 2026-06-16
---

# Visual hierarchy guides the eye

> Users don't read screens — they scan them. Visual hierarchy is how you decide *what they see first*. If everything shouts, nothing is heard.

## Why it matters

Every screen has one primary thing the user should do or notice. Hierarchy uses visual weight to rank elements so the eye lands on that first, then flows to secondary and tertiary content. Flat, undifferentiated UIs force users to read everything to find anything — slow and tiring.

## The guideline

Rank elements with these levers (combine a few, not all at once):

- **Size** — bigger = more important.
- **Weight & color** — bold/saturated draws the eye; muted recedes.
- **Spacing** — whitespace isolates and elevates; grouping implies relationship.
- **Position** — top/left and above-the-fold get seen first (LTR scanning).
- **Contrast** — the highest-contrast element wins attention.

**Do**

- ✅ Pick **one primary action per view**; style it as clearly dominant.
- ✅ Demote secondary/tertiary actions (ghost/text buttons, smaller, muted).
- ✅ Use **whitespace** to separate groups — proximity = relationship.
- ✅ Establish 3 tiers (primary / secondary / supporting) and stick to them.

**Don't**

- ❌ Make everything bold, boxed, or brightly colored ("everything is loud").
- ❌ Show two equally-weighted primary buttons competing for the click.
- ❌ Rely on color alone for emphasis (fails for color-blind users).
- ❌ Cram with no breathing room so nothing stands out.

## Pitfalls & anti-patterns

- **Competing CTAs** — two equal buttons cause hesitation; rank them.
- **Decoration as hierarchy** — borders/boxes everywhere flatten emphasis.
- **Color-only signals** — pair color with weight/size/icon for accessibility.

## Notes from experience

> *(draft — replace with your own)* When a screen feels "busy" or testers hesitate, it's usually missing hierarchy, not features. Demoting everything except the one primary action is faster and cheaper than a redesign.

## References

- Refactoring UI — *Creating Hierarchy*
- Gestalt principles (proximity, similarity)
