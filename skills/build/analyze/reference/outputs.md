# Producing files

Documents, spreadsheets, charts, diagrams, and processed media. Scripts run in an isolated Linux environment with the usual data and visualisation tooling available, and anything missing can be installed.

Generated files go to the project's **Files area, not its code**, so the per-file code size limit does not apply to them. They are stored with the project, versioned on revision (`report_v2.pdf` alongside the original), and **deleting one cannot be undone**.

## Specify the artefact, not the topic

The single biggest determinant of output quality. "Make a report" produces something generic; naming the structure produces the thing you wanted.

State: the sections and their order, what goes in each, the format, and the filename if it matters.

> Create a PDF report with a cover page, a summary table of the quarter's metrics, one section per product line with a chart, and a closing section listing the three largest changes. Save it as q1-summary.pdf.

## Always open the result

Generated files are frequently subtly wrong in ways the generating script cannot detect. Check before delivering:

| Format | What breaks |
|---|---|
| **PDF** | Content clipped at page edges, tables split badly across pages, text overflowing its box, fonts substituted |
| **Spreadsheet** | Numbers stored as text, dates as serial numbers, a column dropped, headers misaligned with data |
| **Chart** | Overlapping or truncated labels, a misleading axis that does not start at zero, an unreadable legend, categories silently merged |
| **Diagram** | Nodes overlapping, text outside its shape, a layout that renders differently than intended |
| **Images** | Aspect ratio distorted rather than preserved, transparency lost on format conversion |

Deliver a file you have actually looked at. A broken PDF handed over as finished is worse than one more iteration.

## Charts

A chart makes a claim. Make sure it is the true one.

- **Label the axes and state the units.** Including the currency and whether figures are thousands.
- **Start a bar chart's value axis at zero.** A truncated axis exaggerates differences, which is the most common way an honest chart misleads.
- **Say what the period is** and whether it is complete. A final partial month reads as a collapse.
- **Do not plot more series than can be distinguished.** Beyond about five, a table communicates better.
- **Check readability at the size it will be viewed**, not at full resolution.

## Exports

For a CSV or spreadsheet someone else will use:

- **Header names that mean something** without the original context.
- **One consistent date format**, ISO where there is any doubt about locale.
- **Numbers as numbers**, not text, and without embedded currency symbols in a numeric column.
- **State the row count and the period covered** when delivering, so a truncated export is noticed immediately rather than after it is used.

## Documents

For reports and decks:

- **Lead with the conclusion.** The person who reads only the first page should get the answer.
- **Attach the caveats to the figures they qualify**, not to a methodology note at the end — the figures get quoted, the note does not.
- **Say when the data was pulled.** Any report about live data is a snapshot, and undated snapshots get reused months later.

## Iterating

Context is retained across the conversation, so revisions are described rather than re-specified: *make the summary table sortable by revenue*, *add a section for refunds*, *use the brand colours*. Each revision is stored as a new version, so comparison stays possible.

Where the first attempt is substantially wrong, say what was wrong before regenerating — an unexplained retry tends to produce a differently wrong file.

## Pulling from connected tools

Where tools are connected, they can serve as the data source directly — issues, messages, documents — with the output generated from what is pulled.

Two things to state when doing this: **what was actually retrieved** (how many items, over what period), and **what was not**, since these sources paginate and truncate. A report summarising "the last 50 messages" should say that it was 50 and not everything.
