# Setting up payments

## Prerequisites

- A paid Lovable plan.
- Lovable Cloud, which handles webhooks and subscription data. If it is not enabled, setup will ask for it.
- **Authentication in the app.** Strictly recommended rather than required, but a purchase that cannot be linked to a user is a purchase you cannot honour later. If the app has no auth yet, add it first — see the `auth` skill.

Provider accounts are created and managed for you; there is no separate signup, and the cost is the same as going to the provider directly.

## Choosing a provider

One provider per project, and switching later is disruptive (see [changing.md](changing.md)), so this is worth a minute now rather than a migration later.

The practical differences that affect the build:

- **Checkout presentation.** One provider offers an overlay modal (default) or inline embedding within the page; the other embeds only, and its styling is configured in its own dashboard rather than through Lovable.
- **Physical goods.** Built-in payments assume digital products by default. Selling physical items points you at a different integration.

Both provide a hosted customer portal for cancellations, payment method updates, and invoices.

If the user has no preference, say so and pick one rather than opening a comparison — the difference rarely matters as much as getting the entitlement logic right.

## Products and prices

**Create and edit them through Lovable, not in the provider's dashboard.** Products created through Lovable sync from test to live at publish; ones created directly in the provider dashboard do not participate in that sync and produce ID mismatches between environments that are painful to unpick.

A product can have several prices — monthly and annual for the same plan is the normal case.

## Entitlements: the part that actually matters

The checkout is the easy half. The half that produces bugs is deciding what a paying user is allowed to do, and that logic is yours.

**Resolve entitlement on the server, from subscription state.** Not from a value in client state, not from a flag the client sent, not from what the UI last saw. A component may *render* based on entitlement; it may never *decide* it. See the `secure` skill.

Design the entitlement check as a single function that answers "what is this user entitled to right now", and call it everywhere. Access rules scattered across components drift apart, and the drift is invisible until someone gets access they did not pay for.

**Handle every subscription state, not just active.** At minimum: active, trialing, past_due, cancelled-but-still-within-period, and none. Each has a different correct answer, and the ones that get forgotten are `trialing` and cancelled-within-period — both of which should still grant access.

## The customer portal

Add a way for users to manage their own subscription, or every cancellation becomes a support request:

> Add a Manage subscription button that opens the customer portal.

**The portal opens in a new tab and cannot be embedded in an iframe, so it does not work inside the Lovable preview panel.** Testing it requires opening the deployed site in a standalone browser tab. A report that "the manage button does nothing" is almost always this and not a bug.

## Checkout presentation

Overlay versus inline is a request away where the provider supports both:

> Show the checkout inline on my pricing page instead of as a modal.

Fonts, colours, logo, and available payment methods are configured in the provider's dashboard, not through Lovable.

## Before you consider setup done

Payments in the preview work immediately, which makes it easy to believe you are finished. You are not until the lifecycle has been tested — [testing.md](testing.md) — and the go-live steps completed, without which live checkout will not process anything.
