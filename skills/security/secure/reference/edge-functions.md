# Edge functions: the security boundary

Edge functions run server-side in an isolated environment, where users cannot read the code or modify what it does. Everything that must be true regardless of what the client sends belongs here.

## What belongs server-side

Move it into a function if it is any of these:

- **Authentication and authorisation.** Who is asking, and are they allowed to do this.
- **Validation that matters.** Every rule from [frontend.md](frontend.md) that would be a problem if bypassed.
- **Business logic and workflows.** Registration, payments, approvals, state transitions, anything multi-step where a skipped step is a problem.
- **External API calls.** Anything using a secret key, or that costs money per call.
- **Sensitive data processing.** Personal or financial data, and the logging around it.
- **Any value the client should not choose.** Prices, quotas, roles, limits, identifiers of records the user does not own.

The last one catches the subtle cases. A function that accepts a `userId` from the request body and returns that user's data is an unauthenticated read of anyone's account, however carefully the frontend passes the right value. Derive identity from the session, never from the payload.

> Move [payments / registration / this external call] from the frontend into a secure edge function with proper validation and authorisation.

## The shape of a safe function

Every function that touches data or money follows the same order. Skipping a step is where vulnerabilities live.

1. **Identify the caller.** Read the session server-side and resolve who this is. Reject unauthenticated requests before anything else.
2. **Authorise the action.** Confirm this specific user may perform this specific operation on this specific record. Being signed in is not permission.
3. **Validate the input.** Types, ranges, formats, enum membership, sizes. Reject anything unexpected instead of coercing it.
4. **Derive, don't accept.** Prices from the catalogue, ownership from the session, timestamps from the server, roles from the database. Anything security-relevant that arrives in the request body is a claim, not a fact.
5. **Do the work.**
6. **Return only what the caller may see.** Do not pass an internal record straight through — it frequently carries fields the user should never receive.

```js
// The first check in any protected function
const { user } = await supabase.auth.getUser();
if (!user) {
  return new Response("Unauthorized", { status: 401 });
}
```

Authentication is step one, not the whole job. A signed-in user is still not allowed to edit someone else's record, and only step 2 catches that.

## Errors and logging

**Return errors that help the caller without describing your internals.** A stack trace, a raw database error, or a failing SQL statement sent to the client is reconnaissance. Return a status and a plain message; keep the detail in the logs.

**Distinguish "not allowed" from "does not exist" deliberately.** Telling an attacker that a record exists but is not theirs is itself information. For sensitive resources, respond the same way to both.

**Log the security-relevant events** — failed authorisations, unusual input, privileged actions — with enough context to investigate. Never log secrets, tokens, passwords, or full personal records.

**Never let a failure fall through to success.** A caught error that returns a bare 200, or an authorisation check inside a `try` whose `catch` continues, converts a denial into an approval. Fail closed.

## Secrets inside functions

Secrets are stored in backend infrastructure and injected into functions at runtime. They exist only server-side and never travel to the client.

Two rules: never return a secret in a response, even partially, and never write one into a log line. A key logged during debugging is a key in your log retention.

If a function needs a secret that is not configured, it should fail clearly at the point of use rather than proceeding with an undefined value — that failure mode produces confusing downstream errors that look like application bugs. See the backend section of the `debug` skill.

## Rate and abuse limits

Any function that costs money, sends messages, or can be called anonymously needs a ceiling. Without one, a public endpoint calling a paid API is an open tab on your account.

Apply limits per user where there is a session, per IP where there is not. Cap request body size, especially for uploads. Validate file type and size server-side before storing anything — a client-side accept filter is a suggestion.

## Verifying

A function is not verified by the happy path. Confirm each of these:

- Unauthenticated request → rejected.
- Authenticated but unauthorised request → rejected.
- Request with a manipulated body — someone else's record id, a changed price, an out-of-range value — → rejected, not silently accepted.
- Failure inside the function → returns an error, does not fall through to success.
- The response contains only fields this caller is entitled to see.

If any of these were only tested through your own UI, they were not tested. The UI sends well-formed requests by construction; an attacker does not.
