# Backup Log

The **Backup Log** sidebar item opens the audit list of every backup
ever taken on this database — manual or scheduled.

## What you see

A table, newest at the top. Columns:

| Column | What it shows |
|---|---|
| **Date** | When the backup ran. |
| **Type** | FULL / DIFF / LOG. |
| **Size** | The file size on disk. |
| **Status** | Saved / Failed / Running. |
| **File** | The path to the file (click to open the parent folder). |
| **Description** | Whatever was typed in the Run Backup dialog or the schedule's Description field. |
| **Run by** | User who initiated (or *Schedule* for cron jobs). |
| **Duration** | How long the backup took. |

## Filters

* By type — FULL / DIFF / LOG.
* By status — Saved / Failed.
* By date range.

## Actions

* **Refresh** — re-pull the list.
* Per-row click → opens the folder containing the file.
* **Backup Log Report** (Storage → Backup Log Report) — printable
  version for distribution.

## Tips

* Use **Description** when you take a backup before a risky change —
  it becomes the searchable label in the log.
* The log keeps every entry forever — the **Audit / log overage**
  checklist row + safe fix is how you purge old rows. Default
  retention is set in Settings.

➡ Continue to **[Storage & Reports](storage-and-reports.md)**.
