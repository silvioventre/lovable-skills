---
name: ship
description: Use when the user is about to publish, deploy, ship, launch, or go live with a project, or has already published and something about the live site is wrong — "publish this", "make it live", "deploy it", "am I ready to launch", "my changes aren't showing on the live site", "who can see this", "make it private", "share it with my team", "unpublish it". Covers the pre-flight checks before going live, the difference between project access and website access, choosing who can reach the published app, verifying the live site afterwards, and republishing after changes. Not for custom domain DNS setup or workspace role administration, which are configuration the user does in the Lovable interface.
---

# Ship

Getting live is three things: knowing what publishing actually does, checking the right things before it, and verifying the right things after it. Each has a failure mode that is invisible until someone else finds it.

## What publishing actually does

**Publishing deploys a snapshot of the current version.** It is not a live link to your project. Once published, further edits keep changing the project and do not change the live site until you publish again.

This produces the single most common confusion: *"my changes aren't showing on the live site."* Almost always the answer is that the changes were never published. A dot appears on the Publish button when the project is ahead of the live version. Republishing is the fix, not debugging.

Two consequences worth stating explicitly:

- **The live site is always behind or equal to the project, never ahead.** When diagnosing a live-site problem, first establish whether the live version even contains the code you are reading. Debugging current source against a stale deployment wastes entire sessions.
- **A published site does not expire.** Preview share links do, after seven days. If someone reports a dead link, work out which of the two they were given.

## Route the task

| The task | Playbook |
|---|---|
| About to publish for the first time | [reference/preflight.md](reference/preflight.md) |
| "Am I ready to launch?" | [reference/preflight.md](reference/preflight.md) |
| Who can see this, or how to make it private | [reference/access.md](reference/access.md) |
| Sharing with a team, client, or reviewer | [reference/access.md](reference/access.md) |
| Enabling or questioning public remixing | [reference/access.md](reference/access.md) |
| Changes not showing on the live site | [reference/after-publish.md](reference/after-publish.md) |
| Verifying or updating a published app | [reference/after-publish.md](reference/after-publish.md) |
| Taking a published app down | [reference/after-publish.md](reference/after-publish.md) |

## The two access settings

Nearly every access mistake here comes from thinking there is one setting. There are two, they are independent, and neither implies the other.

| Setting | Controls | Covers |
|---|---|---|
| **Project access** | Who can open the project in the editor | Source code, chat history, work in progress, unpublished changes |
| **Website access** | Who can visit the published app at its URL | The live site only |

Publishing does not change who can open your project. Restricting your project does **not** restrict who can visit the published site. An app whose project is locked down and whose website is public is fully public — the restriction protects the code, not the app.

Full combinations and how to choose in [reference/access.md](reference/access.md).

## Before you publish, non-negotiable

**Run the security gate.** Publishing exposes the app to whoever can reach it. The `secure` skill's pre-publish gate covers secrets, server-side validation, RLS, and privileged endpoints — run it and report the result. A basic scan runs automatically when the publish dialog opens, but it checks configuration and known patterns; it cannot tell whether your access rules express what you meant.

**Know who will be able to reach it.** On some plans the published site is reachable by anyone with the link and cannot be restricted afterwards. Establish this *before* publishing, not after — an app published publicly by accident has been public, and the fix is not retroactive.

**Never publish to test something.** The preview is for testing. Publishing to see whether something works puts an untested build in front of real users, and on a public plan there is no way to take back who saw it.

## Report

After publishing, state:

1. **The live URL**, and who can reach it.
2. **What was verified on the live site**, not the preview — they are different builds.
3. **Anything left unverified**, explicitly.
4. **What still needs republishing**, if changes were made after the deploy.
