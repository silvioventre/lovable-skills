# SAML SSO for your app's end users

Lets users of your published app sign in with their company identity provider — Okta, Entra ID, Google Workspace, OneLogin, JumpCloud, or any SAML 2.0 provider that publishes a metadata URL.

**This is about your app's users, not your team.** For your team's access to Lovable itself, that is workspace SSO; for an internal tool whose users are workspace members, identity reuse is usually the better answer. See the disambiguation table in the main skill.

## When it is warranted

- **B2B products selling to enterprises.** It comes up in security review, and it frequently blocks the deal.
- **Internal tools** where employees should sign in with their corporate account.
- **An app shipped to one customer** who requires their identity provider.

If the app needs only consumer logins, it does not need this. **Do not build it speculatively** — it is per-project configuration with a real cost, and the wrong thing to have built if the enterprise customer never arrives.

## What it buys the customer

Worth understanding, because it explains why they insist:

- Access is provisioned and de-provisioned in their identity provider, and your app inherits those decisions — including the removal when someone leaves.
- Their MFA, conditional access, and device policies apply to your app without you implementing any of it.
- Their employees use an account they already have.

That first point is usually the real requirement. An enterprise cannot accept an app where a departed employee retains access because nobody remembered to remove them from a separate user list.

## The setup is a two-way exchange

Both directions are required, and each half is done in a different place:

1. **Lovable → identity provider.** Copy two service-provider values — the ACS URL and the Audience URI — into the SAML application on their side.
2. **Identity provider → Lovable.** Copy their metadata URL back, together with the email domains that should route to this provider.

The email domain list is what makes routing work: a user entering an address at one of those domains is sent to that provider rather than shown a password field.

**Confirm the domain list is complete.** A company with several domains — a country domain, an acquired brand, a legacy address — will have users on each, and the ones missing from the list silently fall back to whatever other sign-in method exists. That looks like a broken login to the user and like nothing at all to you.

## Sign-in starts in your app

**Service-provider-initiated only.** Users must begin at your app; starting from a tile in the identity provider's dashboard is not supported here.

Say this to the customer during setup, because their IT team will otherwise add the tile, users will click it, and the resulting failure will be reported as your bug. It is worth stating in whatever onboarding note goes to them.

## Prerequisites

- A Cloud project with Lovable-managed auth.
- SSO permitted by the workspace auth policy.
- Admin access to the identity provider on the customer's side — which means their timeline, not yours. Plan the launch accordingly.
- The list of email domains to route.

## Verify

The parts that fail are the ones only testable with a real account at the customer:

- **Sign-in completes** from your app and lands the user signed in.
- **A user at each configured domain** is routed to the provider, not to a password form.
- **A user at an unconfigured domain** still gets the ordinary sign-in path, without an error.
- **A de-provisioned user loses access.** This is the requirement the customer cares about most and the one nobody tests. Ask them to disable a test account and confirm.
- **The account is the same one** on second sign-in, rather than a duplicate.

Then, as always, the `secure` skill: SSO establishes identity with high confidence and says nothing about what that identity may do inside your app.
