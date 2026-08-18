# Frontend: the layer that decides nothing

Everything here runs in the user's browser. It can be read, modified, and replayed by anyone. Treat all of it as published.

## Secrets

Any value that reaches the browser is public — in source, in a config object, in a build-time environment variable, in a comment, in a network response.

```js
// Wrong: readable by anyone who opens the bundle
const API_KEY = "sk-1234567890abcdef";
const STRIPE_SECRET = "sk_live_...";
```

Build-time variables are the trap that catches most people: a value injected at build time is *compiled into the bundle*. Prefixing it, hiding it in a config file, or naming it something innocuous changes nothing.

**Where secrets go instead:** stored in backend infrastructure and read only inside edge functions. Ask for the key to be added securely rather than pasting it into a component:

> Add an API key for [service] securely, so it is never exposed in frontend code.

**Publishable vs secret keys.** Some services issue a key intended for the client — a publishable or anonymous key — alongside a secret one. The publishable key is designed to be public and is safe in the browser *provided the server enforces what it can do*. The secret key never is. If you cannot tell which you have, treat it as secret.

**A secret that has ever shipped is compromised.** Removing it from the code does not remove it from a user's cache, a deploy history, or a bundle someone already downloaded. Rotate it at the provider, then remove it. Deleting without rotating leaves the key live and the app feeling fixed.

To sweep for exposures:

> Review all frontend code for exposed secrets, API keys, tokens, or credentials, including build-time environment variables compiled into the bundle.

## Validation

Client-side validation is a user-experience feature. It tells someone their email is malformed before they wait for a round trip. It provides no security whatsoever, because the request can be sent without ever loading your form.

```js
// Fine for UX, worthless as a control
const validateUser = (userData) => userData.email.includes("@");
```

Every rule that matters must be enforced again server-side, where it cannot be bypassed. That includes the ones that look like formatting rather than security:

- Field formats, lengths, and types
- Required fields
- Numeric ranges — **especially quantities, prices, and discounts**
- Enum and status values
- File type and size
- Business rules: is this transition allowed, is this user permitted, is this within quota

The price field is the canonical example. A checkout that sends the amount from the client lets anyone set it to zero, however carefully the UI restricts the input. Amounts are derived server-side from the item, never accepted from the browser.

Keep client validation for the feedback it gives. Duplicating a rule in both layers is correct and expected — the client one is convenience, the server one is the control.

> Identify client-side validation that enforces a rule the server does not, and move the enforcement into edge functions.

## Auth state in the UI

Frontend auth state controls **what is displayed**, never what is permitted.

```js
// Wrong: an access decision made in the browser
const isAuthenticated = localStorage.getItem("authToken") !== null;
if (isAuthenticated) showAdminPanel();
```

Two things are wrong here. The check is trivially satisfied by setting a value in browser storage, and the panel it guards presumably calls endpoints that must do their own checking anyway.

Hiding a control does not protect the action behind it. A route not in the navigation is still reachable by typing the URL. A disabled button still has a working endpoint behind it. If the API permits the call, the call is permitted — the UI is a suggestion.

The correct division: the browser asks the server who the user is and what they may do, then renders accordingly. The server re-checks on every request that matters, independently, without trusting anything the client claims about itself.

## What is legitimately safe here

To keep the rule usable rather than paranoid:

- Publishable and anonymous keys designed for client use, when the server constrains what they can do
- Public content, and data the signed-in user is entitled to see
- UI state, presentation logic, formatting, routing
- Validation for feedback, mirrored by real enforcement server-side

The test is simple: **if a user modified this value or skipped this code entirely, what could they reach?** If the answer is anything other than a worse interface, it does not belong in the frontend.
