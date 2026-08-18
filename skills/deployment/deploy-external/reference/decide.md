# Deciding what to move

## Start with the constraint, not the architecture

Ask what is actually forcing this. There are three answers that justify moving a component, and one that does not.

**Justified:**
- A compliance or data-residency requirement tied to a specific provider or region.
- Networking the platform does not offer — VPC peering, private endpoints, traffic that must not leave a network.
- An organisational policy mandating self-managed or independently audited hosting.

**Not justified on its own:**
- "We might need to scale." Managed infrastructure scales; the question is whether a specific limit has been hit.
- "We want more control." Control here means responsibility, and the next section lists what that costs.
- "We don't want to be locked in." There is no lock-in to escape. Code syncs to GitHub, data is portable, and the stack is open. The exit stays available whether or not it is used.
- "It seems more professional." It is more work, which is not the same thing.

If none of the justified reasons applies, say so directly and stop. A migration performed without a driving constraint is a permanent operating cost bought for nothing.

## The three configurations

**Everything on Lovable Cloud.** Preview and production managed, custom domains supported, no infrastructure to run. The right answer for most applications, including most that are live and earning.

**Hybrid.** Lovable for development and previews; one or more production components on managed services, with GitHub as the bridge. The usual shape when a specific backend or compliance requirement exists. Most commonly this is the frontend on a managed host with the backend staying put.

**Fully self-managed.** Code in your repository, backend and database on infrastructure you operate, frontend in containers or on VMs. Real infrastructure work, justified by policy rather than preference.

Note the asymmetry: the frontend is easy to move and easy to move back. The backend is neither. Prefer moving the frontend first when a partial move satisfies the constraint.

## What you take on

This is the part that gets underestimated, because it is ongoing rather than one-off.

**Moving the frontend out** makes you responsible for deployment pipelines and rollbacks, production environment variables, CDN and caching behaviour, uptime, production logs and deployment history, and preview environments for branches.

**Moving the backend out** makes you responsible for database availability, scaling, and backups; monitoring and incident response; RLS configuration and maintenance; authentication provider configuration; OAuth credentials, redirect URLs, and secret rotation; backend environment variables; security scanning; and the compliance posture of that infrastructure.

**Leaving entirely** adds development environments, CI/CD, SSL, infrastructure operation, AI provider accounts and billing, and ongoing security and compliance work.

Two consequences that are easy to miss until they bite:

- **Debugging changes shape.** Lovable cannot see infrastructure it does not control, so production diagnosis moves to that provider's logs and tools. The integrated debugging that made development fast does not extend past the boundary.
- **Some capabilities are Cloud-only.** Managed OAuth configuration and automatic token refresh are examples: they exist because the backend is managed, and reimplementing them is part of the cost of moving.

## Sequence it

Even when a move is justified, do it in the order that keeps a working system at every step:

1. **Sync to GitHub.** Do this regardless of any migration. It secures code ownership, enables external collaboration, and every external path builds from it.
2. **Move one component.** Usually the frontend. Verify it fully in production before continuing.
3. **Stop there unless the constraint is still unmet.** Most constraints are satisfied by one move. Moving further because the migration is "in progress" is how a frontend hosting change becomes a six-week infrastructure project.

**Before touching the backend, resolve the user-password question.** Passwords cannot be exported and every user will need a reset. If real users already exist, that is a communication and support problem to plan before the technical one — see [backend-migration.md](backend-migration.md).

## Presenting the plan

Separate what happens in the project from what the user does elsewhere. The in-project work — Dockerfiles, environment variables, configuration files, migration files — can be done here. Provider accounts, DNS, dashboards, and deployments cannot.

A plan that mixes them without saying so leaves the user waiting on steps nobody is going to perform.
