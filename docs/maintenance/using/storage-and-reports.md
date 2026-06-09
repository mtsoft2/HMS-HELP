# Storage & Reports

The **Storage** branch of the sidebar groups three table / file
oriented views.

## Table Sizes (live)

A live grid — one row per table, sortable.

| Column | What it shows |
|---|---|
| **Table** | Table name. |
| **Rows** | Current row count. |
| **Data size** | Size of the table data (excluding indexes). |
| **Index size** | Total size of every index on the table. |
| **Total size** | Data + index. |
| **% of DB** | This table's share of the total database size. |

Sort by **Total size** descending to spot the heavyweights — those are
usually the tables whose growth pattern drives the database forward.

### Use cases

* **Capacity planning** — which tables are growing fastest?
* **Index audit** — when *Index size* > *Data size*, the table likely
  has unused indexes (cross-reference with the **Unused indexes**
  checklist row).
* **Archive candidates** — old audit / log tables often top this list
  and are good candidates for the retention purge.

## Backup Log Report

Printable version of the **Backup Log** sidebar item. Same data, A4
layout, branded header, ready to attach to an audit ticket or
e-mail.

* Pick a date range.
* Group by Day / Week / Month.
* Filter by Type / Status.
* Export to PDF or print directly.

## Table Sizes Report

Printable version of **Table Sizes**.

* Snapshot at the moment you run it.
* Grouped by schema.
* Highlights the top 20 tables by size.
* Export to PDF or print directly.

## Tips

* Run **Table Sizes Report** monthly and keep the PDFs — comparing
  reports across months is the cleanest way to see growth trends.
* The two reports share the dashboard's print stylesheet, so they
  match the branding of the rest of HMS automatically.

➡ Back to **[Overview](../index.md)**.
