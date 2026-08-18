# Google sign-in

Standard OAuth 2.0. The user clicks sign in, Google shows a consent screen, they approve, and Google redirects them back to the app signed in.

Under it: a client id identifying the application, a client secret authorising it, and redirect URLs telling Google where to send people afterwards. Those three are the whole configuration, and the redirect URLs are what breaks.

## Managed credentials, or your own

The user-facing experience is identical. The only difference is who holds and rotates the OAuth credentials.

| | Managed | Your own credentials |
|---|---|---|
| OAuth client | Managed for you | You create it in Google Cloud Console |
| Redirect handling | Handled | Yours to configure |
| Credential rotation and security updates | Handled | Yours |
| Google Cloud Console setup | None | Required |

**Managed is the default and the right answer for nearly everyone.** Choose your own credentials only for a concrete reason — a policy requiring OAuth clients to live in your organisation's Google Cloud project, a branded consent screen you control, or scopes beyond sign-in.

If the user asks for their own credentials without naming such a reason, ask why. It is ongoing maintenance — rotation, redirect URLs, verification if scopes expand — accepted permanently in exchange for something they may not need.

## Redirect URLs, which is where it fails

The single most common Google auth failure: sign-in appears to work, Google shows the consent screen, and the user lands somewhere broken or back at the login page.

That is nearly always a redirect URL mismatch. Google will only send users to URLs registered for the client, and the registered set has to include every origin the app is actually reachable at:

- The preview URL, for development.
- The published URL.
- **Any custom domain**, added when the domain is connected, not before.

The failure mode after connecting a custom domain is exactly this: everything worked yesterday, the domain changed, and sign-in now dead-ends because the new origin was never registered. With managed credentials this is handled; with your own it is a step you must remember when the `ship` skill's domain work happens.

## What arrives with the user

Google returns a verified email address and basic profile information. Two consequences worth designing around:

- **The email is already verified**, so no verification flow is needed for these users. Do not build one.
- **You get a name and usually a picture**, which is enough to skip a profile-setup step at onboarding. Use it.

## The account-identity question

Decide before launch: if someone signs up with email and password, then later signs in with Google using the same address, is that one account or two?

Two separate accounts is a support problem — the user is certain they have data that is "gone", and it is in the other account. Merging afterwards is genuinely unpleasant work. Decide now, and if the answer is "one account", test it explicitly with a real second sign-in.

## Verify

- Sign-in completes and lands the user somewhere sensible, from a fresh browser with no session.
- **Sign-in works from every origin the app is reachable at** — preview, published URL, custom domain. This is the check that catches the redirect problem before users do.
- A returning user is recognised as the same account, not a new one.
- Sign-out clears the session, and signing in as a different account shows no trace of the previous one.
- The app still behaves for a user who cancels at the Google consent screen — a path that usually returns them with no session and frequently crashes.

Then move to the `secure` skill: sign-in establishes identity, and nothing about it constrains what that identity can reach.
