# analyze

Analysing data and producing files — reports, exports, charts, diagrams, processed media — in an isolated environment that never touches the project's source code. Then building features from what the analysis found.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/analyze
```

## Use

```
/analyze what are my top 5 products by revenue in this CSV?
/analyze generate a PDF report of this quarter's metrics from my database
/analyze turn this spreadsheet into a working app with a dashboard
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | What it covers, the rules, and how to get good output |
| `reference/analysis.md` | Understanding the data before answering, and stating precision honestly |
| `reference/outputs.md` | Specifying the artefact, and what breaks in generated PDFs, spreadsheets and charts |
| `reference/build-from.md` | Building from a data file, a specification, or a finding |

## Scope

Not for changing the app's own data-fetching code, which is ordinary development — use [plan](../plan/) for that.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
