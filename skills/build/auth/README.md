# auth

Decides whether the app needs its own login at all, then which method fits the people who will use it, then sets it up. Most auth work that gets built and thrown away is a login system for an audience that was already signed in somewhere.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/auth
```

## Use

```
/auth add login — it's a consumer app, people signing up themselves
/auth my team shouldn't need a separate account for this internal tool
/auth a customer is asking for SSO, what does that involve?
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The two questions in order, and the disambiguation of three similarly named identity features |
| `reference/choosing.md` | Picking the method from the audience, and the decisions that shape the data model |
| `reference/google.md` | Google sign-in, managed versus your own credentials, and the redirect URLs that break it |
| `reference/email.md` | Email and password: what it commits you to, and testing password reset properly |
| `reference/saml.md` | Enterprise SSO for your app's customers, and the de-provisioning check nobody runs |

## Scope

Establishes *who* someone is. What they are then allowed to do is enforced server-side on every request — that is [secure](../../security/secure/), and an app that has only done this half is not protected.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
