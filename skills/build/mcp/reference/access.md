# Access and permissions

## The three layers

Keeping these apart is what makes an integration safe. Collapsing them is how private data ends up in an assistant.

**Sign-in identifies the caller.** Users authenticate through your app's own sign-in screen, then approve the assistant on a consent screen. Both are expected parts of connecting, not friction to remove.

**Your app's rules decide what that caller can do.** Backend rules keyed on the signed-in user apply to tool calls, and generated tools are not permitted to work around them. Anything beyond that — owning the record, holding a role, being on a paid plan — applies only where the action itself checks it.

**The tool definition decides what is exposed.** Its inputs, its action, its returned fields. See [tools.md](tools.md).

The failure mode is assuming layer two covers everything. Row-level rules stop a user reading someone else's records; they do not stop a signed-in free user calling an action meant for paying customers, unless that action checks the plan.

## The two configurations

**Sign-in required** — the default, and the right answer almost always. Every tool requires authentication, and individual actions can then enforce role, ownership, and plan requirements in the backend. An app that limits a feature to paying users keeps that limit for assistant calls, provided the action checks it.

Enabling this activates the OAuth capability on your backend at publish, without changing how users sign in to the app normally.

**No sign-in** — every tool is callable without authenticating anyone. This is a deliberate choice you must confirm, and it is warned about at publish. On workspaces with strict security policies it may be blocked outright.

Treat a public integration as fully public: **assume the link is copied and shared.** Only allow it when every active tool and every returned field is safe for anyone at all — a public knowledge base, a public price lookup.

## It is all or nothing

**You cannot make some tools public and others protected within one integration.** Sign-in applies to the whole thing.

So a single tool that needs anonymous access forces the entire integration public. When that comes up, the answer is nearly always to keep sign-in on and reconsider whether that one tool needs to be exposed at all.

## Switching later is a build, not a toggle

Moving between public and protected changes your app's authentication setup, so it is a build rather than a settings change. There is a shortcut on the status card, or ask directly:

> Require users to sign in before they can use this agent integration, and make sure the export report action checks whether the user is on a paid plan.

Note that request does both layers at once, which is the right shape — sign-in alone does not enforce the plan.

## Check what you actually have

The panel shows the current state as a status card: protected with a sign-in badge, or public access with an add-sign-in button.

**If the integration was set up a while ago, open the panel and confirm it says what you expect.** Access is the setting most likely to have been chosen quickly during setup and never revisited.

## The automated checks

**A basic check at every publish** flags whether the integration allows access without sign-in. On strict workspaces, publishing is blocked when a non-public app exposes unauthenticated tools.

**A deep scan when publishing a public integration** examines what the tools actually expose, flagging private-data exposure, unintended record changes, bulk data access, and paywall bypass. Findings appear under the project's security view; serious ones are marked critical, and on some workspaces block further publishing until resolved.

Both are useful and neither is sufficient. **They cannot evaluate risks that depend on your business logic** — a tool that correctly returns records the caller owns, where owning that record was never supposed to imply seeing every field of it, passes every automated check.

## Rate limits

There are none, and no spending cap.

Requiring sign-in stops anonymous calls and ties every call to a user. It does not limit how often that user calls a tool.

The practical rule: **do not expose an action that costs money or consumes resources unless your app already enforces usage and plan limits on it.** If the limit lives only in the interface, it does not exist for tool calls.

## Traceability

Tool errors surface in your app's logs like any other backend error. If you need calls attributable to people, keep sign-in on — it is what makes every call belong to an identified user of your app.
