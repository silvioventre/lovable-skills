# Testing payments

The test environment is live from the moment setup finishes. Use it properly — this is the only chance to find these bugs without a real customer finding them.

## Test cards

| Card number | Result |
|---|---|
| `4242 4242 4242 4242` | successful payment |
| `4000 0000 0000 3220` | payment requiring 3D Secure |
| `4000 0000 0000 0002` | failed payment |

Any future expiry, any 3-digit CVC, any billing address.

A test-mode banner is added automatically and appears only in the preview, never on the published site.

## Test the lifecycle, not the purchase

A successful purchase proves the smallest part of the system. Everything expensive happens afterwards, and each of these is a distinct code path that fails independently:

| Scenario | What must be true |
|---|---|
| **Purchase** | The right features unlock, immediately, for that user only |
| **Upgrade** | The new tier's features unlock and the old tier's limits lift |
| **Downgrade** | Access reduces correctly, and at the right moment rather than instantly |
| **Cancellation** | Access continues to the end of the paid period, then stops |
| **Renewal** | The subscription renews and access continues without interruption |
| **Failed renewal** | `past_due` is handled gracefully — prompt to update payment, not an immediate lockout |
| **Trial** | A trialing user has access, and billing starts correctly when the trial ends |
| **Discount code** | The reduced price applies at checkout, and entitlement is unaffected |

The two most commonly broken: **cancellation revoking access immediately** rather than at period end, and **trialing users being treated as unpaid**. Both come from checking only for an `active` status.

Subscription renewals can be simulated in test mode without waiting a billing cycle — ask how to trigger one rather than assuming it must be waited out.

## After each test purchase

1. **Confirm the entitlement actually changed** — the feature is genuinely usable, not just that a success message appeared.
2. **Check the transaction appears** in the Payments tab with the expected amount and status.
3. **Check a second, non-paying account is unaffected.** Entitlement leaking to other users is the failure nobody tests for and the worst one to ship.

That third check matters as much here as it does in the `secure` skill's RLS work, and for the same reason: it cannot be established from your own session.

## When entitlement does not unlock

The common report — *"I paid but nothing happened"*. Work down the chain and find the first broken link rather than guessing:

1. **Did the payment succeed?** Check the Payments tab. If not, this is a checkout problem, not an entitlement one.
2. **Did the webhook arrive?** Subscription state is updated by the provider calling back. If the payment succeeded and nothing changed server-side, the webhook is the suspect. Check the edge function logs — the `debug` skill's backend playbook covers this.
3. **Is the subscription state stored correctly?** Query it directly. A state of `trialing` or `past_due` that the entitlement logic does not handle looks identical to no subscription at all.
4. **Does the entitlement check read that state?** If the state is right and access is still denied, the bug is in the check — commonly a comparison against `active` only.
5. **Does the UI reflect it?** A correct server-side entitlement rendered against stale client state. Not a payments bug at all.

Never fix this by granting access in the client. That resolves the symptom for the reporter and makes the feature free for everyone who opens dev tools.

## What the preview cannot test

- **The customer portal**, which opens in a new tab and cannot be iframed. Test it on the deployed site.
- **Real card behaviour**: genuine 3D Secure challenges, bank declines, regional payment methods.
- **Real webhook timing** under load.

These move to live, which is why the go-live checklist exists — [go-live.md](go-live.md).
