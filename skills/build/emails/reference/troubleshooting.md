# When email is not working

## Emails are not sending at all

Check in this order. Each is a complete stop, and the first four cost seconds.

1. **Is a domain linked to this project?** Email is configured per project, and a project can end up with none.
2. **Is its status `Verified`?** Nothing sends from any other status.
3. **Are emails enabled for this project?** When disabled, auth emails fall back to the default sender and **app emails stop entirely** — so a report of "the order confirmations stopped but sign-up still works" is this, not a bug.
4. **For auth emails**, is Cloud Auth enabled and is the event you expect one of the six supported types?
5. **Was the sending function deployed?** Especially after editing templates.
6. **Have you hit the rate limit?** 100 emails per hour, per workspace, across every project in it.

Then use a template's test send and read the analytics log for delivery failures and bounces. The log distinguishes "never sent" from "sent and rejected", which point in completely different directions.

## Template changes are not showing

Users are still receiving the old version.

**This is almost always a missing redeploy.** Template changes take effect only after the corresponding function is redeployed:

> Redeploy my email templates.

Do not start editing the template again. Editing further and redeploying nothing produces a growing pile of changes that all appear not to work.

## The domain is stuck in Verifying

Causes, in rough order of frequency:

- DNS records have not propagated yet.
- The `NS` delegation is wrong.
- The `TXT` verification record is missing.
- Records were added at the wrong level of the domain — a subdomain instead of the root, typically.

Recheck the exact records shown in the emails settings against what is actually published, confirm they went on the correct root domain, allow up to 48 hours for propagation, then retry verification.

Do not add a second domain because the first is slow. That starts another reputation from zero and leaves two half-configured domains.

## The domain shows Offline

Required records were changed, removed, or expired **after** verification succeeded.

Verification is not permanent. A registrar migration, a DNS cleanup, or another mail provider's setup can remove records nobody associated with your app. Restore the missing `NS` or `TXT` records and re-verify.

This is the first thing to check when email stops working and nothing in the app changed.

## The domain shows Domain removed

It was deleted at the workspace level while this project was using it. Connect a different verified domain to the project, or add and verify a new one.

Worth checking with whoever administers the workspace before re-adding — a domain deleted deliberately may have been deleted for a reason.

## Bounce rates are climbing

Usually invalid addresses: typos at signup, and retries against addresses that already hard-bounced.

The fix is upstream. Validate email input at signup, and never retry a hard bounce — repeated sends to invalid addresses damage reputation faster than almost anything else.

## Test emails land in spam

Expected for a newly provisioned domain, and **not a signal to change anything**.

The wrong response — more test sends to check, a new sender identity, a different subdomain — makes it worse. Send a couple, then let genuine user-triggered traffic build reputation over the following weeks. See [deliverability.md](deliverability.md).

## Everything is configured and mail still lands in spam

At this point the question is reputation rather than configuration, so confirm in order:

1. Domain status is still `Verified`, so authentication is passing.
2. The domain is not brand new — if it is, this is not a problem yet.
3. Links in the templates point at the sending domain rather than elsewhere.
4. Nothing promotional has crept into transactional templates.
5. Bounce rates are not elevated.

If all five hold and placement is still poor at meaningful volume, external reputation and blocklist tools are the next step.
