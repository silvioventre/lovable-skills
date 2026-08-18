# Security policy

## What this repository contains

This repository holds markdown instruction files. It ships no runtime code, no dependencies that execute in a user's application, and nothing that runs on a server. The only executable file is `scripts/validate-skills.py`, a local development helper.

That shapes what a security issue means here.

## What counts as a security issue

**A skill that instructs unsafe behaviour.** These playbooks are followed by an AI agent working inside real projects with real data. A skill that recommends an insecure pattern — weakening an access policy, exposing a secret, disabling a protection to make something work — is a genuine security problem, because it will be acted on.

This is the category that matters most. If you find a playbook whose advice would make an app less safe, please report it.

**Instructions that could cause data loss.** A step describing an irreversible operation without saying so, or advice that would delete or overwrite something without confirmation.

**A vulnerability in the validator script**, for example unsafe file handling.

## What does not count

- Disagreeing with a recommendation on style or approach — open a normal issue.
- Security problems in Lovable itself, which belong to [Lovable's own security process](https://lovable.dev).
- Security problems in an app you built. The [`secure`](skills/security/secure/) skill may help, but the app is yours.

## Reporting

Email **silvio.ventre@v3-advisory.com** with a description of the issue, the file and line involved, and what an agent following the instruction would do wrong.

For issues in the first two categories above, please report privately rather than opening a public issue, so the instruction can be corrected before it is more widely seen.

You can expect an acknowledgement within a few days. There is no bounty programme.

## Supported versions

The `main` branch is the only supported version. Skills already imported into a Lovable workspace are copies and do not update automatically — after a correction lands here, re-import the skill to pick it up.
