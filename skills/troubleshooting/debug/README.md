# debug

Routes a symptom to the diagnostic playbook that owns it, finds the root cause, and fixes that. A change that makes the error message disappear without explaining why it happened is not a fix — it relocates the bug.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/troubleshooting/debug
```

## Use

```
/debug the checkout page shows a blank screen after I click pay
/debug the inventory list is empty for my second account but the rows exist
/debug I've tried to fix this four times and it keeps coming back
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The symptom routing table, and the rules — including that two failed attempts means stop fixing and start investigating |
| `reference/triage.md` | The first five minutes: evidence to gather, how to classify, and inverting the question |
| `reference/build-and-preview.md` | Build errors, blank screens, sandbox problems, oversized files |
| `reference/behavior.md` | It runs but does the wrong thing — vanished components, stale state, wrong data |
| `reference/backend.md` | Data, edge functions, permissions, auth, and schema drift after a revert |
| `reference/loops.md` | Recognising a fix loop and the ordered procedure for escaping it |
| `reference/prompts.md` | Reusable recipes: investigate-without-editing, fragile-area, audit, performance |

## Scope

For a project-wide cleanup of dead code and unused dependencies, [lovable-codebase-audit-cleanup](../../code-quality/lovable-codebase-audit-cleanup/) covers that ground in more depth.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
