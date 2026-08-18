# Who can see what

Two independent settings, and conflating them is the most consequential mistake in this area.

| Setting | Controls | What it covers |
|---|---|---|
| **Project access** | Opening the project in the editor | Source code, chat history, work in progress, unpublished changes |
| **Website access** | Visiting the published app at its URL | The live site only |

Neither implies the other. Publishing does not change who can open the project. Restricting the project does not restrict who can visit the site.

## The combinations

| Project access | Website access | This gives you |
|---|---|---|
| Workspace | Anyone | **Public app, private code.** The normal shape for a public product |
| Workspace | Workspace | **Internal tool.** Team can build it and use it, nobody outside sees either |
| Restricted | Anyone | **Public app, code visible only to a few.** Client work, or a solo launch |
| Restricted | Workspace | **Private experiment.** Most closed configuration |

The row that surprises people is the third: a locked-down project whose website is public is a **fully public app**. Restricting the project protects the source, not the service.

## Choosing website access

Available options depend on the plan, and this matters *before* you publish rather than after.

- On lower-tier plans, a published app is reachable by anyone with the link, and this cannot be restricted. There is no "publish privately" — publishing is publishing.
- On higher-tier plans you can restrict the published site to authenticated workspace members, which is what makes internal tools possible.

**Confirm which situation applies before publishing anything sensitive.** If the app must not be public and the plan cannot restrict it, do not publish — say so, and suggest keeping it in preview and sharing a preview link instead.

Workspace defaults exist for both settings and are applied to new projects. A default is not a decision: check what it actually is for this project rather than assuming.

## An unrestricted site still needs its own auth

Website access controls who reaches the URL. It does not control what they can do once there.

An app published to "anyone" that contains user data must authenticate and authorise users itself — that is the app's job, covered by the `secure` skill, not the publish setting's. Publishing to workspace-only is a perimeter, not a substitute for access control inside the app. Perimeters get changed, and an app that never enforced anything is defenceless the moment it does.

## Sharing before launch

For showing work to someone who should not have editing rights, a preview share link is usually right. **These expire after seven days** — unlike published sites, which do not expire.

If someone reports a dead link, establish which kind they were given before investigating anything: an expired preview link is not a broken site.

## Public remixing

Enabling public remixing lets anyone with the link copy the project.

**This exposes your source code.** Everyone who remixes sees the code as it stands — including anything in it that should not be there. Before enabling it, confirm there are no keys, credentials, tokens, personal data, real customer records, or internal notes anywhere in the repository.

Remixing copies; it does not grant editing rights on your project, and the original is unaffected. Only the reading of your code is the exposure — but a secret read once is a secret gone, and it must be rotated rather than removed. See the `secure` skill.

## When access is the actual problem

If the complaint is "someone can see something they shouldn't", work out which layer failed before changing settings:

1. **Can they open the project?** → project access.
2. **Can they reach the site at all?** → website access.
3. **Can they reach the site legitimately but see the wrong data?** → not a publishing problem at all. That is RLS or authorisation, and belongs to the `secure` skill.

The third is the dangerous one, because tightening a publish setting appears to fix it while the underlying data exposure remains for every user who is still allowed in.
