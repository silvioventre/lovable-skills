# Security review and pre-publish gate

Use this for a full review, for "am I safe to publish", or as the dispatcher when a concern spans layers.

## The review, in order

Work outside-in. Each pass has a different failure mode, and the order matters: an exposed secret is worth more to an attacker than a missing policy, and finding it first changes what else you need to check.

### 1. Secrets — always first

Search the frontend for API keys, tokens, credentials, and connection strings, including build-time environment variables compiled into the bundle. Details in [frontend.md](frontend.md).

Anything found is **critical and time-sensitive**: report it immediately and say what must be rotated. A secret that has shipped is compromised regardless of whether anyone noticed, and removing it from the code does not revoke it.

### 2. Layer placement

For each security-relevant decision in the app — who may do what, what something costs, what is valid — ask which layer makes it. Anything decided in the browser is a finding. See [frontend.md](frontend.md) and [edge-functions.md](edge-functions.md).

The high-yield questions: where do prices come from, where is the user's identity established for each request, and does any endpoint accept a record id without confirming ownership.

### 3. Database policies

Per table: is RLS enabled, which operations have policies, and could one user reach another's rows. Writes are usually weaker than reads. Full procedure in [rls.md](rls.md).

Verify with a second account rather than by reading the policies. Policy review catches missing rules; only a second identity catches wrong ones.

### 4. Authentication and roles

Where identity is established, whether roles are resolved server-side per request, and whether privileged endpoints check permission independently of the UI. See [auth.md](auth.md).

### 5. Exposure

What is published, and to whom. An internal tool published publicly is a finding regardless of how good its access rules are.

## Pre-publish gate

Before going live, confirm each. Report every item as pass, fail, or unverified — an item you did not check is unverified, never a pass.

| # | Check |
|---|---|
| 1 | No secrets in frontend code, config, or build-time variables |
| 2 | Every validation that matters is enforced server-side |
| 3 | RLS enabled and policied on all tables holding user data |
| 4 | A second account cannot read or modify the first account's data |
| 5 | Authentication and role checks enforced server-side, per request |
| 6 | Privileged endpoints reject normal users when called directly |
| 7 | External API calls and paid operations happen server-side, with limits |
| 8 | Errors return no stack traces, raw database messages, or internals |
| 9 | Project visibility matches intent — internal apps not published publicly |
| 10 | Findings from the platform's own security scans addressed |

Items 4 and 6 are the ones that get skipped and the ones that catch real breaches. Both require actually issuing the request as the wrong user; neither can be established by reading code.

## Reporting

Order by severity, and describe impact in terms of what someone can actually do. "The Stripe secret key is in the bundle, so any visitor can read it and issue charges against your account" is actionable. "Hardcoded credentials detected" is not.

For each finding: where it is, what an attacker could do with it, what fixes it, and — for exposed secrets — what must be rotated and in what order.

Fix critical findings before anything else, and before continuing the review if the app is already live.

## What a passing review does not mean

Automated scans check configuration, dependencies, and known patterns. They cannot tell whether your access rules express what you meant. A policy that is syntactically perfect and grants the wrong people access passes every scan.

So: never report an app as secure because a scan came back clean. Report what was checked, what passed, and what remains unverified.

Security is not a milestone. Re-run this review whenever authentication changes, a table is added, data access is modified, an integration is introduced, or a new role appears. Each of those is a chance for the floor to develop a hole — and the review is cheap compared to the alternative.
