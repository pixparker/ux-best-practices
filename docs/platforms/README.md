# 📱 Platforms — *where it runs*

A **platform** is a delivery context. It imposes constraints and conventions independent of *what* you're building. Pick your [archetype](../archetypes/) first, then layer the platform rules here on top.

> Archetype × Platform. A "consumer mobile app" delivered as a "PWA" inherits both playbooks.

## Platforms

### 📲 Mobile web
- Thumb zones & reachability (bottom-anchored primary actions) — [bottom sheets & thumb zone](../patterns/bottom-sheet-and-thumb-zone.md)
- Tap targets ≥ 44×44px, generous spacing
- `font-size ≥ 16px` on inputs (avoid iOS zoom-on-focus)
- Own your touch feedback — kill the default tap-highlight flash — [tap & touch feedback](../ui/tap-and-touch-feedback.md)
- Safe areas (`env(safe-area-inset-*)`), no hover-only affordances
- Performance on mid-range devices & flaky networks

### ⚡ PWA (installable web app)
- Offline-first & graceful degradation
- App manifest, install prompt timing, splash & icons
- Caching strategy (stale-while-revalidate), update flow
- Feeling "native": no rubber-band jank, standalone display mode

### 🖥️ Desktop / web
- Keyboard shortcuts & focus management
- Hover, right-click, multi-select, drag & drop
- Responsive breakpoints & large-screen layout (don't just stretch mobile)
- Window resizing, multi-column density

## Planned entries

- Thumb-zone layout guide (mobile-web)
- Offline strategy cookbook (pwa)
- Keyboard & focus management (desktop)
- Responsive breakpoints that aren't arbitrary

> Want to add one? Copy [`../_TEMPLATE.md`](../_TEMPLATE.md).
