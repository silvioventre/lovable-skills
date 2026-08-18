# Disconnecting and switching provider

The irreversible operations. Everything here needs stating plainly and confirming explicitly before it happens.

## Disconnecting is permanent

**The same provider account cannot be reconnected to the same project afterwards.** Setting payments up again on that project requires a different provider account entirely.

There is no undo, and the confirmation dialog asks you to type `DISCONNECT` in capitals precisely because people do this by accident.

**What disconnecting does:**

- Removes the API keys, webhook secrets, and payment environment variables from the project.
- Deletes the registered webhooks — on a best-effort basis. If that call to the provider fails, the webhook stays on their side and is auto-disabled after repeated delivery failures.
- Stops checkout, subscription syncing, and webhooks immediately. **Live checkout on the published site breaks at once.**

**What it does not do, and this is where people get hurt:**

- **It does not cancel active subscriptions.** Customers keep being billed by the provider until each subscription is cancelled in the provider's dashboard. Disconnecting and walking away means charging people for a product they can no longer access.
- **It does not issue refunds.**
- **It does not notify customers.** If checkout is going away, that communication is yours to plan.
- It does not close or modify the provider account, and does not affect other projects using it.

So the order matters: **decide what happens to existing subscribers before disconnecting, not after.** Cancel or migrate them, and tell them, while you still have working integration to do it with.

## Switching provider

Only one provider per project. Switching is disruptive, and the losses are not recoverable:

- **Products and prices do not carry over.** The catalogue is recreated by hand.
- **Existing subscriptions do not migrate.** Current subscribers stay on the old provider until they cancel and resubscribe, or are moved manually.
- **Transaction and analytics history stays with the old provider.** Past payments, payouts, and reporting remain in that dashboard.
- Webhooks, customer IDs, and provider-specific code are all regenerated.

If there are paying subscribers, the migration is a customer communication project with a technical component, not the reverse. Say that before starting.

### The sequence, and why the middle step exists

1. **Disconnect the current provider**, from the Payments dashboard. This cannot be done from chat.

2. **Remove the old provider's code before enabling the new one.** SDK imports, hooks, server functions, webhook routes, and any database tables that existed only for the old provider.

   This step is not tidiness. With two providers' code in the same project, the agent gets confused about which one it is wiring, and produces broken edits while appearing to work. Removing the old code first is what makes the next step reliable.

3. **Enable the new provider** and recreate products, prices, and checkout:

   > Switch my payments from Paddle to Stripe.

Then test the entire lifecycle again in the test environment — [testing.md](testing.md) — and go through go-live again from the start. The previous provider's verification does not carry over.

## Other closed doors

- **A project with payments cannot be remixed.** If forking the project might matter, that is decided when payments are enabled, not later.
- **One subscription per user per environment** by default. Add-ons or multiple concurrent subscriptions require asking for that behaviour to be adjusted.
- **Checkout styling and payment methods** live in the provider's dashboard, not in Lovable.

## Before performing any of this

State which operation is about to happen, that it is irreversible, what is lost, and what happens to existing customers. Then wait for explicit confirmation.

A user who says "just remove the payments stuff" is usually thinking about their code, not about the subscribers who will keep being charged for it.
