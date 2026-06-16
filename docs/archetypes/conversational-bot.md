---
title: "Archetype: Conversational / bot UI"
summary: Chat & assistant interfaces — make turn-taking clear, set expectations, and build trust in a free-form box.
category: archetype
tags: [chatbot, conversational, ai, assistant, messaging]
platforms: [mobile-web, pwa, web, conversational]
archetypes: [conversational-bot]
status: seed
related:
  - ../principles/feedback-for-every-action.md
last_updated: 2026-06-16
---

# Archetype: Conversational / bot UI

> A text box hides everything the app can do. The core challenge is **affordance and trust**: helping users know what to say, what's happening, and whether to believe the answer.

## Who it's for

Users of chatbots, AI assistants, and messaging-based flows — from support bots to LLM copilots. They face a blank prompt with no menu.

## Must do ✅

- **Reveal capability** — starter prompts, examples, or quick-reply chips so users know what to ask.
- **Clear turn-taking** — distinct user/bot bubbles, a visible **typing/thinking** indicator, and streamed responses so it feels alive.
- **Set expectations** — say what the bot can and can't do; don't pretend to be human if it isn't.
- **Trust & verifiability** — cite sources, show confidence/uncertainty, and let users correct or retry.
- **Graceful fallback** — when the bot doesn't understand, offer options or a path to a human.
- **Safe actions** — confirm before any real-world/destructive action taken on the user's behalf.

## Should avoid ❌

- ❌ A blank box with no guidance ("What can you do?" should never be a mystery).
- ❌ Long silences with no thinking/streaming indicator.
- ❌ Walls of text; no structure, no formatting, no chunking.
- ❌ Overclaiming certainty; hiding that it's an AI.
- ❌ Dead-ends on misunderstanding with no recovery.

## Notes from experience

> *(seed — to expand)* Starter chips + streaming responses are the two changes that most improve how capable and trustworthy a bot feels — before touching the model at all.
