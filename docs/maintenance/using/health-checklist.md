# Health Checklist

The **Checklist** tab is the heart of the Maintenance module — every
database-health rule on one scored list, with one-click fixes for the
safe ones.

![Database Health Checklist](../screenshots/02-checklist.png)
/// caption
The **Database Health Checklist**. The Health Score (top-right) is a
weighted 0-100 figure over every check. Use the category and status
pills to narrow down; click the wrench on a row to apply its safe fix.
///

## The header

| Control | What it does |
|---|---|
| **Health Score** | A single 0-100 figure summarising every check. Coloured ring around the number tells you at a glance. |
| **Scan All** | Re-runs every check. Updates the score. |
| **Run Safe Fixes** | Applies the safe fix for every row that has one — non-destructive, audit-logged. |
| **Refresh** | Re-pull cached results without re-running. |

## Filters

Two rows of pills above the list:

* **Category pills** — *All · Backup · Configuration · Integrity ·
  Maintenance · Operations · Performance · Security*.
* **Status pills** — *Critical · OK · Warn · Fail · Info* with the
  count for each.

Click a pill to toggle filtering. Multiple status pills can be active
at once.

## The list

Each row is one check. Columns:

| Column | What you see |
|---|---|
| **#** | Row number. |
| **Status** | Coloured dot — OK / Info / Warn / Fail / Critical. |
| **Check** | Name of the check + one-line helper. |
| **Category** | Backup, Configuration, … |
| **Score** | `X / 10`. |
| **Detail** | Current measured value or finding. |
| **Last Run** | When the row last ran. |
| **info button** | What the check does and why it matters. |
| **▶ Run** | Re-run just this check. |
| **🔧 Fix** | Apply the safe fix (when one exists). |

## Status meanings

* **OK** — full marks. Nothing to do.
* **Info** — informational; not a problem (e.g. *Recovery model is
  SIMPLE — log backups not required.*).
* **Warn** — degraded; investigate.
* **Fail** — the check failed (e.g. *Could not find stored procedure
  …*).
* **Critical** — the database is at material risk; fix immediately.

## What gets checked

A non-exhaustive list grouped by category — the on-screen catalogue is
the source of truth:

* **Backup** — last full / log backup age, backup-policy adequacy,
  drive free space, full / log schedule defined, file retention.
* **Configuration** — auto-shrink off, auto-close off, MAXDOP, cost
  threshold, recovery model.
* **Integrity** — days since DBCC CHECKDB, suspect pages, page-verify
  is CHECKSUM.
* **Maintenance** — stale statistics, high-impact missing indexes,
  unused indexes, Virtual Log File count, audit / log overage.
* **Operations** — failed Agent jobs in last 24 h, errorlog severe
  entries, long-running sessions.
* **Performance** — top wait type, buffer-cache hit ratio, TempDB
  contention.
* **Security** — login lockouts, dangerous surface area, `sa` enabled,
  weak SQL-login passwords, `xp_cmdshell` enabled.

## How fixes work

* **Safe fix** — non-destructive (e.g. update statistics, create a
  missing maintenance job, set a configuration option to its
  recommended value).
* **Destructive fix** — only ever triggered by clicking the per-row 🔧
  button explicitly (e.g. drop an unused index, purge audit rows
  older than retention). Confirmation is required.
* **No fix** — some checks (e.g. *Top wait type*) are informational
  only.

Every fix is logged with the user, timestamp, before-and-after value,
and the row it ran against — so a future auditor can trace what
changed.

➡ Continue to **[Run Backup](run-backup.md)**.
