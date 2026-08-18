---
name: secure
description: Use when the user asks about the security of their app, wants a security review or audit, is about to publish or go live, or is building anything that handles credentials, payments, personal data, roles, or permissions — "is this secure", "review my security", "check for vulnerabilities", "am I safe to publish", "where do I put my API key", "set up RLS", "add authentication", "can users see each other's data", "protect this route". Also use when a change touches secrets, API keys, edge functions, row-level security, login, sessions, or role checks. Routes the concern to the right layer — frontend, edge function, database policy, or authentication — and applies the rule that belongs there. Not for platform account security or general web security theory; this is about the code in this app.
---

# Secure

Lovable apps have three layers, and each has exactly one security job. Nearly every real vulnerability comes from putting a decision in the wrong layer.

| Layer | Runs | Trust | Job |
|---|---|---|---|
| **Frontend** | In the user's browser | **None.** Public, inspectable, modifiable | Presentation only. Never decides access |
| **Edge functions** | Server-side, isolated | Trusted | Validation, authorisation, business logic, external calls |
| **Database (RLS)** | In the database | Trusted | Enforces row access even when the layers above fail |

The frontend is not a weak line of defence — it is **not a line of defence at all**. Anything shipped to the browser is readable and changeable by anyone who wants to.

## Route the concern

| The question or task | Playbook |
|---|---|
| Where do I put an API key, token, or secret? | [reference/frontend.md](reference/frontend.md) |
| Is there anything sensitive exposed in my client code? | [reference/frontend.md](reference/frontend.md) |
| Is form or input validation enough as written? | [reference/frontend.md](reference/frontend.md) |
| What belongs server-side rather than in a component? | [reference/edge-functions.md](reference/edge-functions.md) |
| Calling an external or paid API safely | [reference/edge-functions.md](reference/edge-functions.md) |
| Payments, uploads, registration, anything multi-step | [reference/edge-functions.md](reference/edge-functions.md) |
| Can users see or change each other's data? | [reference/rls.md](reference/rls.md) |
| Setting up or reviewing row-level security | [reference/rls.md](reference/rls.md) |
| Team, organisation, or shared-record access rules | [reference/rls.md](reference/rls.md) |
| Login, sessions, roles, protecting a route | [reference/auth.md](reference/auth.md) |
| Admin areas and privileged actions | [reference/auth.md](reference/auth.md) |
| Full security review, or "am I safe to publish?" | [reference/review.md](reference/review.md) |

If the request spans layers — most real ones do — start at [reference/review.md](reference/review.md) and let it dispatch.

## The rules that hold everywhere

**Every security decision is made server-side.** Authentication, authorisation, validation, pricing, quotas, role checks. The browser may reflect a decision; it may never make one.

**Assume all client input is hostile.** Not because the user is, but because the request can be replayed, edited, or forged by anyone regardless of what your UI allows.

**Hiding is not protecting.** A button that is not rendered, a route not linked, a field disabled — none of these stop the underlying request. If the API allows it, it is allowed.

**RLS is the floor, not the fallback.** Policies enforce access even when a function has a bug or a query is wrong. An app whose safety depends on every query being written correctly has no floor.

**Never widen a policy to unblock a feature.** A policy relaxed during development is a data leak that ships. Express the real rule instead.

**Secrets never reach the browser.** Not in code, not in a config file, not in a build-time variable, not in a comment. A secret that was ever shipped to a client must be treated as compromised and rotated, not deleted and forgotten.

## When you find something

Report by severity, and be specific about what an attacker can actually do — not "the key is exposed", but "any visitor can read this key from the bundle and issue paid API calls on your account".

| Severity | Meaning |
|---|---|
| **Critical** | Exploitable now, with real consequences: exposed live secrets, data readable across users, an unprotected privileged action |
| **High** | A decision made in the wrong layer that is currently reachable |
| **Medium** | Missing defence in depth — the exposure is not reachable today, but only by accident |
| **Low** | Hardening, and practices worth changing before they matter |

Fix critical findings immediately and say what needs rotating. Never report an app as secure because a scan passed: automated checks cover configuration and known patterns, not whether your access rules express what you actually meant.
