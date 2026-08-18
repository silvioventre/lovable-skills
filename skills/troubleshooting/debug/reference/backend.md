# Backend failures: data, functions, permissions, auth

Anything that fails server-side. The defining move here is to **establish which layer denies you before changing anything** — the same symptom, "no data", comes from the query, the policy, the function, or the session, and the fixes are unrelated.

## Locate the layer first

An empty list or a failed request can originate at four different depths. Test downward until one answers:

1. **Does the data exist in the table?** Query it directly. If the rows are not there, the bug is in whatever should have written them, and everything below is a distraction.
2. **Does the request return them?** Check the network response. Rows present but response empty means access control, not the query.
3. **Does the function run and succeed?** Check the function logs. A function failing before it returns produces the same empty UI as a permission denial.
4. **Does the client render what it received?** A correct response rendered wrongly is a frontend bug — continue in [behavior.md](behavior.md).

Skipping this ordering is how RLS policies get rewritten to fix what was a client-side filter.

## Row-level security and permissions

RLS is the most common cause of "the data is there but I can't see it", and the symptom is usually silence rather than an error: an empty array, not a denial.

| Symptom | Likely cause |
|---|---|
| Empty result, rows exist, no error | A policy excludes this user. Silent filtering is normal RLS behaviour |
| Works for one user, not another | The policy depends on identity or role, and one case is not covered |
| Reads fine, writes denied | Separate policies per operation; the insert or update policy is missing or stricter |
| Worked before, empty after adding a table or column | A new table has no policy, or the schema change broke the policy's assumption |
| A user sees other users' data | Too permissive — a real security bug, not just a functional one. See the `secure` skill |

Diagnose by asking what the policy allows for **this specific user in this specific role**, then compare against what the query asks for. State the mismatch before editing a policy.

Never widen a policy to make a feature work. A policy relaxed to unblock development is a data leak that ships. If a user legitimately needs the rows, the policy should express that rule precisely, not permit everything.

## Edge functions

Check the function logs first. Almost every edge function failure names itself there, and reading the logs is faster than reasoning about the code.

Ordered by frequency:

- **A missing secret or environment variable.** The function throws on a value that is undefined at runtime. Confirm every secret it reads is actually configured.
- **An unhandled error in the body.** A throw with no catch returns a generic failure to the client and tells the caller nothing. The log has the real message.
- **The caller's expectations do not match.** Wrong method, wrong content type, a body shape the function does not parse, a missing auth header.
- **A downstream failure.** The function is fine; the service it calls rejected the request — bad credentials, rate limit, changed contract. The log distinguishes this from a bug in your code.
- **Stale deployment.** The running version is not the code you are reading. Redeploy with a trivial change and re-test before debugging further.

When the function returns an error to the client, make sure it returns something *useful*: a status and a message the caller can act on. A function that swallows failures and returns a bare 200 makes every future bug in it invisible.

## Authentication and sessions

- **Signed in, treated as signed out.** The session is not reaching the request. Check that the client attaches it and the function reads it.
- **Access granted that should not be.** Something is deciding authorisation on the client. Client-side checks are advisory only — see the `secure` skill; this is a vulnerability, not just a bug.
- **Works until a reload.** Session persistence or restoration on load.
- **Expired session handled badly.** The app should route to sign-in on expiry, but the decision must be re-validated server-side rather than trusted from client state.
- **Role checks inconsistent.** The role is read from different places in different components. One source of truth, resolved server-side.

## Schema changes

Reverting a project does not cleanly revert the database. A rollback can leave the code expecting one schema and the database holding another — a mismatch that presents as type errors, missing columns, or empty results with no obvious cause.

After any revert that touches data, validate the schema against what the code expects before debugging anything else. Ask explicitly whether the schema still matches the code's assumptions and what diverged.

Prefer additive changes. A new nullable column breaks nothing; a renamed or dropped one breaks every consumer at once, and the failures surface far from the change.

## Verifying a backend fix

A backend fix is not verified until it is exercised through the real path with the real identity. Confirm at minimum:

- The success path returns the expected data for the intended user.
- The denial path still denies — a permission fix that grants access to everyone "works" for the reporter and is a breach.
- Every role that touches the changed policy, function, or table still behaves correctly.
