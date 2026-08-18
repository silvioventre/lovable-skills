---
name: emails
description: Use when the app needs to send email, or email it already sends is going wrong — "send emails from my own domain", "add order confirmation emails", "brand my auth emails", "customize the password reset email", "my emails are going to spam", "emails aren't sending", "set up a sending domain", "add a notification email when someone signs up", "my template changes aren't showing". Covers the two kinds of transactional email an app sends, setting up a verified sending domain, generating and customizing templates, and the deliverability practices that decide whether messages reach the inbox. Not for marketing campaigns or newsletters, which are a different kind of sending with different rules.
---

# Emails

Two things decide whether email works: whether the app sends the right message at the right moment, and whether that message reaches the inbox. The second is the one people discover late, and it is largely determined by choices made in the first weeks of sending.

## Two kinds of email, one set of rules

| | Triggered by | Templates | Unsubscribe |
|---|---|---|---|
| **Auth emails** | Cloud Auth, on account and identity events | Six built-in, generated on request | Not required — they are necessary for service |
| **App emails** | Your application logic, on things happening | None built in; generated from what you ask for | Added automatically, and must stay |

The six auth templates cover signup confirmation, password reset, magic link, invite, email change, and reauthentication. App emails are whatever your product needs — order confirmations, shipping notices, account updates.

Both are **transactional**: sent because a specific person did a specific thing. That is not a category label, it is the constraint that governs everything below.

## Route the task

| The task | Playbook |
|---|---|
| Setting up a sending domain, DNS, verification | [reference/setup.md](reference/setup.md) |
| Generating or customizing templates | [reference/templates.md](reference/templates.md) |
| Adding a new app email to a flow | [reference/templates.md](reference/templates.md) |
| Emails going to spam, or building reputation | [reference/deliverability.md](reference/deliverability.md) |
| Emails not sending, domain stuck, changes not showing | [reference/troubleshooting.md](reference/troubleshooting.md) |

## The rules

**Keep transactional email strictly transactional.** No marketing, no upsells, no promotional language — especially in auth emails. Mixing them triggers spam filtering and costs you the deliverability of the messages that actually matter, like password resets.

**Never remove the unsubscribe footer from app emails.** It is added automatically, removing it violates sending requirements, and it feeds a suppression list that blocks future sends to people who opted out. Auth emails do not carry one and do not need it.

**Do not send bulk test emails from a new domain.** The instinct after setup is to fire off twenty tests. That is precisely the pattern that damages a fresh domain's reputation, because it looks like exactly what spammers do. Send a couple, then let real user traffic build the reputation.

**Template changes require a redeploy.** Editing template files and seeing old emails arrive is not a bug. Ask for a redeploy.

**Links inside an email should point at the sending domain.** Inbox providers compare the two, and a mismatch is a phishing signal.

**Keep the outer email body white.** Inner components can carry brand colours; the outer background must stay `#ffffff` or rendering breaks across email clients.

## Constraints worth knowing before designing a flow

- **100 emails per hour per workspace.** A flow that fans out to many recipients at once will hit this. Design around it or request a higher limit.
- **50,000 transactional emails per month** included per paid workspace, counted across every project in it.
- **Domains are workspace-level, one active per project.** Deleting a domain is workspace-wide, and every project using it falls back to default auth emails while app emails stop entirely.

## Report

Say which domain is sending, whether it is verified, and — for anything touching templates — whether a redeploy has happened. An email change that was never redeployed looks identical to one that did not work.
