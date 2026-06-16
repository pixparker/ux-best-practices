# Docs — the map

This reference is organized along **two axes** plus a set of cross-cutting craft topics.

```
            WHAT you're building  →  archetypes/   (product playbooks)
            WHERE it runs         →  platforms/    (delivery constraints)
                                        ×
   craft  →  principles/ · ui/ · patterns/ · techniques/
   action →  checklists/
```

Pick an **archetype** (the kind of app), layer the **platform** constraints, then pull from the craft topics. Checklists turn it all into something you can ship against.

---

## Browse by area

### 🧠 Principles — *why*
The timeless laws behind good UX & UI. Stack-agnostic, slow to change.
→ [`principles/`](principles/)

### 🎨 UI craft — *look*
Visual interface best practices: typography, color & contrast, spacing & layout, motion, iconography, components, design tokens.
→ [`ui/`](ui/)

### 🧩 Patterns — *behavior*
Reusable solutions to recurring interaction problems: navigation, forms, empty states, search & filtering, etc.
→ [`patterns/`](patterns/)

### ✨ Techniques — *feel*
Modern tricks that make apps feel smooth and alive: skeleton loading, optimistic UI, view transitions, micro-interactions, prefetching.
→ [`techniques/`](techniques/)

### 📦 Archetypes — *what you're building*
Opinionated playbooks per product type. Each bundles the priorities, patterns, and pitfalls that matter most for that kind of app.
→ [`archetypes/`](archetypes/)

### 📱 Platforms — *where it runs*
Constraints and conventions per delivery target: mobile web, PWA, desktop, web.
→ [`platforms/`](platforms/)

### ✅ Checklists — *ship it*
Actionable, scannable lists to run before kicking off or shipping a project.
→ [`checklists/`](checklists/)

---

## How an entry is structured

Every guideline follows [`_TEMPLATE.md`](_TEMPLATE.md): a takeaway, *why it matters*, concrete **do / don't** advice, a link to a runnable showcase when one exists, pitfalls, and **notes from experience**.

Each entry carries front-matter with a `status:` — `seed` (a stub idea), `draft` (taking shape), or `stable` (battle-tested).
