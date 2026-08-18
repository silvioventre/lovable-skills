# deployment

Going live and hosting: publishing, controlling access to the published site, and running outside Lovable Cloud.

| Skill | What it does |
|---|---|
| [ship](ship/) | Pre-flight before publishing, the difference between project access and website access, verification on the live site, republishing. |
| [deploy-external](deploy-external/) | Whether and what to move outside Lovable Cloud, what becomes your responsibility, what migrates by hand, build requirements and Docker. |

## How they divide the work

- **`ship`** is publishing *on* Lovable Cloud and controlling who can reach it.
- **`deploy-external`** is running the frontend or backend *somewhere else*.

Both defer to `secure` for the security gate rather than duplicating it.

Add skills here as `skills/deployment/<skill-name>/SKILL.md` — see [`skills/_template/`](../_template/).
