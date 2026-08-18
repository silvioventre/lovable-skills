# emails

Sending transactional email from your own domain, and the deliverability practices that decide whether any of it reaches an inbox. The second part is what people discover late.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/emails
```

## Use

```
/emails set up sending from my own domain
/emails add order confirmation emails when someone checks out
/emails my emails are going to spam
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The two kinds of transactional email, the constraints, and the rules that protect deliverability |
| `reference/setup.md` | Sending domain, subdomain isolation, workspace scope, and what each status means |
| `reference/templates.md` | Generating and customizing templates, editing the files, and why a redeploy is required |
| `reference/deliverability.md` | Why a new domain starts in spam, and why the instinctive reaction makes it worse |
| `reference/troubleshooting.md` | Not sending, stuck verifying, offline, changes not showing, rising bounces |

## Scope

Not for marketing campaigns or newsletters — a different kind of sending with different rules.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
