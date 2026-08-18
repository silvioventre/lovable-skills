# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project does not use semantic versioning, because it ships instructions rather than software — entries are grouped by date instead.

Skills imported into a Lovable workspace are copies and do not update automatically. After a change here, re-import the skill to pick it up.

## [Unreleased]

### Added

- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and this changelog.
- Issue and pull request templates.
- A `README.md` for every skill, so each folder is a usable landing page when imported or browsed on its own.

### Changed

- The entire repository is now in English. The root README, the six category READMEs, and the skill template were previously in Italian.
- The root README now covers what a skill is, how these are built, the full catalogue, installation, usage examples across the life of a real project, and how the skills hand off to each other.
- The validator reports skills and templates separately, rather than counting the scaffold as a skill.

### Removed

- `skills/design-and-ux/responsive/LICENSE`, which duplicated the repository's MIT license. Only `art-direction` carries its own, because it is Apache-2.0.

## 2026-08-18

### Added

- `mcp` — publishing an app as an MCP server for AI assistants.
- `emails` — sending domains, templates, and deliverability.
- `analyze` — data analysis and file generation.
- `payments` — test and live environments, subscription lifecycle, go-live.
- `auth` — choosing and setting up authentication.
- `knowledge` — writing and maintaining persistent instructions.
- `plan` — understanding and scoping before building.
- `test` — routing verification to the right tool.
- `ship` — pre-flight, access control, and going live.
- `deploy-external` — running outside Lovable Cloud.
- `debug` — routing a symptom to its diagnostic playbook.
- `secure` — routing a security concern to the layer that owns it.
- `responsive` — making a layout work at every width, against a pass gate.
- `art-direction` — design guidance, adapted from [Impeccable](https://github.com/pbakaus/impeccable).
- `scripts/validate-skills.py` and a GitHub Actions workflow running it on every push and pull request.

## 2026-07-17

### Added

- Initial repository scaffolding and `lovable-codebase-audit-cleanup`.
