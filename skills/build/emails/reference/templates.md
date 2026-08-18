# Templates

## Auth emails

Six built-in templates, generated on request rather than automatically — until you generate them, users receive the defaults.

| Template | Sent when |
|---|---|
| Confirm signup | An account is created and email confirmation is on |
| Password reset | A reset is requested |
| Magic link | Passwordless sign-in is enabled and a link is requested |
| Invite | Someone is invited to the project |
| Email change | A user updates their address — confirms the new one |
| Reauthentication | Identity must be re-verified before a sensitive action |

Magic link and reauthentication may need enabling before their templates do anything; ask if they are not already configured.

Generating them applies the app's branding automatically: CSS variables from the stylesheet for colours, fonts and radius, a logo detected in the public or assets folders and uploaded to an email asset store, and copy adapted to the app's tone and language.

## App emails

No built-in templates — you describe the behaviour and the template is generated with it:

> Add order confirmation emails to my app. When an order is placed, send a confirmation email to the customer.

Design the trigger as carefully as the content. **An app email should be the consequence of one identifiable action by one identifiable person.** Anything that sends to a list, on a schedule, or to people who did not act is outside what transactional sending permits and will damage the domain.

The unsubscribe footer is added automatically and feeds a suppression list, so unsubscribed addresses are blocked before sending. Leave it alone.

## Customizing

Ask for changes in plain language:

> Match the emails to my brand by using #2563eb for buttons and headings, and add my logo.

Copy and tone, brand colours, layout, images and logo placement, and subject lines are all fair game. Authentication variables, secure callback links, and the unsubscribe footer are preserved automatically — and must be, or the flows they belong to break.

**The outer body background must stay `#ffffff`.** Inner components can carry your colours. This is a rendering constraint across email clients, not a style preference.

Each template can be previewed and test-sent, to your own address or another. Use that sparingly on a new domain — see [deliverability.md](deliverability.md).

## Editing the files directly

| | Templates | Sending logic |
|---|---|---|
| **Auth** | `supabase/functions/_shared/email-templates/` | `supabase/functions/auth-email-hook/` |
| **App** | `supabase/functions/_shared/transactional-email-templates/` | `supabase/functions/send-transactional-email/` |

Written with React Email components and **inline styles** — email clients do not support external CSS, so styling that works in the app will not work here.

Two things must survive any edit: the authentication variables and callback links in auth templates, without which sign-up and password reset break; and the unsubscribe footer in app templates.

**After editing files or subject lines, ask for a redeploy:**

> Redeploy my email templates.

Changes do not take effect until then. Users receiving old content after an edit is the expected behaviour of a missing redeploy, not a bug — this is the single most common false alarm in this area.

## Writing subject lines and content

Deliverability is decided partly here, before any sending happens.

**Do:** describe what happened plainly — "Reset your password", "Your order has shipped". Include the details the message exists to convey: order numbers, tracking links, amounts, dates. Make the required action obvious. Match the email to the action the user took.

**Do not:** use all caps, stack exclamation marks, write misleading or curiosity-gap subject lines, build image-heavy layouts, or link to domains unrelated to your sending domain.

**No marketing in auth emails.** An upsell in a password reset is the fastest way to have password resets filtered as promotional — which means locked-out users who cannot get back in.
