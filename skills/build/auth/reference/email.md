# Email and password

The method with the most surface area. It looks like the simple default and brings the most obligations — password reset, verification, session policy, and the handling of credentials themselves.

Include it when part of the audience will not use social login, or when an organisation blocks it. Do not build it *only* because it seems basic.

## What it commits you to

Each of these is a flow that must work, and each is a place users get stuck:

- **Sign-up**, including what happens when the address is already registered.
- **Sign-in**, including a wrong password and a non-existent account.
- **Password reset**, end to end: request, email delivery, the link, setting a new password, and signing in with it. The most commonly broken flow in any app, because it is the least tested.
- **Email verification**, if addresses need to be trusted. Decide whether an unverified user can use the app at all, or only some of it.
- **Session length**, and what happens at expiry.

Use the platform's built-in session and credential handling. Hand-rolled token storage is where the subtle, serious bugs live, and there is nothing to gain by writing it.

## Password reset: test it properly

Testing this means completing the whole loop with a real address you can open, not clicking "send" and seeing a confirmation.

Check specifically:

- **The email arrives**, and not in spam. Deliverability from a default sending domain is frequently poor — if resets matter, custom email sending is worth configuring.
- **The link works**, and still works a few minutes later.
- **The link expires**, and expiry is handled with a message rather than an error.
- **A used link cannot be reused.**
- **The new password works**, and the old one does not.
- **Any existing sessions behave as intended** after a reset. If the reset was because of a compromise, leaving other sessions signed in defeats it.

## Error messages: two competing goals

Sign-in failures sit between usability and account enumeration.

Telling a visitor "no account with that email" confirms which addresses are registered, to anyone who asks. Telling them nothing useful means real users cannot tell a typo in the address from a wrong password.

The usual resolution: **a single generic message on the sign-in form** — the credentials do not match — and a **password reset flow that behaves identically whether or not the account exists**, so requesting a reset for an unregistered address reports the same "check your email" as for a registered one.

If the app is internal or the audience is not sensitive, a clearer message is a reasonable trade. Make it a decision rather than an accident.

## Rate limiting

Sign-in and password reset endpoints are the ones that get hammered — credential stuffing on one, mail-flooding on the other. Both need a ceiling.

An unlimited password reset endpoint lets anyone send unlimited email to any address in your user base, which is an abuse problem and a deliverability problem at the same time.

## Alongside other methods

If Google sign-in also exists, settle the identity question: same email through two methods is one account or two. See [google.md](google.md) — the answer must be decided once and implemented consistently, not per flow.

## Verify

With a fresh account, not the one already signed in:

- Sign-up, sign-in, sign-out.
- **Password reset, all the way through**, including actually signing in with the new password.
- Session survives a reload; expiry redirects to sign-in rather than showing a broken page.
- Sign-out clears cached data — sign in as a different user afterwards and confirm nothing from the previous one is visible.
- Wrong password, unknown address, and already-registered address all produce sensible messages.

Then the `secure` skill for what a signed-in user is permitted to do, which none of the above establishes.
