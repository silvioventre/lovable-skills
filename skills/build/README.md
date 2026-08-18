# build

Building work: understanding before writing, verifying after, and the capabilities you wire into an app.

| Skill | What it does |
|---|---|
| [plan](plan/) | Explores the project, compares approaches, breaks a vague request into verifiable increments. Writes no code. |
| [test](test/) | Routes verification to the right tool — browser testing, frontend tests, direct calls and edge tests. |
| [auth](auth/) | Decides whether the app needs its own login at all, which method fits the audience, and sets it up. |
| [payments](payments/) | Test and live environments, the subscription lifecycle, go-live, and the irreversible operations. |
| [emails](emails/) | Sending domain, auth and app templates, and the deliverability practices that decide whether mail arrives. |
| [analyze](analyze/) | Analyses data and generates files without touching project code, then builds from what it found. |
| [knowledge](knowledge/) | Writing and maintaining the persistent instructions: workspace versus project, and when a rule should be a skill instead. |
| [mcp](mcp/) | Publishing the app as an MCP server for ChatGPT and Claude — which tools to expose, the access model, and testing before sharing the link. |

## The natural order

`plan` → `auth` → build → `test` → `payments` → `secure` → `ship`.

`auth` comes before `payments`: a purchase that cannot be attached to an account is a purchase you cannot honour. And `secure` before publishing, always — `auth` and `payments` establish *who* a user is and *what they paid for*, not what they are allowed to do.

Add skills here as `skills/build/<skill-name>/SKILL.md` — see [`skills/_template/`](../_template/).
