---
name: mcp
description: Use when the user wants their published app usable from an AI assistant, or is working on one that already is — "publish my app as an MCP server", "make my app work with ChatGPT", "connect my app to Claude", "add an agent integration", "expose my app as tools", "let assistants call my app", "review my MCP tools", "should this tool require sign-in", "my users can't connect the integration". Covers whether an integration is worth adding, designing the tool surface, the access model, testing it before sharing, and keeping it current. Not for connecting external services into the Lovable editor while you build, and not for letting AI tools edit the Lovable project itself.
---

# MCP

Turning a published app into a set of tools an AI assistant can call. People use an app by clicking; an assistant cannot click, so it needs a list of actions instead. That list is the MCP server.

The integration runs against your **live published app**, not a copy. The assistant gets the tools you expose, and nothing else about your project.

## Three things called MCP, doing opposite jobs

Confusing these wastes real time, because they point in different directions.

| Feature | Direction | What it does |
|---|---|---|
| **Agent integrations** (this skill) | Assistants → your app | Your users' assistants call actions you expose in your published app |
| **Lovable MCP server** | AI tools → Lovable | External tools create and edit your Lovable projects |
| **Chat connectors** | Lovable → external tools | The agent pulls context from Notion, Linear and similar while you build |

This skill is only the first. It does not let an assistant edit your Lovable project.

## The security fact that governs everything

**A tool call does not go through your app's screens.**

Buttons you hid, pages you removed from the menu, fields you disabled, flows that are hard to reach — none of them protect the backend action underneath. An assistant calls the action directly.

So an app whose access control lives in its interface is fully exposed the moment tools go live. Everything real must be enforced in the backend, which is the `secure` skill's territory and is a prerequisite here, not a follow-up.

Three separate layers, and keeping them apart is what makes this safe:

1. **Sign-in identifies the caller.** Users authenticate through your app's own sign-in, then approve the assistant on a consent screen.
2. **Your app's rules decide what that caller can do.** Backend rules keyed on the signed-in user apply to tool calls. Anything extra — ownership, role, paid plan — applies only where the action itself checks it.
3. **The tool definition decides what is exposed.** Its inputs, its action, and the fields it returns.

## Route the task

| The task | Playbook |
|---|---|
| Deciding whether to add one at all | [reference/fit.md](reference/fit.md) |
| Designing, reviewing, or changing tools | [reference/tools.md](reference/tools.md) |
| Sign-in, permissions, public versus protected | [reference/access.md](reference/access.md) |
| Testing before sharing, publishing, maintaining | [reference/launch.md](reference/launch.md) |

## The rules

**Keep sign-in on.** It is the default, and making tools public is always an explicit choice. Allow anonymous access only when every exposed action and every returned field is safe for anyone at all.

**Access is all or nothing.** Sign-in applies to the whole integration — you cannot mix public and protected tools. Individual actions can still enforce their own role, ownership, and plan checks inside a protected integration.

**There is no rate limit and no spending cap.** A signed-in user can call a tool as often as they like. Do not expose an action that costs money or consumes resources unless your app already enforces its own usage and plan limits on it.

**Write actions must be safe to retry.** An assistant will retry after a timeout or a dropped connection. A tool that creates an order twice has created two orders. Design writes so a repeated call does not duplicate the effect.

**Start read-only and narrow.** A small set of focused read tools, live and working, is a better starting point than a broad surface you review once. Add write actions deliberately.

**Automated checks do not replace your review.** A basic check runs at every publish and a deep scan on public integrations, but neither understands your business logic. Work through [reference/tools.md](reference/tools.md) and test as a real user before sharing.

## Prerequisites

- **A publicly published app.** Workspace-only and internal apps are not supported.
- **A backend** — a front-end-only site cannot host an integration.
- **Backend-enforced access control.** Not formally required, and in practice the thing that decides whether this is safe.
