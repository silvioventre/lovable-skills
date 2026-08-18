# mcp

Publishing an app as an MCP server so AI assistants can call it. Organised around the fact that governs the whole feature: a tool call does not go through your app's screens.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/mcp
```

## Use

```
/mcp publish my app as an MCP server so people can use it from ChatGPT
/mcp review the tools before I share the link
/mcp should these tools require sign-in?
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The three unrelated things called MCP, the three access layers, and the rules |
| `reference/fit.md` | Whether an integration is worth adding at all, and the prerequisites that catch people mid-build |
| `reference/tools.md` | Designing and reviewing the tool surface, including retry safety |
| `reference/access.md` | Sign-in, permissions, why access is all-or-nothing, and the absence of rate limits |
| `reference/launch.md` | Testing before sharing, publishing, maintenance, and what it cannot do |

## Scope

Backend-enforced access control is a prerequisite, not a follow-up — see [secure](../../security/secure/). Not for connecting external services into the editor while you build, and not for letting AI tools edit the Lovable project itself.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
