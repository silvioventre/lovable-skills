# deploy-external

Running the frontend or backend somewhere other than Lovable Cloud. Leads with whether to move at all — since nothing is locked in, moving later costs the same as moving now, so a move without a named constraint buys a permanent operating cost for nothing.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/deployment/deploy-external
```

## Use

```
/deploy-external can I host this on Netlify?
/deploy-external generate a Dockerfile for this project
/deploy-external we need the backend on our own infrastructure for compliance
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | Whether to move, the three parts that move independently, and the two facts that change plans |
| `reference/decide.md` | The constraints that justify moving, what you take on, and how to sequence it |
| `reference/frontend-hosting.md` | Build requirements, build-time variables, SPA routing, containers, and what to verify |
| `reference/backend-migration.md` | What migrates by hand, why user passwords do not, and rolling back |

## Scope

For publishing on Lovable Cloud, see [ship](../ship/).

## License

MIT — see the [repository LICENSE](../../../LICENSE).
