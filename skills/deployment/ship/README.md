# ship

Going live: the checks before publishing, who can reach what afterwards, and verification on the live site. Two facts do most of the work — publishing deploys a snapshot, and project access and website access are independent settings.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/deployment/ship
```

## Use

```
/ship publish this, it should be public
/ship am I ready to launch?
/ship my changes aren't showing on the live site
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | What publishing actually does, the two access settings, and the non-negotiables |
| `reference/preflight.md` | The ordered gate before a first publish, from security to placeholder copy |
| `reference/access.md` | The four access combinations, sharing before launch, and what public remixing exposes |
| `reference/after-publish.md` | Verifying on the live URL, republishing discipline, and what unpublishing does not undo |

## Scope

Defers the security gate to [secure](../../security/secure/) rather than restating it. For running the app outside Lovable Cloud, see [deploy-external](../deploy-external/). DNS and registrar setup is configuration you do in the Lovable interface, not covered here.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
