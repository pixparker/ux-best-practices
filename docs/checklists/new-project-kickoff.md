---
title: New-project UX kickoff checklist
summary: Decide the fundamentals — archetype, platform, key flows, and constraints — before designing screens.
category: checklist
tags: [kickoff, planning, archetype, scoping, founder]
status: draft
related:
  - ../archetypes/README.md
  - ../platforms/README.md
last_updated: 2026-06-16
---

# New-project UX kickoff checklist

> Run this at the start of a project. It's the founder-reuse flagship: answer these once, up front, and you stop re-deriving the basics mid-build.

## 1. Frame the product
- [ ] **Archetype** chosen — see [archetypes](../archetypes/): consumer-mobile · ops-panel · fancy-app · ecommerce · conversational-bot · game.
- [ ] **Primary platform** chosen — see [platforms](../platforms/): mobile-web · PWA · desktop · web. (Mobile-first unless proven otherwise.)
- [ ] **Who is the user?** Technical vs. non-technical, frequency (daily power-user vs. first-timer).
- [ ] **The one job** the product must nail in v1 (resist scope creep).

## 2. Map the critical flows
- [ ] List the **top 1–3 user flows** that define success.
- [ ] For each flow, name the **single primary action** per screen.
- [ ] Identify the **first-run experience** (what a brand-new, empty account sees).

## 3. Lock the foundations (reuse the system, don't reinvent)
- [ ] **Type scale** + body ≥16px on mobile — [type scale](../ui/type-scale-and-readability.md).
- [ ] **Spacing scale** (4/8pt) — [spacing & layout](../ui/spacing-and-layout.md).
- [ ] **Color tokens** + contrast plan + dark mode decision — [color & contrast](../ui/color-contrast-and-dark-mode.md).
- [ ] Component basics: buttons, inputs, cards, modals/sheets.

## 4. Non-negotiables (apply from day one)
- [ ] **Every state designed**: empty / loading / error — [design every state](../principles/design-every-state.md).
- [ ] **Feedback for every action** + no double-submit — [feedback](../principles/feedback-for-every-action.md).
- [ ] **Forgiveness**: destructive actions reversible/undoable — [forgiveness](../principles/forgiveness-undo-over-confirm.md).
- [ ] **Accessibility baseline** planned — [a11y checklist](accessibility-checklist.md).
- [ ] **Perceived performance** plan (skeletons, optimistic UI where it fits).

## 5. Constraints & reality
- [ ] Target devices & **network conditions** (test on mid-range + throttled).
- [ ] Localization / RTL needed?
- [ ] Brand/visual direction or reference [prototype](../../prototypes/) picked.
- [ ] Analytics/feedback loop to learn from real users post-launch.

## Notes from experience

> *(draft — replace with your own)* Naming the archetype and the one job first prevents 80% of mid-project UX debates. Most rework comes from skipping step 1 and designing screens before deciding what kind of app this even is.
