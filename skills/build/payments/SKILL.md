---
name: payments
description: Use when the user wants to take money in their app or is working on something already taking it — "add payments", "add Stripe", "set up subscriptions", "add a pricing page with checkout", "sell a plan", "test the checkout flow", "go live with payments", "add a manage subscription button", "switch from Paddle to Stripe", "my subscription isn't unlocking features", "handle failed payments". Covers choosing a provider, building the entitlement logic, testing the full subscription lifecycle in the test environment, the go-live checklist, and the irreversible operations. Not for the server-side security of pricing and permissions, which the secure skill owns.
---

# Payments

Payment bugs are expensive in a way other bugs are not — they charge people wrongly, or they hand out access nobody paid for, and both are discovered by customers rather than by you. Everything here is built around testing the full lifecycle before real money is involved.

## Two environments, always

| Environment | Applies to | Cards | Money |
|---|---|---|---|
| **Test** | the preview | test cards only | none |
| **Live** | the published app | real cards | real |

Each has its own products, prices, and transaction history. Publishing syncs products and prices from test to live automatically, so **test is the source of truth for the catalogue** — this is why editing products directly in the provider's dashboard causes ID mismatches and should be avoided.

Both stay active after going live, so new products and changes get tested in the preview before they reach paying customers.

## Route the task

| The task | Playbook |
|---|---|
| Choosing a provider, enabling payments | [reference/setup.md](reference/setup.md) |
| Products, prices, checkout, entitlements | [reference/setup.md](reference/setup.md) |
| Testing a purchase or the subscription lifecycle | [reference/testing.md](reference/testing.md) |
| "Subscription isn't unlocking features" | [reference/testing.md](reference/testing.md) |
| Going live, readiness check, verification | [reference/go-live.md](reference/go-live.md) |
| Disconnecting, switching provider | [reference/changing.md](reference/changing.md) |

## Before doing anything irreversible

Three operations here cannot be undone. Say so plainly before performing any of them, and get explicit confirmation.

- **Disconnecting payments is permanent.** The same provider account cannot be reconnected to the same project afterwards. Setting payments up again requires a different provider account.
- **Switching providers loses the catalogue and the subscribers.** Products, prices, and existing subscriptions do not migrate. Current subscribers stay on the old provider until they cancel and resubscribe.
- **A project with payments cannot be remixed.** If forking the project matters, that door closes when payments are enabled.

Details and the correct sequence in [reference/changing.md](reference/changing.md).

## The rules

**Never trust an amount that came from the browser.** The client sends a request; the server decides the price. A checkout that accepts the amount from the frontend lets anyone pay zero, however the UI restricts the field. This is the `secure` skill's territory and it is not optional here.

**Entitlement is a server-side question.** "Does this user have access to this feature" is answered by checking the subscription state on the server, never by a flag in client state or a value the client passed in.

**Do not revoke access the moment a subscription is cancelled.** The user has paid through the end of their billing period and keeps access until then. Cutting access at cancellation is a support ticket and a chargeback waiting to happen.

**Handle a failed renewal gracefully.** A `past_due` subscription should prompt the user to update their payment method, not immediately lock them out. Payments fail for expired cards far more often than for abandonment.

**Do not create webhooks manually.** They are registered automatically, and duplicates cause problems that are hard to trace.

## Report

State which environment the work applies to — test or live — in every message about payments. A change described without its environment is ambiguous in the one area where ambiguity costs money.
