# Setting up a sending domain

Domain verification, DNS, SPF, DKIM, and DMARC are handled for you — no external email provider account and no API keys. What you provide is a domain you control and access to its DNS.

## Prerequisites

- Lovable Cloud enabled on the project.
- A paid workspace.
- Ownership of a domain, and the ability to manage its DNS.
- Workspace admin or owner, to add, verify, or delete domains.

## Use a sending subdomain

A dedicated transactional subdomain — `notify.yourdomain.com` rather than the root — is created for sending.

This is not cosmetic. Sending reputation attaches to the domain that sends, so isolating transactional mail on a subdomain means a problem there does not damage the reputation of your root domain, which is what your human email and any future marketing sending depend on. Keep it that way.

## How the scope works

Domains live at the **workspace** level, and this catches people out:

- A workspace can hold several verified domains.
- One verified domain can serve many projects.
- Each project picks which verified domain it uses, and **only one is active per project**.
- Only `Verified` domains send anything.
- Email can be enabled or disabled per project independently.

**Deleting a domain is a workspace-wide action.** Every project using it immediately falls back to default auth emails, and their app emails stop sending entirely. Before deleting, check which projects are on it — this is not reversible by undo, only by re-adding and re-verifying.

## Statuses and what they mean

| Status | Meaning | What to do |
|---|---|---|
| **Verifying** | DNS records not yet confirmed | Wait for propagation, up to 48 hours, then retry |
| **Verified** | Sending is active | Nothing |
| **Offline** | Records were changed, removed, or expired after verification | Restore the missing records and re-verify |
| **Domain removed** | Deleted while this project was using it | Connect a different verified domain, or add a new one |

`Offline` is the one that surprises people: verification is not permanent. Anything that touches DNS later — a registrar migration, a cleanup of old records, a new mail provider — can silently break sending. If email stops working and nothing in the app changed, check this first.

## Disabling rather than deleting

Emails can be turned off per project. When disabled, **auth emails keep sending from the default sender** rather than your domain, and **app emails stop entirely**.

That asymmetry matters. Disabling does not break sign-up and password reset — users just receive unbranded messages — but it does silently stop order confirmations and every other app email. If a project's app emails vanished, check whether email was disabled before investigating the code.

## After verification

Verification enables sending; it does not create any templates. Templates are generated on request — see [templates.md](templates.md).

Then resist the urge to test heavily. A newly provisioned domain has no reputation, and a burst of test sends is the fastest way to start badly. Send one or two, confirm they arrive, and let real traffic do the rest — [deliverability.md](deliverability.md) explains why.
