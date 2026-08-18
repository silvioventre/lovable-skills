# test

Routes verification to the tool that matches what you are checking, and insists on the sequence that makes a fix provable: reproduce, fix, confirm with the same input, then protect it with a test.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/test
```

## Use

```
/test verify the whole checkout flow end to end
/test write tests for the login form
/test call the signup function directly with an invalid email
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The routing table, the two kinds of verification, and the rules — including that a test which has never failed has proven nothing |
| `reference/browser.md` | Real user flows: where it runs, whose session it uses, what it cannot reliably interact with |
| `reference/frontend-tests.md` | UI logic in isolation — testing behaviour rather than implementation |
| `reference/backend-tests.md` | Direct calls and edge tests, including the inputs your UI would never send |
| `reference/what-to-test.md` | What earns a test, what does not, and the order to build coverage in |

## Scope

Not for diagnosing a failure whose cause is unknown — [debug](../../troubleshooting/debug/) covers that first. `debug` finds the cause; `test` proves the fix and stops it regressing.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
