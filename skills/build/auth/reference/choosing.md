# Choosing the method

Start from who will use the app. Every other consideration is downstream of that.

| Who uses it | Method | Why |
|---|---|---|
| Only your workspace members | **Workspace identity reuse** | They are already signed in. No login page, no second account, nothing to maintain |
| Consumers, general public | **Google sign-in**, optionally with email | Expected, removes password friction, arrives with a verified email address |
| Professional or SaaS users | **Google plus email and password** | Google covers most; email covers everyone else |
| Business customers with their own IdP | **SAML SSO for Cloud apps** | Their security team will require it. Not optional for enterprise sales |
| Mixed audience | **Google plus email**, SSO added later when a customer asks | Do not build enterprise SSO before a customer needs it |

## Internal tools: check before building

The most common wasted work in this area is a login system for an app only the team will use.

Ask directly: *who will actually open this?* If the answer is "us", identity reuse gives the app the user's name, email, and id with no login flow, and it works whether the team signs in to Lovable with SSO, Google, or email.

Two things to confirm before relying on it: it is a Business and Enterprise capability, and it has been rolling out gradually so it may not be available in every workspace yet. Check before designing around it.

If the tool might later be used by people outside the workspace — contractors, clients, a customer pilot — that is real auth, and retrofitting it onto an app built around identity reuse means reworking every place that assumed a workspace member. Ask about that future before choosing.

## Google sign-in

The default for consumer and professional apps. Faster onboarding, no password to reset, and the email address arrives pre-verified — which removes an entire verification flow you would otherwise build.

Two setup options with an identical user experience; the difference is who manages the OAuth credentials. Managed is the default and right for nearly everyone — see [google.md](google.md).

## Email and password

Still worth including alongside Google in most public apps. Some people will not use a Google account, and some organisations block social login.

It brings obligations Google does not: password reset, email verification, session length decisions, and the security of credential handling. Do not build it because it seems like the basic option — it is the one with the most surface area. See [email.md](email.md).

## Enterprise SSO

For apps whose users belong to a company that runs its own identity provider. Their security review will require it, and it is frequently the thing that blocks a deal.

**Do not build it speculatively.** It is per-project configuration work with a real cost, and it is the wrong thing to have built if the first enterprise customer never arrives. Add it when one asks.

Note it is distinct from the workspace SSO your own team might use to sign in to Lovable — see the table in the main skill. Setup and the checks that matter are in [saml.md](saml.md).

## Decide these at the same time

Choosing the method is half of it. The other half shapes the data model, and changing it later is disruptive:

- **What identifies a user across methods?** If someone signs up with email and later uses Google with the same address, is that one account or two? Deciding after launch means merging accounts.
- **What does a new account start with?** Empty state, a default workspace, a trial. This is the onboarding flow and it is easier designed now than bolted on.
- **Are there roles?** If yes, where do they come from and who can change them. Roles resolved on the client are a vulnerability — see the `secure` skill.
- **What happens on sign-out?** Cached data from the previous user must be cleared, or the next person to sign in on that browser sees data that is not theirs.

That last one is a real leak with no vulnerability in the access rules at all, and it is only ever found by signing out and in as someone else.

## Then

Set up the chosen method, then run the `secure` skill's auth checks. Establishing identity is this skill; enforcing what that identity may do is that one, and an app that has only done the first half is not protected.
