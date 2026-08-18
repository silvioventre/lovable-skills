# Is an integration worth adding?

Tools get proposed automatically from what the app does. Whether the integration is *valuable* — or appropriate — is a judgement nobody makes for you, so make it before building.

## It fits when the app holds something an assistant can use

Data, workflows, knowledge, or repeatable expertise. The test is whether a user would plausibly ask their assistant a question your app can answer, or a task it can perform.

| App | Tools that make sense | What a user asks |
|---|---|---|
| CRM | `find_customer`, `update_deal_stage`, `draft_follow_up` | "Cross-check my stalled deals against last week's notes" |
| Quoting tool | `generate_quote`, `compare_options` | "Generate a quote for this job from the specs" |
| Client portal | `create_request`, `get_request_status` | "Submit this and tell me what's waiting on me" |
| Operations console | `list_pending_approvals`, `approve_item` | "Show submissions needing review" |
| Dashboard | `query_metrics`, `summarize_trends` | "Summarise this week's signups and flag anything odd" |
| Knowledge base | `search_articles`, `get_policy` | "What is our refund policy, exactly?" |

One clear job that works well through an assistant is enough. It does not need to cover the whole app.

## It does not fit when

- **The value is visual or interactive.** A game or a portfolio. A game might still expose statistics or tournament management, but turn-by-turn play belongs in the app.
- **The app is static**, with no meaningful action or information behind it.
- **The only possible tools are slow, expensive, destructive, hard to reverse, or unsafe to run twice.** An assistant retries; a tool that must never run twice is a bad tool.
- **The tools would expose more than the use case needs.** If a useful integration requires handing over broad data access, the integration is not the right shape yet.

Saying "this app does not need one" is a legitimate and frequently correct outcome. An integration is a permanent new entry point into your backend, and it earns its place or it does not.

## Check the prerequisites early

Two of these have caught people mid-build:

- **The app must be publicly published.** Workspace-only and internal apps are not supported. If the app is deliberately internal, this is the end of the conversation — decide that before designing tools.
- **A backend is required**, either the platform's own or a connected one. A front-end-only site cannot host an integration.
- **A connected external backend needs its OAuth authorization server enabled** and then reconnected, or the integration cannot require sign-in and will not be built at all.

## What it costs

There is no separate fee for hosting the integration or for tool calls. But **a tool call runs your app's normal backend logic**, so database work, platform usage, AI features, and third-party services are consumed exactly as they are through the app.

Combined with the absence of any rate limit, that is the real cost consideration: an exposed action that calls a paid API is an open tab, and the only thing limiting it is whatever your app already enforces.

Enabling or changing the integration uses ordinary build credits.

## Before designing tools

Confirm the app's access control lives in the backend, not the interface. Tools bypass every screen, so an app relying on hidden buttons and unlinked pages becomes fully exposed the moment the integration goes live.

If that work has not been done, do it first — the `secure` skill — and treat this integration as blocked until it has. It is much cheaper than discovering it through a deep-scan finding after publishing.
