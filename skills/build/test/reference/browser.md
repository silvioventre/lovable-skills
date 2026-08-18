# Browser testing: real user flows

Drives the app in a real browser — navigating, clicking, filling forms, submitting — while capturing screenshots, inspecting elements, and observing console and network activity.

Slower than the other tools and worth it, because it is the only one that sees what a user actually experiences. Everything else verifies a piece; this verifies the assembly.

## When it is the right tool

- Someone reports broken or unexpected behaviour and you need to see it.
- A multi-step flow needs checking end to end: onboarding, checkout, sign-up, a wizard.
- The problem may involve routing, authentication, timing, or state — the things that only fail when the parts are combined.
- You want to confirm a change from the user's point of view rather than the code's.

## Test the flow, not the page

A flow test that only loads a page and asserts something rendered has verified almost nothing. The value is in the sequence: arrive, act, and check that the *consequence* happened.

For any flow, walk it as a person would and assert at each meaningful step:

1. **Arrive** where a real user would — usually signed out, from the entry point, not from a deep link into the middle.
2. **Act** the way a user would, including the mistakes: submit empty, submit invalid, go back, refresh mid-flow.
3. **Assert the effect, not the appearance.** A success message is not proof the record was created. Check the thing that was supposed to change.
4. **Continue past the success.** Does the next page load with the new state? A flow that "works" and leaves the user somewhere broken has failed.

## Flows worth covering

For most apps, in rough priority:

- **Sign-up, sign-in, sign-out, password reset**, with a fresh account rather than an already-authenticated session.
- **The core action** — whatever the app exists to do, done once, completely.
- **Payment**, if there is one, end to end at least once before launch.
- **The signed-out path.** Visit as a stranger. Does anything crash because it assumed a user?
- **Each role**, if roles exist. Shared components behaving correctly for one role and wrongly for another is a common and invisible bug.

## Reading the output

Browser testing captures console logs and network requests alongside the screenshots. When something fails, read those before theorising:

- **A console error at the moment of failure** usually names the cause outright.
- **A failed or missing network request** distinguishes a frontend bug from a backend one immediately, and tells you which skill to continue in.
- **A request that succeeded but returned the wrong thing** points at the backend — continue in [backend-tests.md](backend-tests.md).
- **A correct response rendered wrongly** points at the frontend.

That distinction, made from the network tab in seconds, is worth more than an hour of reading code.

## Its limits

- **It is slow.** Do not use it to check a rule that a frontend test could check in milliseconds.
- **It can be timing-sensitive.** A test that fails intermittently is usually waiting for the wrong thing, not finding a real intermittent bug. Wait for the state you care about, not a duration.
- **It proves the flow worked once**, in one environment, with one set of data. It does not prove the rule holds generally — that is what the isolated tests are for.

## After it passes

A browser test confirming a fix is the moment to decide whether the behaviour deserves permanent protection. If this bug could plausibly return — and most fixed bugs can — add the cheaper isolated test that would catch it, per [what-to-test.md](what-to-test.md). The browser test proved the fix; the isolated test keeps it proved.
