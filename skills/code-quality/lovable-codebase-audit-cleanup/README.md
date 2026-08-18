# lovable-codebase-audit-cleanup

A two-phase rationalisation of a project that has grown. Phase one is a read-only audit finding dead code, unused dependencies, duplication and maintainability risks. Phase two is a strictly scoped cleanup of only the batches you explicitly approve.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/code-quality/lovable-codebase-audit-cleanup
```

## Use

```
/lovable-codebase-audit-cleanup audit this codebase
/lovable-codebase-audit-cleanup find unused dependencies
/lovable-codebase-audit-cleanup implement Batch 2
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | Phase routing, the full audit scope, evidence requirements, the batch roadmap, and the guardrails for both phases |

Single-file skill: the two phases are sequential and share one set of guardrails, so splitting them would separate rules from the work they constrain.

## Scope

Never combines the phases. No code is modified during the audit, and cleanup runs only against finding IDs you have approved. For a single failing symptom rather than a project-wide sweep, use [debug](../../troubleshooting/debug/).

## License

MIT — see the [repository LICENSE](../../../LICENSE).
