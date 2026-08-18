---
name: analyze
description: Use when the user wants data examined or a file produced rather than app code changed — "analyze this CSV", "what are my top products by revenue", "generate a PDF report from my database", "export the last 30 days of orders", "convert this JSON to Excel", "make a chart of monthly signups", "turn this spreadsheet into a dashboard", "read this PDF spec and build the first version", "resize these images", "how many users signed up this week". Covers analysing uploaded files and database data, producing documents, spreadsheets, charts, diagrams and processed media, and building app features from what the analysis found. Not for changing the app's own data-fetching code, which is ordinary development work.
---

# Analyze

Analysis and file generation run as scripts in an isolated environment. **The project's source code is never touched by this work** — which is what makes it safe to explore data freely, and what distinguishes it from ordinary development.

Generated files land in the project's Files area, not in its code, so they escape the per-file code size limit entirely.

## What this covers

| Kind of request | Example |
|---|---|
| **Analysis** | Top products by revenue from an uploaded CSV; signups this week broken down by day |
| **Documents** | A PDF report summarising the quarter from database data |
| **Exports** | Every order from the last 30 days as CSV |
| **Transformation** | JSON converted to a formatted spreadsheet |
| **Visuals** | A bar chart of monthly signups; an architecture diagram as Mermaid |
| **Media** | Images resized and converted to a different format |
| **Database questions** | Counts, breakdowns, and aggregates answered directly |
| **Build from a file** | A tracking spreadsheet turned into a working app; a PDF spec read and implemented |

That last row is the one people miss. The analysis and the build stay in the same conversation, so **what was found can immediately become what gets built** — a drop-off analysis into a reworked onboarding flow, a spreadsheet into a dashboard.

## Route the task

| The task | Playbook |
|---|---|
| Analysing data, answering a question about it | [reference/analysis.md](reference/analysis.md) |
| Producing a document, export, chart, or diagram | [reference/outputs.md](reference/outputs.md) |
| Turning a file or a finding into app features | [reference/build-from.md](reference/build-from.md) |

## The rules

**Say what the numbers mean, not just what they are.** A table of figures answers the literal question and usually not the real one. State what the data shows, what stands out, and what it does not support — an analysis that cannot be acted on has not finished.

**Never present an uncertain figure as exact.** If rows were skipped, dates were ambiguous, duplicates were possible, or a field was inconsistent, say so with the number. A confidently wrong figure is worse than a caveated one, because it gets used in a decision.

**Check the output before delivering it.** Scripts produce files that are subtly broken — a PDF with clipped layout, a spreadsheet missing a column, a chart with unreadable labels. Open the result and confirm it is what was asked for.

**Work a subset first on large data.** Process a sample, confirm the shape and the logic are right, then run the whole thing. Discovering a wrong assumption after a long run costs the run.

**Do not confuse this with app development.** Generating a report about orders is this skill. Changing how the app queries orders is ordinary development, and belongs in `plan` or straight into building.

## Getting good output

The quality of the result tracks the specificity of the request more directly here than almost anywhere else.

- **Name the structure.** "A PDF report with a cover page, section headers, and a summary table" beats "a report".
- **Name the file.** Ask for a specific filename if one matters.
- **Name the data source.** An upload, a database table, a connected tool.
- **Iterate rather than restart.** Context from earlier outputs is retained, so describing what to change is cheaper than re-specifying from scratch. Revisions are stored as new versions rather than overwriting.

## Limits worth knowing

- Uploads are capped per file and per message, with a much smaller cap on the free plan.
- Database access during code execution depends on the project's read and write permissions being granted.
- **Deleting a generated file cannot be undone.**
