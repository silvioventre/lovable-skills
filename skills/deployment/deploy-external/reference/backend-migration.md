# Moving the backend and data

Harder than moving the frontend and much harder to reverse. Do not start without a named constraint that requires it — see [decide.md](decide.md).

## Settle this before anything else

**Passwords cannot be exported.** Schema, policies, and table contents migrate. Password hashes do not. Every existing user must go through a password reset on the far side.

With a handful of users this is an email. With a real user base it is a support event, a drop in returning users, and a reason people never come back. So:

- **If the app has no real users yet, migrate now** if you are going to at all. The cost is near zero today and grows with every signup.
- **If it has real users**, the reset flow is part of the migration plan, not an afterthought: when it is sent, what it says, what happens to users who ignore it, and how support handles the ones who are locked out.

Raise this at the start of the conversation. Discovering it mid-migration is how a technical task becomes an incident.

## What migrates, and how

| Component | Method | Notes |
|---|---|---|
| Database schema | Automatic, via SQL migrations | Tables, columns, indexes, RLS policies, functions, triggers |
| Storage buckets | Automatic, via SQL migrations | Includes access policies |
| Table contents | Manual | Export per table, or request a full database export, then import |
| Storage files | Manual | Download and re-upload |
| Auth providers | Manual | Reconfigure OAuth and other providers at the destination |
| Secrets and env vars | Manual | Re-enter API keys and credentials for every external service |
| User accounts | Manual, partial | Data exports; **passwords do not** |

"Automatic" means the migration files already exist in the project and run against the new database. Everything marked manual is work someone performs, and each item is a chance to arrive with an app that connects but does not function.

## The in-project changes

These are real edits to the project and can be done here:

- **`.env`** — replace the connection values with the new project's URL, project ID, and publishable key.
- **`supabase/config.toml`** — update the project id.
- **`supabase/migrations/`** — the existing migration files, run against the new database **in chronological order by their filename timestamps**. Out of order, they fail or produce a schema that differs subtly from the original.

Everything else is dashboard work at the destination provider: creating the project, running the migrations, importing data, reconfiguring auth, entering secrets. Say so explicitly when laying out the plan.

## What you take on

Once the backend is elsewhere, you own: database availability, scaling, and backups; monitoring and incident response; RLS configuration and maintenance; authentication provider configuration; OAuth credentials, redirect URLs, and secret rotation; backend environment variables; security scanning; and the compliance posture of that infrastructure.

Some capabilities do not travel because they exist as part of the managed backend. Managed OAuth configuration and automatic token refresh are the usual examples — reimplementing them is part of the cost, not a surprise afterwards.

The underlying database is PostgreSQL, but the app depends on Supabase-specific services: auth, storage, realtime, edge functions. Moving to managed or self-hosted Supabase is a supported path. Moving to plain PostgreSQL means building equivalents for all of those yourself, and is not a migration so much as a rewrite of everything above the database.

## Verify

Do not consider it done until each of these passes against the new backend:

- **Schema matches.** Tables, columns, indexes, functions, triggers — compare rather than assume the migrations covered everything.
- **RLS is enabled and policies are present on every table.** Migrations carry policies, but confirm rather than trust: a table arriving without RLS is an open table.
- **A second account cannot read the first account's data.** The check from the `secure` skill. Run it again here — a migration is exactly the event that silently drops a policy.
- **Sign-in works**, including OAuth providers and their redirect URLs, which usually still point at the old origin.
- **Reads and writes work** from the deployed frontend, not just from a dashboard.
- **Edge functions run**, with every secret they need present. A missing secret surfaces as a confusing runtime error rather than a clear configuration failure.
- **Storage files are actually there** and reachable at the paths the app expects.

## Rolling back

Keep the original backend running until the new one is verified under real use. Cutting over and decommissioning the same day removes the only fallback at the moment it is most likely to be needed.

Data written to the new backend after cutover does not exist in the old one, so a rollback beyond that point means losing it. That window is the real deadline for verification, and it is worth naming out loud before the switch rather than discovering it during one.
