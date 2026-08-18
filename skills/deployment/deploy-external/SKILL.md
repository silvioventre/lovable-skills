---
name: deploy-external
description: Use when the user wants to run part or all of their app outside Lovable Cloud, or is weighing whether to — "can I self-host this", "deploy to Netlify or Vercel or Cloudflare", "host it on AWS", "generate a Dockerfile", "move my backend to Supabase", "export my data", "am I locked in", "what happens if I stop using Lovable", "we need this on our own infrastructure for compliance". Covers whether to move at all, what you become responsible for once you do, what migrates automatically versus manually, the build requirements for hosting the frontend elsewhere, and the in-project changes a migration needs. Not for publishing on Lovable Cloud, which the ship skill covers.
---

# Deploy external

Running the app somewhere other than Lovable Cloud. The technical work is mostly routine; the decision and the transfer of responsibility are where this goes wrong.

## First: is this the right move?

The default answer is no, and saying so is more useful than a migration plan the user did not need.

The apps are standard Vite + React projects on open technologies, synced to GitHub, with a PostgreSQL-based backend. Nothing is locked in, which means **moving later costs the same as moving now** — so there is no deadline forcing an early decision, and no reason to pay the operating cost before something requires it.

Move a component when a real constraint demands it:

- Compliance or data residency tied to specific infrastructure
- Networking the platform does not support, such as VPC peering or private endpoints
- Organisational policy requiring self-managed or audited hosting

Do not move for a hypothetical: "we might need to scale", "we want more control", "it feels safer to own it". Each of those trades a managed platform for an operational burden that has to be carried indefinitely.

**If the user has not named a constraint, ask what is driving this** before planning anything. The honest answer is frequently that nothing is, and the conversation ends there — which is the correct outcome, not a failure to help.

## The three parts move independently

| Part | Default | Can move to |
|---|---|---|
| **Code** | Managed in Lovable, syncs to GitHub | Any Git workflow |
| **Frontend** | Lovable Cloud | Managed hosts, object storage plus CDN, containers, VMs |
| **Backend and data** | Lovable Cloud | Managed or self-hosted Supabase, or equivalent services |

You do not move all three at once, and most who move anything move only the frontend. Moving frontend hosting requires no architectural change and the backend can stay where it is.

**Sync to GitHub first, regardless.** It costs nothing, secures code ownership, and every external hosting path builds from the repository.

## Route the task

| The task | Playbook |
|---|---|
| Deciding whether and what to move | [reference/decide.md](reference/decide.md) |
| What you take on by moving | [reference/decide.md](reference/decide.md) |
| Hosting the frontend elsewhere | [reference/frontend-hosting.md](reference/frontend-hosting.md) |
| Build settings, env vars, Dockerfile | [reference/frontend-hosting.md](reference/frontend-hosting.md) |
| Moving the backend or database | [reference/backend-migration.md](reference/backend-migration.md) |
| Exporting data, "am I locked in" | [reference/backend-migration.md](reference/backend-migration.md) |

## Two facts that change plans

**User passwords cannot be exported.** Database contents migrate, but password hashes do not. Every existing user has to go through a password reset on the far side. This is survivable with ten users and a serious event with ten thousand — so if a backend migration is even a possibility, **do it before onboarding real users.** Raise this early; it is the kind of thing discovered at the worst moment.

**Build-time variables are baked into the bundle.** Variables prefixed `VITE_` are embedded when the frontend is built, not read at runtime. Changing one means rebuilding and redeploying, and any value placed there is shipped to every visitor. Never put a secret in one — see the `secure` skill.

## What Lovable can and cannot do here

**In the project, and doable:** generating a Dockerfile and deployment configuration, updating environment variables and backend configuration files, preparing migration files, adjusting build setup.

**Outside the project, and the user's to do:** creating accounts with a hosting provider, DNS and registrar configuration, dashboard steps, uploading storage files, running deployments on their infrastructure.

Say which is which when laying out a plan. A migration plan that silently mixes the two leaves the user waiting for steps that will never happen on their own.

Once anything runs outside Lovable Cloud, **Lovable cannot monitor or debug infrastructure it does not control.** Production failures there are diagnosed with that provider's logs and tools.
