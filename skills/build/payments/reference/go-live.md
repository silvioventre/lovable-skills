# Going live

Until every go-live step is complete, **live checkout does not work** — the published site will have a checkout that fails. Plan the launch around that rather than discovering it.

## The sequence

1. **Readiness check.** An automated review of the live site confirming the pages and content a payment provider requires.
2. **Project setup.** At least one product with a price exists, and the latest changes are published.
3. **Verification (KYC/KYB).** The provider's seller verification: product information, compliance screening, and personal or business details. Business types range from sole trader to registered company.
4. **Publish**, which also syncs the catalogue from test to live.

Run the readiness check *before* submitting verification. Fixing what it finds first avoids a rejected submission and a second review cycle.

## What the readiness check wants

The failures are almost always content rather than code:

- **A privacy policy** that exists and is reachable.
- **Terms of service.**
- **A refund policy.** The one most often missing entirely.
- **Genuine site content.** Placeholder copy, lorem ipsum, sample products, and empty sections read as an incomplete or fraudulent business and get flagged.

If a check fails, the dashboard explains what to fix. Fix it, then run the check again rather than submitting anyway.

## Use a custom domain first

Providers review the live domain during verification. A custom domain reads as a real business; a default platform subdomain reads as a test project, and slows or fails review.

Connect the domain before starting verification, not after. See the `ship` skill.

## The catalogue sync

Publishing syncs products and prices from test to live automatically. There is nothing to copy by hand, and every subsequent publish re-syncs catalogue changes — which is why test stays the source of truth.

**Discounts are not synced.** They are created directly against the live environment, and they are the one thing you will look for in live and not find. Be explicit about the environment when creating one:

> In live, create a 20% discount code LAUNCH valid for the first 3 months.

## Before announcing anything

Run one **real transaction end to end** with a real card, on the live site, and then refund it. This is the only way to know that live actually works, and it costs the price of one transaction fee.

Confirm on that real purchase:

- The charge appears in the Payments tab in the live environment.
- Entitlement unlocked for that account.
- The receipt or confirmation the customer receives is correct and looks like it comes from you.
- **The statement descriptor** — what appears on the customer's bank statement — is recognisable. An unrecognised descriptor generates chargebacks from people who genuinely bought something and did not recognise the name.
- The customer portal opens and works, in a standalone tab.

Then refund it and confirm the refund appears as an adjustment.

## After going live

Both environments stay active. New products, price changes, and new flows get built and tested in the preview first, then reach live at the next publish.

That discipline is the point of the two-environment model: **never test a payment change against real customers.** The test environment exists precisely so that the code path handling money is exercised before it handles anyone's money.
