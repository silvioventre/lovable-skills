# Testing, sharing, and maintaining

## Test before you share

Connect your own app in an assistant your users actually use, and run the real workflows. If sign-in is required, test the full connection flow including your app's sign-in and consent screens — connection problems surface there first.

Work through all seven. The middle ones are the ones that find real problems, and they are the ones skipped.

1. **Run each tool as an ordinary signed-in user.** The baseline.
2. **Try a protected tool as a user without the required role, ownership, or plan.** Confirm it is denied. This is where an interface-only permission check is exposed.
3. **Request a record that does not exist**, and one belonging to another user. Confirm both are refused, and that the refusal does not itself confirm the record exists.
4. **Check every tool returns only the fields its task needs.** Read the actual response, not the description.
5. **Run a write action twice** and confirm no duplicate or unintended change. Assistants retry.
6. **Test a paid or resource-intensive action against your app's limits.** Confirm the limit applies to the tool call and not only to the interface.
7. **For a public integration**, connect from a session where you are not signed in and verify exactly what is reachable.

Checks 2, 3, and 6 cannot be performed from your own privileged session. They need a second account, deliberately under-privileged — the same requirement the `secure` skill has, for the same reason.

## Sharing

After publishing, the MCP link appears in the integration panel. Users add it as a custom connector in their assistant.

Rather than sending a bare link, a connection page inside your app explaining what the integration does works better. One caution: **assistant setup flows change**, so link to each assistant's own documentation rather than copying detailed steps into a page nobody will maintain. Stale connection instructions generate support requests that look like bugs in your integration.

Any assistant that can connect to a remote MCP server and complete its sign-in flow will work, not only the ones with in-product instructions.

## Keeping it current

The integration serves the **published** version of your app. After changing the app, its tools, its access logic, or its domain:

1. **Publish again.** This is what updates the live server. Tool changes do nothing until you do.
2. **Redeploy the backend function** on older app stacks, so the live integration picks up backend changes.
3. **Tell users to refresh their connector** when you add, remove, or rename tools. Assistants cache the tool list, so until they refresh they see the old one. Changes to existing behaviour do not need a refresh.
4. **Share the new link if it changed.**

That third point is the practical brake on iteration: every tool rename is a message to your users. It is the reason to get the tool surface right before sharing widely.

## When the link changes

**It cannot be changed on demand**, and whether it changes at all depends on the app's stack.

On newer apps the link derives from the app's web address, so **changing the primary custom domain changes the MCP link**, and every connected user must paste the new one. On older apps the link points at a backend function and survives a domain change.

Plan a domain migration accordingly — see the `ship` skill. A domain change that silently breaks every connected assistant is a bad way to find this out.

## Stopping

| Action | Effect |
|---|---|
| **Remove a tool** | Ask, then publish. It disappears from the integration |
| **Remove the integration** | Ask, then publish. The generated code goes and the server goes offline. The app keeps working |
| **Unpublish the app** | The server goes offline immediately, along with the app |
| **Delete the project** | Permanent |

**Unpublishing disconnects every connected user**, and republishing recreates the server with a link that may differ. Unpublishing a live integrated app is therefore not a neutral pause — treat it as a disconnection with notice owed to whoever is connected.

## What it cannot do

- **Tools cannot notify anyone.** Assistants act only when a user asks, so "watch this and alert me" is not possible. If someone expects that, say so before they design around it.
- **Long-running tools time out.** Keep tools fast; run heavy work inside the app.
- **There is no directory.** Nobody discovers your integration; you share the link yourself.
- **An existing hand-built MCP server is not detected in advance.** If it uses the same routes, the build fails rather than overwriting it — which is the good outcome. Ask for it to be rebuilt as an integration, or set up on a different path.
