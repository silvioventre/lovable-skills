# Pre-flight: before the first publish

Publishing is cheap to do and expensive to undo. On a plan where the published site cannot be access-restricted, whoever reaches it has reached it, and unpublishing later does not un-see it.

Work through these in order. The first two are gates: do not continue past a failure.

## 1. Security gate

Run the `secure` skill's pre-publish gate in full and report each item. In short, the ones that block a launch:

- No secrets in frontend code, config, or build-time variables.
- RLS enabled and policied on every table holding user data.
- A second account cannot read or modify the first account's data.
- Privileged endpoints reject a normal user called directly.
- Errors return no stack traces or raw database messages.

The automatic scan that runs when the publish dialog opens checks database configuration and known patterns in 10–15 seconds. It is a useful floor and not a substitute for the gate — it cannot know which rows a given user was *supposed* to see.

**If the app handles real user data, payments, or personal information, treat a failure here as blocking.** Say so plainly rather than publishing with caveats.

## 2. Access intent

Decide, and state, who should be able to reach the live site — before publishing, because on some plans this cannot be narrowed afterwards.

Ask directly if it is not obvious: *is this for the public, for your team, or for a few named people?* An unexamined default is how internal tools end up indexed by search engines. Options and constraints in [access.md](access.md).

## 3. The app actually works

Verified in the preview, in this order. Each of these has shipped to production more than once.

- **Every route loads.** Including the ones not linked from the navigation.
- **The signed-out path.** Visit as a stranger: does the landing page work, does sign-up work, does anything crash because it assumed a user?
- **Sign-up, sign-in, sign-out, password reset** end to end, with a fresh account rather than the one already logged in.
- **Each role** sees what it should, if the app has roles.
- **Empty states.** A new account sees empty lists everywhere. "No data" is not an empty state; a first-run user seeing raw emptiness is the most common launch-day disappointment.
- **Error and loading states.** Something slow, something failed — does the UI say so and offer a way forward?
- **Mobile.** The `responsive` skill's gate if it has not been run; at minimum, no horizontal scroll and reachable primary actions at 320px.

## 4. Content and metadata

- **Site title, description, and icon** set to real values, not the auto-filled defaults.
- **Social preview** correct — the link will be pasted somewhere.
- **No placeholder copy left**: lorem ipsum, TODO, "Your headline here", sample names, test products.
- **No test data visible**: seeded rows, dummy accounts, debug panels.
- **Legal pages** if the app collects data or takes payment.

## 5. Environment

- **No development URLs, localhost references, or test keys** in what is about to ship. A test payment key in production takes payments that never arrive.
- **Every required secret configured** for the environment being published.
- **Analytics or event tracking** firing, if the launch is supposed to be measured.

## Report the gate

Give each section a pass, fail, or unverified. Unverified is never reported as a pass — for a launch, an unchecked item is a risk the user is accepting, and they can only accept it if they know about it.

If anything fails, say what it is and what it would cost to ship anyway. The decision to publish regardless is the user's; presenting it as ready when it is not takes that decision away from them.
