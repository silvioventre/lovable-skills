# Third-Party Notices

## This skill is a derivative work

`art-direction` is a derivative work of **Impeccable**, a design guidance system for AI coding agents.

**Original work:** https://github.com/pbakaus/impeccable
**Original license:** Apache License 2.0
**Author:** Paul Bakaus
**Copyright:** Copyright 2025 Paul Bakaus

This skill is distributed under the same Apache License 2.0. See [LICENSE](LICENSE).

It is **not** affiliated with, endorsed by, or supported by Paul Bakaus or the Impeccable project. The name "Impeccable" is used here only to describe the origin of the work, as permitted by section 6 of the Apache License 2.0. For the original — including the parts this port cannot provide — go to the upstream project.

### Modifications made to the original work

Adapted from Impeccable's Agent Skills package (`.agents/skills/impeccable/`) to run inside Lovable, an environment with no shell, no subagents, and no bundled Node runtime. Specifically:

**Removed** — components that Lovable cannot execute:

- All bundled Node scripts (102 `.mjs` files): the context loader, the 59-rule anti-pattern detector, the pin/doctor/hook administration commands, the decision-page server, and the image helpers.
- The `live` command and its browser server, DOM injection, and manual-edit flow (`live.md`, `live-setup.md`, and the `manual-edit-applier` role).
- The `hooks` command and its post-edit detector hook (`hooks.md`).
- The `doctor` command and its artifact drift repair (`doctor.md`).
- The deprecated `craft` alias, which the original documents as adding nothing.
- Agent definition files for other runtimes (`agents/*.toml`, `agents/openai.yaml`).

**Not reproduced** — content that does not ship with the original source:

- The challenger catalog behind `concept-seed.mjs`. The original resolves it from a private catalog directory or the hosted API at `impeccable.style/api`; the source comments state that "the full catalog does not ship with the skill." This port replaces the catalog draw with an inline procedure in which the agent derives its own challenger directions, and preserves only the anti-argmax mechanism (never leading with your own top-ranked candidate). No network call and no telemetry.

**Rewritten** — to work without the toolchain:

- `SKILL.md`: setup now reads `PRODUCT.md` / `DESIGN.md` from the project instead of invoking `context.mjs`; the command table drops the removed commands; a section on working inside Lovable replaces the harness-specific guidance.
- Mechanical scans in `critique.md`, `typeset.md`, `layout.md`, `polish.md`, and `routing.md`: the detector invocation is replaced by reading the source against the anti-pattern families in `craft-floor.md` and `audit.md`, plus inspection of the rendered preview.
- Sub-agent orchestration in `critique.md`: the two isolated assessments now run sequentially in one context, with explicit rules to preserve the isolation the two-process design provided.
- The `degraded/` role files, which the original used only as a fallback for runtimes without subagents, are the primary path here and are renamed `reference/roles/`.
- Persisted artifacts move from `.impeccable/` to `docs/design/`, and script-mediated storage (surface briefs, critique snapshots) becomes plain files with documented paths and frontmatter.
- Instructions specific to other runtimes (Codex, Cursor, GitHub Copilot) are removed throughout.

## Platform Design Skills

The `reference/ios.md` and `reference/android.md` platform reference files are distilled from ehmo's `platform-design-skills` (Apple Human Interface Guidelines and Material Design 3 rules), and were rewritten in Impeccable's voice by its author before being carried into this port unchanged.

**Original work:** https://github.com/ehmo/platform-design-skills
**Original license:** MIT
**Author:** ehmo
