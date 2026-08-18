# After publishing

## "My changes aren't showing on the live site"

The most frequent live-site report, and almost never a bug.

Publishing deploys a snapshot. Later edits change the project, not the live site. If the changes were never published, the live site is correctly serving the older version.

Check in this order, and do not skip to the third:

1. **Were the changes published?** A dot on the Publish button means the project is ahead of the live version. Republish and re-check. This resolves the large majority of cases.
2. **Is it a cache?** Hard refresh, and try a private window. A stale browser or CDN cache looks identical to a failed deploy.
3. **Only then treat it as a bug.** And when you do, remember the live site runs the *published* build — debugging current source against a stale deployment is a guaranteed waste of a session.

**Never fix a publishing gap by editing code.** Changing the app to explain why the live site looks old adds real bugs on top of a non-problem.

## Verify on the live site, not the preview

They are different builds in different environments. A preview that works proves the code is right; it does not prove the deployment is.

After publishing, on the live URL:

- **The site loads** — from a private window, signed out, as a stranger would arrive.
- **Every route resolves**, including deep links typed directly rather than navigated to.
- **Sign-up and sign-in work** against the live environment, with a fresh account.
- **Data reads and writes work** — the live app may point at different configuration than the preview.
- **No console errors** on the main routes.
- **Assets load**: images, fonts, icons. Broken paths often survive preview and fail in a production build.
- **The social preview** renders, by pasting the link somewhere that unfurls it.

If the app has roles, check at least two. If it takes payments, run one real transaction end to end before telling anyone it is live.

## Updating

Every change after publishing needs an explicit republish. Two habits prevent most incidents:

**Verify in the preview before publishing, not after.** The live site is not a staging environment, and on a public plan a broken deploy is broken in front of whoever arrives during it.

**Publish deliberately, not continuously.** Batch verified changes and publish once. Publishing after every edit means shipping unreviewed states, and it makes "when did this break" unanswerable.

After any republish, re-verify the part you changed on the live site. The most common regression is a change verified in preview and never checked in production.

## Unpublishing

Taking the app down makes the live URL inaccessible. The project itself is untouched — code, history, and settings all remain, and you can publish again later.

Two things unpublishing does not do:

- **It does not undo exposure.** Anything that was public was public. Data that leaked, keys that were readable, and content that was indexed are not recalled by taking the site down. If a secret was exposed, rotate it — see the `secure` skill.
- **It does not affect project access.** Whoever could open the project still can.

## After a plan change

A published app stays live through a downgrade or cancellation, and connected domains keep serving. Restrictive website access settings continue to be enforced as stored, but re-applying them later may require the higher plan.

The practical consequence: **do not assume a downgrade quietly took anything offline.** If the intent was to stop serving an app, unpublish it explicitly and confirm the URL is dead.

Apps using platform backend or AI features still need available credits to serve requests, so an app can be published, reachable, and non-functional at the same time. If a live app started failing with no code change, check that before debugging anything.
