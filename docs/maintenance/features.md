# Features

Every feature of the Maintenance module, grouped by what it lets you
do. Exhaustive but not technical — use it as a training checklist or
as a gap-analysis against another DBA console.

---

## 1. Database identity strip

* Database name.
* Server name.
* Data file path.
* Log file path.
* Backup folder.
* Last scan timestamp.

The strip is pinned at the top of every tab — you can never lose
track of which database you're acting on.

## 2. Toolbar actions

* **Backup Now** — open the Run Backup dialog.
* **Backup Schedule** — open the schedules list and editor.
* **Send Log** — generate the maintenance log and upload to Drive.
* **Settings** — module-wide settings (backup folder, retention).

## 3. Sidebar

The left sidebar is a fixed navigation tree:

* **Desktop** — the main KPIs + Checklist dashboard.
* **Backup**
    * **Backup Log** — every backup run, with type, date, size,
      status, target file.
* **Storage**
    * **Table Sizes** — live row count and size per table.
    * **Backup Log Report** — printable backup history report.
    * **Table Sizes Report** — printable table-size report.

## 4. Dashboard — two tabs

### KPIs tab

A tile-based dashboard arranged in coloured bands.

#### Band 1 — Live activity & performance

* Total DB size.
* Log file size.
* Backup disk free.
* TempDB size.
* Active sessions.
* Running requests.
* Blocked sessions.
* Buffer cache hit %.
* SQL Server CPU %.
* Batch requests / sec.
* Transactions / sec.
* Server memory used.

Tiles colour-code by health — green / yellow / red.

#### Band 2 — Backup

* Last backup age (e.g. *8m ago*, *2h ago*).
* Next scheduled backup (or *no schedules*).
* Backup folder size.
* Backup files count.
* **Policy (clinical)** — Adequate / Inadequate with reason.
* **Full schedule** — Configured / Missing.
* **Log schedule** — Configured / Missing / N/A (when recovery model is
  SIMPLE).

#### Band 3 — Licensing

* Licensed users (used / total).
* License serial.
* License expiry.
* Connected now (distinct logins).
* Active users (enabled accounts).
* Total users (including disabled).
* Last user login.

### Checklist tab

The 48-point scored checklist — the heart of the module.

* **Health Score** — single 0-100 figure at the top-right.
* **Scan All** — re-runs every check.
* **Run Safe Fixes** — applies every fix flagged as safe.
* **Refresh** — re-pulls the cached results without re-running.
* Category pills — **All · Backup · Configuration · Integrity ·
  Maintenance · Operations · Performance · Security**.
* Status pills — **Critical · OK · Warn · Fail · Info** with counts.
* One row per check with:
    * `#` row number.
    * **Status** — coloured dot.
    * **Check** — name and short helper text.
    * **Category**.
    * **Score** — `X / 10` per check.
    * **Detail** — current value and explanation.
    * **Last run** time.
    * **Info** — what this check does.
    * **▶ Run** — re-run just this check.
    * **🔧 Fix** — apply the safe fix (when available).

### Tab-level actions

* **Edit** — opens the dashboard template editor (admin only).
* **Refresh** — refresh the data.
* **Export** — export the current tab as a printable report.

## 5. Backup — Run Backup dialog

* **Backup Type** — FULL · DIFF · LOG.
* **Backup Folder** — pre-filled from Settings; can be overridden
  per-run.
* **Description** — free text label saved with the backup file.
* **Run Backup** — kicks the backup; a progress strip appears while it
  runs (*Running backup, please wait…*).
* **Close** — abandon.

Outputs land in the configured folder with a date-stamped file name
and immediately update the **Last Backup** KPI tile.

## 6. Backup — Schedules

### List

* **+ New Schedule** — create.
* **Refresh** — re-pull from disk.
* Empty state — *No backup schedules yet. Click 'New Schedule' to add
  one.*
* Per-row columns: Name, Type, Frequency, Start, Last Run, Last Status,
  Next Run, Active.
* Per-row actions: **Edit · Delete · Run this schedule now**.

### Editor

* **Identity**
    * Name.
    * Description.
* **What to back up**
    * Backup Type — FULL · DIFF · LOG.
    * Backup Folder.
* **When to run**
    * Frequency — **Hourly · Daily · Weekly · Monthly**.
    * Start Time (HH:MM).
    * Days of Week (Weekly).
    * Day of Month 1–31 (Monthly).
* **Active (will run on schedule)** — pause without deleting.
* **Save / Cancel**.

## 7. Health checks — what's measured

Across the seven categories the checklist covers (non-exhaustive — the
on-screen list is the source of truth):

### Backup
* Last full backup age.
* Last log backup age.
* Backup drive free space.
* Backup-policy adequacy for clinical use.
* Full schedule defined.
* Log backup schedule defined (when recovery FULL).
* Backup files retention.

### Configuration
* Auto-shrink disabled.
* Auto-close disabled.
* MAXDOP set.
* Cost threshold for parallelism.
* Recovery model fits the workload.

### Integrity
* Days since DBCC CHECKDB.
* Suspect pages clear.
* Page-verify is CHECKSUM.

### Maintenance
* Stale statistics.
* High-impact missing indexes.
* Unused indexes.
* Virtual log file count.
* Audit / log overage (rows older than retention).

### Operations
* Failed Agent jobs (24h).
* Errorlog severe entries.
* Long-running sessions.

### Performance
* Top wait type.
* Buffer cache hit ratio.
* TempDB contention.

### Security
* Logins locked (24h).
* Dangerous surface area.
* `sa` account enabled.
* Weak SQL-login passwords.
* `xp_cmdshell` enabled.

## 8. Score system

* Each check returns a **0–10 score**.
* Status is derived from the score: **OK** (full marks), **Info**
  (cosmetic), **Warn** (degraded), **Fail** (failing), **Critical**
  (broken).
* The **Health Score** is a weighted average across all categories, on
  a 0–100 scale.
* Scores are coloured — green / yellow / red — so a glance is enough.

## 9. Send Log — Maintenance Log report

* Generates a self-contained HTML file containing every KPI tile,
  every check, the backup history, the schedules list, and licensing.
* Uploads the file to the configured **Google Drive** folder.
* While uploading: *Generating and uploading…*.
* On success — *Uploaded to Google Drive* with **Open in Drive** and
  **Copy link** buttons.
* On failure — *Drive upload failed* with the diagnostic message
  (*Check Maintenance:LogUpload settings in appsettings.json and
  verify the Drive folder is shared with the service-account email.*).
* Useful for head-office reviews and audit trails — the link goes in
  the ticket.

## 10. Settings

* **Backup Folder (single source of truth)** — used by Backup Now,
  every scheduled backup, and the disk-free check. The folder must be
  writable by the SQL Server account; it is created if it does not
  exist.
* **Audit retention (days)** — purges audit rows older than this when
  the *Audit overage* check's fix runs.
* **Log retention (days)** — same idea for log rows.
* **Save / Close**.

## 11. Edit dashboard template (admin)

* The **Edit** button on the dashboard opens the underlying dashboard
  template editor.
* A timestamped `.bak` copy is saved before each write.
* The path the file lives at is displayed so an admin can open the
  file in a system editor too.
* After save, click **Reload now** in the dashboard to apply the
  changes without restarting HMS.

## 12. Reload from disk

* Force the module to re-read its dashboard definition from disk —
  useful after editing the template in an external editor.
* Toast feedback: *Saved at*, *Opened in*, *Loading…*.

## 13. Storage views

### Table Sizes (live)
* Per-table row count and size (data + index).
* Sortable.
* Drill into the table-sizes report for a printable version.

### Backup Log Report
* Printable history of every backup run — date, type, size, status,
  file name.
* Same data the **Backup Log** sidebar lists, formatted for
  distribution.

### Table Sizes Report
* Printable per-table size and growth report.

## 14. UI quality-of-life

* Top strip pinned across every screen — never lose database context.
* Tile colour-coding (green / yellow / red).
* Per-row info / run / fix buttons.
* Sidebar position and selected tab persist between sessions.
* Toast notifications for every long-running action.
* Loading spinners on every async fetch.
* **Refresh** buttons everywhere — never reload the page.
* Read-only mode when the user lacks the *Maintenance* role.
* Dark / light theme follows the HMS app theme.
* Localised — English / Arabic.

## 15. Safety guardrails

* **Run Safe Fixes** only applies fixes flagged as safe — destructive
  fixes (drop unused index, purge audit rows) always require an
  explicit per-row 🔧 click.
* Dashboard template edits create a `.bak` before each save.
* Backups respect the SQL Server account permission set — failures
  surface immediately with the OS error.
* Scheduled backups don't run if **Active** is unticked — pause
  without deleting.
* Backup folder is validated on Settings save — non-existent / read-only
  folders are rejected with a clear message.

## 16. Integration points

| Surface | Powered by |
|---|---|
| Backup / restore | SQL Server BACKUP / RESTORE |
| Health checks | SQL Server DMVs, `sys.*` catalog, msdb |
| Backup history | msdb backup tables + per-run audit |
| Drive upload | OAuth-based Drive API (service account, configured in `appsettings.json`) |
| Schedules | SQL Server Agent (Daily / Weekly / Monthly) and an in-app Hourly tick |
| Licensing tiles | HMS licensing service |
| Edit pencil on each page | Source markdown on GitHub |

➡ Back to **[Overview](index.md)** or **[Getting Started](getting-started.md)**.
