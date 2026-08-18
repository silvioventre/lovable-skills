# secure

Routes a security concern to the layer that owns it and applies the rule that belongs there. Built on one principle: the frontend is not a weak line of defence, it is not a line of defence at all.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/security/secure
```

## Use

```
/secure review this before I launch on Friday
/secure where should I put my Stripe API key?
/secure can users see each other's data?
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The three layers and their jobs, the routing table, and how to report severity |
| `reference/frontend.md` | Secrets, why build-time variables are public, and validation that is only ever cosmetic |
| `reference/edge-functions.md` | What belongs server-side, the shape of a safe function, and failing closed |
| `reference/rls.md` | The four access patterns, writing policies, and the verification that needs a second account |
| `reference/auth.md` | Authentication versus authorisation, protecting routes, privileged actions |
| `reference/review.md` | The full review order and the ten-item pre-publish gate |

## Scope

About the code in this app, not platform account security. Establishing *who* a user is belongs to [auth](../../build/auth/); this covers what they are then allowed to do.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
