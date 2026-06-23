---
title: A reload lands on the main content
summary: Reloading (or cold-opening/sharing) a page should bring the user to the main, meaningful content — never strand them inside an ephemeral overlay, a half-finished transient step, or a blank/error.
category: principle
tags: [reload, state, url, overlays, robustness, navigation]
status: draft
related:
  - design-every-state.md
  - ../patterns/back-friendly-modals.md
  - ../patterns/preview-modal-over-full-page.md
last_updated: 2026-06-16
---

# A reload lands on the main content

> When a user hits refresh, they should arrive at the **main content** — the list, the home, the thing the page is *about*. They should never be dumped into a leftover modal, a transient half-step, or a blank screen. Reload is the universal "give me a clean, working view" gesture; honor it.

## Why it matters

Users reload to recover — when something feels stuck, slow, or off. If a refresh restores a transient overlay, a partially-filled wizard step, or a spinner-that-never-ends, you've re-trapped them in the very state they were trying to escape. The main content is the dependable "home base"; reload should always reach it.

## The principle

Treat UI state as two kinds, and persist accordingly:

| Kind | Examples | On reload |
| --- | --- | --- |
| **Ephemeral UI** | Quick-preview modal, drawer, toast, tooltip, unsaved transient step | **Gone** — reload shows the main content behind it |
| **Meaningful destination** | A filtered list view, a specific record's page, a search results URL | **Restored** — because it's URL-backed and worth sharing |

## The guideline

**Do**

- ✅ Keep ephemeral overlays in memory/history (not the URL) so a refresh returns to the base view. *(This is why the [preview pattern](../patterns/preview-modal-over-full-page.md) reload-lands on the list.)*
- ✅ Give **meaningful, shareable** states a real URL (filters, item pages) so reload restores *that* destination — a coherent place, not a fragment.
- ✅ Make the main content the reliable landing for a cold open / shared link / refresh.
- ✅ If you restore persisted state (scroll, draft), **validate it still makes sense** and degrade to the main content if not.

**Don't**

- ❌ Strand the user inside a modal/overlay after reload with nothing usable behind it.
- ❌ Reload into a half-completed, unsaved transient step that can't stand on its own.
- ❌ Land a refresh on a blank screen, an infinite spinner, or a raw error when real content exists.
- ❌ Persist ephemeral UI so aggressively that a refresh unexpectedly re-opens a transient preview.

## Showcase

- 👉 [`showcases/ops-panel/`](../../showcases/ops-panel/) — open a row's **preview** and reload → you're back on the list (ephemeral). **Enlarge** it to the full view and reload → that exact item is restored, because the full view has its own URL (`?item=…`). Both halves of this principle, side by side.

## Relationship to deep-linking & Back

This complements — doesn't contradict — [back-friendly modals](../patterns/back-friendly-modals.md) and deep-linkable views. **Back** peels the last overlay; **the URL** captures meaningful destinations; **reload** resolves to whatever the URL means — which for an ephemeral overlay is simply the main content beneath it. The rule of thumb: *if a state is worth surviving a reload, it earns a URL; otherwise it's ephemeral and a refresh clears it.*

## Notes from experience

> My rule: a reload always brings the user to the main content. Overlays, previews, and transient steps are ephemeral — refreshing should never leave someone stuck inside one. If a state is genuinely worth keeping across a reload (a filtered view, a specific item), it earns its own URL; everything else clears on refresh and the user lands back on the main content.

## References

- MDN — History API & `popstate` vs. document reload
- web.dev — URL as state / shareable, reload-safe views
