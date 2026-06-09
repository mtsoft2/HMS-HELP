# Getting Started

A typical first session — verify the backups are healthy, run a manual
backup, schedule the next one, and e-mail the maintenance log to head
office.

## 1. Confirm which database you're working with

Read the strip at the top:

* **Database** — name of the live database.
* **Server** — SQL Server instance.
* **Data File / Log File** — physical paths.
* **Backup Folder** — where backups go.
* **Last Scan** — when the health check last ran.

If anything looks wrong, **stop and verify** — every action on this
screen affects the database in the top strip.

## 2. Glance the KPIs

The **KPIs** tab gives you the database's health in three bands:

* **Live activity & performance** — total DB size, log file size,
  backup disk free, TempDB, sessions, requests, blocked sessions,
  buffer cache hit ratio, CPU, batch/sec, transactions/sec, server
  memory.
* **Backup** — last backup age, next scheduled, backup folder size,
  number of backup files, **policy compliance**, schedule status.
* **Licensing** — licensed seats, license serial, expiry, connected
  now, active users, total users, last user login.

Tiles in **red / yellow** are issues — click any tile to drill into
its checklist row.

## 3. Run the health checklist

Switch to the **Checklist** tab.

![Database Health Checklist with scoring and one-click fixes](screenshots/02-checklist.png)
/// caption
The **Database Health Checklist** — 48 checks across Backup,
Configuration, Integrity, Maintenance, Operations, Performance and
Security, each with a 0–10 score and one-click safe fix.
///

* Click **Scan All** to refresh every check. The **Health Score**
  (top-right) recomputes — out of 100.
* Click **Run Safe Fixes** to apply every fix that is known to be
  safe (creates missing maintenance jobs, updates stale statistics,
  purges old logs).
* Use the **category pills** (Backup, Configuration, Integrity,
  Maintenance, Operations, Performance, Security) and **status pills**
  (Critical, OK, Warn, Fail, Info) to narrow the list.

Per-row buttons:

* **info** — opens an explanation of what the check does and why
  it matters.
* **▶ Run** — re-runs just that check.
* **🔧 Fix** — applies the safe fix for that check (when one exists).

## 4. Run a manual backup

Click **Backup Now** in the toolbar.

![Run Backup dialog with FULL/DIFF/LOG choices](screenshots/03-run-backup.png)
/// caption
The **Run Backup** dialog — pick FULL, DIFF, or LOG, optionally add a
description, and click Run Backup.
///

* Pick the **Backup Type** — FULL, DIFF (differential), or LOG.
* The **Backup Folder** is pre-filled from Settings.
* Add an optional **Description** to label the file.
* Click **Run Backup**. A progress message appears; the backup is
  written to the folder and a new entry appears in the *Backup Log*
  sidebar entry.

## 5. Schedule recurring backups

Click **Backup Schedule**, then **+ New Schedule**.

![New Schedule dialog](screenshots/04-new-schedule.png)
/// caption
The **New Schedule** dialog — name, description, backup type, folder,
frequency (Hourly / Daily / Weekly / Monthly), start time, and the
*Active* toggle that decides whether the schedule actually runs.
///

* **Identity** — Name and Description.
* **What to back up** — FULL / DIFF / LOG, Backup Folder.
* **When to run** — Frequency (Hourly · Daily · Weekly · Monthly),
  Start Time (HH:MM).
* **Active (will run on schedule)** — tick to enable; untick to pause
  without deleting.

Click **Save**. The schedule appears in the list with **Last Run /
Next Run / Last Status** columns. Click **Run this schedule now** to
fire it on demand without waiting for the cron tick.

## 6. Send the maintenance log

Click **Send Log** in the toolbar.

The system generates an HTML file containing the same KPIs, checks,
backup history, and schedules you see on screen — then uploads it to
the configured Google Drive folder. When it finishes, a Drive link
appears with **Open in Drive** and **Copy link** buttons; share that
link with head office.

![Generated maintenance-log report](screenshots/05-maintenance-log.png)
/// caption
The generated **Maintenance Log** as it appears in Drive — KPIs,
licensing, live activity, backup, health-by-topic and the full
checklist on a single shareable page.
///

## 7. Done

The dashboard remembers the last tab you used (KPIs vs Checklist),
the sidebar position, and the export format. Future sessions open
where you left off.

➡ Continue to **[Features](features.md)** for the exhaustive list of
everything Maintenance can do.
