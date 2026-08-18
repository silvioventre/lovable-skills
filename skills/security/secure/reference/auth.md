# Authentication and authorisation

Two different questions, and conflating them is the most common access-control bug in these apps.

- **Authentication:** who is this? Establishes identity.
- **Authorisation:** may they do this, to this? Establishes permission.

Being signed in is not permission. A function that checks only for a valid session lets any registered user act on any record it accepts an id for.

## Every decision is server-side

The browser may reflect a decision. It may never make one.

```js
// Wrong: satisfied by writing a value into browser storage
const isAuthenticated = localStorage.getItem("authToken") !== null;
if (isAuthenticated) showAdminPanel();

// Correct: the server decides, on every request
const { user } = await supabase.auth.getUser();
if (!user) {
  return new Response("Unauthorized", { status: 401 });
}
```

The same applies to roles. A role read from client state, a JWT decoded in the browser, or a flag returned by an earlier request are all claims the client controls or can replay. Resolve the role from the database, server-side, on the request being authorised — not once at login and trusted thereafter.

## Protecting routes

A protected route needs two independent things, and only the second is a control:

1. **A client-side guard**, so an unauthorised user sees a redirect rather than a broken page. Convenience.
2. **Server-side enforcement on every endpoint that route uses.** The actual protection.

Removing a route from the navigation does not protect it — the URL still resolves. What protects the admin area is that every endpoint behind it refuses callers who are not admins, independently, every time.

The test: if someone typed the URL directly with a normal account, what would they be able to do? If the answer is anything beyond seeing an error, the route is not protected.

## Sessions

- **Use the platform's built-in session handling.** Hand-rolled token storage is where the subtle bugs live.
- **Validate the session server-side on every request that matters.** A session that was valid at login may have expired, been revoked, or belong to a user whose role changed.
- **Redirect to sign-in on expiry** for the user's sake, but never treat the absence of a redirect as evidence of a valid session.
- **Clear state fully on sign-out**, including cached user data and any query cache holding another user's rows. Stale cache after a user switch shows one person another person's data with no vulnerability in the access rules at all.

## Privileged actions

Anything destructive, financial, or administrative needs its own check at the point of execution, not inherited from context:

- Deleting or modifying records the user does not own
- Changing another user's role or permissions
- Refunds, payouts, credits, quota changes
- Bulk operations
- Anything in an admin interface

Two specific traps. **Role escalation:** an endpoint that updates a user record and accepts a `role` field lets a user promote themselves unless role changes are handled separately and authorised explicitly. **Insecure direct object reference:** an endpoint that accepts a record id and acts on it without confirming ownership lets anyone act on anyone's record by changing a number.

## Internal and workspace-only apps

For an app that should not be publicly reachable:

- Set project access to workspace rather than public.
- Confirm it is not published publicly — check, do not assume.
- Require authentication anyway. Internal tools become externally reachable through link sharing, migration, or a settings change, and an app that never authenticated has no defence when that happens.
- Audit who has access periodically, especially after people join or leave.

## Verifying

Testing as yourself proves nothing about access control. For each protected surface, confirm:

- Signed out → cannot reach it, and cannot reach its endpoints directly.
- Signed in as a normal user → cannot reach privileged actions, including by calling their endpoints directly.
- Signed in as each role → sees and does exactly what that role should, no more.
- After sign-out → no cached data from the previous session remains visible.
- After a role change → the new permissions apply immediately, without needing a re-login to take effect.

The direct-endpoint checks are the ones that matter and the ones usually skipped. The UI only ever sends the requests it was built to send.
