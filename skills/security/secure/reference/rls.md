# Row-level security: the floor

RLS decides who can read or modify each individual row, enforced by the database itself. It holds even when a function has a bug or a query forgets a filter — which is exactly why it is the layer that matters most.

Basic policies are set up automatically, but they encode a guess about your access model. Review them early: RLS is far easier to change before real data exists, and a wrong policy discovered after launch is a breach rather than a task.

## The four patterns

Most apps are a combination of these. Identify which one each table needs before writing anything — the policy follows from the pattern.

| Pattern | Rule | Typical tables |
|---|---|---|
| **Personal data** | A user reads and writes only their own rows | profiles, settings, notes, orders |
| **Team or organisation** | Members access rows belonging to their team | projects, documents, shared records |
| **Public read, owner write** | Anyone reads, only the owner modifies | posts, listings, comments |
| **Role-based** | Access depends on the user's role | admin tables, moderation, billing |

If a table does not fit any of them, that is worth pausing on. Access rules that resist description are usually a sign the data model is wrong, and a complicated policy is much harder to verify than a clear one.

## Writing policies

**Separate policies per operation.** Read, insert, update, and delete are distinct. The most common gap is a table with a working read policy and no update policy, or an update policy that lets a user change rows they can only read.

**Ownership comes from the session, never from the row.** The policy compares the authenticated user against the row's owner column. A policy that trusts a value supplied by the request is not a policy.

**Keep policies about access, not business logic.** A policy answers "may this user touch this row". Whether the action makes sense — the right status, the right time, the right quota — belongs in an edge function. Policies carrying business rules become slow, hard to reason about, and quietly wrong when the rules change.

**Every new table needs a policy.** A table added later without one is the most common way a secured app develops a hole. If it holds anything user-specific, it needs a policy on the day it is created.

> Add RLS policies to [table] so users can only access their own rows, with separate rules for read, insert, update, and delete.

> Set up RLS for teams and projects so team members only see projects belonging to their team.

## Verifying — the part that gets skipped

A policy that lets the intended user through is half tested. The half that matters is whether it keeps everyone else out, and that is invisible when you test as yourself.

Test each of these explicitly:

- **The intended user** sees exactly their own rows — not fewer, not more.
- **A second, unrelated user** sees none of the first user's rows. This requires an actual second account; it cannot be reasoned about.
- **Writes are constrained too.** Can user B update or delete a row belonging to user A? Read policies are usually right and write policies usually are not.
- **Shared and public data** behaves as intended for a signed-out visitor.
- **Every role** that touches the table, including the ones you rarely use.

Silence is the normal failure mode here: RLS filters rather than errors, so a wrong policy shows up as an empty list, not a denial. An empty result during development frequently means the policy is wrong — and the temptation is to widen it.

**Never widen a policy to make a feature work.** That is how a data leak ships. If the user legitimately needs those rows, express that rule precisely. If they do not, the empty result was correct and the bug is elsewhere.

## Before publishing

- RLS is enabled on every table holding user or sensitive data — enabled, not just policied.
- No table added since the last review is missing policies.
- A second test account cannot read or modify the first account's data.
- Write policies are as strict as read policies.
- Public and shared data is exactly as public as intended, checked while signed out.
- Any table deliberately left open is a documented decision, not an oversight.

> Review all RLS policies and report, per table: which operations are covered, which are missing, and whether a user could reach another user's rows through any of them.
