# Analysing data

## Understand the data before answering

The fastest way to produce a confidently wrong number is to run an aggregate over data whose shape you assumed.

Before answering anything, establish:

- **What one row represents.** An order, a line item, or an order-line join produce very different revenue totals from the same file.
- **Where the boundaries are.** What date range does this actually cover, and is it complete at both ends? A "last 30 days" file that starts mid-month makes every daily average wrong.
- **What is missing.** Empty cells, nulls, placeholder values like `N/A` or `-`. How many, and whether they are concentrated somewhere meaningful.
- **What is duplicated.** Especially if the data came from an export or a join.
- **What the types actually are.** Numbers stored as text, dates in mixed formats, currency with symbols embedded, decimal separators varying by locale. These break aggregation silently rather than loudly.

State what you found before the answer. A user who learns that 12% of rows had no date *after* acting on the analysis has been misled by a technically correct number.

## Answer the question that was asked

"What are my top 5 products by revenue" is a specific question. Answer it directly, then add what is worth knowing — not the reverse.

Where the question is ambiguous, resolve it explicitly rather than silently. Revenue before or after refunds; a period by calendar month or rolling 30 days; a customer counted by account or by email. Pick the sensible reading, **say which you picked**, and note the alternative if it would change the answer materially.

## Say what it means

A table is not an analysis. After the figures, say:

- **What stands out**, and whether it is large enough to matter.
- **What it does not tell you.** Correlation that is not causation, a spike that coincides with a campaign, a decline that is a data artefact rather than a real change.
- **What would answer the question better**, if the available data cannot.

That third point is frequently the most useful output. Data that cannot support the decision being made is worth saying so about, rather than producing a number that will be used anyway.

## Be honest about precision

Attach the caveat to the number, not to a footnote:

> Top product is X at €48,200 — excluding 340 rows (4%) with no product id, which may concentrate in one category.

Not:

> Top product is X at €48,200.
>
> *(Note: some rows were skipped.)*

The first survives being copied into a message to someone else. The second does not, and these numbers get copied.

## Work in stages on large data

Process a sample first. Confirm the row shape, the parsing, and the logic against something you can eyeballs-check, then run the whole set.

This catches the errors that are invisible in aggregate — a date format that silently failed on a subset, a currency column that parsed to zero, a join that multiplied rows.

## Querying the database

Counts, breakdowns, and aggregates can be answered directly against project data, provided the project's read permissions allow it.

Two cautions:

- **A query is a snapshot.** Say when it ran. "How many users signed up this week" answered on Tuesday means something different when read on Friday.
- **Read the schema before assuming a column means what its name suggests.** `created_at` on a row that gets upserted is not a signup date, and `status` fields accumulate values nobody documented.

## Then

If the analysis should become a deliverable, continue in [outputs.md](outputs.md). If it should become a feature — an improved flow, a dashboard, a fix — continue in [build-from.md](build-from.md), while the findings are still in the conversation.
