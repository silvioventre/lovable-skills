---
name: auth
description: Use when the user is adding, choosing, or reworking how people sign in to their app — "add authentication", "add login", "add sign in with Google", "let users create accounts", "add SSO", "my team shouldn't need a separate login", "should I use email or Google", "use my own Google credentials", "add password reset", "which auth should I pick". Covers deciding whether the app needs its own login at all, choosing between email, Google, enterprise SSO and reusing the workspace identity, and setting up the chosen method. Not for enforcing access once someone is signed in — roles, permissions and server-side checks belong to the secure skill.
---

# Auth

Two questions, in this order, and getting the first one wrong is the expensive mistake.

1. **Does this app need its own login at all?**
2. If so, **which method fits the people who will use it?**

Most auth work that gets built and thrown away is a login system for an audience that was already signed in somewhere.

## First: does it need one?

**If everyone who uses this app is already in your Lovable workspace, it may not need a login.** Workspace identity reuse lets the app recognise the signed-in workspace member — name, email, and user id — with no login page and no second account. It works regardless of how they sign in to Lovable, and does not require workspace SSO.

Building a login for an internal tool means your teammates sign in twice and you maintain an account system for people you already have accounts for. Ask who will actually use this before designing anything.

If the audience is anyone outside the workspace, the app needs its own auth. Continue below.

## Three features that sound the same

These get confused constantly, and picking the wrong one produces weeks of work solving the wrong problem.

| Feature | Controls | Affects |
|---|---|---|
| **Workspace identity reuse** | Whether the apps you build can recognise a workspace member who is already signed in to Lovable | Your team, using apps your team builds |
| **Workspace SSO** | How your team signs in to Lovable itself | Your team, signing in to Lovable |
| **SAML SSO for Cloud apps** | How outside end users of a published app sign in with their own company credentials | Your app's external users |

The distinction that keeps them apart: **identity settings decide how people get into Lovable; identity reuse decides what your apps can know about people who are already in; SAML SSO for Cloud apps is about your app's own users, not yours.**

None requires another. Identity reuse works whether the team signs in to Lovable with SSO, Google, or email.

## Route the choice

| The situation | Playbook |
|---|---|
| Internal tool for workspace members only | [reference/choosing.md](reference/choosing.md) |
| Public app, consumer users | [reference/choosing.md](reference/choosing.md) |
| Business customers with their own identity provider | [reference/choosing.md](reference/choosing.md) |
| Setting up Google sign-in | [reference/google.md](reference/google.md) |
| Managed credentials versus your own | [reference/google.md](reference/google.md) |
| Email and password, sessions, password reset | [reference/email.md](reference/email.md) |

## The rules

**Choose the method from the audience, not from the tech.** Consumers expect social login. Business buyers ask for SSO. Your own team already has an identity. Building the wrong one is not a small correction — it changes the data model, the session handling, and the onboarding flow.

**Signing in is not permission.** Everything in this skill establishes *who someone is*. What they are then allowed to do is a separate question, enforced server-side on every request, and it belongs to the `secure` skill. An app with perfect Google sign-in and client-side role checks is wide open.

**Add auth before payments.** A purchase that cannot be attached to an account is a purchase you cannot honour. If both are planned, this one comes first.

**Do not build a second identity system alongside an existing one.** Two sources of truth about who a user is produces bugs that look like data problems and are actually identity problems. If the app already has auth, extend it rather than adding a parallel path.

## Verify

Auth is verified by trying to get in wrongly, not by signing in successfully. At minimum: sign-up, sign-in, sign-out, password reset with a fresh account, session persistence across a reload, and expiry behaviour. Then the `secure` skill's checks, which cover what a signed-in user can reach.
