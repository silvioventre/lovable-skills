# payments

Taking money, with the two-environment model as the organising fact and the irreversible operations behind an explicit confirmation. Built around testing the whole subscription lifecycle before real money is involved.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/payments
```

## Use

```
/payments add monthly and annual plans, unlock premium features for subscribers
/payments I paid in test mode but nothing unlocked
/payments I'm ready to go live
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | Test versus live, the three operations that cannot be undone, and the entitlement rules |
| `reference/setup.md` | Choosing a provider, products and prices, and the entitlement logic that actually matters |
| `reference/testing.md` | Test cards and the lifecycle scenarios — cancellation, renewal, failed payment, trial |
| `reference/go-live.md` | The readiness check, verification, catalogue sync, and the one real transaction to run |
| `reference/changing.md` | Disconnecting and switching provider, and what happens to existing subscribers |

## Scope

Server-side enforcement of prices and permissions belongs to [secure](../../security/secure/). Add [auth](../auth/) first — a purchase that cannot be attached to an account is one you cannot honour.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
