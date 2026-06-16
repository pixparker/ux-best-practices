---
title: Feedback for every action
summary: Every user action must produce an immediate, visible response — otherwise users feel lost and retry.
category: principle
tags: [feedback, responsiveness, trust, states]
status: stable
related:
  - ../techniques/skeleton-loading.md
last_updated: 2026-06-16
---

# Feedback for every action

> When a user does something, the interface must *visibly* acknowledge it — instantly. Silence reads as "broken."

## Why it matters

Humans expect cause and effect. Tap a button, something happens. When nothing visibly changes within ~100ms, users assume the tap didn't register and tap again — causing double submissions, frustration, and lost trust. The interface feels dead.

Feedback is how the UI says *"I heard you, I'm working on it, here's what happened."* It's the single cheapest way to make an app feel responsive and trustworthy.

## The guideline

Acknowledge every interaction across the **full lifecycle**: *intent → in-progress → result.*

**Do**

- ✅ Give an **instant** visual response on press (color, scale, ripple) — within 100ms, before any network call resolves.
- ✅ Show a **busy state** for anything that takes time (spinner, progress, skeleton, disabled+loading button).
- ✅ Confirm the **outcome** — success toast, inline checkmark, updated value, or a clear error with a next step.
- ✅ Disable or lock controls during submission to prevent double-firing.
- ✅ Use [optimistic UI](../techniques/) for high-confidence actions so the result *feels* instant.

**Don't**

- ❌ Fire a network request with zero visual change and hope it's fast.
- ❌ Show a generic "Error" with no cause and no recovery path.
- ❌ Block the whole screen with a spinner for a small, local change.
- ❌ Let success be invisible — "did my save work?" is a UX failure.

## The three states to always cover

| State | User question | Answer with |
| --- | --- | --- |
| **Pressed** | "Did it register?" | Active/pressed style, ripple, haptic |
| **Pending** | "Is it working?" | Spinner, skeleton, progress, disabled-loading |
| **Resolved** | "What happened?" | Toast, inline confirmation, error + recovery |

## Pitfalls & anti-patterns

- **Feedback theater** — fake 2-second spinners on instant actions feel slower, not more "premium."
- **Over-toasting** — a toast for every trivial action becomes noise. Confirm in place when you can.
- **Blocking the UI** for background work that doesn't need to block it.

## Notes from experience

> The most common bug I see in MVPs: a submit button with no loading/disabled state. On a slow connection the user taps three times, three records get created, and now there's a "duplicate data" bug that's really a *missing-feedback* bug. Fix it at the source — lock the control the instant it's pressed.

## References

- Nielsen Norman Group — *Response Times: The 3 Important Limits*
- Material Design — *States* and *Communicating status*
