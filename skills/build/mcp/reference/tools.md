# Designing and reviewing tools

Each tool is one action from your app. The proposed set is a starting point — add, remove, rename, and reshape it in plain language:

> Remove any tool that can delete records.
> Rename the customer lookup tool so it is clear it searches by email address.

**Tools go live when you publish. There is no separate approval step**, so every active tool must be reviewed before the link is shared.

## Names and descriptions are functional

The assistant chooses which tool to call from the name and description. A vague one is not a cosmetic problem — it causes the wrong tool to be called, or the right one to be missed.

| | |
|---|---|
| **Vague** | `get_data` — "Gets data." |
| **Clear** | `list_open_orders` — "Returns the signed-in customer's open orders with order number, status, and total." |

The clear version states whose data, which subset, and what fields come back. Write every description that way: what it does, what it needs, what it returns.

## Review every tool against five questions

**What action does it perform?** Confirm it does only what its name and description claim. A tool that quietly does more than it says is the hardest kind of problem to notice later.

**What inputs does it accept?** Prefer narrow, specific inputs — a particular record identifier — over broad queries or arbitrary field values. A tool accepting a free-form filter is a tool whose behaviour you cannot fully predict.

**What data does it return?** Return only the fields the task needs. **A read-only tool still exposes everything it returns**, and returning a whole record because it was convenient is the most common over-exposure here.

**What access does it check?** Confirm the action enforces the ownership, role, permission, and paid-plan requirements your app expects. Remember that the interface enforces nothing — see the main skill.

**Is it safe to retry?** For anything that changes data, confirm a repeated call does not duplicate the effect.

## Retry safety, specifically

Assistants retry after timeouts and dropped connections. This is normal behaviour, not an error condition, and it means every write tool is called more than once eventually.

A `create_order` tool that is called twice has created two orders, and the user sees a duplicate they did not make.

Ask for write tools designed so a repeat is harmless — checking whether the change was already applied, or accepting a request identifier that makes the second call a no-op:

> Make the create request tool safe to retry, so calling it twice with the same input does not create two records.

## Separate reading from writing

Keep the two clearly distinct, in naming and in what each tool does. Every tool carries a capability label — read-only, or may modify data — and the modifying ones deserve most of your review time.

Mixing them produces the worst case: a tool that reads and, as a side effect, changes something. The assistant will call it as if it were a query.

## Start small

A handful of focused read-only tools, live and working, beats a broad surface reviewed once.

Two reasons beyond caution. **New app features do not become tools automatically** — you ask for each action you want exposed, so the surface only grows deliberately. And **users must refresh their connector when tools are added, removed, or renamed**, which makes churn on a live integration visibly annoying for them.

Get the shape right while nobody is connected.

## Statuses

| Status | Meaning |
|---|---|
| **Active** | Live in the published integration; assistants can call it |
| **Not published** | Added or changed since the last publish. The previous version keeps working until you publish |
| **Inactive** | The integration is unavailable, typically because the app is no longer publicly published |

The middle one is the routine trap: tool changes are not live until the app is published again.

## Keeping tools fast

Tools run one action at a time and the assistant waits with a time limit. Work taking more than tens of seconds — processing a large file, generating media — appears stuck or interrupted.

Keep tools fast and leave heavy work inside the app. A tool that starts a job and returns its status is a better shape than a tool that does the job and times out.
