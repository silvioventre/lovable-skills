# Browser testing: real user flows

Drives the app in a real browser — navigating, clicking, filling forms, submitting — while capturing screenshots, inspecting elements, and observing console and network activity.

Slower than the other tools and worth it, because it is the only one that sees what a user actually experiences. Everything else verifies a piece; this verifies the assembly.

## Where it runs, and as whom

Three facts that change how you use it.

**It is a real browser in a remote virtual environment**, not your local one. It does not take over your session.

**It runs against the preview of the current project** — exactly the version you are looking at. Not the published site. If the bug is only on production, this cannot see it; the `ship` skill covers verifying live. Where the project separates test and live environments, this runs against the test environment preview.

**It is signed in as whatever app user you are currently signed in as in the preview.** This is the one that matters: the agent acts with your account's permissions and can trigger anything that account can trigger. Before testing a surface with destructive actions — deleting records, sending messages, issuing refunds, contacting real people — **say explicitly what must not be clicked**. Signed-in testing requires the platform's own backend; apps using an external auth provider can only test pages that do not require signing in.

## Do not combine a big change with its test

Ask for the change, then ask for the test in a follow-up.

If browser testing gets stuck mid-run and you stop it, work done during that step can be lost — and when the same prompt also contained the implementation, that is the implementation at risk. Building first and testing second costs one extra message and protects the work.

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

## Screen sizes

It can drive the app at mobile, tablet, and desktop widths, defaulting to the preview's current size. Useful for confirming a flow completes on a phone — but for a real responsive audit, the `responsive` skill's width ladder and gate are the right instrument. This checks that a flow works at a size; that one checks that the layout holds at every size.

## Its limits

- **It is slow.** Do not use it to check a rule that a frontend test could check in milliseconds.
- **It can be timing-sensitive.** A test that fails intermittently is usually waiting for the wrong thing, not finding a real intermittent bug. Wait for the state you care about, not a duration.
- **It proves the flow worked once**, in one environment, with one set of data. It does not prove the rule holds generally — that is what the isolated tests are for.

Some interactions are genuinely unreliable, and a failure on one of these is more likely a limit of the tool than a bug in your app:

| Interaction | Reliability |
|---|---|
| Clicking text-labelled buttons and links, filling inputs | Reliable |
| Icon-only buttons | Harder — no text to identify them by |
| Drag and drop | Possible, noticeably less reliable than clicks |
| Clipboard actions and text selection | Unreliable |
| Custom or complex file upload widgets | Unreliable. Standard file inputs work |
| Canvas-based or drawing tools | Not supported |
| Subtle visual design and colour differences | Not reliable for judging |

That last row is worth stating plainly: this tool verifies behaviour, not aesthetics. Design quality is the `art-direction` skill's job, judged by looking.

## When it keeps failing the same action

Repeated failure on one element is more often an interaction limit than an app bug, but check rather than assume:

1. **Read the screenshots and logs from the run.** They usually show whether the element was there, visible, and in the state expected.
2. **Make the element easier to interact with** — visible text on an icon-only button, or an accessibility label. This frequently improves the app for real users too, which makes it worth doing rather than working around.
3. **If it persists, instruct the agent to avoid that element** and verify the rest of the flow, rather than losing the whole test to one control.

An underlying app problem — a hidden element, broken state, an unexpected layout — presents the same way, so do not skip step 1.

## After it passes

A browser test confirming a fix is the moment to decide whether the behaviour deserves permanent protection. If this bug could plausibly return — and most fixed bugs can — add the cheaper isolated test that would catch it, per [what-to-test.md](what-to-test.md). The browser test proved the fix; the isolated test keeps it proved.
