# Deliverability

Reaching the inbox is not a setting. It is a reputation, built by how you send over weeks, and the first days of a new domain matter more than anything you do later.

## A new domain starts at zero

Inbox providers treat fresh domains cautiously, because spammers use fresh domains and abandon them. Expect a rough start and do not react to it.

| Period | What to expect |
|---|---|
| First few days | Test emails may land in spam. Normal |
| First few weeks | Placement improves as real traffic builds reputation |
| First few months | Reputation stabilises with consistent, engaged sending |

**Helps:** starting with ordinary auth traffic — real signups, real password resets. Letting volume grow with the user base. Adding app emails as transaction volume actually grows. Consistent sending over weeks. Emails that recipients expected because they just did something.

**Hurts:** a sudden volume spike from a brand-new domain. Bulk test sends right after setup. Long silences followed by bursts. Changing domain or sender identity in a panic because the first tests went to spam.

That last one is the trap. The instinct when tests land in spam is to change something — a new subdomain, a different sender name, more tests to check. Every one of those resets or damages the reputation being built. **The correct response to early spam placement is to send normally and wait.**

## Send only what a user triggered

Auth emails follow real user actions. App emails go to the person the event concerns — the customer who placed *that* order, the user whose account changed.

Do not manufacture traffic to test or warm up. Unnatural patterns are exactly what reputation systems detect.

Never send to addresses that previously hard-bounced, to people who unsubscribed from non-essential mail, or to inactive and closed accounts. Each is a direct hit to reputation, and repeated hard bounces are the most damaging of all.

## Keep it transactional

The strongest single rule, and the easiest to erode gradually.

Auth emails should match the action that caused them and explain why they arrived. App emails should carry the information about that specific event. Neither should carry promotional content.

Mixing marketing into transactional mail trains filters to treat all of it as promotional. The cost lands on the messages you can least afford to have filtered — the password reset that a locked-out user needs right now.

If the product needs marketing email, that is a separate sending path with separate rules, not an addition to these templates.

## Consistency and alignment

**Keep the sender identity stable.** Same from-address, same sender name, same domain. Frequent changes read as evasion.

**Align the links with the sending domain.** Mail sent from your domain should link to your domain or its subdomains. Mismatched domains are a phishing pattern and get filtered accordingly. This is worth checking whenever a template embeds a third-party link — a tracking redirect or a hosted asset can quietly break alignment.

## Authentication must keep passing

SPF, DKIM, and DMARC are configured automatically at setup. They stop passing if the DNS records are later changed or removed — and then mail goes to spam with nothing in the app having changed.

If deliverability degrades suddenly, **check that the domain still shows Verified** before investigating anything else.

## Watch bounces

Analytics shows sent, delivered, and bounced over 7, 30, or 90 days, plus a per-project activity log.

Hard bounces from invalid or mistyped addresses are the most harmful signal there is, and repeatedly retrying them compounds the damage. If bounces are climbing, the fix is usually upstream: validate email input at signup, and stop retrying addresses that already hard-bounced.

## When it still will not work

For persistent spam placement or rejections, external diagnostics are worth reaching for — sender reputation and spam-rate dashboards from the major inbox providers, and blocklist lookups to check whether the domain, sending IP, or the URLs inside your emails have been listed.

These matter most at higher volume. At low volume, the answer is nearly always that the domain is young and the sending pattern is impatient.
