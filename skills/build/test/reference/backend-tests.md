# Backend verification: direct calls and edge tests

Two complementary tools, normally used together. Direct calls are for understanding behaviour now; edge tests are for keeping it true later.

**Edge test stack:** the Deno built-in test runner, with native TypeScript.

## The sequence

This is the whole method for a backend bug, and each step exists because skipping it costs more than it saves.

1. **Call the function directly** with the input that triggers the problem. You now have the failure isolated from the UI, with the actual request and response in front of you.
2. **Apply the fix**, knowing what is actually wrong rather than what you assume is.
3. **Call it again with the same input** and confirm the behaviour changed. Same input, so the comparison means something.
4. **Add an edge test** so the rule cannot break silently later.

Step 1 is the one people skip, and it is the one that pays. Debugging backend logic through the UI means every attempt goes through routing, state, rendering, and auth — any of which can produce the same visible symptom.

## Direct calls

Running an edge function with specific inputs and inspecting the result immediately.

Use when:

- You suspect the backend and want to separate it from the UI.
- You need to check specific parameters or a specific input shape.
- You want to compare behaviour before and after a change.
- You are debugging authenticated behaviour — if signed in, the call can use your session.

**What to send.** The happy path proves the least. The calls that find bugs are the ones your UI would never make:

- A missing required field.
- A wrong type — a string where a number is expected, null where the type says non-null.
- An out-of-range value: a negative quantity, a zero price, a date in the past.
- **Another user's record id.** If this returns their data, that is not a bug report, it is a vulnerability — go to the `secure` skill.
- No authentication at all, on an endpoint that requires it.

That last pair matters. The UI only ever sends well-formed, authorised requests, so nothing about a working UI tells you what the endpoint does when someone bypasses it.

**Read the whole response.** Status, body, and headers. A function returning a 200 with an error inside the body is a common shape and looks like success from anywhere but here.

## Edge tests

Automated tests for backend rules, so subtle logic does not break silently.

Use when:

- You changed an edge function and want regression protection.
- You are validating business rules or permissions — the things whose failure is expensive and quiet.
- The behaviour is hard to check manually, so nobody will.

**What to cover:**

- **The rule itself**, with a valid input and the expected result.
- **Rejection.** Invalid input, missing fields, wrong types — assert it is *rejected*, not that it happens to not crash.
- **Authorisation.** Unauthenticated is refused; authenticated-but-not-permitted is refused. If a function guards anything, this is the test that matters most, and it is the one usually missing.
- **Edge values.** Zero, negative, empty, maximum, boundary conditions.

**Assert the failure mode, not just the success.** A test suite that only proves the function works when used correctly leaves every interesting case uncovered — and the interesting cases are exactly where the money and the data live.

## Fail closed, and test for it

A function whose error handling lets a failure fall through to success turns a denial into an approval. Write the test that proves it does not: send something that must fail, and assert it actually failed rather than quietly returning a default.

This is worth stating separately because it passes review easily. Code that looks like it handles errors, but whose catch block continues to the success path, is a security bug wearing the costume of robustness.

## Where this stops

These tools verify the function. They do not verify that the app calls it correctly, that the response renders, or that the flow works for a person. When the backend is proven and the user still cannot complete the task, the problem is above this layer — [browser.md](browser.md), or the `debug` skill if the cause is unknown.
