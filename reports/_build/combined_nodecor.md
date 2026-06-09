title: "HMS Help - Combined Manual"
subtitle: "End-User and Administrator Manual"
author: "MT Soft"
date: "2026-06-09"
toc: true
toc-depth: 3
toc-title: "Table of Contents"
\newpage

# HMS Help

End-User and Administrator Manual for every module in the HMS Hospital Management System.

Generated 2026-06-09.

Source: https://mtsoft2.github.io/HMS-HELP/

Repository: https://github.com/mtsoft2/HMS-HELP

\newpage

\newpage

## HMS Help

## HMS — Hospital Management System
End-user and administrator manual for every module in HMS. Pick a card below to jump in,
or use the search box (top right) to find a feature by name.

### 🆕 What's New

-  **UI Updates**
    Grid R3 spreadsheet-style upgrade, Mini Mode pickers, Patient Avatars on every banner.

    [ Open](ui-updates/index.md)

-  **Setup Wizard v2**
    New installer + patch flow with full patching history and one-click re-apply.

    [ Open](setup-wizard/index.md)

-  **Maintenance**
    Database health dashboard — KPIs, scored checklist with one-click fixes, backups, schedules, and Drive-shareable maintenance log.

    [ Open](maintenance/index.md)

-  **Report Server (V2)**
    Centralised report runner — browse, run, schedule, export.

    [ Open](report-server/index.md)

###  Dashboards

-  **Clinic Dashboard**
    Manager's home screen for one outpatient clinic — Overview, Schedule, Census, Billing, Physicians, Inventory, Quality, CRM.

    [ Open](clinic-dashboard/index.md)

-  **Patient Dashboard**
    The patient's lifetime summary — Profile, Clinical, Care Plan, Appointments, Lab, Imaging, History, Documents, Billing, Insurance.

    [ Open](patient-dashboard/index.md)

###  Clinical

-  **Dental Chart**
    Two-arch chairside chart with status / operation / root tools, six clinical overlays (Plan, Perio, Ortho, Caries, Endo/RG, Occlusion), snapshots & compare, demo mode.

    [ Open](dental-chart/index.md)

-  **Scheduler**
    Day / Week appointment grid with fingerprint find, drag-and-drop reschedule, conflict detection, bulk move.

    [ Open](scheduler/index.md)

-  **Clinic Reception**
    The front desk's one-window workspace — find, book, chart, prescribe, bill in 14 toolbar buttons.

    [ Open](adt-dc/index.md)

-  **Document Manager (DM2)**
    Unified viewer + gallery for every file type — images, PDF, Office, DICOM. Annotate, measure, compare.

    [ Open](dm2/index.md)

###  Integrations

-  **Metasoft Communicator**
    SMS / WhatsApp / e-mail outbound channel with queue, retries, alerts, full audit log.

    [ Open](communicator/index.md)

-  **NPHIES BridgeProxy**
    Saudi NPHIES e-claim submissions, status checks, and pre-authorisations.

    [ Open](bridgeproxy/index.md)

###  Back Office

-  **Human Resources**
    Full employee lifecycle — recruitment, contracts, leaves, appraisals, documents, end of service.

    [ Open](hr/index.md)

-  **Payroll**
    Pay codes, pay runs, registers, pay slips, staff loans.

    [ Open](hr/payroll/index.md)

###  Coming Soon

-  **Patient / Clinical**
    Visit forms, vitals, allergies, problem list, medications. *Coming soon.*

-  **Pharmacy / Inventory**
    Stock, dispensing, formulary, expiry tracking. *Coming soon.*

-  **Laboratory / Radiology**
    Orders, sample tracking, results, imaging studies. *Coming soon.*
### How to use this site
* Use the **top navigation tabs** to jump between modules.
* The **left sidebar** lists every page in the current module.
* The **search bar** (top right) searches the entire site.

### Conventions

| Term | Meaning |
|---|---|
| **Form (FT)** | A data-entry window — e.g. the Employee form. |
| **Search pad (ST)** | A list / search window — e.g. the Employees list. |
| **Grid (GT)** | A child table inside a form — e.g. the Salary history grid inside the Employee form. |
| **Binder (BND)** | The full-screen workspace with a toolbar + side menu — e.g. *Patient Affairs*. |
| **Lookup** | A simple reference table (Department, Position, Nationality, …) administered from the **Data Setup** menu. |

\newpage

###### Setup Wizard v2 — New HMS Setup Wizard (`Setup.exe`)

The **metaSOFT Setup Wizard v2** is the new, redesigned installer that
applies HMS patches to a customer database. It replaces the legacy
INI-driven installer with a guided five-step flow that validates the
database **before** touching it, applies the patch, and reports
every script with a per-script status.

![Welcome step](img/01-welcome.png)

###### What's new in v2

###### 1. Works without `Config.ini`

The wizard no longer requires `Config.ini` to be present. If a
`Config.ini` file *is* found in the install folder, the wizard
auto-loads the previous server / database / authentication values as
defaults — so re-installs are still one-click for support staff who
already configured the box.

###### 2. SQL Server instance selection

The **Server** field on the Database step is a dropdown of every SQL
Server instance discovered on the network. Type a host name to pick
something not in the list — named instances (`HOST\SQLEXPRESS`) and IP
addresses are both accepted.

###### 3. Authentication method selection

Pick either:

* **Windows Authentication** — uses the logged-in Windows account.
* **SQL Server Authentication** — enter a SQL login and password.

Stored procedures, tables, and trigger creation all use the chosen
account.

###### 4. Verify database connection **before** proceeding

The wizard pings the chosen server + database and lists how many
databases were found before letting you click Next. A green
*"Connected — N databases found"* badge confirms reach.

If the connection fails, the wizard stays on the Database step with
the specific error displayed — no half-applied patch can result.

###### 5. Verify required schema objects

After applying the patch, the wizard inspects `sys.objects` and
confirms that **every** expected procedure, function, table, and
trigger from the patch is present. The number shown on the Apply
screen — e.g. *"947 of 947 expected objects verified"* — is the
post-install integrity check.

###### 6. Comprehensive error report

All setup and validation errors — script failures, missing objects,
permission denials, version mismatches — are written to a single
comprehensive text file alongside the wizard. One file to attach to
a support ticket; no log hunting.

###### 7. Patch validation & reporting

The **Patching History** dialog opens from the Welcome step. It
shows every patch ever applied to the connected database **from the
last cumulative (-CM) patch onwards**, with per-patch:

* **Status** — *Applied*, *Error*, *MISSING*.
* **Date** — when the patch ran.
* **Version** — HMS version the patch belongs to.

A red banner at the top counts how many entries are tracked and how
many are **MISSING** — e.g. *"112 entries · 55 MISSING"* — instantly
showing whether the customer's database is up to date.

The wizard refuses to apply a new patch if a prerequisite cumulative
patch is missing, so the patch chain can never get out of order.

 Continue to **[Walkthrough](walkthrough.md)** for the five-step
guided run, or **[Patching History](patching-history.md)** for the
detail of the patch-status report.

\newpage

###### Walkthrough — Applying a Patch

The wizard is **five steps**, shown in the progress bar at the top of
every screen: **Welcome  Patch  Database  Apply  Finish**.

The lower-left corner shows the wizard version (e.g. *Version 1.1.0*).
The lower-right corner has **Cancel** at every step — safe to press
until step 4.
###### Step 1 — Welcome

![Welcome step](img/01-welcome.png)

The welcome card shows the patch the wizard is about to apply:

* **Patch #** — the patch number.
* **Date** — the patch's release date.
* **Size** — the patch payload size.

A reminder line under the card asks you to **close any open HMS
clients** before continuing — uncommitted edits on the patient form
or any other live screen are at risk during the patch.

The **Patching History** button at the bottom-left opens the patch-status
report against the current database — see
**[Patching History](patching-history.md)**.

Click **Get started** to move to Step 2.
###### Step 2 — Patch information

![Patch step](img/02-patch.png)

Two fields:

* **Install folder** — the on-disk HMS installation the patch is
  targeting (the wizard pre-fills the standard install path; click
  **Browse** to point at a different one).
* **What's new** — a scrollable preview of the release notes shipped
  with the patch. **Open** pops the same notes out into Notepad
  for easier reading.

Confirm the folder is correct and click **Next**.
###### Step 3 — Database connection

![Database step](img/03-database.png)

* **Install path** — read-only, carried forward from Step 2.
* **Server** — the SQL Server instance to patch. Pick from the
  dropdown (auto-discovered network instances) or type a host name
  / IP / named instance.
* **Authentication** — Windows or SQL Server. If SQL Server, the
  wizard expands to ask for user name and password.
* **Connect** — pings the server. On success the wizard fills the
  **Database** dropdown with every database found on that instance
  and shows a green badge — *"Connected — N databases found"*.
* **Database** — pick the customer database to patch.

The wizard refuses to leave this step until the connection is
green — preventing half-applied patches.

Click **Next** to move to the Apply step.
###### Step 4 — Apply patch

![Apply step](img/05-apply.png)

The wizard runs the patch in two phases:

1. **Run SQL scripts** — every script in the patch executes in order
   against the chosen database. Each script appears as a row in the
   table with its status — **DONE**, **VERIFIED**, or an error pill if
   it failed.
2. **Copy files to the HMS install folder** — DLLs, templates,
   reports.

When everything completes, a green summary at the top reads:

>  **Patch applied successfully.**
> All scripts executed and files copied. *N of N expected objects
> verified in sys.objects.*

The number reflects the post-install integrity check.

###### Filter the table

* **Show only errors** checkbox — hides every DONE / VERIFIED row so
  you can focus on what failed.

###### Action buttons (bottom of the screen)

* ** Previous** — go back to the Database step (only before Apply
  starts; once scripts are running the patch must finish or be
  cancelled).
* **Re-Verify** — re-inspect `sys.objects` against the expected list
  without re-running any scripts. Useful when a verification glitch
  was caused by a temporary lock.
* **Re-Apply** — re-runs the SQL scripts and re-copies the files.
  Safe — scripts are written to be idempotent.
* **Next ** — only enabled once the patch is successful.
* **Cancel** — abandons the patch.

Click **Next** to move to Step 5.
###### Step 5 — Finish

A short confirmation card shows the patch is applied and the wizard
exits. The customer database now reports the new patch in **Patching
History**.
###### What if a script fails?

The wizard does **not** silently continue.

* The failing row shows in red on the Apply table with the SQL error
  text inline.
* **Show only errors** lets you list every failure in one view.
* The comprehensive error file (saved next to the wizard) holds the
  full output for the support team.
* Press **Re-Apply** after fixing the underlying issue (permissions,
  missing prerequisite, etc.) — the wizard re-runs idempotently and
  moves past previously-applied scripts.

If the failure is a missing prerequisite cumulative patch, the
Patching History will surface that — see
**[Patching History](patching-history.md)**.

\newpage

###### Patching History

Open from the **Patching History** button on the Welcome step. The
dialog shows the patch trail for the connected database — every
patch that has been recorded since the **last cumulative (-CM)
patch**.

![Patching History dialog](img/04-patching-history.png)

###### Header

The grey banner at the top tells you at a glance:

* **Current patch** — the patch number of the wizard you launched
  (e.g. *"current patch 462"*).
* **Entries** — how many patch rows are tracked.
* **MISSING** count — how many of those rows are MISSING.

Example: *"112 entries · 55 MISSING"* — a database that has gone
through 112 patches' worth of script slots, but 55 of them never
recorded a successful install.

###### Columns

| Column | Meaning |
|---|---|
| **Patch** | The patch number. Patches that are cumulative end in **`-CM`** (e.g. `350-CM`). |
| **Status** | *Applied* (green), *Error* (red), or **MISSING** (red, no date). |
| **Date** | When the patch ran (blank if MISSING). |
| **Version** | The HMS version the patch belongs to (e.g. *HMS 23.00*). |

###### Status meanings

* **Applied** — the patch ran end-to-end successfully.
* **Error** — the patch ran but one or more scripts failed. The
  database is in an undefined state for that patch; rerun the
  wizard with that patch's installer.
* **MISSING** — the patch was never recorded as applied on this
  database. Either it has not been applied yet, or it was applied
  before the patch-tracking machinery existed.

###### Reading the report

Scroll through the list looking for **red rows**:

* A line of consecutive *Applied* greens means the database is
  healthy in that range.
* An **Error** row means that specific patch needs to be re-applied
  before the database is fully in sync.
* A **MISSING** row means an earlier patch in the chain was never
  recorded — chase that one first, because subsequent patches may
  have depended on its schema changes.

###### Why the report starts at the last CM

A cumulative patch consolidates every change up to its number into
a single, idempotent installer — running it brings any database up
to that version regardless of which intermediate patches were
applied or missed. So the history before the last `-CM` is
irrelevant: the `-CM` guarantees the baseline.

The report only lists patches **after** the last `-CM` because those
are the ones whose individual install status still matters.

###### Acting on the report

* **Many MISSING rows + an old `-CM`**  apply the most recent `-CM`
  cumulative patch first. That clears almost every MISSING in one
  go.
* **A few Error rows scattered**  re-apply each errored patch
  individually. The patch installers are idempotent — re-applying
  is safe.
* **MISSING rows with no Error rows**  the customer skipped a few
  patches. Apply them in order; later patches may need their schema
  changes.

###### Close

Click **Close** to return to the wizard's Welcome step. Nothing in
the report itself is editable — it is a read-only audit view.

\newpage

###### Features

Every Setup Wizard v2 feature, grouped by what it lets you do.
###### 1. Guided five-step flow

* **Welcome  Patch  Database  Apply  Finish** — progress visible
  at the top of every screen.
* **Previous / Next / Cancel** on every step (cancel safe up to
  Apply).
* **Get started** card on Welcome shows patch number, date, size,
  and a reminder to close open HMS clients first.
* **Patching History** is one click away from Welcome — no need to
  start the patch to know whether the database is up to date.

###### 2. Config-free install

* **Works without `Config.ini`** — no pre-configuration required.
* **Auto-loads `Config.ini`** if present — re-installs are still
  one-click.
* No registry footprint.

###### 3. Database targeting

* **SQL Server instance dropdown** — every instance discovered on
  the network.
* **Free-text typing** — host name, IP, or named instance
  (`HOST\SQLEXPRESS`).
* **Authentication selector** — Windows or SQL Server.
* **Connect button** — validates the choice before letting the
  wizard proceed.
* **Database dropdown** — populates from the connected instance
  with the count of databases found.
* **Green / red badge** confirms connection status with the specific
  error if it fails.

###### 4. Patch information

* **Install folder** — pre-filled with the standard path, override
  with Browse.
* **What's new** preview — scrollable inside the wizard, **Open**
  pops the notes out into Notepad.

###### 5. Safe application

* **Two-phase apply** — SQL scripts first, then file copy.
* **Per-script status row** — DONE / VERIFIED / Error visible during
  the run.
* **Show only errors** filter to focus on what failed.
* **Stops on first hard failure** — the wizard surfaces the error
  instead of soldiering on.
* **Idempotent scripts** — re-applying is safe.

###### 6. Post-install verification

* **Object count** — *"N of N expected objects verified in
  sys.objects"* shown when the patch completes.
* **Re-Verify** button — re-inspects the database without re-running
  scripts.
* **Re-Apply** button — full re-run (idempotent).

###### 7. Patch validation & history

* **Patching History** dialog — every recorded patch from the last
  cumulative (-CM) onwards.
* **Entries + MISSING counter** — one-line health summary
  (*"112 entries · 55 MISSING"*).
* **Per-patch status** — Applied / Error / MISSING with date and HMS
  version.
* **Prerequisite check** — the wizard refuses to apply a patch when a
  prerequisite cumulative patch is missing.

###### 8. Comprehensive error reporting

* **Single error file** — every setup and validation error from the
  run is written to one text file next to the wizard. Attach to
  support tickets in one click.
* **Per-script error text** inline on the Apply screen.
* **Database version mismatch** detection — flagged in the error
  file with the expected vs found version.

###### 9. Modern UI

* Clean dark-blue header on every step.
* Light step body with consistent spacing.
* Step numbers on the right (*"STEP N OF 5"*).
* metaSOFT HMS branding panel on the Welcome screen.
 Continue to **[Walkthrough](walkthrough.md)** for the step-by-step
run, or **[Patching History](patching-history.md)** for the patch
report.

\newpage

###### Maintenance Module

The **Maintenance** module is the DBA / site-administrator workspace —
the one screen where the person responsible for the database can see
its health, run a backup, schedule routine backups, run the safety
checklist, fix problems, and ship a complete report to head office.

It is built around two ideas:

* **One dashboard, full context.** The top strip pins the database
  identity (name, server, data + log file paths, backup folder, last
  scan) so you never have to ask *"which DB am I looking at?"*.
* **One checklist, scored.** Every database-health rule (backup,
  configuration, integrity, maintenance, operations, performance,
  security) is a row in one checklist with a colour, a score, an
  explanation, and — for almost every row — a one-click **safe fix**.

![Maintenance dashboard with KPIs](screenshots/01-kpis-dashboard.png)

*The Maintenance dashboard on the **KPIs** tab — live database health
overview, backup status, and licensing in one screen.*

###### How to open it

From the HMS main menu pick **Maintenance**. The module is restricted
to the **Maintenance / Supervisor** role; the *supervisor* badge in
the top-right confirms which role you're using.

###### The screen

* **Top strip** — Database, Server, Data File, Log File, Backup
  Folder, Last Scan.
* **Action toolbar** — *Backup Now · Backup Schedule · Send Log ·
  Settings*.
* **Sidebar** — Desktop · Backup (Backup Log) · Storage (Table Sizes,
  Backup Log Report, Table Sizes Report).
* **Main pane** — two tabs: **KPIs** and **Checklist**, with **Edit /
  Refresh / Export** controls on the right.

###### Two tabs

| Tab | What it shows |
|---|---|
| **KPIs** | Live database health, live activity, backup state, licensing — all as coloured tiles. |
| **Checklist** | The 48-point scored health checklist with one-click fixes. |

 Continue to **[Getting Started](getting-started.md)** or jump to
**[Features](features.md)**.

\newpage

###### Getting Started

A typical first session — verify the backups are healthy, run a manual
backup, schedule the next one, and e-mail the maintenance log to head
office.

###### 1. Confirm which database you're working with

Read the strip at the top:

* **Database** — name of the live database.
* **Server** — SQL Server instance.
* **Data File / Log File** — physical paths.
* **Backup Folder** — where backups go.
* **Last Scan** — when the health check last ran.

If anything looks wrong, **stop and verify** — every action on this
screen affects the database in the top strip.

###### 2. Glance the KPIs

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

###### 3. Run the health checklist

Switch to the **Checklist** tab.

![Database Health Checklist with scoring and one-click fixes](screenshots/02-checklist.png)

*The **Database Health Checklist** — 48 checks across Backup,
Configuration, Integrity, Maintenance, Operations, Performance and
Security, each with a 0–10 score and one-click safe fix.*

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
* ** Run** — re-runs just that check.
* ** Fix** — applies the safe fix for that check (when one exists).

###### 4. Run a manual backup

Click **Backup Now** in the toolbar.

![Run Backup dialog with FULL/DIFF/LOG choices](screenshots/03-run-backup.png)

*The **Run Backup** dialog — pick FULL, DIFF, or LOG, optionally add a
description, and click Run Backup.*

* Pick the **Backup Type** — FULL, DIFF (differential), or LOG.
* The **Backup Folder** is pre-filled from Settings.
* Add an optional **Description** to label the file.
* Click **Run Backup**. A progress message appears; the backup is
  written to the folder and a new entry appears in the *Backup Log*
  sidebar entry.

###### 5. Schedule recurring backups

Click **Backup Schedule**, then **+ New Schedule**.

![New Schedule dialog](screenshots/04-new-schedule.png)

*The **New Schedule** dialog — name, description, backup type, folder,
frequency (Hourly / Daily / Weekly / Monthly), start time, and the
*Active* toggle that decides whether the schedule actually runs.*

* **Identity** — Name and Description.
* **What to back up** — FULL / DIFF / LOG, Backup Folder.
* **When to run** — Frequency (Hourly · Daily · Weekly · Monthly),
  Start Time (HH:MM).
* **Active (will run on schedule)** — tick to enable; untick to pause
  without deleting.

Click **Save**. The schedule appears in the list with **Last Run /
Next Run / Last Status** columns. Click **Run this schedule now** to
fire it on demand without waiting for the cron tick.

###### 6. Send the maintenance log

Click **Send Log** in the toolbar.

The system generates an HTML file containing the same KPIs, checks,
backup history, and schedules you see on screen — then uploads it to
the configured Google Drive folder. When it finishes, a Drive link
appears with **Open in Drive** and **Copy link** buttons; share that
link with head office.

![Generated maintenance-log report](screenshots/05-maintenance-log.png)

*The generated **Maintenance Log** as it appears in Drive — KPIs,
licensing, live activity, backup, health-by-topic and the full
checklist on a single shareable page.*

###### 7. Done

The dashboard remembers the last tab you used (KPIs vs Checklist),
the sidebar position, and the export format. Future sessions open
where you left off.

 Continue to **[Features](features.md)** for the exhaustive list of
everything Maintenance can do.

\newpage

###### Features

Every feature of the Maintenance module, grouped by what it lets you
do. Exhaustive but not technical — use it as a training checklist or
as a gap-analysis against another DBA console.
###### 1. Database identity strip

* Database name.
* Server name.
* Data file path.
* Log file path.
* Backup folder.
* Last scan timestamp.

The strip is pinned at the top of every tab — you can never lose
track of which database you're acting on.

###### 2. Toolbar actions

* **Backup Now** — open the Run Backup dialog.
* **Backup Schedule** — open the schedules list and editor.
* **Send Log** — generate the maintenance log and upload to Drive.
* **Settings** — module-wide settings (backup folder, retention).

###### 3. Sidebar

The left sidebar is a fixed navigation tree:

* **Desktop** — the main KPIs + Checklist dashboard.
* **Backup**
    * **Backup Log** — every backup run, with type, date, size,
      status, target file.
* **Storage**
    * **Table Sizes** — live row count and size per table.
    * **Backup Log Report** — printable backup history report.
    * **Table Sizes Report** — printable table-size report.

###### 4. Dashboard — two tabs

###### KPIs tab

A tile-based dashboard arranged in coloured bands.

###### Band 1 — Live activity & performance

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

###### Band 2 — Backup

* Last backup age (e.g. *8m ago*, *2h ago*).
* Next scheduled backup (or *no schedules*).
* Backup folder size.
* Backup files count.
* **Policy (clinical)** — Adequate / Inadequate with reason.
* **Full schedule** — Configured / Missing.
* **Log schedule** — Configured / Missing / N/A (when recovery model is
  SIMPLE).

###### Band 3 — Licensing

* Licensed users (used / total).
* License serial.
* License expiry.
* Connected now (distinct logins).
* Active users (enabled accounts).
* Total users (including disabled).
* Last user login.

###### Checklist tab

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
    * ** Run** — re-run just this check.
    * ** Fix** — apply the safe fix (when available).

###### Tab-level actions

* **Edit** — opens the dashboard template editor (admin only).
* **Refresh** — refresh the data.
* **Export** — export the current tab as a printable report.

###### 5. Backup — Run Backup dialog

* **Backup Type** — FULL · DIFF · LOG.
* **Backup Folder** — pre-filled from Settings; can be overridden
  per-run.
* **Description** — free text label saved with the backup file.
* **Run Backup** — kicks the backup; a progress strip appears while it
  runs (*Running backup, please wait…*).
* **Close** — abandon.

Outputs land in the configured folder with a date-stamped file name
and immediately update the **Last Backup** KPI tile.

###### 6. Backup — Schedules

###### List

* **+ New Schedule** — create.
* **Refresh** — re-pull from disk.
* Empty state — *No backup schedules yet. Click 'New Schedule' to add
  one.*
* Per-row columns: Name, Type, Frequency, Start, Last Run, Last Status,
  Next Run, Active.
* Per-row actions: **Edit · Delete · Run this schedule now**.

###### Editor

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

###### 7. Health checks — what's measured

Across the seven categories the checklist covers (non-exhaustive — the
on-screen list is the source of truth):

###### Backup
* Last full backup age.
* Last log backup age.
* Backup drive free space.
* Backup-policy adequacy for clinical use.
* Full schedule defined.
* Log backup schedule defined (when recovery FULL).
* Backup files retention.

###### Configuration
* Auto-shrink disabled.
* Auto-close disabled.
* MAXDOP set.
* Cost threshold for parallelism.
* Recovery model fits the workload.

###### Integrity
* Days since DBCC CHECKDB.
* Suspect pages clear.
* Page-verify is CHECKSUM.

###### Maintenance
* Stale statistics.
* High-impact missing indexes.
* Unused indexes.
* Virtual log file count.
* Audit / log overage (rows older than retention).

###### Operations
* Failed Agent jobs (24h).
* Errorlog severe entries.
* Long-running sessions.

###### Performance
* Top wait type.
* Buffer cache hit ratio.
* TempDB contention.

###### Security
* Logins locked (24h).
* Dangerous surface area.
* `sa` account enabled.
* Weak SQL-login passwords.
* `xp_cmdshell` enabled.

###### 8. Score system

* Each check returns a **0–10 score**.
* Status is derived from the score: **OK** (full marks), **Info**
  (cosmetic), **Warn** (degraded), **Fail** (failing), **Critical**
  (broken).
* The **Health Score** is a weighted average across all categories, on
  a 0–100 scale.
* Scores are coloured — green / yellow / red — so a glance is enough.

###### 9. Send Log — Maintenance Log report

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

###### 10. Settings

* **Backup Folder (single source of truth)** — used by Backup Now,
  every scheduled backup, and the disk-free check. The folder must be
  writable by the SQL Server account; it is created if it does not
  exist.
* **Audit retention (days)** — purges audit rows older than this when
  the *Audit overage* check's fix runs.
* **Log retention (days)** — same idea for log rows.
* **Save / Close**.

###### 11. Edit dashboard template (admin)

* The **Edit** button on the dashboard opens the underlying dashboard
  template editor.
* A timestamped `.bak` copy is saved before each write.
* The path the file lives at is displayed so an admin can open the
  file in a system editor too.
* After save, click **Reload now** in the dashboard to apply the
  changes without restarting HMS.

###### 12. Reload from disk

* Force the module to re-read its dashboard definition from disk —
  useful after editing the template in an external editor.
* Toast feedback: *Saved at*, *Opened in*, *Loading…*.

###### 13. Storage views

###### Table Sizes (live)
* Per-table row count and size (data + index).
* Sortable.
* Drill into the table-sizes report for a printable version.

###### Backup Log Report
* Printable history of every backup run — date, type, size, status,
  file name.
* Same data the **Backup Log** sidebar lists, formatted for
  distribution.

###### Table Sizes Report
* Printable per-table size and growth report.

###### 14. UI quality-of-life

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

###### 15. Safety guardrails

* **Run Safe Fixes** only applies fixes flagged as safe — destructive
  fixes (drop unused index, purge audit rows) always require an
  explicit per-row  click.
* Dashboard template edits create a `.bak` before each save.
* Backups respect the SQL Server account permission set — failures
  surface immediately with the OS error.
* Scheduled backups don't run if **Active** is unticked — pause
  without deleting.
* Backup folder is validated on Settings save — non-existent / read-only
  folders are rejected with a clear message.

###### 16. Integration points

| Surface | Powered by |
|---|---|
| Backup / restore | SQL Server BACKUP / RESTORE |
| Health checks | SQL Server DMVs, `sys.*` catalog, msdb |
| Backup history | msdb backup tables + per-run audit |
| Drive upload | OAuth-based Drive API (service account, configured in `appsettings.json`) |
| Schedules | SQL Server Agent (Daily / Weekly / Monthly) and an in-app Hourly tick |
| Licensing tiles | HMS licensing service |
| Edit pencil on each page | Source markdown on GitHub |

 Back to **[Overview](index.md)** or **[Getting Started](getting-started.md)**.

\newpage

###### KPIs Dashboard

The default tab in Maintenance — every important number about the
database, on a single screen, refreshed live.

![Maintenance KPIs dashboard](../screenshots/01-kpis-dashboard.png)

*The KPIs tab. Top strip pins the database identity; the toolbar
exposes Backup Now / Backup Schedule / Send Log / Settings; the
sidebar offers Backup Log and the storage reports.*

###### How it is organised

Three colour-coded bands:

###### Live activity & performance

| Tile | What it means |
|---|---|
| **Total DB size** | Combined data-file size. |
| **Log file size** | Transaction-log file size. |
| **Backup disk free** | Space left on the disk that hosts the backup folder. |
| **TempDB size** | Total TempDB data + log. |
| **Active sessions** | Logged-in sessions right now. |
| **Running requests** | Requests executing this moment. |
| **Blocked sessions** | Sessions blocked by another. |
| **Buffer cache hit %** | Percentage of reads served from RAM. |
| **SQL Server CPU %** | CPU consumed by SQL Server. |
| **Batch requests / sec** | Average since startup. |
| **Transactions / sec** | Average since startup. |
| **Server memory used** | RAM used by SQL Server right now. |

###### Backup

| Tile | What it means |
|---|---|
| **Last backup** | Time since the most recent backup (e.g. *8m ago*). |
| **Next scheduled** | When the next scheduled backup will run, or *no schedules*. |
| **Backup folder size** | Total size of files currently in the backup folder. |
| **Backup files** | Number of backup files in that folder. |
| **Policy (clinical)** | Whether the backup setup meets the clinical-use policy. *Inadequate* shows the reason. |
| **Full schedule** | *Configured* or *Missing*. |
| **Log schedule** | *Configured* / *Missing* / *N/A* (when the database uses SIMPLE recovery, log backups are not applicable). |

###### Licensing

| Tile | What it means |
|---|---|
| **Licensed users** | Used vs total seats. |
| **License serial** | The product key currently active. |
| **License expiry** | The renewal date. |
| **Connected now** | Distinct sessions logged in right now. |
| **Active users** | Enabled user accounts. |
| **Total users** | Including disabled. |
| **Last user login** | Most recent successful login. |

###### Reading the colours

* **Green** — healthy / within target.
* **Yellow** — degraded but not failing (e.g. backup disk close to
  full).
* **Red** — failing / policy non-compliant.

###### Actions on this tab

Top-right:

* **Edit** — open the dashboard template editor (admin only).
* **Refresh** — re-pull the KPI values.
* **Export** — export the current dashboard as a printable report.

###### Drill-down

Click any tile to open the underlying detail — most tiles jump to the
matching row in the **Checklist** tab; the licensing tiles jump to the
users / licenses screen.

 Continue to **[Health Checklist](health-checklist.md)**.

\newpage

###### Health Checklist

The **Checklist** tab is the heart of the Maintenance module — every
database-health rule on one scored list, with one-click fixes for the
safe ones.

![Database Health Checklist](../screenshots/02-checklist.png)

*The **Database Health Checklist**. The Health Score (top-right) is a
weighted 0-100 figure over every check. Use the category and status
pills to narrow down; click the wrench on a row to apply its safe fix.*

###### The header

| Control | What it does |
|---|---|
| **Health Score** | A single 0-100 figure summarising every check. Coloured ring around the number tells you at a glance. |
| **Scan All** | Re-runs every check. Updates the score. |
| **Run Safe Fixes** | Applies the safe fix for every row that has one — non-destructive, audit-logged. |
| **Refresh** | Re-pull cached results without re-running. |

###### Filters

Two rows of pills above the list:

* **Category pills** — *All · Backup · Configuration · Integrity ·
  Maintenance · Operations · Performance · Security*.
* **Status pills** — *Critical · OK · Warn · Fail · Info* with the
  count for each.

Click a pill to toggle filtering. Multiple status pills can be active
at once.

###### The list

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
| ** Run** | Re-run just this check. |
| ** Fix** | Apply the safe fix (when one exists). |

###### Status meanings

* **OK** — full marks. Nothing to do.
* **Info** — informational; not a problem (e.g. *Recovery model is
  SIMPLE — log backups not required.*).
* **Warn** — degraded; investigate.
* **Fail** — the check failed (e.g. *Could not find stored procedure
  …*).
* **Critical** — the database is at material risk; fix immediately.

###### What gets checked

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

###### How fixes work

* **Safe fix** — non-destructive (e.g. update statistics, create a
  missing maintenance job, set a configuration option to its
  recommended value).
* **Destructive fix** — only ever triggered by clicking the per-row 
  button explicitly (e.g. drop an unused index, purge audit rows
  older than retention). Confirmation is required.
* **No fix** — some checks (e.g. *Top wait type*) are informational
  only.

Every fix is logged with the user, timestamp, before-and-after value,
and the row it ran against — so a future auditor can trace what
changed.

 Continue to **[Run Backup](run-backup.md)**.

\newpage

###### Run Backup

Click **Backup Now** in the toolbar to open the Run Backup dialog.

![Run Backup dialog](../screenshots/03-run-backup.png)

*The **Run Backup** dialog — pick FULL, DIFF, or LOG, confirm the
backup folder, add a description, and click Run Backup.*

###### Fields

* **Backup Type** — three buttons, mutually exclusive:
    * **FULL** — complete backup of the database. Use as the baseline
      from which DIFF and LOG backups recover.
    * **DIFF** — differential. Captures everything changed since the
      last FULL. Smaller and faster.
    * **LOG** — transaction-log backup. Only valid when the database
      is in FULL recovery model.
* **Backup Folder** — pre-filled from Settings (single source of
  truth). Can be overridden for this one run.
* **Description** — optional free text. Stored in the backup metadata.

###### Run

Click **Run Backup**. A progress strip appears: *Running backup,
please wait…*.

When the backup finishes:

* The file is written to the folder.
* The **Last Backup** KPI tile updates immediately.
* A new entry appears in the **Backup Log** sidebar item.
* A toast confirms success.

If the backup fails the dialog shows the SQL error and the *Last
Status* column on the Backup Log marks it **Failed**.

###### When to use which type

| Type | When |
|---|---|
| **FULL** | At least once a day for clinical databases. Before a major upgrade. After a successful restore drill. |
| **DIFF** | Several times a day to shorten the restore chain. |
| **LOG** | Every 15-60 minutes when the database is in FULL recovery to limit RPO (data loss window). |

###### Tips

* The folder must be writable by the **SQL Server account**, not just
  the user running HMS — if it can't write, the backup fails with a
  permission error.
* Use **Description** to mark special backups (*Pre-upgrade*,
  *End-of-month*, *Migration*) so they stand out in the Backup Log.
* Run **Backup Now** before a risky operation — restoring a DIFF that
  was taken five minutes ago beats restoring last night's FULL.

 Continue to **[Backup Schedules](backup-schedules.md)**.

\newpage

###### Backup Schedules

Click **Backup Schedule** in the toolbar to open the schedules list.
A schedule fires a backup on a recurring cadence without anyone having
to click *Backup Now*.

###### The list

* **+ New Schedule** — create.
* **Refresh** — re-pull from disk.
* Empty state — *No backup schedules yet. Click 'New Schedule' to add
  one.*

Per-row columns:

* **Name**.
* **Type** — FULL / DIFF / LOG.
* **Frequency** — Hourly / Daily / Weekly / Monthly.
* **Start** — start time (HH:MM).
* **Last Run** — when it last fired.
* **Last Status** — Saved / Failed / —.
* **Next Run** — when it will fire next.
* **Active** — green dot if running on schedule.

Per-row actions:

* **Edit** — open the editor.
* **Delete** — remove the schedule (with confirm).
* **Run this schedule now** — fire on demand without waiting for the
  cron tick.

###### The editor

![New Schedule dialog](../screenshots/04-new-schedule.png)

*The **New Schedule** dialog. Five sections — Identity, What to back
up, When to run, frequency-specific fields, and the *Active* toggle.*

###### Identity

* **Name** — short label that appears in the list. Required.
* **Description** — free text.

###### What to back up

* **Backup Type** — FULL / DIFF / LOG.
* **Backup Folder** — locked to the central folder from Settings.
  Single source of truth; all schedules use the same folder.

###### When to run

* **Frequency** — Hourly · Daily · Weekly · Monthly.
* **Start Time** — HH:MM (24-hour clock).
* Frequency-specific extra:
    * **Weekly**  *Days of Week* — tick which weekdays.
    * **Monthly**  *Day of Month (1-31)*.
    * **Hourly** / **Daily**  no extra fields.

###### Active (will run on schedule)

* Tick to enable. Untick to pause without deleting.

###### Save / Cancel

Save commits the schedule and registers the corresponding SQL Server
Agent job (Daily / Weekly / Monthly) or in-app tick (Hourly). Cancel
abandons changes.

###### Patterns

| Goal | Suggested schedules |
|---|---|
| Clinical database, low write volume | FULL daily 02:00 + LOG every 30 min during business hours |
| Clinical database, high write volume | FULL daily + DIFF every 6 h + LOG every 15 min |
| Reporting copy, off-hours updates | FULL weekly Sunday 03:00 |
| Pre-upgrade snapshot | Run **Backup Now** with FULL + a descriptive Description; no schedule needed |

###### Common pitfalls

* **Active unticked** — schedules don't fire. Check the green dot.
* **Backup folder unwritable** — every run fails with the same error.
  Fix the OS permission on the folder.
* **No FULL backup yet** — DIFF and LOG schedules need a FULL baseline.
  Run **Backup Now** with FULL once before relying on DIFF/LOG
  schedules.
* **Recovery model is SIMPLE** — LOG schedules will be marked N/A.
  Switch the database to FULL recovery if you need log backups.

 Continue to **[Send Log](send-log.md)**.

\newpage

###### Send Log

Click **Send Log** in the toolbar to generate a shareable maintenance
report and upload it to Google Drive.

###### What it generates

A self-contained HTML file with everything an off-site auditor or
head-office DBA needs to review the site's health — all on one
scrollable page.

![Generated maintenance-log report](../screenshots/05-maintenance-log.png)

*The **Maintenance Log** as rendered on Drive. Sections from top to
bottom: identity strip, KPIs (Database Health Overview), Live activity
& performance, Backup, Licensing, Health by topic, and the full
Database Health Checklist.*

###### Sections

1. **Title strip** — Maintenance Log, database, server, generated
   timestamp.
2. **Licensing** — customer, license expiry, connected now, active
   users.
3. **KPIs**
    * Database Health Overview (counters per category).
    * Live activity & performance.
    * Backup.
    * Licensing.
4. **Health by topic** — one tile per category with the OK / total
   score.
5. **Database Health Checklist** — every check with status, score,
   detail and last-run timestamp.

The output is fully styled and prints cleanly to A4.

###### Flow

1. Click **Send Log**. The button shows *Generating and uploading…*.
2. The system writes the HTML file and uploads it to the Google Drive
   folder configured in **Maintenance  Settings**.
3. On success — *Uploaded to Google Drive* — the result panel shows:
    * **Open in Drive** — opens the file in a new browser tab.
    * **Copy link** — copies the share-link to your clipboard.
4. Share that link in the ticket / e-mail thread.

###### When it fails

If the upload fails the panel shows *Drive upload failed* with the
diagnostic text:

> *Check Maintenance:LogUpload settings in appsettings.json and verify
> the Drive folder is shared with the service-account email.*

Typical causes:

* The configured Drive folder has not been shared with the
  service-account e-mail.
* The OAuth refresh token in `appsettings.json` has expired.
* The site has no outbound network access to Google APIs.
* The configured folder ID is wrong.

###### When to use it

* **Routine reporting** — weekly / monthly snapshot for head office.
* **Incident ticket** — send the log link with the ticket so support
  sees the full health picture without dialling in.
* **Pre-upgrade** — generate before a major upgrade for an immutable
  record of the pre-change state.
* **Audit** — attach the link to the audit trail.

 Continue to **[Settings](settings.md)**.

\newpage

###### Settings

Click **Settings** in the toolbar to open the Maintenance Settings
dialog. Three short fields that affect every other screen.

###### Backup Folder (single source of truth)

The directory every Maintenance backup writes to:

* Used by **Backup Now**.
* Used by every **Scheduled backup**.
* Used by the **Backup disk free** KPI tile.
* Used by the **Backup drive free space** checklist row.

Rules:

* The folder must be writable by the **SQL Server account**, not the
  Windows user running HMS. SQL Server writes the backup file itself.
* If the folder does not exist, the system creates it on first save.
* Changing the folder does not move existing files — old files stay
  where they are.

###### Audit retention (days)

The maximum age (in days) of audit rows before the *Audit / log
overage* check on the **Checklist** considers them excess.

* Affects two tables: **SEC_Log** and **SEC_PasswordLog**.
* The matching safe fix purges rows older than this limit.

###### Log retention (days)

Same concept for application-log rows.

* Affects two tables: **DBHealth_History** and **Backup_Run**.

###### Save / Close

* **Save** persists the settings to the central configuration file and
  refreshes every dependent KPI tile.
* **Close** abandons changes.

###### Where these settings live

The settings are stored centrally — change them once and every
schedule, every backup, every KPI tile and every checklist row picks
up the new values without a restart.

 Continue to **[Backup Log](backup-log.md)**.

\newpage

###### Backup Log

The **Backup Log** sidebar item opens the audit list of every backup
ever taken on this database — manual or scheduled.

###### What you see

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

###### Filters

* By type — FULL / DIFF / LOG.
* By status — Saved / Failed.
* By date range.

###### Actions

* **Refresh** — re-pull the list.
* Per-row click  opens the folder containing the file.
* **Backup Log Report** (Storage  Backup Log Report) — printable
  version for distribution.

###### Tips

* Use **Description** when you take a backup before a risky change —
  it becomes the searchable label in the log.
* The log keeps every entry forever — the **Audit / log overage**
  checklist row + safe fix is how you purge old rows. Default
  retention is set in Settings.

 Continue to **[Storage & Reports](storage-and-reports.md)**.

\newpage

###### Storage & Reports

The **Storage** branch of the sidebar groups three table / file
oriented views.

###### Table Sizes (live)

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

###### Use cases

* **Capacity planning** — which tables are growing fastest?
* **Index audit** — when *Index size* > *Data size*, the table likely
  has unused indexes (cross-reference with the **Unused indexes**
  checklist row).
* **Archive candidates** — old audit / log tables often top this list
  and are good candidates for the retention purge.

###### Backup Log Report

Printable version of the **Backup Log** sidebar item. Same data, A4
layout, branded header, ready to attach to an audit ticket or
e-mail.

* Pick a date range.
* Group by Day / Week / Month.
* Filter by Type / Status.
* Export to PDF or print directly.

###### Table Sizes Report

Printable version of **Table Sizes**.

* Snapshot at the moment you run it.
* Grouped by schema.
* Highlights the top 20 tables by size.
* Export to PDF or print directly.

###### Tips

* Run **Table Sizes Report** monthly and keep the PDFs — comparing
  reports across months is the cleanest way to see growth trends.
* The two reports share the dashboard's print stylesheet, so they
  match the branding of the rest of HMS automatically.

 Back to **[Overview](../index.md)**.

\newpage

#### UI Updates

System-wide UI improvements that touch every screen in HMS — not tied
to any one module. Three big ones in this release:

| Update | What changes | Page |
|---|---|---|
| **Grid R3** | Every data grid in HMS gets a spreadsheet-style overhaul — sticky headers, fullscreen, keyboard navigation, sortable / hideable / reorderable columns, footer totals, row density, and more. | [Open](grid-r3.md) |
| **Mini Mode** | A compact layout for selection popups and search views — faster, less cluttered, optimised for picker workflows and smaller screens. | [Open](mini-mode.md) |
| **Patient Avatar** | Circular patient photos on binder headers and patient forms — with one-click camera capture and large preview. | [Open](patient-avatar.md) |

These updates apply **everywhere** in the system. Once installed, you
will see them in every clinic, every binder, every module that uses
grids, pickers, or shows the patient banner.

\newpage

#### Grid R3 — Enhancements & Usability Improvements

Every data grid in HMS gets a top-to-bottom overhaul in **Grid R3**.
The result is a grid that behaves like a modern spreadsheet —
faster keyboard entry, better visibility for big datasets, flexible
column management, and improved fullscreen usability.

##### Layout & Visibility

* **Sticky headers while scrolling** — column headers remain visible
  when scrolling long or maximised grids.
* **Fullscreen / maximise mode** — expand the grid to fill the entire
  screen, then restore it back instantly.
* **Search-as-you-type filtering** — quickly filter rows using the
  built-in search box.
* **Loading & empty states**
    * **Loading spinner** appears while data is being fetched.
    * Empty grids display a clean **“No Records Found”** message
      instead of a blank area.

##### Column Features

###### Show / hide columns

* **Right-click the grid header** to choose which columns are visible.
* Column visibility preferences are remembered per user.

###### Column reordering

* **Drag and drop column headers** to rearrange columns.

###### Parent / grouped headers

* Related columns can appear under a shared parent caption such as:
    * **Pricing**
    * **Tax**
    * **Patient Information**

###### Column sorting

* **Click once**  Ascending.
* **Click again**  Descending.
* **Click a third time**  Clear sorting.
* Active sort direction is shown with an arrow indicator.

###### Footer summaries

* Footer rows can display **totals and sums** for selected numeric
  columns.

##### Row Features

###### Row number column (#)

* Every grid now includes a fixed **row-number column** on the left
  side.
* The footer of the # column displays the **total number of records**.

###### Row density / resize modes

* Switch between:
    * **Compact**
    * **Normal**
    * **Comfortable**
* Preferences are automatically saved and restored.

###### Duplicate row

* **Right-click any row** and choose **Duplicate** to insert a new row
  containing the same values as the selected row.

##### Editing & Keyboard Navigation

###### Single-click editing

* Click any cell and start typing immediately — **no double-click
  required**.
* New typing automatically **replaces** the existing value.

###### Spreadsheet-style keyboard navigation

| Key | Action |
|---|---|
| **Tab / ** | Move forward |
| **Shift + Tab / ** | Move backward |
| ** / ** | Move vertically |
| **Enter** | Move to the first editable cell in the next row |

###### Automatic row creation

Pressing **Enter** on the last row automatically creates a new row and
moves focus into it.

###### Selected cell highlighting

The active cell is **visually highlighted** at all times.

###### Auto-select existing text

When entering a cell, the **current text is automatically selected**
so typing immediately replaces it.

###### Read-only cells

Read-only cells are **skipped automatically** during keyboard
navigation.

##### Toolbar Improvements

* **Show / hide toolbar buttons** — right-click the toolbar to choose
  visible buttons.
* **Modern icon toolbar** — toolbar buttons now use cleaner, simplified
  icons for a more modern appearance.

##### Overall Experience

The grid now behaves much more like a modern spreadsheet application,
offering:

* **Faster keyboard-based editing**
* **Better visibility for large datasets**
* **Flexible column management**
* **Improved fullscreen usability**
* **Faster navigation and data entry workflows**

\newpage

#### Mini Mode — Compact Selection Popups & Search

**Mini Mode** is a compact layout for selection popups and search
views — cleaner, faster, optimised for picker workflows and smaller
screens.

##### Where it applies

* **Selection popups** — every "pick a record" dialog (pick a patient,
  pick a doctor, pick an item, …).
* **Search views** — the searchable list windows behind the pickers.

##### How to enable it

* **System-wide as a user preference** — toggle the **Mini Mode** icon
  in the toolbar.
* Once enabled, every selection popup automatically switches to a
  **compact Mini Mode** version of the search view.
* Toggle back any time — the choice is remembered per user.

##### What you get in Mini Mode

###### Cleaner, more compact layout

The popup is sized for **fast selection on smaller screens** — less
chrome, more results, less scrolling.

###### Hidden clutter

* **Advanced icons** are hidden.
* **Secondary actions** are hidden.
* **Less frequently used controls** are hidden.
* Only the controls a user actually needs to *pick a record* stay
  visible.

###### Unified Quick Search box

One search box searches across the **most critical fields** at once:

* Patient Name
* MRN
* Phone Number
* Arabic Name
* ID Number

Type once  all five fields are matched simultaneously.

###### Quick filter pills / tags

Filters remain available as **quick pills / tags** at the top of the
popup — click any pill to narrow the results without opening the
advanced search panel.

###### History menu

The popup includes a **History menu** that displays the **last 10
selections** — one click to reuse a record you just picked. Ideal for
repetitive workflows (e.g. taking five payments from the same patient
in a row).

##### Why use Mini Mode

* **Faster pick** — Quick Search + History menu eliminates most clicks.
* **Less screen real-estate** — works comfortably on laptops, tablets,
  and wall-display kiosks.
* **Less cognitive load** — advanced controls are tucked away; only
  what you need is visible.

If you regularly use pickers (front desk, scheduler, cashier), Mini
Mode is the recommended default.

\newpage

#### Patient Avatar Integration

Circular **patient avatars** are now shown on binder headers and
patient forms throughout HMS. A photo lives with every patient record
and surfaces wherever the patient banner appears.

##### Where you see it

* **Binder headers** — every binder that shows a selected patient gets
  a circular avatar to the left of the patient name and case number.
* **Patient forms** — the patient edit form shows the same avatar
  prominently at the top.

##### Interactions

###### Empty avatar

* Shown as a placeholder circle with a **“+” badge** indicating that
  a photo can be uploaded.
* **Click an empty avatar**  opens the camera dialog for **immediate
  photo capture**.

###### Existing avatar

* Shown as the patient's current photo, cropped to a circle.
* **Click an existing avatar**  opens a **larger preview** of the
  full photo.

##### Preview actions

Inside the large preview the user can:

*  **Recapture** — open the camera and take a fresh photo.
*  **Browse** — pick an existing image from disk.
*  **Delete** — remove the current photo (returns to the empty
  state).

##### Benefits

* **Faster patient recognition** across the system through clear
  visual identification.
* **Reduces the risk** of selecting or opening the wrong patient file,
  especially in busy clinics and multi-patient workflows.
* **Streamlines patient registration** by allowing immediate camera
  capture directly from the avatar area.
* **Large image preview** helps staff verify patient identity before
  procedures, billing, or documentation.
* **Improves continuity of care** by helping clinical staff visually
  confirm the correct patient during repeated visits.
* Creates a **more personalised patient experience** during
  appointments and registration workflows.

!!! tip "Enrol photos at first registration"
    Take a fresh photo at the moment the patient first registers —
    it pays back across every future visit, every form, every
    cashier interaction, and every clinical workflow.

\newpage

#### Report Server (V2)

The **Report Server** is the central catalogue of every printable
report in HMS — clinical, financial, HR, inventory, lab, radiology,
quality. V2 is the rebuilt browser-first catalogue with a sidebar of
categories, a live search, favourites, and an inline parameters panel
that ends with one click on **Print Preview**.

##### What it looks like

A single full-screen page with three regions:

| Region | What it does |
|---|---|
| **Header** | Hamburger to toggle the sidebar · *Report Catalog* brand (with the *V2* badge) · live search box · Favorites / All filter pills · Close button. |
| **Sidebar** | Two stat tiles (*Reports*, *Categories*) and a category list with per-category report counts. Collapsible. |
| **Main pane** | One of three states — **Welcome** (all-categories tiles), **Category drill-down** (a single category's reports grouped by sub-category), or **Report parameters** (the chosen report's filters + Print Preview). |

##### Three states

1. **Welcome** — Hero block + a tile per category. The hero text:
   *"Pick a category to see its reports, or use the search to find a
   report by name or description."*
2. **Category** — All reports in the picked category, grouped by
   sub-category, with title + description and a *Back* link.
3. **Report** — The chosen report's parameters (filters), a breadcrumb
   (Catalog  Category  Sub-category  Report), an optional description
   strip, and the **Print Preview** button.

##### How to open it

Open **Reports** from anywhere in HMS — main menu, dashboard quick
links, or a module's *Reports* ribbon button. The V2 catalogue opens
in a full-screen layout that respects your light/dark theme and RTL
language setting.

##### See also

* **[Getting Started](getting-started.md)** — print your first report
  in under a minute.
* **[Features](features.md)** — the exhaustive categorised list of
  everything Report Server V2 can do.

\newpage

#### Getting Started

Print your first report in under a minute.

##### 1. Open the catalogue

From the HMS main menu click **Reports**. The catalogue opens on the
**Welcome** state — a hero block and a tile per category (Admissions,
Billing, Clinical, HR, Inventory, Lab, Radiology, Quality, …).

##### 2. Find the report

Three ways:

* **Pick a category tile** — opens that category, grouped by
  sub-category.
* **Type in the search box** — the sidebar and main pane filter live
  as you type. Search matches the report's name **and** description.
* **Filter by Favorites** — click the heart pill in the header to show
  only the reports you've marked as favourite.

If no reports match, you'll see *No reports match your search* (or the
in-category variant).

##### 3. Open the report

Click any report card. The main pane switches to the **Report**
state. A breadcrumb at the top reads:

> Catalog &nbsp;›&nbsp; **Category** &nbsp;›&nbsp; Sub-category &nbsp;›&nbsp; **Report Title**

If the report has a description, a small info strip explains what it
shows.

##### 4. Fill in the parameters

Below the breadcrumb the report's filters appear as ordinary controls
— text boxes, date pickers, dropdowns, radios, checkboxes. Each
parameter has:

* A **caption** (what it filters by).
* A **default value** (pre-filled so the report works on first click).

Adjust whatever you need. Tab between controls; Enter doesn't submit.

##### 5. Click **Print Preview**

The button is at the bottom-right of the parameters block. The report
renders in the preview window — from there you can:

* **Print** to paper.
* **Save as PDF**.
* **Export** to Excel or Word (when supported by the layout).
* **Email** the file.

Close the preview to come back to the same parameters — change one
value and re-preview without re-navigating.

##### 6. Pin it for next time

While viewing the report, three small switches at the top of the
parameter pane let you **personalise** the report:

* **Favorite** — appears under the Favorites filter pill.
* **Report List** — appears on the module's quick reports list.
* **QuickBar** — appears on the QuickBar (the per-user shortcuts row).

Toggle any of them on / off at any time.

##### 7. Done

Click **Back** to return to the category, or **Close** to return to
the screen you opened the catalogue from.

 See the **[Features](features.md)** page for the exhaustive list of
what V2 can do.

\newpage

#### Features

Every Report Server V2 feature, grouped by what it lets you do.
Exhaustive but not technical — use it as a training checklist or as a
gap analysis against the legacy V1 catalogue.
##### 1. Discovery — find a report

* **Welcome page** with a hero block:
    * Title — *Report Catalog*.
    * Helper text — *"Pick a category to see its reports, or use the
      search to find a report by name or description."*
    * Tile-per-category grid (icon + name + report count).
* **Category sidebar** on the left:
    * Two stat tiles at the top — total **Reports**, total
      **Categories**.
    * Category list, each row with an icon, name, and count badge.
    * *All Categories* shortcut at the top of the list.
    * Selected category highlighted.
    * Empty-tree message — *No reports match your search* — when the
      search excludes every category.
* **Live search box** in the header:
    * Searches report **name** *and* **description**.
    * Filters both the sidebar and the main pane as you type.
    * **Clear** () button appears once there's text.
    * Empty-state messages in the pane — *No reports match your search*
      and *No reports match your search in this category*.
* **Filter pills** in the header:
    * **Favorites** — show only reports you've marked as favourite.
    * **All** — show every report (default).
* **Category drill-down**:
    * Big folder icon + category name + total report count.
    * Reports grouped by **sub-category** (defaulting to *General* when
      no sub-category is set).
    * Each report shown as a card with an icon, title, and description.
* **Breadcrumb** in the report view — Catalog › Category ›
  Sub-category › Report Title.

##### 2. Navigation

* **Hamburger button** in the header — toggle the sidebar open / closed.
* **Brand button** — *Report Catalog · V2 badge* — click to return to
  the welcome state.
* **Back to Catalog** tooltip on the brand button.
* **Back arrow / Back button**:
    * From a report  back to its category.
    * From a category  back to the welcome state.
* **Breadcrumb links** — click *Catalog* or the category name to jump
  back.
* **Close** () button in the header — returns to the screen the user
  opened the catalogue from. Falls back to the home screen if there
  is no history.
* **RTL support** — back arrow flips direction; sidebar moves to the
  right when the language is Arabic.

##### 3. Reports list — cards

Each report card shows:

* File icon.
* **Title** (the report's display name).
* **Description** (when defined).
* A chevron on the right to hint it's clickable.

States:

* Hover effect.
* Click  opens the report.
* Disabled / hidden when the user doesn't have access (driven by
  Security).

##### 4. Report parameter panel

When a report is open, its parameters are rendered as a form. Five
control types are supported:

| Type | What you see |
|---|---|
| **Edit (text)** | A plain text input — for free-text filters such as patient name fragment, account number. |
| **Date** | A date picker — for date-from / date-to filters. Default values are decoded from preset tokens (today, first-of-month, etc.). |
| **Dropdown (lookup)** | A searchable dropdown filled from a database lookup — e.g. branches, departments, physicians, payers. |
| **Radio** | Mutually-exclusive options (e.g. *Detailed / Summary*, *Active / Inactive*). |
| **Checkbox** | On/off flags (e.g. *Include cancelled*, *Show inactive*). |
| **Hidden** | Parameters that exist but are not shown — pre-filled from context. |

Every control carries:

* A **caption** (what it filters by).
* A **default value**.
* An **option to disable / hide** based on context.

##### 5. Running a report

* **Print Preview** button at the bottom of the parameter pane.
* A loading spinner while the report renders.
* Errors surfaced inline (red banner) with the message and a
  developer trace strip when debug is on.

##### 6. Output & sharing

From the preview window the user can:

* **Print** to a connected printer.
* **Save as PDF**.
* **Export to Excel** (when the layout supports it).
* **Export to Word**.
* **Email** the rendered file.
* **Re-render** without leaving the preview after changing a
  parameter.

##### 7. Personalisation — per user

Three switches at the top of the report-parameter pane let the user
pin a report to one of three personal surfaces:

* **Favorite** — surfaces under the Favorites pill and the user's
  favourite-reports list.
* **Report List** — surfaces under the module's *Reports* quick list.
* **QuickBar** — surfaces under the QuickBar shortcuts row.

All three are independent; a report can be on any / all / none.

##### 8. Security

* Each report has its own access-rights mapping.
* Reports the user can't access don't appear in the catalogue at all.
* Right-click on the report header  **Access Rights** opens the
  per-report security editor for admins.
* The catalogue obeys the session timeout — when the session expires
  the report list re-fetches with the user's current permissions.

##### 9. Internationalisation

* All catalogue labels (search, filters, breadcrumb, empty states,
  buttons) are localised — English / Arabic out of the box.
* The report **Title** is localised too.
* **RTL layout** flips the sidebar, the breadcrumb chevrons, and the
  back-arrow icon.
* Number / date formats follow the user's locale.

##### 10. Empty / edge states

* Sidebar empty tree — *No reports match your search*.
* Category empty pane — *No reports match your search in this category*.
* Welcome empty pane — *No reports match your search* (when the search
  excludes everything).
* Tabs / cards never render without their counts.

##### 11. UI quality-of-life

* Live search — no submit button needed.
* Clear-search button appears only when the box has text.
* Sidebar state (open / closed) persists per session.
* Sticky header — search and filters remain reachable while scrolling
  the catalogue.
* Cards adapt to screen width — phones, tablets, big monitors.
* Light / dark theme follows the HMS app theme.
* Icons throughout: folder tree (brand), folder (category), file
  (report), heart (favourites), printer (preview), magnifying glass
  (search), chevron (drill-down), bars (hamburger), info (description),
  arrow-left/right (back).
* **Stat counters** in the sidebar update live as the search narrows
  the visible set.

##### 12. Categories & organisation

* Two-level category hierarchy — **Category** and **Sub-category**.
* Sub-category defaults to *General* when omitted.
* Reports are listed alphabetically inside each sub-category.
* Categories are listed alphabetically inside the sidebar.
* Per-category and per-sub-category headings show the count of
  reports they contain.

##### 13. Per-report descriptions

* Each report can carry a **short description** that:
    * Appears under its name on the card in the category view.
    * Appears as an info strip above the parameter pane in the report
      view.
* Searched alongside the title — so a user can find a report by what
  it shows rather than what it's called.

##### 14. Direct-launch (deep link)

* Reports can be launched directly by URL (bookmarkable / linkable
  from dashboards and other forms) — the catalogue opens straight on
  the parameter pane, ready to preview.
* Pre-fill parameters via URL query so a dashboard tile can open a
  pre-filtered report.

##### 15. V1  V2 coexistence

* V2 ships alongside the legacy catalogue — the **V2** badge in the
  header is your reminder which one you're in.
* Both versions read the same report definitions, so a report is
  available in both immediately without re-cataloguing.
* The user can choose V1 / V2 as their default catalogue in personal
  preferences.

##### 16. Integration points

* **Favourites / Report List / QuickBar** — the same personalisation
  back-end every other HMS surface uses, so favouriting a report here
  surfaces it on the dashboard's quick reports list too.
* **Localisation** — central HMS translation dictionary.
* **Security** — central HMS role / access-rights store.
* **Report engine** — the same Crystal-Reports-based engine for
  output; V2 only replaces the catalogue / launcher.

 Back to **[Overview](index.md)** or jump to **[Getting Started](getting-started.md)**.

\newpage

#### Clinic Dashboard

The **Clinic Dashboard** is the manager's home screen for one
outpatient clinic. It packs the headline numbers — revenue, no-show
rate, bed occupancy, claim acceptance, stock-out risk, quality alerts,
referral pipeline — onto one page and lets you drill into any of them
with a click.

It is the page the clinic manager opens first thing in the morning, the
medical director glances at between rounds, the billing supervisor
keeps in a second tab, and the front-desk lead leaves running on a
wall display.

##### What it shows you

Eight focused sub-tabs, each owning a slice of the clinic:

| Sub-tab | Answers the question |
|---|---|
| **Overview** | How is the clinic doing today, in one glance? |
| **Schedule** | Who is booked, arrived, no-show, completed today? |
| **Census** | Which beds are occupied, who is being discharged when? |
| **Billing** | Are we collecting revenue and getting claims paid? |
| **Physicians** | Which physicians are over- or under-utilised today? |
| **Inventory** | Are we about to run out of anything critical? |
| **Quality** | Are readmissions, incidents, and satisfaction trending right? |
| **CRM** | How is the referral / opportunity / campaign pipeline? |

##### How it relates to other dashboards

* **Clinic Dashboard** (this) — *one* clinic's operations.
* **Hospital Dashboard** — the whole hospital rolled up.
* **Patient Dashboard** — *one* patient's lifetime.
* Module dashboards (HR, Inventory, Lab, …) — drill-downs into a
  single module across the whole hospital.

All of them share the same look-and-feel — KPI tiles + sparklines + a
side cards section — so if you can read one you can read them all.

 Continue to **[Getting Started](getting-started.md)** for a 60-second
tour, or jump to the full **[Features](features.md)** catalogue.

\newpage

#### Getting Started

A 60-second tour of the Clinic Dashboard.

##### 1. Open it

From the HMS main menu pick **Clinic Dashboard**. The dashboard
loads on the **Overview** sub-tab — the manager's "everything in one
glance" view.

##### 2. Read the headline numbers

Six tiles run across the top:

| Tile | What it tells you |
|---|---|
| **Revenue today** | How much money the clinic has invoiced so far today, with a chip showing whether that is more or less than yesterday. |
| **Appointments** | How many appointments are booked for today, with a chip versus the same day last week. |
| **Waiting now** | How many patients are currently in the waiting room. |
| **No-show rate** | The % of appointments missed over the last 7 days. |
| **Bed occupancy** | The % of inpatient beds that are full right now. |
| **Claims accepted** | The % of insurance claims accepted in the last 30 days. |

Each tile has:

* A **value** and **unit**.
* A coloured **delta chip** — green if up vs the comparison period,
  red if down, grey if flat.
* A small caption telling you the comparison period or the
  denominator.

##### 3. Check the trend

Below the tiles a **30-day revenue sparkline** shows the day-by-day
revenue trend. Hover any dot to see the date and amount; the y-axis
labels show the min and max.

##### 4. Switch sub-tabs

The eight sub-tabs along the top let you zoom into a specific area:

* **Schedule**  today's appointment grid + arrivals counters.
* **Census**  inpatient ward occupancy + bed map.
* **Billing**  revenue trend + A/R aging + top revenue items.
* **Physicians**  today's physician scorecards.
* **Inventory**  low-stock alerts + stockout risk.
* **Quality**  readmission rate + incidents + satisfaction.
* **CRM**  opportunity funnel + referral sources + campaigns.

The dashboard remembers your last sub-tab and opens there next time.

##### 5. Drill into anything

Almost every number on every sub-tab is **clickable**:

* Click a KPI tile  the underlying list (e.g. *No-show rate* opens
  today's no-show appointments).
* Click an item in a side list  the full record.
* Click a chart segment  the records that contributed.

##### 6. Hide cards you don't need

Right-click any card and pick **Hide this card**. The dashboard keeps
your show / hide preferences per user, per sub-tab. Bring them back
from the **Settings** menu on the right rail.

##### 7. Refresh

Numbers refresh automatically every few minutes. To force an immediate
refresh, click the **Refresh** button (top-right of any sub-tab).

 Continue to **[Features](features.md)** for the exhaustive
categorised feature list, or **[Sub-tabs](sub-tabs/overview.md)** for a
page per area.

\newpage

#### Features

Every Clinic Dashboard feature, grouped by what it lets you do.
Exhaustive but plain-English — no system internals.
##### 1. Layout & Navigation

* **Eight sub-tabs** — Overview, Schedule, Census, Billing, Physicians,
  Inventory, Quality, CRM.
* **Sub-tab memory** — the dashboard reopens on the sub-tab you used
  last.
* **Refresh** button on every sub-tab for an immediate re-pull.
* **Auto-refresh** — numbers update on their own every few minutes.
* **Responsive layout** — six-column KPI strip on a wide screen drops
  to three or two columns on smaller displays.
* **Right-rail controls menu** — hide / show any card on the current
  sub-tab; preferences saved per user.
* **Card hide / show** — right-click any card  *Hide this card*; bring
  hidden cards back from the controls menu.
* **Click anything to drill down** — KPI tiles, list rows, chart
  segments all open the underlying records.

##### 2. Overview sub-tab

Six headline KPI tiles plus a 30-day revenue sparkline.

###### KPI tiles

* **Revenue today** — money invoiced so far today, with delta vs
  yesterday.
* **Appointments** — appointments booked today, with delta vs same day
  last week.
* **Waiting now** — live count of patients in the waiting room.
* **No-show rate** — % of appointments missed over the last 7 days,
  with delta.
* **Bed occupancy** — % of inpatient beds full right now (with
  busy / total caption).
* **Claims accepted** — % of claims accepted over the last 30 days,
  with delta.

###### Revenue trend card

* **30-day daily revenue sparkline** with axis labels (date and value).
* **Hover any data point** for the exact daily total.
* Auto-handles **empty period** — friendly *"no billing activity in
  the last 30 days"* message.

##### 3. Schedule sub-tab

Today's appointment grid in dashboard form.

* **Today's schedule heat-strip** — each cell coloured by status
  (Booked / Confirmed / Arrived / Attended / Cancelled / No-show /
  Free) with the patient initial.
* **Hover tooltip** — patient + physician + time + status.
* **Click a cell**  opens that appointment.
* **Status counters** — Booked, Confirmed, Arrived, Attended,
  Cancelled, No-show, Free.
* **Date navigator** — Previous day, Today (jump back), Next day.
* **Physicians on duty** side panel — who is working today.
* **Show less / Show more** for the physician list when it overflows.

##### 4. Census sub-tab

Inpatient occupancy and discharge planning.

###### Cards

* **Occupancy** — % of beds full, plus busy / total counts.
* **Wards** breakdown — per-ward Occupied / Free / Available counts.
* **Admits today** counter.
* **Discharges today** counter.
* **Free beds** counter across all wards.
* **Average length of stay (LOS)** — for current inpatients.
* **Bed map** — visual grid of every bed, coloured by status, click
  any bed to open the patient.
* **Discharge queue · next 48h** — patients expected to leave with
  their planned discharge time.
* **Click "Open admission"** on any row  opens the full admission
  record.

##### 5. Billing sub-tab

Cash flow, A/R, claims, and top items.

###### Cards

* **Revenue today** KPI.
* **MTD average bill** ("Avg ticket") — month-to-date average bill
  size.
* **A/R outstanding** — total amount owed by patients / payers.
* **Severely overdue** — A/R aged past the configured threshold.
* **Revenue · last 30 days** — daily-totals sparkline.
* **A/R aging** breakdown — 0–30, 31–60, 61–90, 90+ buckets, with a
  bar chart and exact amounts.
* **Outstanding only** filter on A/R aging to hide settled balances.
* **Top revenue items · 90d** — leaderboard of the highest-revenue
  service codes; click *"Open <item>"* to see the item.
* **Claim status · 60d** — accepted / pending / rejected /
  re-submitted breakdown.
* **Currency display** — drives the unit chip on every monetary
  field (defaults to SAR if not configured).

##### 6. Physicians sub-tab

Per-physician productivity, today and month-to-date.

###### Per-physician card

* **Physician name** + click-through to their full record.
* **Today's counters**: Booked, Pending, Arrived, Done, Cxl, No-show.
* **Utilization** % — what share of the physician's bookable hours
  are filled today.
* **Patients MTD** — count of distinct patients seen this month.
* **Revenue MTD** — money invoiced under this physician this month.

###### Other features

* **Sort by** — utilization, revenue MTD, or patients MTD.
* **Show less / Show more** when the physician list is long.
* **Date navigator** — Previous day, Today, Next day.
* **Empty-state** — *"No appointments today"* on physician cards with
  a fully open calendar.

##### 7. Inventory sub-tab

Stock visibility for the clinic.

###### Cards

* **Stockout risk** — items currently at zero or below safety stock.
* **Low-stock alerts** — items below their min-on-hand threshold.
* **Critical alerts** count.
* **In stock**, **Low stock**, **Out of stock** counters.
* **Total items** in catalogue.
* **Stock value** — current inventory value in the configured currency.
* **Stock by location** breakdown — per location (chair, pharmacy,
  store) with on-hand counts.
* **Top movers · last 90 days** — items by volume or revenue (toggle).
* **Stock vs min** view — visual bar showing on-hand against
  minimum-on-hand.
* **Action** column on alerts — quick replenishment link.
* **Distribution** view — which locations hold the bulk of stock.

##### 8. Quality sub-tab

Outcomes, incidents, and patient satisfaction.

###### Cards

* **Readmission · 30-day** — % of patients readmitted within 30 days.
* **Satisfaction proxy · 90d** — derived satisfaction score
  ("Built from attended / no-show / cancelled mix").
* **Quality alerts** list — open alerts with severity, age, and
  click-through.
* **Incidents · last 90 days** — incident register with Date, Severity,
  Category, Type, Subject, Tracking #, Stage.
* **Open incidents** counter.
* **Open <alert title>** click-through on every alert row.
* **Open incident #<id>** click-through on every incident row.
* **Attendance** breakdown that feeds the satisfaction proxy.

##### 9. CRM sub-tab

Acquisition and growth.

###### Cards

* **Opportunity funnel** — funnel chart from Lead  Contact  Quote 
  Won.
* **Open opportunities** counter.
* **Pipeline value** — sum of open opportunity values.
* **Referral sources · 90d** — where new patients come from
  (advertising channel, doctor referral, walk-in, online …).
* **New patients · last 12 months** — monthly bar chart.
* **Campaigns** list — campaign name, Sent count, Responses count,
  Response rate %.
* **Active campaigns** counter.
* **Status** column on campaigns.
* **Open <opportunity / campaign>** click-through on every row.

##### 10. Common card features (every sub-tab)

* **Card head** strip with icon + title + meta info (period, units).
* **Sparklines** with hover tooltips and min/max y-axis labels.
* **Delta chips** — green up, red down, grey flat — wherever a number
  compares against a previous period.
* **Empty state** messages — every card handles a no-data case with a
  friendly italic message ("No billing activity in the last 30
  days.").
* **Click row / open record** is universal — every list row has a
  click target to the source record.
* **Period labels** — visible *vs yesterday*, *vs last week*, *last 30
  days*, *MTD*, *90d*, *12 months* — so a tile is never ambiguous
  about its window.

##### 11. Customisation

* **Card show / hide** per user, per sub-tab.
* **Sub-tab order** — fixed; cannot be re-ordered.
* **Auto-refresh interval** — configurable per clinic.
* **Currency** — drives the unit chip on monetary KPIs; falls back to
  SAR.
* **Sub-tab visibility** — administrators can hide entire sub-tabs
  for users whose role does not need them (e.g. hide CRM from
  clinical staff).

##### 12. Permissions

* **View access** — controlled per sub-tab on the user role
  (Overview / Schedule / Census / Billing / Physicians / Inventory /
  Quality / CRM).
* **Drill access** — a user can see a KPI without necessarily
  having permission to open the underlying record; in that case the
  click is suppressed.
* **Hide-card preferences** are per-user and do not affect anyone
  else.

##### 13. Performance & freshness

* KPIs and lists come from **live aggregates** — no batch wait.
* **Auto-refresh** keeps the dashboard current without reloading the
  page.
* **Heavy charts** (sparklines, funnels) re-render only on data change
  to keep the page responsive.
* **Live data fall-back** — if a feed isn't provisioned yet, the
  dashboard renders sensible placeholder values instead of breaking,
  with a small note.

##### 14. Quality-of-life

* **Single-page** — no nested screens; everything fits in one
  scroll.
* **Tooltips everywhere** — hover any chart point, KPI value, or
  delta chip to see the formal definition.
* **Show less / Show more** on long lists.
* **Language follows login** — every label and tooltip is translated
  to your interface language.
* **Wall-display friendly** — the dashboard runs full-screen on a
  TV without UI clipping.

 Continue to **[Overview sub-tab](sub-tabs/overview.md)** or jump to
any other sub-tab in the left nav.

\newpage

###### Overview

The default sub-tab — the manager's "everything in one glance" view.

###### What you see

Two cards stacked vertically:

###### Headline KPIs

A six-tile strip:

| Tile | Meaning | Comparison |
|---|---|---|
| **Revenue today** | Money invoiced so far today, in the clinic's configured currency. | vs yesterday |
| **Appointments** | Bookings on the schedule today. | vs same day last week |
| **Waiting now** | Patients currently in the waiting room (live count). | — |
| **No-show rate** | % of bookings missed over the last 7 days. | vs previous 7 days |
| **Bed occupancy** | % of inpatient beds full right now. Caption shows *busy / total beds*. | — |
| **Claims accepted** | % of insurance claims accepted in the last 30 days. | vs previous 30 days |

Each tile shows:

* A coloured icon.
* The **label** in small caps.
* The **value** with its **unit**.
* A **delta chip** — green up, red down, grey flat — when a comparison
  is defined.
* A short **footer caption** clarifying the period or the denominator.

###### Revenue · last 30 days

A daily-totals sparkline:

* Filled area under a line for visual trend.
* **Dots** on the first day, last day, and every 7th day, with a hover
  tooltip showing date + amount.
* **Y-axis** labels — min and max values.
* **X-axis** labels — start date, mid date, end date.
* **Empty state** — *"No billing activity in the last 30 days."*

###### What you do with it

* **First check** of the morning — five seconds tells you whether
  today is on track.
* **Hover the deltas** for the formal comparison period.
* **Click any KPI tile** to drill into the underlying list (the
  appointments, the no-shows, the beds, the claims).
* **Hover any sparkline dot** to read the exact day's revenue.

 Continue to **[Schedule](schedule.md)**.

\newpage

###### Schedule

The day's appointment grid in dashboard form — what's booked, what
arrived, what was missed, who is on duty.

###### Date navigator

A small bar at the top:

* **Previous day** — step back one day.
* **Today** — jump to today (also titled *Jump to today*).
* **Next day** — step forward.
* **Refresh** — re-pull the data.

The date drives every counter and the heat-strip below.

###### Status counters

A row of compact tiles, each with an icon and the count for the
selected day:

| Counter | Hover tooltip | Meaning |
|---|---|---|
| **Booked** | *Total booked today* | Every appointment, all statuses included. |
| **Scheduled** | *Newly scheduled, not yet confirmed* | Just-booked, awaiting confirmation. |
| **Confirmed** | *Confirmed bookings* | Patient confirmed (e.g. by SMS reply). |
| **Arrived** | *Patients who have arrived* | Checked-in at reception. |
| **Attended** | *Completed visits* | Patient seen and visit closed. |
| **Cancelled** | *Cancelled / deleted* | Cancelled or removed. |
| **No-show** | *No-shows* | Patient did not turn up. |
| **Free** | — | Slots still open for new bookings. |

###### Heat-strip

A horizontal strip representing the whole day, one cell per booking
slot:

* **Cell colour** = status (matches the status counters).
* **Cell content** = patient's initial.
* **Hover tooltip** = patient name + physician + time + status.
* **Click a cell** = open that appointment.

This is the fastest way to see "where are the gaps" or "who is in
chair 3 at 11:00".

###### Physicians on duty

A side panel listing the physicians working that day:

* Each row shows the physician's name + a compact mini-counter
  (booked / attended / no-show).
* **Show less / Show more** when the list is long.
* **Click a physician**  opens their full record.

###### What you do with it

* **Morning huddle** — open the heat-strip on the wall, walk the team
  through the day in 30 seconds.
* **Mid-morning sanity check** — *Arrived* counter should be tracking
  *Confirmed*; large gap  someone is slow at check-in.
* **End of day** — *No-show* count is your hit-list for next-day
  reminder calls.

 Continue to **[Census](census.md)**.

\newpage

###### Census

Inpatient occupancy and discharge planning — the bed-side of the
clinic.

###### Cards

###### Occupancy

A radial / percentage card showing the % of beds full right now, with:

* The exact **Occupied** and **Free** bed counts.
* **Admits today** counter.
* **Discharges today** counter.
* **Free beds** total across all wards.

###### Wards

A per-ward breakdown:

| Column | Meaning |
|---|---|
| **Ward** | Ward name. |
| **Occupied** | Beds currently in use. |
| **Free** | Beds available for admission. |
| **Available** | Free beds that are *also* clean and ready. |

Use this when reception calls asking *"do we have a bed in
paediatrics?"* — the answer is in this card.

###### Bed map

A visual grid of every bed across every ward:

* **Cell colour** = bed status (occupied / free / cleaning / blocked).
* **Click a bed** = opens the admission record (if occupied) or a
  blank admission form (if free).
* The map respects ward groupings so adjacent beds in the same room
  stay adjacent in the map.

###### Discharge queue · next 48h

A list of patients planned to leave in the next two days:

| Column | Meaning |
|---|---|
| **Patient** | Name. |
| **Ward** | Where they are now. |
| **LOS** | Length of stay so far. |
| **Discharge by** | Planned discharge date / time. |
| **Complaint / Note** | Reason for admission + any planning note. |

Each row has an **Open admission #<id>** link  opens the full
admission record. Use this list to drive the daily discharge huddle.

###### What you do with it

* **Bed-managers** — the bed map answers "do we have a bed" in two
  seconds.
* **Discharge planners** — the queue is their work list for the next
  two days.
* **Clinical leads** — Occupancy + Admits/Discharges tell you whether
  the in/out flow is balanced.

 Continue to **[Billing](billing.md)**.

\newpage

###### Billing

Cash flow at a glance — revenue, A/R, claims, top items.

###### Headline counters

* **Revenue today** — same KPI as the Overview tab, repeated here so
  you don't have to leave Billing.
* **MTD average bill** ("Avg ticket") — average bill size month-to-date.
* **A/R outstanding** — total amount currently owed by patients and
  payers.
* **Severely overdue** — A/R aged past the configured threshold —
  this is the at-risk number.

Every monetary value uses the configured clinic currency (defaults to
**SAR** if not set).

###### Cards

###### Revenue · last 30 days

A daily-totals sparkline with hover tooltips, identical in style to
the Overview tab — drawn here in larger size with extra detail.

###### A/R aging

Four buckets — **0–30**, **31–60**, **61–90**, **90+ days** —
shown as horizontal bars with the exact amounts. A **Outstanding
only** toggle hides bills that have already been settled to keep the
chart focused on the at-risk piece.

###### Top revenue items · 90d

A leaderboard of the highest-revenue service codes over the past 90
days:

| Column | Meaning |
|---|---|
| **Item** | Service / procedure name. |
| **Volume** | Number of times invoiced. |
| **Revenue** | Total money under this code. |

Each row has an **Open <item>** link  opens the item / service
record.

###### Claim status · 60d

A breakdown of insurance claims submitted in the last 60 days:

* **Accepted** — paid in full.
* **Pending** — awaiting payer decision.
* **Rejected** — declined; needs resubmission or write-off.
* **Re-submitted** — second pass currently in review.

Each segment is clickable  opens the claim list pre-filtered to that
status.

###### What you do with it

* **Daily cash check** — Revenue today + Avg ticket give you the
  daily cash-velocity in five seconds.
* **Receivables triage** — A/R aging + Severely overdue identify the
  bills that need a phone call this week.
* **Service-mix view** — Top revenue items shows what is *actually*
  paying the clinic's bills, vs what management *thinks* is.
* **Claims chase** — Claim status flags how many claims are stuck in
  Pending and how many got Rejected.

 Continue to **[Physicians](physicians.md)**.

\newpage

###### Physicians

Per-physician productivity, today and month-to-date.

###### Date navigator

Same controls as the Schedule sub-tab — **Previous day**, **Today**
(jump back), **Next day**, **Refresh**.

###### Physician scorecard · today

One card per physician on duty:

###### Today's counters

| Counter | Meaning |
|---|---|
| **Booked** | Total appointments scheduled. |
| **Pending** | Booked but not yet confirmed. |
| **Arrived** | Patients checked in. |
| **Done** ("Attended") | Visits completed. |
| **Cxl** | Cancelled. |
| **No-show** | Patient did not arrive. |
| **Utilization** | % of bookable hours filled — chair efficiency for the day. |

###### Month-to-date counters

* **Patients MTD** — distinct patients seen this calendar month.
* **Revenue MTD** — money invoiced under this physician this month, in
  the clinic currency.

###### Row actions

* Click the physician's name  **Open <doctor>'s record** — opens the
  full physician profile.
* Empty state — *"No appointments today"* when a physician has a blank
  day.

###### List controls

* **Sort** — pick the metric to rank physicians (utilization, revenue,
  patients, …).
* **Show less / Show more** — collapse to top N or expand the full
  list.

###### What you do with it

* **Daily huddle** — quickly see who is busy and who has spare slots.
* **Re-balance load** — find physicians with low utilization while
  another is over-booked; redirect walk-ins.
* **Monthly review** — Revenue MTD and Patients MTD are the right
  numbers for the end-of-month sit-down.
* **Performance conversations** — the per-physician card is the
  evidence the medical director brings to the chat.

 Continue to **[Inventory](inventory.md)**.

\newpage

###### Inventory

Stock visibility for the clinic — what's full, what's empty, what's
about to run out.

###### Headline counters

* **In stock** — items above their minimum threshold.
* **Low stock** — items below minimum but above zero.
* **Out of stock** — items at zero on-hand.
* **Total items** in the catalogue.
* **Stock value** — current inventory value in the configured
  currency.
* **Critical alerts** count — items that need attention right now.

###### Cards

###### Stockout risk

Items currently at zero or trending to zero in the next few days:

| Column | Meaning |
|---|---|
| **Item** | Item / SKU name. |
| **Location** | Where the stock should be. |
| **On hand** | Current quantity. |
| **Min** | Minimum threshold. |
| **Action** | Quick replenishment link. |

###### Stock by location

A per-location breakdown — chair, pharmacy, store, fridge, …:

* Counts of items per location.
* **Distribution** view shows the share of stock held at each
  location (useful for asking *"why is so much stock locked in
  the back store?"*).

###### Low-stock alerts

A list of every item below its minimum threshold, sorted by severity:

* **Item** name.
* **On hand** vs **Min** with a visual **Stock vs min** bar.
* **Location** of the deficit.
* Click **Open <item>**  opens the item record.

###### Top movers · last 90 days

Leaderboard of items by consumption:

* **Volume** — how many units used.
* **Revenue** — money invoiced under this item (when it is also a
  billable service).
* Toggle between Volume and Revenue.
* Click **Open <item>**  opens the item record.

###### What you do with it

* **Morning stock check** — In stock + Low stock + Out of stock
  answer "are we safe to open today".
* **Replenishment list** — Stockout risk + Low-stock alerts is the
  buyer's work list for the day.
* **Allocation tuning** — Stock by location shows whether you're
  hoarding in the store while running empty in the chair.
* **Catalog cleanup** — Top movers tells you what to keep stocking
  and what is dead weight.

 Continue to **[Quality](quality.md)**.

\newpage

###### Quality

Outcomes, incidents, and patient satisfaction — the soft side of
clinical operations.

###### Cards

###### Readmission · 30-day

A radial / percentage card showing the share of discharged patients
who came back as inpatients within 30 days.

* The lower, the better.
* A short caption explains the formula.
* Click the card  opens the list of readmitted patients.

###### Satisfaction proxy · 90d

A derived satisfaction score using the **attended / no-show /
cancelled mix** as a proxy for whether the clinic is delivering what
patients showed up for.

* A higher attended rate and a lower no-show + cancel rate  higher
  proxy score.
* The card carries the explanatory tag *"Built from attended /
  no-show / cancelled mix"* so users know what they are looking at.
* **Attendance** breakdown shown alongside.

###### Quality alerts

A list of currently-open quality alerts:

| Column | Meaning |
|---|---|
| **Title** | Short description. |
| **Severity** | High / Medium / Low. |
| **Age** | How long the alert has been open. |
| **Status** | Open / Acknowledged / Resolved. |

Click **Open <alert title>**  opens the alert detail.

###### Incidents · last 90 days

The clinical-incident register for the last 90 days:

| Column | Meaning |
|---|---|
| **Date** | When the incident happened. |
| **Severity** | Severity rating. |
| **Category** | Incident category (Medication, Fall, Equipment, …). |
| **Type** | Sub-type within the category. |
| **Subject** | Short title. |
| **Tracking #** | The incident reference number. |
| **Stage** | Where it is in the workflow (Reported, Under review, Closed). |

Click **Open incident #<id>**  opens the incident record.

Plus a top-line **Open incidents** counter.

###### What you do with it

* **Weekly quality huddle** — Readmission rate + Open incidents +
  Quality alerts is the agenda.
* **Trend watch** — sudden change in the satisfaction proxy is your
  first leading indicator that something is off (often before patient
  complaints reach you).
* **Incident triage** — sort by severity, click into anything red.

 Continue to **[CRM](crm.md)**.

\newpage

###### CRM

Acquisition and growth — where new patients are coming from, how the
sales / referral pipeline looks, what campaigns are running.

###### Cards

###### Opportunity funnel

A funnel chart from top to bottom:

* **Lead** — initial enquiry.
* **Contact** — engaged.
* **Quote** — formal quote / treatment plan presented.
* **Won** — converted to a paying patient.

Each step shows the count and the drop-off vs the previous step.
Click any step  opens the opportunity list at that stage.

###### Top-line counters

* **Open opportunities** — count of opportunities still in the
  pipeline.
* **Pipeline value** — sum of the open opportunity values, in the
  configured currency.

###### Referral sources · 90d

Where new patients came from over the last 90 days:

* Advertising channels (Instagram, Google, billboard, …).
* Doctor referrals (specific referring doctor or clinic).
* Walk-ins.
* Online self-booking.

Shown as a horizontal bar chart with counts. Click any bar  opens
the patient list for that source.

###### New patients · last 12 months

A monthly bar chart showing the count of brand-new patient files
created per month over the last 12 months. Use this as the
*acquisition pulse* — flat or trending up is healthy.

###### Campaigns

A list of marketing campaigns:

| Column | Meaning |
|---|---|
| **Campaign** | Name. |
| **Sent** | Messages / contacts sent. |
| **Responses** | Replies / clicks / bookings (depending on type). |
| **Response rate** | Responses ÷ Sent, as %. |
| **Status** | Active / Paused / Ended. |

Plus an **Active campaigns** counter at the top.

Click **Open <campaign>** on any row  opens the campaign record.

###### What you do with it

* **Weekly growth review** — Open opportunities + Pipeline value tell
  you what's coming.
* **Marketing ROI** — Campaign response rates tell you which channels
  to double down on.
* **Source mix** — Referral sources reveals whether you depend too
  heavily on one channel.
* **Acquisition health** — the 12-month chart is the leading
  indicator of revenue 6–12 months from now.

 Back to **[Overview](overview.md)** or jump to
**[Features](../features.md)** for the full categorised feature
catalogue.

\newpage

#### Administration

What the clinic administrator can configure on the Clinic Dashboard.

##### Sub-tab visibility per role

Each of the eight sub-tabs (Overview, Schedule, Census, Billing,
Physicians, Inventory, Quality, CRM) can be turned on or off per user
role:

* **Clinical roles** typically see Overview, Schedule, Census,
  Physicians, Quality.
* **Finance / billing roles** typically see Overview, Billing,
  optionally CRM.
* **Front desk** typically see Overview, Schedule.
* **Clinic manager / director** sees everything.

Turn off any sub-tab a role does not need — a smaller dashboard is a
faster, less confusing dashboard.

##### Card show / hide

Inside each sub-tab, every card can be hidden by the user via
right-click  *Hide this card*. Preferences are per user and persist
across sessions. The administrator does not need to push these — let
each user tune their own page.

##### Currency

The dashboard reads the clinic's configured currency to label every
monetary tile and to format every amount. Set it under
**Clinic Settings  Currency**. If unset, the dashboard falls back
to **SAR**.

##### Auto-refresh interval

How often the dashboard re-pulls live numbers. Defaults to a few
minutes. Tune up for high-traffic dashboards (wall displays) or down
for slow networks.

##### Demo data

For new installs and training environments, the **Fill Demo Data**
action seeds plausible numbers into the underlying tables so the
dashboard renders meaningfully on day one. Turn it off (and clear
the demo data) before going live.

##### Wall-display mode

The dashboard runs full-screen on any modern browser. For a permanent
wall display:

* Open the dashboard URL in full-screen (F11).
* Pin the **Overview** or **Schedule** sub-tab.
* Set the browser to keep the tab awake.
* Auto-refresh keeps the numbers fresh without manual intervention.

##### Permissions

Beyond visibility, drill-down clicks respect the user's permission
on the underlying record. A user can see *"23 no-show appointments
today"* without necessarily being able to open one — in that case
the click is suppressed.

\newpage

#### Patient Dashboard

The **Patient Dashboard** is the patient's single-page summary — every
clinically and administratively important fact about the patient,
organised into ten tabs, available from any screen that already has a
patient selected.

It is the screen the doctor opens before walking into the room, the
screen the receptionist uses to answer *"what does this patient owe?"*
in two seconds, the screen the case manager uses to chase a pending
lab result, and the screen the cashier uses to send a statement on
WhatsApp.

##### What you get on one page

* The patient's **photo**, **identity**, **contact**, **emergency
  contact**.
* Their **insurance** coverage and outstanding **balance**.
* Their **vitals**, **allergies**, **active problems**, **active
  medications**.
* Every **visit**, **prescription**, **lab test**, **imaging study**,
  **immunization**, **referral** they have ever had.
* Every **treatment plan** with its stages, procedures, and costs.
* Their full **document** library (X-rays, consents, scanned IDs,
  reports).
* Their **upcoming appointments** with a one-click booking dialog.

##### How to open it

Wherever a patient appears in HMS — clinic reception, the scheduler,
search results, the admission list — clicking the patient's name or
photo opens the Patient Dashboard for that patient.

##### The ten tabs

| Tab | What it covers |
|---|---|
| **Profile** | Demographics, identity, contact, guarantor — the single-row reference card. |
| **Clinical** | Vitals, allergies, active problems, prescriptions, visit history. |
| **Care Plan** | Treatment plans, procedures, stages, mini dental chart. |
| **Appointments** | Past + upcoming; book / reschedule / cancel; find available slots. |
| **Lab/Imaging** | Lab tests (orders + results). |
| **Imaging** | Radiology requests + results + latest image preview. |
| **History** | Immunisations, family history, social history, referrals, encounter history. |
| **Documents** | Embedded document gallery with upload, view, annotate, compare. |
| **Billing** | Bills, payments, balance, refunds, statement, WhatsApp / email send. |
| **Insurance** | Coverage, contracts, claims history, sent / accepted / rejected. |

Each tab is detailed on its own page in the left sidebar.

##### See also

* **[Features](features.md)** — every Patient-Dashboard feature in one
  exhaustive categorised list.
* **[Getting Started](getting-started.md)** — a typical 60-second
  review of a patient before they walk in.

\newpage

#### Getting Started

A typical 60-second patient review before they walk into the room.

##### 1. Open the dashboard

Click the patient's name anywhere in HMS — reception, scheduler,
search, the wait-list. The dashboard opens on the **Profile** tab.

##### 2. The photo + identity strip

A photo on the left, the name, file number, date of birth (Gregorian
+ Hijri), age, gender, blood group, nationality, and a *VIP* dot if
applicable. Take three seconds to register who you're about to see.

##### 3. Glance the badges

The header strip shows badges for anything you must not miss:

* Known allergies (with the allergen on hover).
* Pending balance over threshold.
* VIP.
* Care alerts (flagged from a previous visit).

##### 4. Jump to the clinically relevant tab

* Walk-in / acute  **Clinical** (vitals, allergies, active problems,
  current medications, last visit summary).
* Follow-up  **Care Plan** (where in the treatment plan they are).
* Lab / X-ray review  **Lab/Imaging** or **Imaging**.
* Financial question  **Billing**.
* Insurance / authorisation  **Insurance**.
* Anything else from the past  **History** or **Documents**.

##### 5. Take action without leaving the page

Every list has small + buttons on the right:

* **+ Vital** — record a new vital sign reading.
* **+ Prescription** — write a new prescription.
* **+ Lab test** — order a new lab test.
* **+ Imaging** — order a new radiology study.
* **+ Document** — upload a file directly into the patient's gallery.
* **+ Bill / Payment** — open the new-bill or new-payment dialog.
* **+ Appointment** — book the next visit from the embedded
  scheduler.
* **+ Immunisation / Referral / Family member** — under the **History**
  tab.

##### 6. Drill in only if you need to

Most rows link to the full form behind them — click any visit,
prescription, lab order, imaging study, bill, payment, claim, or
treatment plan to open it in its native screen. Use the back button
to come straight back to the dashboard.

##### 7. Done

The dashboard remembers which tab you were last on, per patient — open
the next patient and you start on **Profile** again unless you choose
otherwise.

 Continue to the **[Profile tab](tabs/profile.md)** or jump to the
**[Features](features.md)** catalogue.

\newpage

#### Features

Every feature of the Patient Dashboard, grouped by what it lets you
do. Exhaustive but not technical — use it as a training checklist or
a gap analysis against another system.
##### 1. Identity & Demographics

* Patient photo (avatar with fallback initials).
* Full name.
* Salutation (Mr / Mrs / Dr / …).
* File / MRN number.
* Gender.
* Date of birth — Gregorian.
* Date of birth — Hijri.
* Computed age (years / months / days as appropriate).
* Blood group.
* Marital status.
* Nationality.
* Religion.
* National ID — type and number.
* Passport — number, issue place, issue / expiry dates.
* Visa number.
* VIP flag.

##### 2. Contact

* Mobile phone.
* Landline / phone.
* E-mail address.
* Address (home).
* P.O. Box.
* Employer.

##### 3. Emergency / Next-of-kin

* Salutation.
* Name.
* Relation.
* Phone.
* Mobile.
* Address.

##### 4. Insurance & Guarantors

* Primary guarantor — name, contract, network, class.
* Secondary guarantor — same set of fields.
* Self-insured flag.
* Coverage tier / class.
* Currency.
* Latest admission coverage card.
* Edit primary coverage shortcut.
* Edit secondary coverage shortcut.
* Click-to-set-up coverage when none is on file.
* Claims history list — Pending, Sent, Accepted, Rejected, with counts and totals.
* Open the latest admission to add / edit a claim.

##### 5. Vitals

* Last *N* readings of each vital sign.
* Per-reading badge — Normal / Borderline / Low / High / Markedly high.
* Date and time of each reading.
* Free-text note on each reading.
* + Vital — record a new reading.
* Visual sparkline / trend bar per vital.
* Height, Weight, BMI (computed), Area (BSA, computed).

##### 6. Allergies

* Known allergies list.
* Severity & type (drug / non-drug).
* Reaction description.
* Source (chart / by whom).
* Last-reviewed date.

##### 7. Active Problems

* Problem list with diagnosis codes.
* Onset date.
* Status (Active / Resolved / Recurrent).
* Priority.
* Diagnosing physician.
* Free-text notes per problem.

##### 8. Prescriptions / Active Medications

* Active medications list.
* Past prescriptions list (with show-more toggle).
* Drug name, dose, frequency, duration.
* Prescribing physician.
* Start / end date.
* Source visit / encounter.
* Refill flag.
* + Prescription — write a new one.

##### 9. Visit / Encounter History

* Chronological list of every visit.
* Visit date, physician, department, type (OP / IP / ER / dental / …).
* Chief complaint / reason.
* Diagnosis from the visit.
* Click a visit to open its full record.

##### 10. Care Plan (Treatment Plans)

* List of all treatment plans for the patient.
* Plan name, status, total estimated cost, total paid.
* Per-plan progress bar.
* Per-procedure list — tooth, treatment, dentist, planned date.
* Procedure stages — Planned / Existing / Pre-existing / Done /
  Cancelled.
* Status badges: **Planned**, **Existing**, **Procedures already
  completed**, **Procedures still to be performed**, **Existing
  procedures (pre-existing condition records)**.
* + Treatment Plan — create a new plan.
* Open the full Treatment Plans panel.
* Mini dental chart embedded inline.
* Click a tooth to open the full dental chart.

##### 11. Dental Chart Snapshot

* Read-only thumbnail of the patient's current chart state.
* Per-tooth marks (caries / fracture / treated / missing / …).
* Click any tooth  open the full dental chart for that tooth.
* "Open full" button  full-page chart.

##### 12. Appointments

* Upcoming appointments list with status.
* Past appointments list (collapsible).
* Next-upcoming highlight at the top.
* "No upcoming appointment" empty state.
* Per-appointment actions: Attend, Reschedule, Set status, Remind.
* Set status — No-show, Confirmed, Arrived, In-Service, Completed.
* WhatsApp / SMS reminder.
* Book an appointment dialog:
    * Pick a physician.
    * Pick a speciality.
    * Filter by day shift / window / duration.
    * Mini calendar — green days have availability.
    * Available-slots list (Find available slots).
    * Confirm to commit.
* Show more / show fewer toggle.
* "Past" and "Upcoming" segmented filter.

##### 13. Lab Tests

* List of lab orders + results.
* Sample-collection workflow indicators (Q = request closed, C = sample
  collected, R = sample received, P = reply closed).
* Latest results panel.
* Per-test serial number.
* Click row to open the lab request.
* + Lab test — order a new test.

##### 14. Imaging / Radiology

* Latest imaging study with thumbnail.
* Click thumbnail to view in the document viewer.
* Imaging requests list (open / in progress / completed).
* Imaging results list.
* Open the radiology request the image belongs to.
* + Imaging — order a new study.
* Per-image description / physician.
* Direct link into the source admission for context.

##### 15. History — Immunisations

* Vaccine dose list.
* Date of administration.
* Vaccine name.
* Site (left arm, right arm, …).
* Lot / batch number.
* Administrator (nurse / physician).
* Notes per dose.
* + Vaccine dose.
* Edit this vaccine dose.

##### 16. History — Family

* Family member list with relation.
* Per-member health background (genetic, chronic conditions).
* Edit family + add a member.
* Edit this family member.

##### 17. History — Social

* Smoking status.
* Alcohol consumption.
* Substance use.
* Occupation / risk exposure.
* Marital / living arrangement notes.
* Edit social history.

##### 18. History — Referrals

* Referrals to / from other practitioners.
* Reason for referral.
* Referring / receiving clinician.
* Date.
* Status.
* + Referral.
* Edit this referral.

##### 19. Documents

* Embedded **Document Manager (DM2)** gallery scoped to the patient.
* Upload by drag-and-drop or file picker.
* View any file type (PDF, Word, Excel, images, videos, DICOM, …) in
  the unified viewer.
* Annotate, measure, compare images.
* Categories, tags, keywords on every document.
* Search across the patient's library.
* + Document — add a new file.
* Open Patient Documents header link to the full DM2 view.

##### 20. Billing

* List of bills with status badge.
* Bill total, patient share, insurer share.
* Per-bill physician / diagnosis label.
* Per-bill date.
* Payments list.
* Per-payment number, date, method, amount.
* Patient balance — current outstanding.
* Counts strip — number of bills / payments / refunds.
* + Bill — create a new bill.
* + Payment — record a new payment.
* Refund — record a refund.
* Click a bill to open it in the bill editor.
* Click a payment to open it in the payment editor.

##### 21. Statement & Communication

* Open statement (printable).
* Email the patient statement.
* Send statement via WhatsApp.
* Statement totals — total submitted, total estimated, grand total.

##### 22. Insurance Coverage (panel)

* Primary coverage card — insurer, network, plan, validity, copay.
* Secondary coverage card — same.
* Add primary coverage CTA (when missing).
* Add secondary coverage CTA (when missing).
* Edit patient coverage shortcut.
* Latest admission coverage with policy + class.

##### 23. Claims

* Claims history list (all claims for this patient).
* Per-claim status — Pending, Claim sent, Accepted, Rejected.
* Per-claim totals — submitted, accepted, rejected, net.
* Click to open the originating admission.
* Open the latest admission to add or edit a claim.

##### 24. Cross-tab Quick Actions (+ buttons)

A consistent **+** button on every list lets you create:

* New vital reading.
* New prescription.
* New lab order.
* New imaging order.
* New treatment plan.
* New bill.
* New payment.
* New appointment.
* New vaccine dose.
* New referral.
* New family member.
* New document.

##### 25. Drill-down Links

Every row in every list is clickable and opens the originating record
in its native screen:

* Visit row  visit form.
* Prescription row  prescription form.
* Lab row  lab request.
* Imaging row  radiology request / admission.
* Bill row  bill editor.
* Payment row  payment editor.
* Treatment plan row  plan editor.
* Tooth click  full dental chart.
* Document tile  DM2 viewer.
* Claim row  admission with claim panel.

##### 26. UI Quality-of-life

* Per-list **Show all / Show fewer** toggle.
* Per-list **Search** filter.
* Tooltip on every status badge.
* Tooltip on every micro-icon (alerts, flags).
* Tooltip on every clickable row explaining what will open.
* Esc closes any opened drill-down dialog.
* Mobile-friendly — the dashboard re-flows to a single column on small
  screens.
* Empty-state messages on every list ("No appointments on this day.",
  "No upcoming appointment", "No diagnosis", "No description", "Not
  done", …).
* Per-tab last-position memory.
* Avatar fallback when no photo is uploaded.

##### 27. Permissions & Read-only Mode

* Sensitive sections (insurance, billing) hide their + buttons for
  users without the right role.
* Read-only mode hides every Edit / Create control.
* Cashiers see Billing & Insurance + read-only Clinical / History.
* Physicians see everything except + on bills (depends on clinic
  policy).

##### 28. Integration Points

The Patient Dashboard is a single page but every section delegates to
another HMS module:

| Section | Powered by |
|---|---|
| Documents | Document Manager (DM2) |
| Appointments | Scheduler V2 |
| Vitals / Allergies / Problems / Meds | Clinical EMR |
| Care plans + chart | Dental / Treatment-plan engine |
| Lab tests | Laboratory module |
| Imaging | Radiology / PACS module |
| Billing & Payments | Billing engine |
| Insurance & claims | Insurance / NPHIES module |
| History (immunisations, family, social, referrals) | EMR longitudinal record |

Every embedded section keeps the look of the dashboard — you don't
notice you're crossing module boundaries.

 Continue to the **[Profile tab](tabs/profile.md)**.

\newpage

###### Profile

A single-page reference card for the patient — everything you would
write on a hospital wristband, plus contact and guarantor.

###### Sections

###### Identity strip
Photo · Name · MRN · Salutation · Gender · Date of birth (Gregorian
and Hijri) · Age · Blood group · Marital status · Nationality ·
Religion.

###### Documents
National ID — type + number · Passport number, issue place, issue
date, expiry date · Visa number.

###### Contact
Address · Phone · Mobile · E-mail · P.O. Box · Employer.

###### Emergency (SOS) contact
Salutation · Name · Relation · Phone · Mobile · Address.

###### Insurance summary
Primary guarantor · Secondary guarantor · Self-insured flag · Latest
admission coverage · Patient balance.

###### What you can do

* Open the patient's main file (full edit) from the header.
* Click the photo to enlarge.
* Every field is **read-only** here — use the patient file or the
  insurance form for edits. The Profile tab is the trusted summary
  card, not the editor.

 Continue to **[Clinical](clinical.md)**.

\newpage

###### Clinical

Four cards stacked on one page — the clinician's pre-visit briefing.

###### 1. Vitals

* Last several readings for every vital sign on file (BP, pulse,
  temperature, SpO₂, respiratory rate, weight, height, BMI, BSA).
* Each reading carries a band: Normal / Borderline / Low / High /
  Markedly high — colour-coded.
* Date and time of each reading.
* Free-text note per reading.
* **+ Vital** opens the new-reading dialog.

###### 2. Known Allergies

* List of drug and non-drug allergies.
* Severity and reaction description on hover.
* Edit and remove per row.

###### 3. Active Problems

* Diagnosis code + label.
* Onset date.
* Status (Active / Resolved / Recurrent).
* Priority.
* Diagnosing physician.
* Notes per problem.

###### 4. Prescriptions

* Active medications listed first.
* Past prescriptions accessible via *Show more*.
* Each line: drug, dose, frequency, duration, prescribing physician,
  start / end date.
* **+ Prescription** writes a new one with the patient pre-filled.

###### 5. Visit History

* Chronological list of every visit (newest first).
* Date, physician, department, type, chief complaint, diagnosis.
* Click any row to open the visit in its native form.

 Continue to **[Care Plan](care-plan.md)**.

\newpage

###### Care Plan

The longitudinal treatment plan for the patient — every procedure that
was proposed, performed, or pre-existing — plus a mini dental chart.

###### Treatment plans list

* Every plan for the patient, with status, total cost, total paid, and
  a progress bar.
* **All plans** filter / segmented control.
* Click any plan to open the full plan editor.
* **+ Treatment Plan** creates a new plan.

###### Per-plan procedure grid

* Tooth (or area).
* Treatment.
* Dentist.
* Planned date.
* Estimated cost.
* Stage badge:
    * **Planned** — agreed, not yet started.
    * **Procedures still to be performed**.
    * **Procedures already completed**.
    * **Existing** — already in the mouth at the time the plan was
      drawn.
    * **Existing procedures (pre-existing condition records)**.

###### Mini dental chart

* Embedded read-only chart showing the patient's current mouth state.
* Per-tooth marks (caries / treated / missing / fracture / …).
* Click any tooth to open the **full dental chart** for that tooth.
* **Open full** button opens the full-page chart.

###### What you can do

* **Open the full Treatment Plans panel** — opens the dedicated
  treatment-plan workspace.
* **+** new plan, new procedure inside a plan.
* Print a plan as a patient-facing quote.
* Mark stages done as procedures are completed.

 Continue to **[Appointments](appointments.md)**.

\newpage

###### Appointments

Past, present, and future appointments for the patient — plus a
booking dialog so you never have to leave the dashboard.

###### Lists

* **Next upcoming** — the very next appointment, highlighted at the
  top.
* **Upcoming** — all future appointments.
* **Past** — historical appointments (collapsed by default — *Show
  more*).
* Empty state — *No upcoming appointment*.

Each row shows date, time, physician, speciality, status (Pending,
Confirmed, Arrived, In-Service, Completed, No-show, Cancelled).

###### Per-appointment actions

* **Attend** — mark the patient arrived.
* **Reschedule** — move to a new time.
* **Set status** — quick-set Confirmed / No-show / Cancelled.
* **Remind** — send WhatsApp / SMS reminder.

###### Book an appointment dialog

* **Pick a physician** — list filtered by patient's last clinician.
* **Pick a speciality** — filters the physician list.
* **Filters** — Day shift, Window, Duration.
* **Mini calendar** — green days have free slots.
* **Find available slots** — searches across the chosen window.
* **Available slots** list — click one to confirm.
* **Confirm** to commit, **Cancel** to abandon.

###### Tips

* Use **Show all / Show fewer** on the past list to keep the panel
  focused.
* Click any row to open the appointment in the scheduler.

 Continue to **[Lab Tests](lab.md)**.

\newpage

###### Lab Tests

Every lab order and result for the patient on one tab.

###### What you see

* **Lab Tests** list — most recent first, with date, test, ordering
  physician, sample status, result status.
* **Latest Results** card highlighting the most recent result.

###### Sample workflow indicators

A short status string on each row tells you exactly where the sample
is in the pipeline:

* **Q** — request closed (order issued).
* **C** — sample collected.
* **R** — sample received by the lab.
* **P** — reply closed (results posted).

Each letter is a tooltip — *Request closed*, *Sample collected*,
*Sample received*, *Reply closed*.

###### Actions

* Click any row to **open the lab request** in its native screen.
* **+ Lab test** — order a new test with the patient pre-filled.
* Latest serial number printed under each row for cross-reference.

 Continue to **[Imaging](imaging.md)**.

\newpage

###### Imaging

Radiology orders and results for the patient — with a click-through
to the radiology viewer.

###### Sections

###### Latest Imaging Study
The most recent image as a thumbnail with description, date, and
ordering physician. Click the thumbnail to open it in the document
viewer. Click the description to open the parent radiology request.

###### Imaging Requests
All radiology orders for the patient — open, in-progress, completed.
Per-row: date, modality (X-ray, CT, MRI, US, …), body region,
clinician, status.

###### Imaging Results
Posted radiology results — with the report text and a link to the
study.

###### Actions

* Click an image to view it.
* Click a request to open it in the radiology workspace.
* **+ Imaging** — order a new study with the patient pre-filled.
* "Open the radiology request this image belongs to" link on each
  result.

 Continue to **[History](history.md)**.

\newpage

###### History

Background and longitudinal data that doesn't fit on the Clinical tab
— five sections in one place.

###### 1. Immunisations

* Vaccine dose list with date, vaccine name, site of administration,
  lot / batch, administering staff, notes.
* **+ Vaccine dose** — record a new dose.
* Edit / remove per row.

###### 2. Family History

* Family member list with relation, health background, genetic notes.
* **Edit family + add a member**.
* Per-row **Edit this family member**.

###### 3. Social History

* Smoking, alcohol, substance use.
* Occupation and risk exposure.
* Living arrangement and marital notes.
* **Edit social history**.

###### 4. Referrals

* Referrals to and from external practitioners.
* Reason, referring clinician, receiving clinician, date, status.
* **+ Referral** — add a new referral.
* Edit per row.

###### 5. Encounter History

* Full chronological list of every encounter (visits + admissions +
  ER + dental).
* Click any encounter to open its full record.

 Continue to **[Documents](documents.md)**.

\newpage

###### Documents

The patient's full document library — embedded directly in the
dashboard.

###### What you get

The **Document Manager (DM2)** gallery scoped to this patient. Every
feature of the standalone document manager is available here:

* Browse — grid, list, or timeline view.
* Search by title, tags, or keywords.
* Upload by drag-and-drop or file picker.
* Capture from camera (intraoral / UVC).
* View any file type (PDF, Word, Excel, PowerPoint, images, videos,
  audio, DICOM, archives) in the unified viewer.
* Annotate — pen, shapes, text, eraser; saved as a non-destructive
  layer.
* Measure — ruler, angle, polygon area, crosshairs.
* Compare — pin two or more documents side-by-side.
* Edit Word documents in-browser and save back.
* Categories, tags, keywords on every file.
* Soft-delete with recycle bin.
* Content-hash deduplication.

See **[Document Manager (DM2)](../../dm2/index.md)** for the full
manual.

###### Quick header

* **+ Add Document** — quick upload.
* **Refresh** — re-pull the gallery.
* **Open full** — opens DM2 in its own window with the same patient
  context.

 Continue to **[Billing](billing.md)**.

\newpage

###### Billing

Bills, payments, balance — and the tools to send a statement on
WhatsApp or by e-mail.

###### Counters

A top strip showing the lifetime totals — total billed, total paid,
total refunded, current outstanding balance.

A *"Who pays — lifetime billed"* heading summarises payer breakdown
(patient share vs insurer share).

###### Bills list

* Date, bill number, physician, diagnosis, total, patient share,
  insurer share, status.
* Status badge — Draft, Finalised, Paid, Submitted.
* Click any bill to open it in the bill editor.
* **+ Bill** — create a new bill (*Create a new bill*).

###### Payments list

* Date, payment number, method, amount, reference.
* Click any payment to open it in the payment editor.
* **+ Payment** — record a new payment (*Record a new payment*).
* **Refund** — record a refund (*Record a refund*).

###### Statement actions

* **Open statement (printable)** — opens the patient statement for
  printing.
* **Email the patient statement** — sends a PDF to the address on
  file.
* **Send statement via WhatsApp** — pushes the statement to the
  patient's WhatsApp.

###### Tips

* Use the bills filter / segmented control to limit to unpaid or to a
  date range.
* The patient balance figure here is the same one the **Profile** card
  shows — both come from the same source.

 Continue to **[Insurance](insurance.md)**.

\newpage

###### Insurance

Coverage, latest admission coverage, and claims history.

###### 1. Insurance Coverage

Two cards — primary and secondary.

Each card shows: insurer, plan, network, class, contract, currency,
validity dates, copay, and a *Self-insured* flag where relevant.

* **Click to set up primary coverage** — CTA when missing.
* **Click to add secondary coverage** — CTA when missing.
* **Edit primary coverage** / **Edit secondary coverage** — open the
  coverage editor.
* **Edit patient coverage** — opens the patient's full insurance form.

###### 2. Latest Admission Coverage

The coverage attached to the patient's most recent admission — useful
when a question arises mid-stay about which policy is paying.

* Insurer, plan, class, contract.
* **Open this admission for editing** to drill into the admission.

###### 3. Claims History

Every claim ever submitted for this patient — across every admission.

* Per-row: date, claim number, status, total submitted, total
  accepted, total rejected, net.
* Status badge — **Pending**, **Claim sent**, **Accepted**, **Rejected**.
* Click any row to open the originating admission with the claim
  panel.
* **Open the latest admission to add or edit a claim** header link.

 See also the **[Features](../features.md)** catalogue for the full
list of dashboard capabilities.

\newpage

###### Document Manager (DM2)

**DM2** is the second-generation Document Manager — the page used to
upload, browse, view, annotate, and compare every file attached to a
patient, a visit, a tooth, or any other HMS record.

It replaces the legacy Document Manager with a faster gallery, a
unified viewer for every common file type (PDF, Word, Excel,
PowerPoint, images, videos, audio, DICOM, archives), an annotation
layer that can be saved back to the patient record, a compare mode for
before/after analysis, and direct camera capture from intraoral
cameras and any UVC USB device.

###### How it shows up in the system

DM2 is **embedded** wherever HMS needs a file list — patient files,
visit attachments, the dental-chart imaging tab, the lab-result panel,
the consent-form library. The toolbar adapts to the context — inside
the dental chart it becomes a single-tooth gallery; inside a patient
file it shows the full patient timeline.

###### Quick map

* **Overview** (you're here) — what DM2 is.
* **[Getting Started](getting-started.md)** — upload your first document.
* **[Features](features.md)** — full categorised list of every feature.
* **Using DM2** — one page per task (gallery, upload, camera, viewer,
  annotations, measurements, compare, editor, chart mode).
* **Administration** — categories & tags, storage, deduplication.

 Continue to **[Getting Started](getting-started.md)** or jump to the
**[Features](features.md)** catalogue.

\newpage

###### Getting Started

Upload your first document and view it in DM2 in under a minute.

###### 1. Open a context that has DM2

DM2 is always embedded inside something — typically a patient file or
the imaging tab of the dental chart. Open any patient and click the
**Documents** / **Imaging** / **Attachments** tab — the page you see
is DM2.

###### 2. Drop a file in

The simplest way: drag a file from your file explorer **onto the
gallery surface**. The upload starts immediately. A progress bar
appears on the new tile.

Other ways:

* Click **Add document** (single file picker).
* Click **Import multiple** to upload several files with the same
  metadata (category, tags, …) applied to all of them.
* Click **Capture from camera** to take a fresh photo (intraoral camera
  or any USB webcam).

###### 3. Fill in the metadata

After upload, the **Edit** dialog opens so you can label what was just
saved:

* **Title** — defaults to the file name; change it to something
  meaningful.
* **Description** — free text.
* **Category** — pick from your clinic's list (X-ray, Photo, Consent
  form, Lab result, …).
* **Tags** — comma-separated keywords.
* **Keywords** — extra searchable words.

Click **Save**. The new tile shows your title and a category badge.

###### 4. Open the viewer

Click the tile. The viewer fills the screen with the document.
Depending on the file type you get:

* **Image / X-ray / DICOM**  zoom, pan, rotate, annotate, measure.
* **PDF**  page through, text-select, print.
* **Word / Excel / PowerPoint**  in-browser preview.
* **Video**  play / pause / scrub.

The toolbar across the viewer changes to match what makes sense for
that file type.

###### 5. Annotate or measure (optional)

* Click **Annotation tools** to draw, label, or shape on the document.
* Click **Measurement tools** for ruler, angle, polygon area.
* Click **Save annotations to the patient record** to keep your
  layer.

Annotations are stored separately — the original file is never
modified.

###### 6. Close

Press **Esc** or click the **×** in the viewer corner. You're back on
the gallery with your new document filed and ready to find by
title, tag, or keyword.

 See **[Features](features.md)** for the full catalogue of what DM2
can do, or **[Gallery](using/gallery.md)** for how to browse what's
already there.

\newpage

###### Features

Every DM2 feature, grouped by what it lets you do. Use this page as a
checklist when training new users or evaluating gaps against another
DMS.
###### 1. Browse & Find

* **Grid view** — large thumbnails laid out in a responsive grid.
* **List view** — dense one-line-per-document rows for fast scanning.
* **Timeline view** — documents grouped by date, newest first.
* **Search** — by title, tags, or keywords. Live filter as you type.
* **Sort** — by date, title, type, or size.
* **Show / hide soft-deleted** — surface or hide files in the recycle
  bin without permanently removing them.
* **Multi-select** — tick several rows for bulk actions (delete,
  download, move to compare).
* **Dark / light theme toggle**.
* **Maximise** — DM2 fills the whole window for focus work.
* **Chart mode** — when embedded in the dental chart, DM2 narrows to
  *this tooth, grid view, capture/refresh only*.

###### 2. Add Documents

* **Drag and drop** — drop one or many files from Explorer / Finder.
* **Add document** — file picker for single-file upload.
* **Import multiple** — multi-file picker with metadata applied to all
  at once (title template, category, tags, keywords, description).
* **Skip duplicate uploads (by content hash)** — refuses to upload the
  same file twice, even if it has a different name.
* **Capture from camera** — works with intraoral cameras and any UVC
  USB device. Live preview, click to capture, retake or save.
* **DICOM import** — DICOM files keep their metadata (patient,
  modality, series, study date) on import.

###### 3. View — any file type

A single viewer surface handles all of:

| Family | Formats |
|---|---|
| Images | JPG, PNG, GIF, BMP, TIFF, WebP |
| PDF | Native PDF rendering with text selection |
| Word | DOC, DOCX rendered in-browser |
| Excel | XLS, XLSX with sheet tabs |
| PowerPoint | PPT, PPTX slide preview |
| Video | MP4, WebM, MOV with play / pause / scrub |
| Audio | MP3, WAV, OGG with play / pause |
| DICOM | Single-frame, multi-frame (cine), 3D series |
| Archives | ZIP — peek inside without extracting |
| Other | Generic file icon + download |

###### 4. Viewer — Navigation

* **Previous () / Next ()** — page through every document in the
  current selection.
* **Frame strip** — for multi-frame DICOM, scroll or click any frame.
* **Cine play / pause** — auto-advance through DICOM frames at a
  configurable speed.
* **Mouse-wheel mode** — toggle between *zoom* and *scroll frames*.
* **Timeline** — pop the timeline overlay to jump back in chronological
  order without leaving the viewer.
* **Open in new tab** — pop the document out into its own browser tab.

###### 5. Viewer — Transform

* **Rotate left / right** — 90° increments.
* **Mirror horizontal / vertical** — flip the image.
* **Zoom in / out** — wheel, pinch, or buttons.
* **Pan** — click-and-drag in cursor mode.
* **Reset view** — back to default rotation / zoom / pan.

###### 6. Viewer — Annotations

* **Cursor mode** — click any annotation tool, then draw on the image.
* **Pen / freehand draw**.
* **Text labels**.
* **Shapes** — rectangle, circle, polygon, arrow.
* **Eraser** — remove a single annotation.
* **Save annotations to the patient record** — annotations are kept as
  a layer attached to the document; the original file is never
  modified.

###### 7. Viewer — Measurements

* **Ruler** — straight-line distance, with auto-scale from DICOM
  pixel-spacing when available.
* **Combined ruler** — multi-segment measurement.
* **Angle** — three-point angle (e.g. for orthodontic analysis).
* **Crosshairs** — quick centre-cross for symmetry checks.
* **Polygon area** — closed-polygon area measurement.
* **Calibration** — re-calibrate pixels-per-mm if the source image has
  no DICOM scale.

###### 8. Viewer — Image Filters

* **Brightness / contrast** sliders.
* **Inversion** — colour-invert (useful for X-rays).
* **Grayscale**.
* **Sharpen / blur** presets.
* **Window / Level** for DICOM — full radiology W/L control with
  modality presets (bone, soft tissue, lung).

###### 9. Compare

* **Add to compare** — pin a document into a side-by-side compare
  panel.
* **Side-by-side or grid layout** — 2 / 3 / 4-pane comparison.
* **Synchronised zoom & pan** — move one image, the others move with it.
* **Remove from compare** — drop a document out of the compare set.
* **Common use case** — before-and-after orthodontic photos,
  baseline-vs-follow-up X-rays.

###### 10. DICOM-specific

* **Multi-frame stack** — scroll through the whole series.
* **Cine playback** — play / pause / speed.
* **Mouse-wheel = scroll frames** mode.
* **DICOM metadata panel** — patient, modality, series, study date,
  acquisition parameters; toggle open/closed.
* **Window / Level** with modality presets.
* **Pixel spacing** auto-used for measurements.

###### 11. Editor

The bundled in-browser editor lets you make light edits to common
document types without leaving HMS.

* **Word documents** — open `.docx` and edit text, formatting, tables.
  Save back into the patient record.
* **Cancel edit** — discard unsaved changes.
* **Editor host** — full-screen mode for focused editing.

###### 12. Output & Sharing

* **Print** — current document (or the annotated overlay).
* **Download original** — the untouched file as uploaded.
* **Open in new tab** — pop-out viewer for a second-monitor setup.
* **Refresh** — re-pull the gallery from the server.

###### 13. Cataloguing

Each document carries:

* **Title** — defaults to the file name if empty.
* **Description** — free text.
* **Category** — Consent form, Lab result, X-ray, Photo, …
  (configurable per clinic).
* **Tags** — comma-separated keywords, free-form.
* **Keywords** — extra searchable terms (often used for OCR'd content).

All five fields are searchable from the gallery search bar.

###### 14. Safety

* **Soft delete** — deleted documents move to a recycle bin and can be
  restored. Hard delete needs admin permission.
* **Content-hash deduplication** — prevents accidental duplicate
  uploads of the same file.
* **Read-only mode** — when DM2 is embedded in a context the user has
  no write permission for, the upload / delete / edit controls are
  hidden entirely.
* **Annotations are non-destructive** — the original file is never
  modified.

###### 15. UI quality-of-life

* **Keyboard shortcuts** —  /  for prev/next, Esc to close.
* **Drag-and-drop everywhere** — drop into the gallery to upload, drag
  out of the gallery to download.
* **Density / theme** — comfortable vs compact rows; light vs dark.
* **Per-tooth chart mode** — automatic when embedded in the dental
  chart.
* **Loading spinners** for every async action.
* **Toast notifications** for save / delete / import results.

 Continue to **[Gallery](using/gallery.md)** for the day-to-day
browsing UI.

\newpage

###### Gallery

The **gallery** is the main DM2 surface — the grid (or list, or
timeline) of every document attached to the current record.

###### Layout

* **Toolbar** along the top — Add document, Import multiple, Capture
  from camera, Refresh, view-mode toggles, theme toggle, maximise.
* **Search bar** — type to filter by title / tags / keywords.
* **Category & type filters** — narrow by category, file type, date
  range.
* **Sort** — by date, title, type, size.
* **Tile area** — the documents themselves.

###### View modes

| Mode | Best for |
|---|---|
| **Grid** | Visual browsing — thumbnails laid out in a responsive grid. Default for images, X-rays. |
| **List** | Dense scanning — one document per row with metadata. Best when looking for a specific filename. |
| **Timeline** | Chronological — documents grouped by date, newest first. Best for visit-by-visit review. |

Toggle with the three view-mode buttons in the toolbar. Your choice
persists per user.

###### Searching

The single search box matches against **Title**, **Tags**, and
**Keywords** simultaneously. Type a fragment — the gallery filters
live as you type.

Tips:

* Tag conventions pay off — agree on a clinic-wide tag list (e.g.
  *pre-op*, *post-op*, *consent*) and stick to it.
* For OCR'd documents (scanned consent forms, faxed lab results), put
  the most-searched phrases in **Keywords**.

###### Selecting

* **Click** a tile to open the viewer.
* **Tick** the checkbox on a tile to multi-select.
* **Shift-click** to select a range (in List view).

With multiple tiles selected, the toolbar offers bulk actions:

* **Add to compare** — pin the selection into the compare panel.
* **Delete** — soft-delete (recoverable from Show deleted).
* **Download** — zips the originals.

###### Soft-deleted documents

A toggle in the toolbar (**Show deleted**) reveals tiles for documents
that have been soft-deleted. Each shows a *Restore* / *Permanently
delete* link.

Permanent delete needs admin permission and is irreversible.

###### Maximise & dark mode

* **Maximise** — DM2 expands to fill the browser window. Click again
  (or press Esc) to return to embedded size.
* **Dark mode** — viewer background turns black; tile backgrounds turn
  dark grey. Easier on the eyes for radiology review.

Both settings persist per user.

###### Chart mode (automatic)

When DM2 is embedded inside the dental chart for a single tooth, the
gallery simplifies to:

* Grid view only (no list / timeline).
* No search bar, no category / type filters, no import button.
* **Add**, **Capture from camera**, **Refresh**, **Dark mode** stay.
* A header strip shows *Tooth N* so it's clear which tooth you're
  attaching files to.

This is automatic — no setting required.

 Continue to **[Upload & Import](upload-and-import.md)**.

\newpage

###### Upload & Import

Four ways to get files into DM2.

###### 1. Drag & drop

The fastest path. Drag any file (or several files at once) from your
file explorer onto the gallery surface. Upload starts immediately, a
progress bar appears on each new tile. When done, the **Edit** dialog
opens so you can fill in title / category / tags.

###### 2. Add document

Click **Add document** in the toolbar — opens a standard file picker.
Useful when drag-and-drop is blocked by the OS or you are uploading
from a network share you have already navigated to.

###### 3. Import multiple

Click **Import multiple** when you want to upload **many files** and
apply the **same metadata** to all of them (e.g. 20 X-rays from the
same study session).

The Import dialog has:

* A file picker that accepts as many files as you want.
* **Title** template — used for every file (or fall back to the file
  name if empty).
* **Description** — applied to all.
* **Category** — applied to all.
* **Tags** — comma-separated, applied to all.
* **Keywords** — comma-separated, applied to all.
* **Skip duplicate uploads (by content hash)** — recommended on. When
  ticked, files that are already in the patient's gallery (same
  content, regardless of file name) are skipped.

Click **Import** to upload them all, or **Cancel** to abort.

###### 4. Camera capture

For live capture see **[Camera Capture](camera-capture.md)** — works
with intraoral cameras and any UVC USB device.

###### Duplicate detection

DM2 hashes every file on upload. If the hash matches a file already in
**this** patient's gallery, the upload is skipped (when *Skip
duplicates* is on) or warned about (when it is off). The check is by
**file content**, not file name — renamed copies are still detected.

###### Supported file types

DM2 accepts anything; specifically tested viewers exist for:

* Images: JPG, PNG, GIF, BMP, TIFF, WebP.
* PDF.
* Microsoft Office: DOC, DOCX, XLS, XLSX, PPT, PPTX.
* Video: MP4, WebM, MOV.
* Audio: MP3, WAV, OGG.
* DICOM (single and multi-frame).
* Archives: ZIP (peek inside without extracting).

Other file types upload fine and show a generic file icon with a
**Download original** button.

###### Permission gates

* If the embedding context is **read-only**, the *Add / Import /
  Capture* buttons are hidden entirely.
* Per-user permission can restrict upload size (set in HMS user
  config).
* Per-user permission controls **hard delete** vs **soft delete**.

 Continue to **[Camera Capture](camera-capture.md)**.

\newpage

###### Camera Capture

Capture photos directly from an **intraoral camera** or any **UVC USB
device** (standard webcams included) without leaving HMS.

###### Open

Click **Capture from camera (intraoral / UVC)** on the gallery
toolbar. The capture dialog opens, listing every camera the browser
can see.

###### What you see

* **Camera picker** — every available capture device. Includes
  built-in laptop webcams, USB cameras, and intraoral wands.
* **Live preview** — the camera feed, scaled to fit the dialog.
* **Capture** button — grabs the current frame.
* **Retake** — discards the last capture and goes back to live.
* **Save** — keeps the captured frame and uploads it as a new document.

###### Workflow

1. Click **Capture from camera**.
2. Pick the camera from the dropdown — the dialog remembers your last
   choice per user.
3. The live preview starts.
4. Position the patient / tooth in the frame, click **Capture**.
5. Inspect the captured frame. Click **Retake** if you missed it,
   **Capture** again to take another, or **Save** to upload it.
6. Fill in metadata (title, category, tags) — same as a normal upload.

You can capture and save several frames in one session — Save returns
you to the live preview ready for the next shot.

###### Camera permissions

The browser asks for camera permission the first time you click
Capture. Allow it once and the prompt does not return for that
workstation.

If the camera does not appear in the dropdown:

* The driver isn't installed — install the vendor driver for the
  intraoral wand.
* The camera is in use by another application — close it first.
* The browser blocked the camera site-wide — toggle the camera icon in
  the browser's address bar.

###### DICOM-aware capture

If the connected device is a DICOM-capable wand (some Sirona / Acteon
units), DM2 captures **with full DICOM metadata** so the resulting
file behaves like any other DICOM in the viewer (Window/Level, pixel
spacing for measurements).

###### Chart mode

When DM2 is embedded in a single tooth's imaging tab, the captured
frame is automatically tagged to that tooth — no extra step needed.

 Continue to **[Viewer](viewer.md)**.

\newpage

###### Viewer

The DM2 viewer is a single surface that knows how to render every
common file type — images, PDF, Office documents, video, audio, DICOM,
ZIP archives. It opens when you click a document in the gallery.

###### The toolbar

The toolbar groups buttons into four areas — they show or hide
depending on what the file supports.

| Group | Buttons |
|---|---|
| **Cursor** | Cursor mode (pan / select), annotation tools, measurement tools, image filters, more tools |
| **Transform** | Rotate left, Rotate right, Mirror horizontal, Mirror vertical, Reset view |
| **Save** | Save annotations to the patient record |
| **Output** | Print, Download original, Open in new tab |

Plus navigation arrows on the left / right edge for **Previous ()** and
**Next ()** — they walk through every document in the current
selection.

###### Cursor mode — click for menu

The default mode. Click **Cursor** in the toolbar (or just click on
empty viewer space) to switch back to it from any tool. In cursor mode:

* **Drag** = pan the image.
* **Mouse wheel** = zoom (or scroll frames, in DICOM stack mode).
* **Pinch** on touch screens = zoom.
* **Click a tool from the toolbar** to enter annotation, measurement,
  or filter mode.

###### Image transforms

| Button | Effect |
|---|---|
| **Rotate left** | 90° anti-clockwise. |
| **Rotate right** | 90° clockwise. |
| **Mirror horizontal** | Flip left  right. Lights up when active. |
| **Mirror vertical** | Flip top  bottom. Lights up when active. |
| **Reset view** | Removes all rotation, mirroring, zoom, and pan — back to default. |

Transforms are **non-destructive** — the original file is untouched.

###### Frame navigation (DICOM and multi-frame)

When the document has multiple frames (DICOM stacks, multi-page TIFF):

* **Frame strip** along the bottom — click any frame thumbnail.
* **Mouse-wheel mode** — toggle between *zoom* and *scroll frames*.
  The current mode is shown in the toolbar info line:
  *Mouse-wheel: zoom* or *Mouse-wheel: scroll frames*.
* **Play / pause (cine)** — auto-advance through frames at a
  configurable speed.

###### File-type quick reference

| Type | Tools available |
|---|---|
| Image | All annotation, measurement, filter, transform, compare |
| DICOM | All of the above + Window/Level + cine + DICOM metadata panel |
| PDF | Page navigation, text selection, print |
| Word / Excel / PowerPoint | In-browser preview, page / sheet navigation |
| Video | Play / pause, scrub, volume, fullscreen |
| Audio | Play / pause, scrub, volume |
| ZIP | Browse contents, extract any file to viewer |
| Other | Generic icon + Download original |

 Continue to **[Annotations](annotations.md)** or
**[Measurements](measurements.md)**.

\newpage

###### Annotations

Annotations let the clinician mark up an image without changing the
original. They are stored as a separate layer attached to the document
— anyone re-opening the viewer sees the marks; downloading the original
file gives the un-marked file.

###### Open the annotation tools

Click **Annotation tools** in the viewer toolbar. The tool palette
slides open.

###### Tools

| Tool | What it does |
|---|---|
| **Pen / freehand draw** | Click-and-drag to draw a freehand line. |
| **Text label** | Click to place a text box; type your label. |
| **Rectangle** | Click-and-drag to draw a rectangle outline. |
| **Circle** | Click-and-drag for a circle / ellipse outline. |
| **Polygon** | Click each vertex; double-click to close the shape. |
| **Arrow** | Click-and-drag from base to tip. |
| **Eraser** | Click any existing annotation to remove just that one. |

Pick a tool, drop annotations on the image, then click **Cursor** to
go back to pan / zoom mode.

###### Editing an annotation

* **Click** the annotation once  it becomes selected (drag handles).
* **Drag** the handles to resize / reshape.
* **Drag** the body to move it.
* Press **Delete** to remove the selected annotation.

###### Save

Click **Save annotations to the patient record**. The annotation layer
is committed to the document. Anyone opening this document next will
see the same marks.

If you close the viewer without saving, a confirm dialog appears so
unsaved annotations are not lost by accident.

###### Tips

* Use **Text labels** to leave a short clinical note pointing to what
  you found.
* Use **Polygon** to outline lesions, restorations, or anatomy of
  interest.
* For **before / after** comparison, annotate the *current* image and
  pin the *previous* one into compare — both layers are visible.

 Continue to **[Measurements](measurements.md)**.

\newpage

###### Measurements

Measurements are quantitative annotations — distances, angles, areas.
They share the same layer as annotations and are saved to the patient
record the same way.

###### Open the measurement tools

Click **Measurement tools** in the viewer toolbar. The tool palette
slides open.

###### Tools

| Tool | What it does |
|---|---|
| **Ruler** | Click start point, click end point — shows the straight-line distance with units (mm if scale is known, px otherwise). |
| **Combined ruler** | Multi-segment ruler — click each waypoint; double-click to finish. Shows the total length. |
| **Angle** | Three-point angle — vertex point in the middle; the tool shows the angle in degrees. Useful for orthodontic analysis. |
| **Crosshairs** | Quick centre-cross for symmetry checks; no numbers, just visual reference. |
| **Polygon area** | Click each vertex; double-click to close. Shows the enclosed area. |

###### Units & scale

* **DICOM** — pixel-spacing is read from the DICOM header. Measurements
  are reported in **millimetres** automatically.
* **Other images** — by default measurements are in **pixels**. Use
  **Calibrate** to teach DM2 the real-world scale.

###### Calibrate

If the image has a known reference (a ruler in the photo, a calibrated
gauge, a structure of known size):

1. Pick the **Ruler** tool.
2. Draw a line between two points of known real-world distance.
3. Click **Calibrate** on the measurement palette.
4. Type the real distance (e.g. *10 mm*).
5. All subsequent measurements on this image use that scale.

The calibration is saved with the annotation layer so it sticks.

###### Editing & deleting

* **Click** a measurement to select it; drag the end-points to adjust.
* **Eraser** (in the Annotation tool palette) removes a single
  measurement.
* **Reset view** does **not** delete measurements — it only resets
  rotation / mirror / zoom / pan.

###### Save

Same as annotations — click **Save annotations to the patient record**.
Distances, angles, areas, and calibration are all persisted.

 Continue to **[Compare](compare.md)**.

\newpage

###### Compare

The **Compare** panel shows two, three, or four documents side by
side, with synchronised zoom and pan. Use it for before / after
analysis, baseline-vs-follow-up, or comparing the same view across
visits.

###### Pin documents

There are two paths into the compare panel:

* **From the gallery** — multi-select tiles (tick boxes) then click
  **Add to compare** in the toolbar.
* **From the viewer** — open one document, click **Add to compare** on
  the toolbar; open the next document, click **Add to compare** again.

Each pinned document becomes a pane in the compare layout.

###### Layouts

* **2 panes** — left / right.
* **3 panes** — three columns or 2-over-1.
* **4 panes** — 2 × 2 grid.

The layout switches automatically based on how many documents are
pinned; you can also choose explicitly from the layout button.

###### Synchronised navigation

When **Sync** is on:

* **Zoom** in one pane zooms every pane.
* **Pan** in one pane pans every pane.
* **Rotate** in one pane rotates every pane.

Useful when comparing the exact same anatomical view across time.

When **Sync** is off, each pane is independent — useful when comparing
different views (lateral vs frontal, two different teeth).

###### Remove a document

Click **Remove from compare** on the pane to drop one document out of
the comparison.

###### Use cases

* **Orthodontic photos** — pin pre-treatment, mid-treatment,
  post-treatment for a 3-pane progression view.
* **X-rays** — pin baseline and 6-month follow-up to spot caries
  progression or bone-loss.
* **Consent vs signed form** — pin the blank form and the signed copy
  to verify everything was filled in.

###### Annotations & measurements in compare mode

Each pane keeps its own annotation / measurement layer. Saving in one
pane does **not** affect the others.

 Continue to **[Editor](editor.md)** or **[Chart Mode](chart-mode.md)**.

\newpage

###### Editor

DM2 includes an in-browser editor for **Word documents (.docx)** so
small text changes can be made without leaving HMS — handy for
consent forms, referral letters, treatment-plan templates.

###### Open

* From the gallery — right-click a `.docx` tile  **Edit**.
* From the viewer — click the **Edit** (pencil) button on the toolbar.

The editor host fills the viewer area with a rich-text surface
showing the document's content.

###### What you can edit

The editor handles **light edits** — text, basic formatting (bold /
italic / underline), paragraphs, tables, lists. It is **not** a
full-feature Word replacement; complex documents with macros,
tracked-changes, embedded objects, or unusual styles will preview
correctly but should be edited in Word and re-uploaded.

###### Save

* **Save** — writes the edited document back into the patient record
  as a new version. The previous version is kept in the document
  history.
* **Cancel edit** — discards every unsaved change and returns to the
  viewer.

A *Saving…* indicator appears during the upload.

###### Full-screen editing

Click the maximise button (top-right of the editor host) to give the
editor the whole window — useful for longer documents.

###### Read-only preview

When the embedding context is read-only or the user does not have
edit permission, the document opens in **read-only preview** — same
rendering, no editing toolbar.

 Continue to **[Chart Mode](chart-mode.md)**.

\newpage

###### Chart Mode

When DM2 is embedded **inside the dental chart for a single tooth**,
it switches automatically into **chart mode** — a simplified gallery
that shows only that tooth's documents, with only the controls a
clinician needs at the chairside.

###### What changes

| Removed in chart mode | Reason |
|---|---|
| Search bar | Only this tooth's files anyway. |
| Category filter | Same. |
| Type filter | Same. |
| Import multiple | Clinical capture is one-at-a-time. |
| List view toggle | Grid only — thumbnails are what matters. |
| Timeline view toggle | The chart already shows the timeline by visit. |

###### What stays

* **Add document** — quick single-file upload.
* **Capture from camera** — intraoral / UVC capture (the main use).
* **Refresh** — re-pull after another user uploads.
* **Dark mode** — eye-friendly for radiology review.
* **Tile click  viewer** with annotations, measurements, compare.

###### Header strip

A *Tooth N* header appears above the gallery so it is always clear
which tooth you are attaching files to. The number comes from the
chart's currently-selected tooth.

###### Workflow at the chairside

1. Select a tooth in the dental chart.
2. Click the **Imaging** tab — DM2 opens in chart mode for that tooth.
3. Click **Capture from camera** — take the X-ray / photo.
4. Click the new tile to open the viewer.
5. Annotate / measure as needed; save.
6. Move on to the next tooth — DM2 follows the chart selection
   automatically.

###### Multi-tooth view (regular DM2)

To see *every* document for the patient regardless of tooth, open the
patient's main **Documents** tab — that loads the full DM2 with all
filters available.

\newpage

###### Administration

DM2 has two areas the administrator owns:

* [Categories & Tags](categories-and-tags.md) — the dropdown the user
  picks from when filing a document.
* [Storage & Deduplication](storage-and-deduplication.md) — where files
  are kept, how big they can be, how duplicates are handled.

###### Per-user permissions

Set on the HMS user record (system administration, outside DM2):

| Permission | Effect when off |
|---|---|
| Upload | Hides Add / Import / Capture buttons. |
| Edit metadata | Hides the Edit dialog; titles / tags / categories become read-only. |
| Edit document content | Hides the document editor; Word docs open read-only. |
| Soft-delete | Hides the Delete action; documents cannot be sent to the recycle bin. |
| Hard-delete | Hides Permanently delete; soft-deleted items can only be restored. |
| Restore | Hides Restore on soft-deleted items. |
| Annotate | Hides annotation + measurement tools. |
| Compare | Hides Add to compare. |

These permissions compose with the embedding context's read-only flag
— if either says read-only, the user gets read-only.

\newpage

###### Categories & Tags

Three free-text fields are attached to every document — **Category**,
**Tags**, **Keywords**. They look similar but behave differently.

###### Category

* **One per document** — radio-button choice.
* Picked from a **controlled list** the admin maintains.
* Shown as a coloured badge on every tile.
* Drives the Category filter dropdown above the gallery.
* The right value to use for a strong taxonomy you can later filter
  and report on.

###### Typical categories

* X-ray
* Photo
* Consent form
* Lab result
* Referral letter
* Prescription
* Invoice / receipt
* ID document
* Insurance card
* Treatment plan
* Discharge summary
* Other

The list is configurable per clinic — keep it short (12 – 20 items
maximum). Long lists confuse users and dilute the value of filtering.

###### Tags

* **Many per document** — comma-separated free text.
* Not validated — users type whatever they want.
* Searchable from the gallery search bar.
* Good for **ad-hoc grouping** that doesn't deserve a category: *pre-op*,
  *post-op*, *insurance-claim*, *re-do*, *referred-out*.

###### Tip — agree a tag vocabulary

Free-form tags drift fast. Publish a short tag list (10 – 20 tags) and
ask the team to stick to it. Otherwise *preop*, *pre-op*, *Pre-Op*, and
*pre op* all end up as four different tags.

###### Keywords

* Free text, single field.
* Same as tags from a search point of view (the gallery search box
  matches all three).
* Use **Keywords** for searchable content that doesn't fit a short tag
  — e.g. the patient's reported symptom in their own words ("upper
  right molar pain since Monday"), or OCR'd content from a scanned
  document.

###### Where the three fields show up

| UI | Category | Tags | Keywords |
|---|---|---|---|
| Tile badge | Yes (coloured) | No | No |
| Filter dropdown above gallery | Yes | No | No |
| Search box | Yes | Yes | Yes |
| Edit dialog | Picker | Comma-separated input | Comma-separated input |
| Import dialog (bulk) | Single value applied to all | Same | Same |

\newpage

###### Storage & Deduplication

###### Where files live

DM2 stores files in **one of three** places, chosen by the system
configuration:

| Mode | When to pick it | Trade-off |
|---|---|---|
| **OS** | Default. Files are written to the server's upload folder (typically `wwwroot/upload/`). | Fast, simple, easy to back up. |
| **DB** | Files are stored as blobs inside the HMS database. | Single backup covers data + files; database grows fast. |
| **Remote** | Files are streamed to an HMS imaging server (separate machine). | Best for multi-clinic groups sharing one imaging store. |

The choice is set in the system's imaging configuration — typically by
the IT team during install. End users see no difference.

###### Upload-folder path

When the storage mode is **OS**, the default location is
`<wwwroot>/upload/`. The admin can redirect it to an absolute path —
useful for pointing at a NAS, shared volume, or large local drive.

Make sure the path is:

* On a **large** disk — imaging fills space fast.
* **Backed up** — files live here, not in the database.
* Reachable by **every** application server in a load-balanced setup.

###### File size limits

* Per-file maximum is controlled by the application's request-size
  limit (default 100 MB).
* Per-user upload limit can be set on the user record.
* Browsers also impose their own request size — if a user can't
  upload a large video, try the alternate browser before increasing
  server limits.

###### Deduplication

DM2 hashes every uploaded file (SHA-256 of the binary content). On
upload:

1. The hash is computed in the browser before the file is sent.
2. The server checks whether that hash already exists for **this
   patient**.
3. If yes:
   * **Skip duplicate uploads (by content hash)** ON  upload is
     silently skipped; the existing tile is highlighted.
   * **Skip duplicate uploads** OFF  upload proceeds; a small
     duplicate badge appears on the new tile.

The hash check is **per patient**, not global — the same image
attached to two different patients is allowed (they may genuinely
need a copy each).

###### Soft delete & retention

Deleted documents move to a recycle bin and stay there until:

* A user with **Hard-delete** permission removes them permanently, or
* A retention sweep runs (configurable) and removes items older than
  the retention window.

The retention sweep is off by default — clinics opt-in once they have
agreed a retention policy with their compliance team.

###### Audit

Every upload, edit, delete, restore, and download is logged with
user, timestamp, and document ID. The log is queryable from the
system audit module (outside DM2).

\newpage

#### Dental Chart

##### Introduction

The **HMS Dental Chart** is the clinical heart of every dental visit
in HMS. It is the screen the dentist works in chairside — a live,
two-arch view of the patient's mouth where every condition, every
treatment, every prescription, and every measurement is recorded by
clicking the tooth it relates to.

Unlike a paper chart, the HMS Dental Chart links what the dentist
records to the **patient's account** (the bill flows automatically),
the **treatment plan** (planned procedures appear on the chart),
the **prescription queue**, the **lab orders**, and the **patient's
imaging gallery** — all without re-typing anything.

It supports both **adult** (permanent) and **paediatric** (primary)
dentitions, and overlays five specialised clinical views on top of
the base chart — **Treatment Plan**, **Periodontal**, **Orthodontic**,
**Caries**, **Endodontic / Radiographic**, and **Occlusion** — so one
chart serves a general dentist, a perio, an ortho, and an endodontist
without context-switching.

Snapshots let you freeze the chart on any date and compare two
points in time side-by-side — invaluable for follow-up visits,
medico-legal records, and patient-facing progress reviews.

A **Demo mode** loads a realistic showcase case so the dentist can
present the chart's capabilities (perio findings, ortho appliance,
mixed treatment plan) without touching any real patient data.

##### Key benefits

* **Click-driven, not form-driven** — the tooth is the input; no
  separate forms to fill in for each procedure.
* **One chart, many specialties** — perio overlay, ortho overlay,
  endo / radiographic overlay, occlusion overlay, treatment plan
  overlay, caries overlay — each independent, each toggleable.
* **Adult + paediatric in one place** — switch dentitions with a
  single button; the chart redraws appropriately for primary teeth.
* **Snapshots and compare** — capture the chart on any date, compare
  any two snapshots side-by-side, highlight what was added or
  removed between them.
* **Multi-select + mirror** — apply the same procedure to many
  teeth in one click; mirror today's work to the contralateral side
  in another click.
* **Per-tooth depth** — each tooth carries its own notes, images,
  endodontic findings, radiographic findings, plus the chart icons.
* **Linked to the rest of HMS** — every procedure recorded
  contributes to the patient's bill, treatment plan, and imaging
  gallery; no double-entry.
* **Visit-aware** — the chart shows what changed *during this
  visit* vs everything historic.
* **Print-friendly** — a clean chart-only print layout for the
  patient or the file.
* **Demo mode** — sales / training use without polluting real data.

##### How it shows up in the system

The Dental Chart is embedded inside the patient's clinical
workspace. From the **[Clinic Reception](../adt-dc/index.md)**
front desk, the **Dental Chart** toolbar button opens it for the
selected patient. Inside the chart, every change automatically
links to the current visit.

##### Quick map

* **[Getting Started](getting-started.md)** — first patient, first
  procedure, save and close.
* **[Features](features.md)** — the categorised feature list.
* **Using the chart** — layout, tools, selecting teeth, per-tooth
  actions.
* **Overlays** — Plan, Periodontal, Orthodontic, Caries,
  Endodontic / Radiographic, Occlusion.
* **[Snapshots & Compare](snapshots-and-compare.md)** — capture
  and compare points in time.
* **[Demo Mode](demo-mode.md)** — load a showcase case for
  presentations.
* **[Printing & Export](printing-and-export.md)** — clean prints
  and gallery export.
* **Administration** — tooth numbering systems, the procedure
  legend.

 Continue to **[Getting Started](getting-started.md)**.

\newpage

#### Getting Started

A typical chairside visit, start to finish.

##### 1. Open the chart

From the Clinic Reception front desk, with the patient selected,
click **Dental Chart** on the toolbar. The chart fills the screen
with the patient's two arches (upper and lower).

If the patient is a child, click **Pedo** in the toolbar to switch
to the paediatric (primary) dentition. The chart redraws with
primary teeth.

##### 2. Find your tools

The **toolbox** opens on the left. It is split into three groups,
top to bottom:

| Group | What it picks |
|---|---|
| **Status** | What condition you are recording on the tooth — caries, missing, fractured, sound, mobility, … |
| **Operation** | What treatment you are performing — filling, extraction, crown, root canal, scaling, … |
| **Root** | Root-specific findings — RCT-completed, RCT-incomplete, post & core, periapical lesion, … |

Click any button — it becomes the **armed tool**. Every tooth you
click next gets that tool applied.

##### 3. Click teeth

* **Single tooth** — click anywhere on the tooth on the arch.
* **A specific surface** — click the mesial / distal / occlusal /
  buccal / lingual sector of the tooth (the tooth is divided into
  five clickable sectors).
* **Several teeth at once** — see step 5.

The chart updates instantly. The procedure is queued for the
current visit; the price is added to the visit's bill.

##### 4. Disarm or switch tool

* Press the same tool button again to **disarm** (the armed-button
  highlight goes off).
* Click a different tool button to switch — the chart stays where
  it is; only the next click changes.
* Use the **Clear all selections** button (toolbox header) to reset
  the armed tool, the armed status, the armed root, and any tooth
  selections all at once.

##### 5. Multi-select & apply to many

When you need the same procedure on many teeth — *"polish 1, 2, 3,
4, 14, 15, 16"* — use multi-select:

1. Click **Multi-select** in the toolbar.
2. Click each tooth you want — they highlight (no procedure is
   created yet).
3. Pick the tool from the toolbox.
4. Click **Apply** in the toolbar.

Every selected tooth gets the tool applied in one operation, and a
toast confirms *"Applied tool to N of N teeth."*

##### 6. Mirror to the contralateral side

After working one side, click **Mirror** (after multi-select) to
copy today's procedures on the selected teeth to the contralateral
side — useful for symmetric work like 4-quadrant scaling or
bilateral extractions.

##### 7. Add a per-tooth note

Right-click any tooth (or use the tooth-details panel) to add a
**Clinical note**, **Endodontic finding**, **Radiographic finding**,
or attach an **Image**. These are stored against that specific
tooth and reappear next visit.

##### 8. Switch to an overlay (optional)

For specialised work, toggle an overlay:

* **Perio** — opens the periodontal sheet (right drawer) and a
  perio overlay on the arches showing pocket depths, BoP diamonds,
  recession spikes.
* **Ortho** — opens the orthodontic sheet (right drawer) and an
  ortho overlay showing brackets, archwire, elastics, status flags.

Overlays do not consume the chart space — they sit on top of the
base view and can be turned off without losing what you recorded.

##### 9. Save a snapshot

Click **Save snapshot** to capture the chart as of today. Snapshots
become anchor points for the **Compare** view.

##### 10. Print, or close

* **Print** — opens a clean chart-only print layout (no toolbar, no
  drawer, no menus).
* **Documents** — opens the patient's image / document gallery
  (uses [DM2](../dm2/index.md)).
* **Close** — closes the chart. Everything is already saved by the
  per-tooth save; there is no "save chart" button.

 Continue to **[Features](features.md)**.

\newpage

#### Features

Every Dental Chart feature, grouped by what it lets you do.
##### 1. Chart layout

* **Two-arch view** — upper and lower, anatomically correct.
* **Adult dentition** — 32 permanent teeth.
* **Paediatric dentition** — 20 primary teeth; switch with the
  **Pedo** button in the toolbar.
* **Per-tooth, five-sector clicks** — mesial · distal · occlusal /
  incisal · buccal / facial · lingual / palatal — surface-specific
  procedures recorded with one click on the right sector.
* **Treatment-plan band** under each tooth — Existing (green) /
  Planned (red) / Completed (blue) / Referred (gray) — visible
  without opening the plan overlay.
* **Maximise / Exit zoom** — chart fills the whole window for
  detailed work; one click to come back.

##### 2. Tools

* **Status tools** — record conditions (caries, missing, fractured,
  sound, mobility, …).
* **Operation tools** — record treatments (filling, extraction,
  crown, root canal, scaling, …).
* **Root tools** — root-specific findings (RCT completed / incomplete,
  post & core, periapical lesion, …).
* **Class list** — surface-class picker (M, D, O / I, B / F, L / P)
  for procedures that need a class.
* **Clear all selections** — resets armed tool + armed status +
  armed root + tooth selections in one click.
* **Show / hide toolbox** — collapsible panel; *Show toolbox* /
  *Hide toolbox* button.

##### 3. Selecting teeth

* **Single-click** — apply the armed tool to one tooth.
* **Multi-select mode** — click multiple teeth (they highlight) and
  then **Apply** the tool to all of them at once. Confirmation
  toast shows the count.
* **Mirror** — copy today's procedures from selected teeth to the
  contralateral side. Reports *"Copied procedures from N teeth …
  M operation(s) created."*

##### 4. Per-tooth depth

For each tooth (right-click or the details panel):

* **Clinical notes** — free text, dated, attached to the tooth.
* **Tooth notes** — short labels visible on the chart.
* **Image gallery** — attach photos, X-rays, scans for that specific
  tooth.
* **Endodontic findings** — recorded with a marker on the chart.
* **Radiographic findings** — recorded with a marker on the chart.
* Each set surfaces as a small icon on the tooth so the dentist
  knows what is recorded without opening the panel.

##### 5. Snapshots & Compare

* **Save snapshot** — captures the chart state for the current date.
* **Snapshot dropdown** — pick any saved snapshot to view.
* **Compare** — side-by-side compare of any two snapshot dates.
  Highlights procedures added (green) or removed (red) between them.
* **Delete snapshot** — removes only the snapshot *marker* for the
  date; real procedures recorded on that day are not deleted.

##### 6. Treatment Plan overlay

* **Existing / Planned / Completed / Referred** colour-coded band
  per tooth.
* Toggle on / off independently of the perio and ortho overlays.
* Drives the per-tooth band visible by default.

##### 7. Periodontal overlay & sheet

* **Perio overlay** — pocket polylines, BoP (bleeding-on-probing)
  diamonds, recession spikes drawn directly on the chart.
* **Perio sheet** (right drawer) — per-tooth measurement entry
  (six sites per tooth) with mobility, furcation, suppuration.
* Overlay and sheet are independent — the overlay can stay visible
  while the sheet is closed.
* **Perio Demo mode** — loads a realistic Stage II generalized
  periodontitis case (with severe lower-posterior pocketing, BoP,
  mobility, furcation) for showcase / training. Nothing saved to
  the database.

##### 8. Orthodontic overlay & sheet

* **Ortho overlay** — brackets, archwire, elastics, status flags,
  headgear arrows drawn on the chart.
* **Ortho sheet** (right drawer) — case header, tooth-by-tooth
  grid, elastics, encounters, checklists, tasks.
* Overlay and sheet are independent.
* **Start new ortho case** — closes the current active case (kept
  for history) and creates a fresh active case.
* **Close / Reopen case** — close marks a case read-only (chart
  frozen); reopen re-activates it and deactivates any other case
  so only one is current.
* **Quick-fit brackets** — one-click "brackets on incisors / canines
  / premolars + bands on second / third molars" — typical starting
  point after bonding. Fine-tune tooth-by-tooth afterwards.
* **Wipe ortho appliance** — clears brackets / bands / attachments
  / elastics across the whole case; preserves the case header
  (appliance / phase / wires). Useful at debond.
* **Delete ortho case** — permanently deletes the case plus every
  tooth line, elastic, encounter, checklist, and task. Cannot be
  undone.
* **Ortho Demo mode** — mock brackets, elastics, encounters,
  checklists, tasks, headgear, status flags so every feature
  shows up. Nothing saved.

##### 9. Other clinical overlays

* **Caries overlay** — patient-level caries map for surface-by-surface
  caries planning.
* **Endodontic / Radiographic overlay** — markers for endo findings
  and radiographic findings projected on the arches.
* **Occlusion overlay** — occlusal-relationship visualisation.

Each overlay toggles independently — you can run, say, *Plan +
Perio overlay* at the same time, or all six at once.

##### 10. Patient context

* **Patient banner** — name, file number, age, gender, photo at the
  top of the chart.
* **Patient documents shortcut** — opens the patient's full
  document gallery without leaving the chart.
* **Patient info header** — extra demographics and clinical alerts
  visible inline.

##### 11. Numbering systems

* Universal / FDI / Palmer notation supported.
* The currently-active numbering system is shown on each tooth's
  label.
* Configured in administration; the same chart can switch on the
  fly without losing data (numbers re-label).

##### 12. Voice capture

* **Voice capture component** — dictate notes / procedures hands-free
  during the exam.
* Transcribed text lands in the relevant note field for the
  dentist to confirm.

##### 13. Demo mode (chart-wide)

* Loads a realistic showcase case — one of every procedure type —
  so the chart can be demonstrated to a customer or trainee.
* **No DB writes** — toggling Demo back off restores the real
  patient procedures.
* Separate Demo modes exist for the perio sheet and the ortho sheet
  (each loads its own showcase data set).

##### 14. Reload & state

* **Reload chart** — recalculate everything from the saved
  procedures (useful if something looks off).
* **Multi-select** is preserved across overlay toggles.
* **Sidebar collapse** + **Toolbox hide** for chairside screen
  space.

##### 15. Printing & export

* **Print chart** — opens the browser print dialog on a clean
  chart-only layout: no toolbar, no drawer, no menus — just the
  arches and the procedures.
* **Documents** opens the patient gallery — print / export
  individual files from there.

##### 16. Legend

* **Procedure legend** popup — every chart icon's meaning in one
  place. Used by new staff and by patients who want to understand
  the marks on their printout.

##### 17. Action confirmation & errors

* **Verification popup** for irreversible actions (delete
  snapshot, delete ortho case, wipe ortho appliance).
* **Alerts** (top of the chart) for non-blocking warnings.
* **Toast** messages for routine confirmations (snapshot saved,
  procedures mirrored, demo loaded).

##### 18. Visit awareness

* Procedures created during the current visit are visible separately
  from historical procedures.
* The chart shows "this visit" deltas distinctly so the dentist sees
  what changed today.

##### 19. Linked across HMS

* **Bills** — every chart procedure adds a line to the current
  visit's bill at the price-list rate.
* **Treatment plan** — planned procedures appear with the Planned
  status; completing them flips them to Completed.
* **Imaging gallery** — every per-tooth image is filed in
  [DM2](../dm2/index.md) with the tooth as a tag.
* **Prescriptions / Lab orders** — initiated from chairside through
  the same patient context.

 Continue to **[Layout & Toolbar](using/layout.md)**.

\newpage

###### Layout & Toolbar

The dental-chart screen is organised so the dentist's eyes spend
99 % of the visit on the arches in the centre, and 1 % on the
controls around them.

###### Top bar (toolbar)

Across the very top:

| Control | Purpose |
|---|---|
| **Sidebar toggle** | Collapses / expands the left rail and the patient banner. Useful on small screens. |
| **Adult / Pedo** | Switches between the permanent and primary dentitions. Adult is default. |
| **Plan overlay** | Toggles the treatment-plan band visualisation. |
| **Perio overlay** | Toggles the periodontal overlay. |
| **Perio sheet** | Opens / closes the periodontal sheet drawer. |
| **Ortho overlay** | Toggles the orthodontic overlay. |
| **Ortho sheet** | Opens / closes the orthodontic sheet drawer. |
| **Multi-select** | Enters multi-select mode. |
| **Mirror** | Mirrors today's procedures from selected teeth to the contralateral side. |
| **Apply** | Applies the armed tool to every selected tooth. |
| **Snapshot dropdown** | Picks the snapshot date to view. |
| **Save snapshot** | Captures the chart as of today. |
| **Compare** | Opens the side-by-side compare view. |
| **Delete snapshot** | Removes the snapshot marker for the selected date. |
| **Reload** | Recalculates the chart from saved procedures. |
| **Demo** | Loads a chart-wide showcase case. |
| **Print** | Opens the clean chart-only print layout. |
| **Documents** | Opens the patient's document gallery. |
| **Legend** | Opens the procedure legend popup. |
| **Maximise / Exit zoom** | Toggle the chart fullscreen. |
| **Close** | Close the dental chart. |

A **kebab menu** (left rail) holds advanced / debug-style entries
that aren't part of routine chairside use.

###### Patient banner

Below the toolbar:

* Patient photo.
* Name (English + Arabic if both are on file).
* File number.
* Date of birth + age + gender.
* Clinical alerts (allergies, VIP, special-needs flags) when
  present.

The banner is always visible — the dentist never has to wonder
whose chart they are working on.

###### Left rail (toolbox)

The toolbox holds the tools the dentist clicks to record what they
find or do:

* **Status group** — sound, caries (per surface), missing,
  fractured, mobility, restorations.
* **Operation group** — filling, extraction, crown, bridge, RCT,
  scaling, sealant, implant, …
* **Root group** — RCT completed / incomplete, post & core,
  periapical lesion, internal resorption.
* **Class list** — surface class picker (M, D, O / I, B / F, L / P)
  for procedures that take a class.
* **Hints** — small reminder labels under each button explaining
  what the icon means. **Hide hints** turns them off once the team
  is fluent.
* **Hide toolbox** collapses the whole rail when it isn't needed.

###### Centre — the chart

Two arches, anatomically arranged. Each tooth shows:

* The procedure icons stacked on the relevant surface.
* The treatment-plan band underneath.
* Small markers when there are clinical notes, images, endodontic
  findings, or radiographic findings recorded.
* The tooth number (in the active numbering system).

###### Right drawer (overlays' sheets)

When **Perio sheet** or **Ortho sheet** is open, it slides in from
the right and occupies a third of the screen (or covers the chart
on narrow screens). On wide monitors the drawer + chart coexist.

###### Status / Alert area

A thin band above the chart shows non-blocking alerts (e.g.
*"Patient context not loaded yet"*, *"Mirror failed"*, *"Demo mode
on — real procedures hidden"*).

 Continue to **[Tools](tools.md)** or **[Selecting Teeth](selecting-teeth.md)**.

\newpage

###### Tools

Tools are what you record on a tooth. Pick a tool from the toolbox
on the left rail, then click the tooth (or a specific surface) to
record it.

###### Three tool groups

###### Status

What is *currently true* about the tooth — a condition the dentist
observed.

* **Sound** — the tooth is healthy.
* **Caries** — split into surface-specific buttons that combine
  with the Class List to record M / D / O / I / B / F / L / P
  caries.
* **Missing** — tooth absent.
* **Fractured** — visible fracture / crack.
* **Mobility** — combined with a degree (I, II, III).
* **Existing restoration** — already-present filling / crown / etc.

###### Operation

What you are *doing today* to the tooth — a treatment.

* **Filling** — combined with the surface class (M, D, O…).
* **Extraction** — simple or surgical.
* **Crown / Bridge** — fixed prosthesis work.
* **Root canal** — endodontic treatment.
* **Scaling / Root planing** — periodontal work.
* **Sealant** — preventive.
* **Implant** — surgical placement.
* Plus the rest of the procedure catalogue the clinic configures.

###### Root

Root-specific findings.

* **RCT completed** / **RCT incomplete**.
* **Post & core**.
* **Periapical lesion**.
* **Internal resorption**.

###### Arming a tool

Click a tool button — it lights up to show it is **armed**. Every
tooth or surface you click next gets that tool applied.

The toolbox header shows which group's tool is armed (small badge).

###### Disarming

* **Click the same button again** — disarms that one tool.
* **Click a different button** — switches the armed tool.
* **Clear all selections** (toolbox header, small ) — resets the
  armed tool, armed status, armed root, and any tooth selections
  in one click. The chart itself is untouched.

###### Class List

For procedures that need a surface class (almost all fillings and
many cavity classifications), pick the class on the **Class List**
inline:

* **M** Mesial
* **D** Distal
* **O / I** Occlusal / Incisal
* **B / F** Buccal / Facial
* **L / P** Lingual / Palatal

The class is combined with the tool, so a single click records
*"composite restoration on the mesial surface"*.

###### Surface targeting

A tooth is divided into **five clickable sectors** representing its
surfaces. Clicking a sector applies the armed tool to that surface;
clicking the centre applies it tooth-wide (for non-surface
procedures like extractions).

###### Hints

Each tool button has a short text hint underneath in the default
view — useful while new staff learn the icons.

**Hide hints** turns the labels off once the team knows the icon
set; **Show hints** brings them back.

###### Hide / Show toolbox

The whole left rail can be collapsed with the **Hide toolbox**
button — useful when the chart needs the full width (chairside on
a small monitor).

 Continue to **[Selecting Teeth](selecting-teeth.md)**.

\newpage

###### Selecting Teeth

Three ways to tell the chart which tooth (or teeth) the next action
applies to.

###### 1. Single click

The default. Arm a tool, click a tooth (or a surface). The
procedure is created instantly.

Most chairside work happens this way — call the tooth, click the
tool, click the tooth.

###### 2. Multi-select mode

When the same procedure applies to many teeth — *"polish 1–4 and
14–16"* — switch to **Multi-select**:

1. Click **Multi-select** in the toolbar (it lights up).
2. Click each tooth you want — they highlight blue. **No procedure
   is created yet.**
3. Pick the tool from the toolbox.
4. Click **Apply** in the toolbar.

The chart confirms with a toast: *"Applied tool to N of N
tooth/teeth."*

You can keep multi-selecting and applying different tools to the
same selection — useful when the same teeth need both a status
(*"existing restoration"*) and an operation (*"replace with
composite"*).

To clear the selection without applying: press **Clear all
selections** in the toolbox, or click **Multi-select** again to
exit the mode.

###### 3. Mirror to the contralateral side

When you have just recorded work on one side and the same work
applies symmetrically to the other:

1. Make sure the teeth you want mirrored are **multi-selected**.
2. Click **Mirror** in the toolbar.

The chart copies every **today** procedure on those teeth to the
contralateral side and confirms with a toast:

> *Copied procedures from N tooth/teeth to the contralateral side.
> M operation(s) created.*

Mirror only copies **today's** procedures — historic work is left
alone, so you don't accidentally duplicate old fillings.

###### Safety rails

* **Multi-select + Apply with no tool armed**  the chart refuses
  and reminds: *"Pick a tool from the toolbox first, then click
  Apply."*
* **Apply with no selection**  *"Select at least one tooth first."*
* **Mirror with no selection**  same message.

###### Tips

* Multi-select is sticky — it stays on after Apply so you can pick
  a second tool and apply it to the same teeth without re-clicking
  every tooth.
* **Clear all selections** is faster than turning multi-select off
  and on when you want to start over with a clean slate.
* For sequential work on the same teeth, use multi-select to lock
  the set, then change tools as you go.

 Continue to **[Per-Tooth Actions](per-tooth-actions.md)**.

\newpage

###### Per-Tooth Actions

Beyond status / operation / root tools, each tooth carries its own
**clinical depth** — notes, images, and specialist findings — that
follow the tooth across visits.

###### Opening the tooth details

Right-click any tooth (or use the **Tooth details** panel from the
chart) to open the details for that tooth. The panel sits on the
right of the chart and is divided into sections.

A **maximise** toggle in the panel header expands it to fill the
right half of the screen for typing-heavy work.

###### Clinical notes

* Dated, named (the dentist who wrote it), free text.
* Multiple notes per tooth — they stack chronologically.
* A small note-icon appears on the tooth in the chart when any are
  recorded — tooltip: *"Notes recorded for this tooth."*
* Click any note in the list to edit or delete it (with a
  confirmation popup).

###### Tooth notes

Short labels (a word or two) visible on the chart itself — *"watch"*,
*"sensitive"*, *"on hold for ortho"*. Use them sparingly; long
notes belong in **Clinical notes**.

###### Image gallery

* Embedded **[DM2](../../dm2/index.md)** in chart mode — simplified
  gallery just for this tooth.
* **Add document** — single file picker.
* **Capture from camera** — intraoral wand or webcam capture goes
  straight in, tagged to this tooth.
* Click a thumbnail to open the DM2 viewer with annotations,
  measurements, compare.
* A small image-icon appears on the tooth when any images are
  recorded — tooltip: *"Images recorded for this tooth."*

###### Endodontic findings

A dedicated tab for endo-specific information:

* Pulp status (vital / non-vital / necrotic).
* Apical findings.
* Working length (per canal).
* Number of canals.
* Restorability assessment.

A small endo-icon appears on the tooth — tooltip: *"Endodontic
findings recorded"*.

###### Radiographic findings

A dedicated tab for radiographic interpretation:

* Periapical lesion (size, type).
* Bone loss assessment.
* Root anatomy notes.
* Caries radiographic findings.

A small radiographic-icon appears on the tooth — tooltip:
*"Radiographic findings recorded"*.

###### Delete / Restore

* **Delete** removes a procedure from the tooth — confirms first.
* **Remove** strips an image / endo finding / radiographic finding.
* **Restore** brings back a soft-deleted item (until the retention
  sweep removes it permanently).

###### Saving

Every per-tooth action saves immediately on click — there is no
"Save" button for the chart. Closing the chart never loses work.

 Continue to **[Overlays](../overlays/index.md)**.

\newpage

###### Overlays

An **overlay** is a clinical view layered on top of the base
chart. Each overlay covers one specialty and can be turned on or
off independently — the dentist sees only what they need.

###### The six overlays

| Overlay | Purpose | Has a sheet? |
|---|---|---|
| **[Treatment Plan](plan.md)** | Existing / Planned / Completed / Referred band per tooth. | No — band only. |
| **[Periodontal](perio.md)** | Pocket polylines, BoP diamonds, recession spikes. | Yes — right drawer with per-tooth measurement entry. |
| **[Orthodontic](ortho.md)** | Brackets, archwire, elastics, status flags, headgear. | Yes — right drawer with case header, tooth grid, elastics, encounters, checklists, tasks. |
| **[Caries](caries.md)** | Patient-level caries map for surface-by-surface planning. | No. |
| **[Endodontic / Radiographic](endo-rg.md)** | Endo and radiographic finding markers on the arches. | No. |
| **[Occlusion](occlusion.md)** | Occlusal-relationship visualisation. | No. |

###### How they combine

* Overlays **stack** — you can have Plan + Perio + Ortho overlays
  all on at the same time. The chart is still readable; the
  overlay layer simply adds icons on top of the base chart.
* **Sheets** are the editor drawers for overlays that need
  per-tooth data entry (perio and ortho). The overlay and the
  sheet are independent — you can leave the overlay visible while
  the sheet is closed (i.e. read-only chairside view).
* On narrow screens, opening a sheet covers the chart; on wide
  monitors the sheet + chart sit side-by-side.

###### Toggling

Each overlay has its own toolbar button. Click once to enable,
click again to disable. The button highlights to show the state.

###### Demo modes

Two overlays carry their own showcase data sets:

* **Perio Demo mode** — loads a realistic Stage II generalised
  periodontitis case with severe localised lower-posterior
  pocketing, BoP, mobility, furcation involvement.
* **Ortho Demo mode** — loads mock brackets, elastics, encounters,
  checklists, tasks, headgear, status flags.

Both are non-destructive — toggle them off and the real case is
restored. Useful for training, customer demos, and verifying that
your screen and printer set-up look right.

 Pick an overlay from the list above to dive in.

\newpage

###### Treatment Plan Overlay

The treatment-plan overlay paints a **colour-coded band** under
every tooth so the dentist sees at a glance what is *already
there*, what is *planned*, what has been *completed*, and what was
*referred out*.

###### Colours

| Band colour | Meaning |
|---|---|
| **Green** | **Existing** — already present (old restorations, prostheses, missing teeth). |
| **Red** | **Planned** — agreed with the patient but not yet done. |
| **Blue** | **Completed** — finished during the current treatment plan. |
| **Gray** | **Referred** — sent to a specialist. |

###### How rows get there

* When the dentist records a procedure with status *Planned*, the
  band on that tooth turns red.
* When the same procedure is later marked *Completed* — either
  from the chart or from the visit's procedure list — the band
  turns blue.
* **Existing** comes from the patient's history at first visit
  (intake) or from observations recorded with status tools.
* **Referred** is set by hand when the treatment was sent
  elsewhere.

###### Why it matters

A glance at the band tells the receptionist whether to schedule a
follow-up (lots of red), the cashier whether to invoice now (blue
just appeared), and the patient whether their plan is progressing
(more blue than red over time).

The band is **always visible** by default — even when the Plan
overlay is toggled off, the band stays. The overlay toggle
controls extra plan-specific icons on the arches; the band itself
is a built-in part of the chart.

###### Print

The print layout keeps the bands — a printed treatment plan from
the chart shows the patient exactly what was completed and what is
still planned, in colour.

\newpage

###### Periodontal Overlay & Sheet

The periodontal layer covers everything a perio exam needs —
six-point pocket charting, bleeding on probing, recession,
mobility, furcation, suppuration — painted on the same arches the
GP uses.

###### Two parts

The perio layer has **two independent controls**:

| Control | What it does |
|---|---|
| **Perio overlay** | Toggles the periodontal *visualisation* on the chart — pocket polylines, BoP diamonds, recession spikes. Read-only. |
| **Perio sheet** | Opens the perio *data-entry drawer* on the right of the chart. Read-write. |

You can leave the overlay visible while the sheet is closed —
useful chairside when the visualisation is enough and the dentist
doesn't want the drawer covering the chart.

###### The visualisation (overlay)

Drawn on top of the base chart:

* **Pocket polylines** — six points per tooth connected, the line
  height showing pocket depth.
* **BoP diamonds** — red diamonds where bleeding-on-probing was
  recorded.
* **Recession spikes** — downward spikes on the buccal / lingual
  showing recession depth.
* **Mobility** — small marker on teeth with mobility recorded
  (degree shown next to it).
* **Furcation** — marker between roots when furcation involvement
  is recorded.
* **Suppuration** — distinct icon where pus was observed.

Colour intensity scales with severity — deeper pockets, more
recession, all show stronger.

###### The sheet (data entry)

The perio sheet opens as a right-side drawer with:

* **Header** — patient, exam date, recorded-by.
* **Per-tooth grid** — six sites per tooth (DB, B, MB, DL, L, ML for upper / DL, L, ML, DB, B, MB for lower), each with pocket depth and BoP toggle.
* **Mobility row** — degree I / II / III per tooth.
* **Furcation row** — class I / II / III per tooth.
* **Recession row** — buccal + lingual values per tooth.
* **Suppuration toggle** per site.
* **Notes** field for the overall exam.

On narrow screens the sheet **covers the chart**; on wide screens
it sits beside it.

###### Closing the exam case

* **Close case** marks this perio exam read-only — chart frozen,
  no further edits.
* **Reopen** re-activates it and deactivates any other active
  perio exam, ensuring only one is current at a time.

###### Demo mode

The **Perio Demo** button loads a realistic *generalised Stage II
periodontitis* case — severe localised lower-posterior pocketing,
BoP, mobility, furcation involvement — to showcase the chart's
range. Nothing is saved to the database. Click Demo again to exit
and reload the real exam.

###### Tips

* Toggle the **overlay on and the sheet off** when you want to
  *show* the patient their perio status without entering data.
* The overlay redraws automatically when you save the sheet — no
  need to close-and-reopen.
* Pocket depth values 0–12 are accepted; out-of-range entries are
  rejected with a small inline warning.

\newpage

###### Orthodontic Overlay & Sheet

Everything orthodontics needs — bracket / band placement, archwire,
elastics, status flags, headgear — on the same arches, plus a
right-side drawer for full case management.

###### Two parts

| Control | What it does |
|---|---|
| **Ortho overlay** | Draws brackets, archwire, elastics, status flags, headgear arrows on the chart. |
| **Ortho sheet** | Opens the orthodontic editor drawer on the right. |

Independent — overlay can be on while the sheet is closed.

###### The visualisation (overlay)

* **Brackets** — drawn on the buccal of each banded tooth, colour
  reflecting bracket type (metal, ceramic, self-ligating).
* **Bands** — drawn on the appropriate molars.
* **Archwire** — drawn through every bonded tooth on the relevant
  arch.
* **Elastics** — drawn between teeth showing direction and class
  (II, III, cross-elastic, vertical, …).
* **Status flags** — small icons for *to-bond*, *to-reposition*,
  *to-debond*, *holding*.
* **Headgear arrows** — outward arrows indicating headgear forces.

###### The sheet (case management)

The drawer is split into tabs:

###### Case header

Active case, appliance type, current phase, archwire upper / lower,
start date, expected end, treating orthodontist.

###### Tooth grid

One row per tooth — bracket / band, attachment, status flag,
auxiliary, notes.

###### Elastics

A table of every elastic on this case — from/to teeth, class,
size, wear pattern, start date, end date.

###### Encounters

Per-visit log — what was done at each ortho visit (wire change,
spring placed, IPR, reposition).

###### Checklists

Phase-specific checklists (e.g. *initial alignment complete*,
*levelling complete*, *finishing*) so the case can be progressed
deliberately.

###### Tasks

To-do items for the next visit (*"check 14 binding"*, *"order new
elastics"*, *"order retainer"*).

###### Quick-fit brackets

A single click "puts brackets on incisors / canines / premolars
(1–28) and bands on the second / third molars" — typical starting
point right after bonding. Fine-tune tooth-by-tooth afterwards.

###### Wipe ortho appliance

Wipes brackets / bands / attachments / elastics for **every** tooth
on the current case. The **case header** (appliance, phase, wires)
is preserved. Useful at debond.

The chart asks for confirmation before wiping.

###### Start new case / Close / Reopen

* **Start new case** — closes the currently active case (kept for
  history) and creates a fresh active case.
* **Close case** — marks the case read-only (chart frozen, no
  further edits).
* **Reopen** — re-activates the case and deactivates any other
  active case so only one is current at a time.

###### Delete ortho case

**Permanently deletes** this case **and** all its tooth lines,
elastics, encounters, checklists, and tasks. *Cannot be undone.*

Asks for explicit confirmation. Use only when a case was created in
error.

###### Demo mode

The **Ortho Demo** button loads mock brackets, elastics,
encounters, checklists, tasks, headgear, status flags so every
feature appears. Nothing saved to the database. Click again to
exit and restore the real case.

###### Tips

* Open the **sheet** for case management; leave just the **overlay**
  on for chairside review.
* Use the **Encounters** tab as your visit journal — it makes the
  next adjustment visit faster.
* The **Tasks** tab is where you list everything you want to do
  next time — checked off when finished.

\newpage

###### Caries Overlay

The caries overlay paints a **patient-level caries map** on the
arches — every surface marked with a class, severity, and treatment
recommendation. Use it when sitting with the patient to explain
where the cavities are and what the plan is.

###### What is drawn

* **Caries marks** on the affected surfaces (Mesial, Distal,
  Occlusal / Incisal, Buccal, Lingual / Palatal).
* **Colour shading** by severity — light for incipient, darker
  for deeper / cavitated.
* **Recommendation icons** beside each tooth showing what is
  proposed (composite, amalgam, crown, RCT, watch).

###### Where the data comes from

Every caries you recorded through the Status / Operation tools or
through the surface-class picker flows into the caries map
automatically. There is no separate "caries form" to fill in.

###### Why it's useful

* **Patient education** — turning the overlay on and pointing at
  the screen is a much faster patient explanation than reading a
  chart aloud.
* **Treatment planning** — sequence work from heaviest caries
  load to lightest at a glance.
* **Insurance pre-authorisation** — print the chart with caries
  overlay on as evidence for the claim.

###### Toggle

The caries overlay button is in the toolbar. It does not need a
sheet — the data entry happens through the normal Status /
Operation tools.

###### Print with caries overlay on

The print layout respects the overlay state — a chart printed with
caries overlay on shows the full caries map on the paper.

\newpage

###### Endodontic / Radiographic Overlay

The endo / radiographic overlay projects the **endodontic findings**
and **radiographic findings** recorded on individual teeth onto the
arches — so the dentist can see at a glance which teeth have endo
or radiographic notes without opening each tooth's details.

###### What is drawn

* **Endo markers** on teeth with endodontic findings recorded —
  shape varies by pulp status (vital / non-vital / necrotic).
* **Apical lesion markers** at the root tip when one is recorded —
  size scales with the lesion size from the radiographic findings.
* **RCT status markers** — completed (filled root canal icon) /
  incomplete (open root canal).
* **Restorability hints** — colour-coded marker showing whether
  the tooth was assessed restorable / questionable / hopeless.
* **Radiographic abnormalities** — bone loss, root anatomy notes,
  resorption — each surface as a small marker.

###### Where the data comes from

Every entry comes from the per-tooth **Endodontic findings** and
**Radiographic findings** tabs (see [Per-Tooth Actions](../using/per-tooth-actions.md)).
Toggling the overlay on does not change the data — it only shows
it.

###### Use cases

* **Pre-RCT planning** — see every tooth that needs endo work on
  one screen.
* **Recall review** — quickly spot post-RCT teeth and check for
  new radiographic findings.
* **Specialist hand-off** — print the chart with this overlay on
  as a one-page summary to the endodontist.

###### Toggle

A toolbar button. No sheet — the data lives in the per-tooth
details panel.

\newpage

###### Occlusion Overlay

The occlusion overlay visualises the **occlusal relationship** of
the patient's bite — molar class, canine class, overjet, overbite,
crossbites, open bites, midline deviation — drawn on the arches.

###### What is drawn

* **Molar class** (Class I / II / III) — marker at the first
  molars on each side.
* **Canine class** (Class I / II / III) — marker at the canines on
  each side.
* **Overjet** — horizontal arrow at the incisors with the value
  in millimetres.
* **Overbite** — vertical arrow at the incisors with the value or
  percentage.
* **Crossbites** — flagged on the affected teeth.
* **Open bite** — flagged in the affected region (anterior or
  posterior).
* **Midline deviation** — small offset arrow showing direction
  and magnitude.

###### When to use it

* **Initial ortho assessment** — paints the malocclusion in one
  view.
* **Patient education** — the visual is easier than terminology
  for the patient.
* **Treatment progress** — comparing pre- and post-treatment
  snapshots with the overlay on shows the bite change
  immediately.

###### Toggle

Toolbar button. No sheet. Data comes from the orthodontic case
record and from observations recorded on the chart.

\newpage

#### Snapshots & Compare

Snapshots let you **freeze the chart on any date** and then
**compare two snapshots side-by-side** later — invaluable for
follow-up visits, before/after presentations, insurance claims,
and medico-legal records.

##### Saving a snapshot

Click **Save snapshot** in the toolbar.

* A confirmation appears: *"Save a snapshot of the chart as of
  today? A new snapshot point is created so you can use Compare
  later to see what changed."*
* Click **OK** — a snapshot marker is created for **today's date**.
* The new date appears in the **Snapshot dropdown**.
* A toast confirms: *"Snapshot saved for today."*

The snapshot is a **marker**, not a copy of the chart — it
references the procedures dated up to that day. So deleting a
snapshot does not delete procedures (see below).

##### Viewing a snapshot

Open the **Snapshot dropdown** in the toolbar. Pick any date:

* **Today** — live chart with every procedure including ones added
  today.
* **Any past snapshot date** — chart as it was on that date.

The chart redraws with only the procedures recorded up to (and
including) the picked date.

##### Comparing two snapshots

Click **Compare**:

* The Compare view opens with two arch-pair panels side-by-side —
  pick a *Left* date and a *Right* date from snapshot dropdowns
  on each panel.
* Procedures **added** between Left and Right are highlighted
  **green**.
* Procedures **removed** between Left and Right are highlighted
  **red**.
* Procedures that exist on both panels are drawn normally.

A tooltip on each diff shows what changed (procedure name,
surfaces, date).

##### Deleting a snapshot

Click **Delete snapshot** with a snapshot date selected.

> **Removes the snapshot MARKER for the currently-selected date.
> Real procedures dated the same day are NOT deleted.**

The confirmation popup makes the distinction explicit. If the date
was *only* a marker (no procedures dated that day), the date
disappears from the dropdown. If real procedures exist for that
day, those procedures are kept and the dropdown loses just the
marker.

This is by design — snapshot markers are organising hooks, not
data — and protects against accidentally deleting clinical
records.

##### Reload

After importing procedures from another system, or if something
looks off, click **Reload** — the chart recalculates from saved
procedures and re-applies the snapshot view.

##### Use cases

* **Follow-up appointments** — save a snapshot at the end of each
  major visit. Compare to the previous snapshot at the start of
  the next visit and explain to the patient what was done.
* **Ortho progress** — snapshot at every adjustment visit and
  compare across the entire treatment to show progression.
* **Insurance audit** — point in time evidence of what was
  recorded vs what was billed.
* **Patient handover** — when a patient transfers to another
  dentist, the snapshot list shows the chart history without
  needing the full procedure log.

##### Tips

* Save a snapshot at the **end** of each significant visit — it
  takes a second and gives you a clean before/after later.
* Use the **Print** button while viewing a past snapshot to print
  the chart as it was on that date.
* The snapshot dropdown is colour-coded by recency — today on
  top, older below.

\newpage

#### Demo Mode

**Demo mode** loads a realistic showcase case onto the chart so
you can present the system's full range — caries, restorations,
crowns, RCTs, extractions, implants, plus active treatment-plan
items — without touching any real patient data.

Click **Demo** in the toolbar to enable; click again to exit.

##### What loads

A representative case with **one of every procedure type** — so
the chart shows every icon and overlay element in a sensible
clinical context.

A confirmation toast appears:

> *"Loaded showcase case with one of each procedure type
> (no DB writes). Click Demo again to exit."*

While Demo mode is on, the chart's **alert area** displays a
*"Demo mode on"* badge so nobody mistakes the showcase chart for
a real patient.

##### Exiting

Click **Demo** again. The chart reverts to the real patient's
procedures and a toast confirms:

> *"Demo mode off — real patient procedures restored."*

##### Nothing is saved

* The showcase procedures **never touch the database**.
* The real patient's procedures are **never altered**.
* Snapshot dates are **not** modified by Demo mode.
* Closing the chart while Demo is on still leaves the real patient
  intact next time you open it.

##### Per-overlay Demo modes

Two overlays have their **own** Demo data:

* **[Periodontal](overlays/perio.md#demo-mode)** — Stage II
  generalised periodontitis with severe lower-posterior pocketing,
  BoP, mobility, furcation.
* **[Orthodontic](overlays/ortho.md#demo-mode)** — mock brackets,
  elastics, encounters, checklists, tasks, headgear, status flags.

Each overlay's Demo toggle is independent of the chart-wide Demo
button — you can demo perio without the chart-wide showcase, for
example.

##### Use cases

* **Sales presentation** — open the chart on any patient, hit
  Demo, walk the customer through the icons.
* **Training** — junior dentists practise on the showcase case
  without polluting real records.
* **Bug verification** — designers and engineers can reproduce
  layout / colour / overlay issues on the same canonical data set
  in every clinic.
* **Marketing material** — screenshots of the Demo case are safe
  to publish (no real patient).

##### What Demo does *not* hide

* The patient banner still shows the **real patient's** name and
  photo. Demo modifies the chart contents only — not the patient
  context.
* The toolbar / overlays / drawer still function exactly as they
  would on a real case.

So Demo is for **what the chart can show**, not for *"a different
patient"*.

\newpage

#### Printing & Export

The chart prints **cleanly** — no toolbar, no drawer, no menus.
Just the arches, the procedures, and the patient banner.

##### Print the chart

Click **Print** in the toolbar.

* The browser print dialog opens.
* The preview shows the chart-only layout — toolbar / sidebar /
  drawer all hidden.
* The active **dentition** (Adult or Pedo) and the active
  **overlays** are respected. So a chart printed with Plan +
  Perio overlays on will show the plan band and the perio
  overlay on the paper.
* Use the browser's **Save as PDF** option to export instead of
  print.

##### What appears on the printed page

* **Patient banner** — name, file number, age, gender, photo.
* **Arches** — adult or paediatric.
* **Procedures** with all icons.
* **Treatment-plan band** under each tooth.
* **Active overlays** (perio, ortho, plan, caries, endo / rg,
  occlusion) if turned on at print time.
* **Snapshot date** if a past snapshot is selected — the print
  reflects that date.
* **Today's date** at the bottom.

##### Print a past snapshot

To print the chart as it was on an earlier date:

1. Pick the snapshot date in the **Snapshot dropdown**.
2. Verify the chart shows the right state.
3. Click **Print**.

The print uses the snapshot view — useful for medico-legal
documents that need a chart from a specific past date.

##### Print with overlays on

To print a clinical-specific layout:

* Turn on only the overlays you want (e.g. **Caries** alone for
  a caries-only treatment plan).
* Turn off everything else.
* **Print**.

The result is a focused, single-purpose page — much easier to
hand to the patient or attach to a referral than a
"everything visible" print.

##### Patient documents (gallery)

The **Documents** toolbar button opens the patient's full DM2
gallery — every file ever attached to this patient.

From the gallery, individual images / PDFs can be:

* Printed (via DM2's viewer Print button).
* Downloaded.
* Sent to a compare panel.

See **[DM2](../dm2/index.md)** for the full gallery features.

##### Exporting an image of the chart

The cleanest path: use **Print  Save as PDF** and convert that PDF
to an image (if needed). The chart itself is rendered on a canvas,
so a *screenshot* (Windows snipping tool, Mac screen capture) is
also a valid export.

##### Sharing with patients

* **Print** + **hand to patient** at checkout — works in every
  clinic.
* **Print  Save as PDF** + **e-mail / WhatsApp** the file (via
  [Communicator](../communicator/index.md)) — paperless option.
* The Documents tab can also attach the PDF to the patient's file
  for next visit.

\newpage

###### Administration

The dental chart inherits most of its configuration from HMS itself
(procedure catalogue, price list, dentist list, room list). Only two
areas are configured at the chart level.

* **[Tooth Numbering](numbering.md)** — Universal vs FDI vs Palmer.
* **[Procedure Legend](legend.md)** — the catalogue of icons shown
  on the legend popup; what each one means.

###### Other administration done elsewhere in HMS

| Setting | Where |
|---|---|
| Procedure catalogue (the tools available in the toolbox) | HMS  Data Setup  Clinical  Procedures |
| Price list (per-procedure prices) | HMS  Data Setup  Billing  Price List |
| Dentists + their schedules | HMS  Data Setup  Staff |
| Rooms (chairs / operatories) | HMS  Data Setup  Organisation  Rooms |
| User permissions to chart / edit / delete | HMS  User administration |
| Default overlays per user | Per-user preferences, saved on first use |

###### Per-user preferences

Saved automatically on the chart:

* **Active overlays** at last close — re-opened in the same state.
* **Sidebar collapsed / expanded**.
* **Toolbox visible / hidden**.
* **Hints visible / hidden**.
* **Density / theme** preferences (light vs dark).

Nothing else needs to be configured per user — the chart picks up
defaults from HMS.

 Continue to **[Numbering](numbering.md)**.

\newpage

###### Tooth Numbering

The chart supports the three standard tooth-numbering systems used
worldwide. Pick the one your clinic teaches and prints; the chart
labels every tooth in the chosen system without re-mapping data.

###### Supported systems

###### Universal Numbering System (USA)

* **Adult** — 1 to 32 going clockwise from the upper-right third
  molar.
* **Paediatric** — A to T going clockwise from the upper-right
  second primary molar.
* Default in North-American clinics.

###### FDI Two-Digit System (ISO 3950)

* Each tooth has a **two-digit code** — first digit is the
  quadrant (1 upper-right, 2 upper-left, 3 lower-left, 4
  lower-right for adults; 5–8 for paediatric).
* Second digit is the tooth position within the quadrant (1 to 8).
* So upper-right central incisor is **11**, upper-left wisdom is
  **28**, lower-right primary first molar is **84**.
* Default in most of Europe and the Middle East.

###### Palmer Notation

* Quadrant grid — upper-right, upper-left, lower-left,
  lower-right.
* Adult teeth numbered 1–8 from the midline back.
* Paediatric letters A–E from the midline back.
* Tooth identifier is the number + a small bracket showing the
  quadrant.
* Still used in UK and some specialist practices (especially
  orthodontics).

###### Switching numbering systems

The active system is shown on every tooth label.

To change clinic-wide default, an administrator sets the
preference in HMS. Individual dentists can switch on their own
chart through a numbering control without losing or remapping
data — the same teeth are simply re-labelled.

###### Mixed use

If the dentist uses Palmer in conversation and FDI on paper, the
chart can be set to show *both* — primary label in one system and
a small secondary label in the other.

###### Reports & prints

The printed chart uses the **active** numbering at the time of
printing. If you print a historic snapshot in a different
numbering system from the one used when it was recorded, the
tooth identities are still correct — only the labels change.

\newpage

###### Procedure Legend

The **Procedure Legend** popup shows every icon used on the chart
with its meaning — a one-stop reference for new staff and for
patients asking *"what's that mark on tooth 16?"*

###### Opening the legend

Click **Legend** in the toolbar. A popup opens with the full
catalogue.

###### What it shows

The legend lists every procedure type — both **Status** and
**Operation** and **Root** groups — with:

* The **icon** as it appears on the chart.
* The **name** of the procedure.
* The **colour** (where applicable — many procedures are
  colour-coded for severity or status).
* A **short description** of when this icon is used.

It also explains the **treatment-plan band** colour code
(Existing / Planned / Completed / Referred) and the **per-tooth
markers** for clinical notes, images, endodontic findings, and
radiographic findings.

###### Why it's worth keeping open

* **New staff** — keep the legend popup pinned for the first
  week. After that they remember the icons.
* **Patient education** — turning the legend on next to the chart
  helps the patient follow what is being explained.
* **Audit** — when reviewing a chart from another dentist, the
  legend disambiguates icons.

###### Configuration

The legend reflects the **procedure catalogue** configured for the
clinic in HMS. Add a new procedure type to the catalogue and it
shows up in the legend automatically with its assigned icon.

Each procedure has:

* A **code** (the catalogue identifier).
* A **display name**.
* An **icon** (chosen from a library, or uploaded as a small SVG).
* An optional **colour modifier**.
* A **default class** (M / D / O / I / B / F / L / P) — or *none*
  for procedures that don't take a class.

Maintained in HMS  Data Setup  Clinical  Procedures.

###### Printing the legend

The legend popup has a **Print** button — useful for handing a
clean one-page reference to new staff or laminating for the
chairside reference card.

\newpage

#### Scheduler

The **Scheduler** is the clinic's appointment grid — the page the
front desk lives in all day. It shows every physician's day at a
glance, lets you find a patient in two keystrokes, drop them into a
free slot, move them around when something changes, and surfaces the
clinical context the receptionist needs to make a good booking
(allergies, balance, VIP status, no-show history).

##### What the screen shows

* A **toolbar** across the top with the day / week toggle, find,
  bulk-reschedule, full-screen, density, and light/dark switches.
* A **kebab menu** (three dots, top-left)  **Scheduler settings** —
  hours, days, rooms, breaks, holidays, categories, alerts.
* A **side bar** listing the physicians you want to see (with previous
  / next paging when you have more physicians than columns).
* The **main grid** — one column per physician (Day view) or one
  column per weekday for a single physician (Week view), with the
  hours of the day stacked vertically.
* A **status legend** along the bottom — click any status to hide or
  show those appointments.
* A **clipboard banner** that appears whenever you have an appointment
  "in hand" after Copy or Cut.

##### Two views

| View | Best for |
|---|---|
| **Day** | The day's plan across many physicians. Default for reception. |
| **Week** | One physician's whole week. Double-click any physician name in the side bar to jump here. |

##### Three modes

* **Comfort vs Compact** — toggles row height so more or fewer slots
  fit on screen. Persists per user.
* **Light vs Dark** — same data, eye-friendly evening look. Persists per
  user.
* **Focus (full-screen)** — hides every menu and header so the
  scheduler fills the whole window. Press once more to exit.

##### Why "V2"?

The current scheduler is the second-generation rewrite. The legacy
scheduler is still bundled for fall-back but is no longer the default
— this documentation covers V2 only.

 Continue to **[Getting Started](getting-started.md)**.

\newpage

#### Getting Started

Book your first appointment in under a minute.

##### 1. Pick the right view

The scheduler opens in **Day view** by default — perfect for
reception. If you want to see one physician's whole week instead,
click **Week** in the toolbar.

##### 2. Make sure the day is the day you want

Use the date picker (top-left of the grid) to jump to any day, or use
the arrow buttons to walk forward / back one day at a time.

##### 3. Pick the physicians you can see

The side bar lists every physician. If your clinic has more
physicians than columns fit on screen, use **Previous physicians** /
**Next physicians** to page through them. (How many columns to show
at once is in **Scheduler settings  Hours & Days**.)

##### 4. Find the patient

Click **Find** in the toolbar. Type any of:

* **Name** — first, family, or partial.
* **MRN / file number** — the patient's HMS file number.
* **Phone** — last 4 digits is usually enough.

Pick the patient from the result list. They are now your "selected"
patient for the next click.

##### 5. Drop them into a slot

Click an empty cell in the physician's column at the time you want.
The booking dialog opens pre-filled with patient + physician + time.
Pick:

* **Room** — the chair / consultation room.
* **Category** — the appointment type (Consultation, Follow-up, …).
* **Comment** — free text the dentist / doctor will see.

Save.

##### 6. Done

The cell is now filled, coloured by category. Hover it for a tooltip,
click it for the full event info panel on the right (allergies,
balance, VIP, no-show count). Right-click for Edit / Copy / Cut / Delete.

##### Common next moves

* **Move the appointment** — drag it to a different time, or right-click
   **Cut**, then click the new cell to paste.
* **Copy the patient into a second slot** — right-click  **Copy**,
  click the second cell.
* **Reschedule the rest of the day** because the physician is late —
  use [Bulk reschedule](using/bulk-reschedule.md).

 Continue to **[Day & Week views](using/views.md)**.

\newpage

###### Day & Week Views

The scheduler has two layouts. Both show exactly the same
appointments — only the slicing changes.

###### Day view

* One column per **physician**.
* Hours of the day stacked vertically.
* The header row shows physician name + room.
* Default view for reception — best for *"who is free at 2 pm?"*.

The number of physicians shown at once is set in **Scheduler
settings  Hours & Days  Number of physicians to show at once**. If
your clinic has more physicians than that, the **Previous physicians**
/ **Next physicians** buttons in the side bar page through the rest.

###### Week view

* One column per **weekday** for **one physician**.
* Hours of the day stacked vertically.
* Header row shows the dates of the week.
* Best for *"when is Dr X next available?"* or filling a single
  physician's week.

The fastest way to jump there: in Day view, double-click any
physician's name in the side bar. The scheduler flips to Week view for
that physician immediately.

You can also configure how many day columns to show (typically 5 for
weekdays-only or 7 for the full week) — **Scheduler settings  Hours &
Days  Number of day columns to show in Week view**.

###### What's the same in both views

* Click an empty cell  booking dialog.
* Click a booked cell  event info panel.
* Right-click a booked cell  Edit, Copy, Cut, Delete.
* Drag a booked cell to a new time  move (with conflict check).
* Status legend at the bottom controls visibility.

###### Toolbar modes

These three toolbar buttons change how the screen *looks*, not what it
*shows*:

| Button | What it does | Persists |
|---|---|---|
| **Focus** | Full-screen — hides the HMS top menu and side menu so the scheduler fills the window. Click **Exit** to come back. | No |
| **Compact / Comfort** | Compact = tighter rows, more slots on screen. Comfort = roomier rows, easier to read. | Yes (per user) |
| **Dark / Light** | Switches the scheduler colours between light and dark themes. | Yes (per user) |

 Continue to **[Find a Patient & Book](find-and-book.md)**.

\newpage

###### Find a Patient & Book

The fastest path from "patient calls" to "appointment in the grid" is
two clicks.

###### Find

Click **Find** in the toolbar (or press the keyboard shortcut your
admin configured). The patient picker opens with a single search box.

Search by any of:

* **Name** — first, family, or partial match.
* **MRN** — the patient's HMS file number (often the badge number).
* **Phone** — last 4 digits is usually unique enough.

The list narrows as you type. Pick the patient.

###### What if the patient isn't there?

* They've never visited the clinic  book the slot as a **walk-in**
  (skip the picker, just click the slot — the booking dialog lets you
  type the patient's name without linking to a file). The receptionist
  attaches a real file later via **Edit appointment**.
* They've visited a different branch — clear any branch filter at the
  top of the picker; the search runs across all branches.

###### Patient context shown in the picker

Each row shows: name, MRN, date of birth, mobile, last visit. Special
flags appear as small icons:

| Icon | Meaning |
|---|---|
| Heart | VIP patient — handle gently. |
| Triangle | Pending balance over the configured threshold — flag for the cashier before the visit. |
| Allergen symbol | Has documented allergies — the receptionist should remind the physician. |
| Person-x | High no-show count — consider asking for a deposit. |

###### Book

After picking the patient, click the empty cell you want — in the
right physician's column at the right time. The booking dialog opens
pre-filled.

Fill in:

* **From / To** — start and end time. The dialog snaps to the booking
  step set in **Scheduler settings  Hours & Days  Booking step**.
* **Room** — defaults to the physician's room if one is set.
* **Category** — Consultation, Follow-up, Cleaning, Emergency, ….
  Categories drive the appointment colour. List configured in
  **Scheduler settings  Categories**.
* **Reason** — short label that appears on the appointment card.
* **Comment** — longer free text the physician sees in event info.

Save.

###### What you see after save

The cell is filled and coloured by category. Hovering shows a
tooltip; clicking shows the full **Appointment Information** panel
with allergy / balance / VIP / no-show flags. Right-click for
Edit / Copy / Cut / Delete.

 Continue to **[Move, Copy, Paste](move-and-paste.md)**.

\newpage

###### Move, Copy & Paste

There are three ways to move an appointment. Pick whichever is
fastest for the situation.

###### Drag

Click and hold an appointment, drag it to the new time / physician,
release. Best for **small adjustments within the same day**.

The drag handle snaps to the booking step (configured in **Hours &
Days**). If the drop conflicts with an existing booking, the
[Conflict modal](conflicts.md) opens and offers Cancel, Overwrite,
or Move both.

###### Cut and paste

Right-click the appointment  **Cut**. The cell goes pale and a
**clipboard banner** appears at the top of the screen reminding you
that an appointment is "in hand". Click the new cell — the appointment
is removed from the old slot and dropped into the new one.

Use this when the new slot is on **another day or far across the
grid** — easier than a long drag.

###### Copy and paste

Right-click  **Copy** instead of Cut. Now every cell you click
pastes a copy of the patient and the appointment template until you
press Escape or right-click  **Clear clipboard**.

Use this when you need to book **several follow-up sessions** for the
same patient in one go.

###### Drag a physician's day

To move every appointment for one physician at once, use the
[Bulk reschedule](bulk-reschedule.md) toolbar button. It is faster
and safer than dragging dozens of cells.

###### Cancel a paste

* Press **Escape**, or
* Click the **X** on the clipboard banner, or
* Right-click anywhere  **Clear clipboard**.

The original (for Cut) is restored if you cancel before pasting.

 Continue to **[Conflicts](conflicts.md)**.

\newpage

###### Conflicts

When you drop an appointment onto a time that already has bookings, the
scheduler does **not** silently overwrite — the **Conflict** dialog
opens and shows you exactly what would clash.

###### What the dialog shows

A card for each conflicting appointment, with:

* Patient name + MRN
* Time (from – to)
* Physician
* Room
* Status
* Reason

The card at the top is the appointment **you are placing**. The cards
below are what is already in those slots.

###### Your choices

| Action | Effect |
|---|---|
| **Cancel** | Closes the dialog. Nothing changes. The clipboard is preserved if you cut. |
| **Overwrite** | Deletes the conflicting appointments and places yours. Use sparingly — those patients are now unbooked. |
| **Move both** *(when possible)* | Puts yours in and bumps the conflicting one(s) to the next free slot. |

###### Bulk paste conflicts

If you paste several appointments in a row and one of them conflicts,
the dialog shows that *one* conflict. Resolve it and the paste
continues automatically.

###### Why the dialog appears even when slots "look" free

* The slot might be a **break** or **blocked time** the physician
  configured.
* The slot might be inside a **holiday**.
* Another receptionist might have booked it 5 seconds before you (the
  scheduler refreshes on every action).

In all three cases the conflict dialog tells you exactly which kind of
conflict it is.

 Continue to **[Bulk reschedule](bulk-reschedule.md)**.

\newpage

###### Bulk Reschedule

When a physician runs late, gets called away, or wants to flip rooms,
moving the day's appointments one by one is painful. **Bulk
reschedule** does it in one operation.

###### Open

Click **Bulk** in the toolbar.

###### What you choose

| Field | Meaning |
|---|---|
| **From physician** | Whose appointments to move. |
| **On date** | Which day's appointments to consider. |
| **Move to physician** | (Optional) The other physician to take the patients. Leave blank to keep the same physician. |
| **Shift by** | Minutes to shift each appointment forward (positive) or back (negative). E.g. `+30` pushes the whole day half an hour later. |
| **Shift to date** | (Optional) Move the day's appointments to a different date entirely. |

###### Run

Click **Save**. The scheduler:

1. Validates each move against breaks, holidays, and existing
   appointments.
2. If any of the moves would conflict, opens the **Conflict** dialog
   listing every clash. You can cancel, overwrite, or skip per row.
3. Applies the rest atomically — either every appointment moves or
   none of them do.

###### Use cases

* **Doctor is 30 minutes late**  Shift by `+30`.
* **Doctor swapping rooms with a colleague**  set *Move to physician*
  to the other physician. The day moves columns.
* **Public holiday declared on short notice**  Shift to date = next
  open day. Patients are notified by the standard reminder flow.

###### Tip

Bulk reschedule respects the **status filter** at the bottom of the
grid — hide *Cancelled* and *No-show* statuses first if you only want
to move appointments that are still live.

 Continue to **[Block Time](block-time.md)**.

\newpage

###### Block Time

A **Block** is a stretch of time on a physician's calendar that is
**not bookable** — meetings, theatre, surgery slots, training,
leave-of-absence. They show as striped grey bands on the grid and the
booking dialog refuses to place a patient inside them.

###### Add a block

Right-click an empty cell  **Block this time** (or open the Block
dialog from the kebab menu  **Breaks**).

Fill in:

| Field | Meaning |
|---|---|
| **Physician** | Whose calendar the block applies to. |
| **Room** | (Optional) Block only one room — leave blank to block all rooms. |
| **Date from / Date to** | The block's date range (use the same date in both for a single-day block). |
| **Time from / Time to** | The hours within each day that are blocked. |
| **Reason** | Free text shown in the cell tooltip — e.g. *Theatre*, *Conference*. |

Save. The block appears immediately as a grey striped band.

###### Edit / Remove a block

Open the kebab menu  **Breaks**. Every block is listed with Edit and
Remove links. Editing reopens the same dialog; removing deletes the
block (existing appointments inside the same hours are not touched —
just no longer striped).

###### Recurring blocks

For weekly recurring blocks (e.g. *every Wednesday 14:00 – 16:00:
team meeting*):

* Set Date from to the first Wednesday and Date to to a long horizon
  (e.g. end of year).
* The system applies the block on **every** weekday that falls in the
  range and matches the time window — for a true weekly recurrence
  combine this with the working-day toggles in **Hours & Days**.

###### Difference vs Breaks

* A **Break** is the same idea but configured globally under
  **Scheduler settings  Breaks** — typically lunch, prayer time. It
  applies to *all* physicians automatically.
* A **Block** is one physician's calendar entry that you add ad-hoc
  from this dialog.

###### Difference vs Holidays

* A **Holiday** blocks the entire clinic on that date — no physician
  works. Configured under **Scheduler settings  Holidays**.

 Continue to **[Event Info Panel](event-info.md)**.

\newpage

###### Event Info Panel

Click any booked cell to open the **Appointment Information** panel on
the right. It is the single place that pulls together everything the
front desk needs to know before the patient walks in.

###### What it shows

* **Patient** — name, MRN, photo (if on file).
* **Time** — from / to, duration.
* **Physician**.
* **Room**.
* **Category** with its colour swatch.
* **Reason** (short label).
* **Comment** (longer note from whoever booked it).
* **Status** — Pending, Confirmed, Arrived, In-Service, Completed,
  No-show, Cancelled.

###### Flags & alerts

The top of the panel highlights anything the receptionist should not
miss.

| Flag | Meaning |
|---|---|
| **VIP patient** | The patient is flagged as VIP — small dot on the cell, banner on the panel. Handle gently. |
| **Allergy** | Known allergies — review patient chart. The cell shows a small symbol. |
| **Pending balance over threshold** | The patient owes more than the configured threshold; flag for the cashier before the visit. |
| **No-show history** | Past missed appointments (count). Bands shown on the panel. |
| **Procedure has instructions — see event info panel** | The booking has special prep instructions (e.g. fasting, take medication). |
| **Walk-in — patient not yet registered. Edit the appointment to attach a patient file.** | The appointment was created without linking to a patient file. Click **Edit** to find or create the file. |

These flags come from your **[Alerts](../configuration/alerts.md)**
configuration — turn them on / off and set thresholds there.

###### Quick actions

The panel's footer has the same actions as the right-click menu:

* **Edit** — opens the booking dialog.
* **Cancel edit** — discards changes.
* **Delete** — removes the appointment after a confirm.
* **Status** — quick-set Arrived / In-Service / Completed / No-show
  without opening the full editor.

 Continue to **[Scheduler Settings](../configuration/index.md)**.

\newpage

###### Scheduler Settings

Open **Scheduler settings** by clicking the **kebab menu** (three dots,
top-left of the scheduler)  **Scheduler settings**.

The settings dialog is organised into ten tabs. Use this overview to
pick the right tab; each one has its own page below.

| Tab | What it sets | Stored where | Page |
|---|---|---|---|
| **Display** | Theme, density, full-screen | Per user | [Display](display.md) |
| **Filters** | Which appointment statuses are visible | Per user | [Filters & Statuses](filters-and-statuses.md) |
| **Hours & Days** | Clinic open / close times, booking step, working days, columns | Per clinic | [Hours & Days](hours-and-days.md) |
| **Alternative** | Special hours during a date range (Ramadan, summer) | Per clinic | [Alternative Hours](alternative-hours.md) |
| **Rooms** | Treatment rooms with per-room day-of-week availability | Per clinic | [Rooms](rooms.md) |
| **Breaks** | Recurring or one-off breaks blocked across the day | Per clinic | [Breaks](breaks.md) |
| **Holidays** | Fixed and annual closures | Per clinic | [Holidays](holidays.md) |
| **Categories** | Appointment categories with their colours | Per clinic | [Categories & Colours](categories-and-colors.md) |
| **Alerts** | Wait threshold + no-show banding + balance threshold | Per clinic | [Alerts](alerts.md) |
| **System** | Release, version, app name, current user (read-only) | — | — |

!!! tip "Per-user vs per-clinic"
    The **Display** and **Filters** tabs save automatically and only
    affect your own screen. Every other tab saves to the clinic
    configuration — your changes apply to **everyone in the clinic**
    the next time their scheduler loads.

!!! warning "Permission"
    Saving anything outside **Display** and **Filters** needs the
    *Scheduler administrator* permission. Without it, those tabs open
    in read-only mode.

\newpage

###### Display

Per-user appearance settings. Save automatically when you change them.

###### Color theme

| Option | When to pick it |
|---|---|
| **Light** | Bright clinics, daytime use. |
| **Dark** | Dim reception, evening shifts, less eye strain. |

The toolbar **Dark / Light** button toggles between the two — both
controls do the same thing.

###### Row density

| Option | When to pick it |
|---|---|
| **Compact** | Big appointment days; you want to see more slots at once. |
| **Comfort** | Default; easier to read. |

The toolbar **Compact / Comfort** button toggles between the two.

###### Focus (full-screen) mode

When on, the HMS top bar and side menu hide so the scheduler fills the
whole window. Click **Exit** in the toolbar (or press the same button
again) to come back.

Unlike Theme and Density, **Focus is per-session, not persisted** —
the next time you open the scheduler it starts in normal mode.

\newpage

###### Filters & Statuses

Controls which appointments appear in the grid based on their status.

###### Show appointments with status…

A list of every appointment status with a checkbox. Tick to show, untick to hide. The legend at the bottom of the grid is the same list — clicking a legend swatch toggles the matching checkbox.

Typical statuses:

* **Pending** — booked but not yet confirmed.
* **Confirmed** — patient confirmed (often by SMS reply).
* **Arrived** — patient has checked in at reception.
* **In-Service** — patient is currently with the physician.
* **Completed** — visit finished.
* **No-show** — patient did not turn up.
* **Cancelled** — appointment cancelled.

!!! tip
    Hide **Completed**, **No-show**, and **Cancelled** to keep the grid
    focused on what's still live today.

###### Reset to default visible statuses

Click **Reset to default visible statuses** to bring back the
out-of-the-box visibility (typically: Pending, Confirmed, Arrived,
In-Service).

###### Filter mode (read-only)

Shown for reference only — it tells you which filter logic the clinic
is using globally (e.g. *Hide cancelled by default*, *Show everything*).
The setting itself is in the clinic's global configuration, not editable
from here.

\newpage

###### Hours & Days

The clinic's standard working hours, days, and grid sizing.

###### Hours

| Setting | Meaning |
|---|---|
| **Clinic opens at (hour, 0–23)** | First bookable hour of the day. |
| **Clinic closes at (hour, 0–24)** | Last bookable hour of the day. Use 24 for midnight. |
| **Booking step (minutes)** | The increment for booking — 15, 20, 30. Every cell in the grid is one step. |
| **Scroll-to hour on open (start)** | What hour the grid scrolls to when you first open the scheduler. |
| **Scroll-to hour on open (end)** | The bottom of the initial scroll window. |
| **Lunch / midday gap 1 (minutes)** | A visual gap inserted at the lunch hour — purely cosmetic. |
| **Lunch / midday gap 2 (minutes)** | Optional second gap for clinics with two midday breaks (e.g. prayer + lunch). |
| **Show all working hours** | When ticked, the grid shows every hour from open  close on first load (overrides the *Scroll-to* settings). |

###### Working days of the week

A row of seven day toggles — Sat, Sun, Mon, Tue, Wed, Thu, Fri (order
depends on locale). Tick the days the clinic is open. Non-working days
are greyed out and refuse bookings.

###### Calendar options

| Setting | Meaning |
|---|---|
| **Number of physicians to show at once** | How many physician columns fit on screen in Day view. Use **Previous / Next physicians** to page through the rest. |
| **Number of day columns to show in Week view** | Usually 5 (work-week) or 7 (full week). |

###### Tips

* If the receptionist regularly scrolls back to early morning slots,
  set **Scroll-to hour on open (start)** to the earliest expected
  booking — saves a daily scroll.
* The **Booking step** also controls how drag-and-drop snaps. Smaller
  step = finer precision; larger step = harder to mis-click.

\newpage

###### Alternative Hours

Some clinics shift their hours for a few weeks or months (Ramadan,
summer, winter break). Instead of editing the main hours and remembering
to put them back, use **Alternative Hours** — a parallel schedule that
takes over for a date range, then automatically reverts.

###### Fields

| Setting | Meaning |
|---|---|
| **Use alternative hours** | Master switch. Off = ignore everything below. |
| **Alternative hours — start date** | First day the alt schedule applies. |
| **Alternative hours — end date** | Last day the alt schedule applies. |
| **Alt-opens at (hour, 0–23)** | Open hour during the alt window. |
| **Alt-closes at (hour, 0–24)** | Close hour during the alt window. |
| **Alt-gap 1 (minutes)** | Lunch / midday gap during the alt window. |
| **Alt-gap 2 (minutes)** | Optional second alt gap. |

###### How it interacts with regular hours

* Inside the alt window  alt hours win, regular hours are ignored.
* Outside the alt window  regular hours apply, alt settings are
  ignored.
* Working-day toggles (Sat, Sun, …) come from **Hours & Days** in both
  cases — there is no separate alt day-of-week list.
* Booking step comes from **Hours & Days** in both cases.

###### Use cases

* **Ramadan** — open 21:00 – 01:00 for one month.
* **Summer school break** — earlier opening (07:00 – 14:00) for July /
  August.
* **Winter Holidays** — shortened day (10:00 – 16:00) for a week.

###### Tip

Set up the next Ramadan schedule at the start of the year and leave
it in place — the **Use alternative hours** master switch lets you
toggle the whole thing on and off without re-entering dates.

\newpage

###### Rooms

The list of physical treatment rooms / consultation rooms / chairs the
clinic books patients into. Every appointment carries a room so the
patient (and the cleaner) know where to go.

###### What you see

A list, one row per room. Above the list a counter — *Treatment
rooms — N configured*.

###### Add a room

Click **New Room**. The editor opens with:

| Field | Meaning |
|---|---|
| **Room #** | The room number. Must be unique. |
| **Name (EN)** | The room's English name (printed on the appointment slip). |
| **الاسم** | The room's Arabic name. |
| **Doc ID** | (Optional) Default physician for this room — appointments booked in this room default to this physician. |
| **Type** | (Optional) Room type code — used in some reports. |
| **Day-of-week toggles** | A row of seven day buttons — tick the days this specific room is in use. Leave them all on for a "always available" room. |

Save. The room is immediately available on the booking dialog and in
the rooms picker.

###### Edit / Delete

Each row has **Edit** and **Delete** links. Editing reopens the same
editor. Delete asks for confirm — rooms that have past appointments
are kept in the database for audit but no longer appear on the
booking dialog.

###### Tips

* Set **Doc ID** for chairs that are *always* used by one dentist —
  every booking in that chair pre-selects them.
* Use the day toggles for a room that is only available on certain
  days (e.g. a mobile X-ray that comes in twice a week).

\newpage

###### Breaks

Recurring or one-off slots of time that are **not bookable** for the
whole clinic — typically lunch, prayer time, mandatory staff meetings.

A break is different from a [Block](../using/block-time.md): a Block
is one physician's calendar entry; a Break applies to every physician
in the clinic.

###### What you see

A list with a counter at the top — *Breaks & blocked time — X of Y
shown* — and a filter box to narrow it down by physician or reason.

Each row shows: physician (or *All*), room (or *All*), date range,
time range, reason, Edit and Remove links.

###### Add a break

Click **New Break**. Fill in:

| Field | Meaning |
|---|---|
| **Physician** | The physician the break applies to. Pick *All* for a clinic-wide break (lunch / prayer). |
| **Room** | (Optional) Only block a specific room — leave blank for all rooms. |
| **Date from / Date to** | The range of days the break is in effect. Use the same date in both for a one-off. |
| **Time from / Time to** | The hours within each day. |
| **Reason** | Free text shown in the cell tooltip — e.g. *Lunch*, *Prayer*, *Staff meeting*. |

Save. Cells inside the break are now striped grey and refuse bookings.

###### Recurring weekly break

The classic *every weekday 13:00 – 14:00 = lunch* break:

* Pick *All* physicians, *All* rooms.
* Date from = today, Date to = end of year (or further).
* Time from = 13:00, Time to = 14:00.
* Reason = *Lunch*.

The break applies on every working day in the range (working days are
set in [Hours & Days](hours-and-days.md)).

###### Edit / Remove

Use the per-row links. Removing a break frees up those slots
immediately for new bookings — existing appointments inside the
window are kept as-is.

\newpage

###### Holidays

A **Holiday** closes the entire clinic on a given date — no physician
works, no bookings accepted, the whole day shows as struck-through on
the grid.

###### What you see

A list of every holiday with its date, name, and whether it is annual.

* *No holidays configured.* — if the list is empty.

###### Add a holiday

Click **New Holiday**. Fill in:

| Field | Meaning |
|---|---|
| **Date** | The day the clinic is closed. |
| **Name** | Free text — e.g. *National Day*, *Eid Al Fitr Day 1*. |
| **Annual** | When ticked, the holiday repeats every year on the same Gregorian date (use for fixed-date holidays like New Year's Day). For Hijri-calendar holidays, leave Annual off and add a fresh row each year. |

Save. The day greys out across the whole grid immediately.

###### Edit / Remove

Each row has Edit and Remove links. Removing a holiday opens that day
for bookings again; existing appointments on the day (if any) are not
deleted.

###### Tips

* Plan the year ahead — bulk-add every public holiday in January so
  receptionists never accidentally book a closed day.
* For multi-day holidays (Eid, end-of-year), add one row per day. There
  is no "range" mode — each closed day is its own entry.

\newpage

###### Categories & Colours

Up to **12 appointment categories**, each with its own colour. The
colour is what fills the cell on the grid — so the receptionist
recognises an emergency vs a routine cleaning at a glance.

###### What you see

A 12-row table. Each row has the category **name** and a **colour
swatch**.

###### Editing

The table is **read-only** in the standard settings dialog — the
clinic configuration team sets the categories and colours during
implementation. To request a change:

* Add a new category  contact the system administrator (they update
  the master clinic configuration).
* Change a colour  same — the swatch palette is managed centrally so
  every clinic in a group uses the same colour for the same category.

###### Choosing colours

Some guidance from clinics that have shipped this for years:

* **Reserve red for Emergency** — receptionists instinctively look for
  it.
* **Use a muted colour for the most common category** — *Routine
  follow-up* in pale blue keeps the grid calm.
* **Pick distinct colours for adjacent categories** — pale-blue
  follow-up next to pale-green check-up is hard to tell apart on a
  small screen.
* **Don't use grey** — grey is reserved for breaks and blocks.

###### Where the colour shows up

* Cell fill on the grid.
* Swatch on the **event info panel**.
* Swatch in the booking dialog's category picker.
* Legend at the bottom of the grid (clicking the swatch toggles
  visibility — see [Filters & Statuses](filters-and-statuses.md)).

\newpage

###### Alerts

Thresholds that drive the **flags on the event info panel** and the
**icons on appointment cards**. Tune these once for the clinic and
every receptionist sees consistent warnings.

###### Wait threshold

How long a patient is considered "waiting" before the scheduler shows
a warning band. Typical values: 15 – 20 minutes.

If a patient has status **Arrived** and the configured wait threshold
elapses without moving to **In-Service**, the cell gets a warning band
and the patient appears on the front-desk *patients waiting*
dashboard.

###### No-show banding

Patients with a history of missing appointments get a coloured band
that scales with the count. Configure the bands:

| Band | Default range | Meaning |
|---|---|---|
| **None** | 0 missed | No flag. |
| **Yellow** | 1 – 2 | Cautionary — receptionist may want to send a reminder the day before. |
| **Orange** | 3 – 4 | Strong — consider asking for confirmation. |
| **Red** | 5+ | High-risk — clinic policy may require a deposit. |

Edit the cut-off counts to match the clinic's policy.

###### Pending balance threshold

The amount above which an outstanding patient balance triggers the
*Pending balance over threshold* flag on the event info panel. Set this
to the value where the receptionist should hand the patient to the
cashier **before** the visit (rather than after).

The flag also adds a small icon on the appointment card so the
receptionist sees it without opening the panel.

###### How alerts and flags work together

| Source | Where it shows |
|---|---|
| **Allergy** flag | Pulled from the patient's chart. Card icon + panel banner. |
| **VIP** flag | Patient profile flag. Card icon + panel banner. |
| **Pending balance** | Set by the threshold here. Card icon + panel banner. |
| **No-show band** | Computed from past appointments + bands above. Panel band only. |
| **Wait threshold** | Computed from arrival time + threshold above. Card band only. |
| **Procedure has instructions** | Pulled from the booked procedure (if it carries prep instructions). Panel banner only. |

\newpage

#### Clinic Reception

**Clinic Reception** is the receptionist's home screen. From this one
window the receptionist can find the patient, open their chart, create
a visit, take a payment, print a receipt, issue a prescription, and
book the next recall — without hopping between modules.

##### The toolbar at a glance

The top toolbar groups every common front-desk action into 14 buttons,
laid out left  right in the order a typical visit happens:

| Section | Buttons |
|---|---|
| **Find the patient** | Finger Print Scan · Select Patient |
| **Patient file** | Edit Patient · Open Patient File · Dental Chart · Treatment Plans |
| **Create activity** | New Visit · New Appointment · New Patient · New Recall |
| **Prescriptions** | Prescriptions History · New Prescription |
| **Money** | New Receipt · New Bill |

A **green banner** across the top always shows the currently-selected
patient — name, file number, date of birth, allergies, and the
fingerprint status. If no patient is selected the banner reads
*Fingerprint Patient* and prompts you to either scan a print or use
**Select Patient**.

The **Patient Toolbox** on the right edge of the screen surfaces extra
shortcuts (medical history, alerts, attachments) that change based on
who is selected.

##### How to open it

From the HMS main menu open **Clinic Reception**, or pin the shortcut
to the launcher for one-click access.

 Next: **[Getting Started](getting-started.md)** — walk through a full
patient visit, start to finish.

\newpage

#### Getting Started

A typical dental-clinic visit, step by step, from the moment the
patient walks in to the moment they leave with a printed receipt.

!!! tip "Keep one hand on the fingerprint reader"
    90 % of returning patients are found in under a second by simply
    asking them to place a finger on the reader. Use **Select Patient**
    only for first-time visitors and walk-ins without a fingerprint on
    file.

##### 1. Find the patient

* **Returning patient**  ask them to scan their fingerprint
  (**Finger Print Scan** button). The banner fills with their details.
* **New patient**  click **New Patient** (see step 2).
* **Anything else**  **Select Patient** opens a searchable picker
  (name, file number, mobile, national ID).

##### 2. (First visit only) Create the patient file

Click **New Patient**. Fill in the personal tab (name, gender, date of
birth, nationality, marital status), the contact tab (mobile, e-mail,
address), and the medical-history tab (allergies, chronic conditions,
current medications). Save.

The patient now appears in the banner and is the *current patient* for
every other toolbar button.

##### 3. Open the patient's full file (optional)

**Open Patient File** opens the patient's complete clinical workspace
in a new window — useful when the dentist asks you to print old
X-rays, lab results, or the previous treatment plan.

##### 4. Create today's visit

Click **New Visit**. The visit form opens pre-filled with the patient
and today's date. Pick the treating dentist, the room, and the visit
type (consultation, follow-up, emergency). Save.

This creates the bill header — every procedure the dentist performs
during the visit is charged to it.

##### 5. Show the Dental Chart

Click **Dental Chart**. The chart opens to today's visit. The dentist
clicks teeth, picks conditions and treatments, and saves. Every
treatment they tick becomes a line on the visit bill automatically.

##### 6. Review the Treatment Plan

Click **Treatment Plans** to show the running plan for this patient —
treatments that were proposed on previous visits, with their status
(planned / in-progress / completed) and their cost.

##### 7. Issue a prescription (if needed)

Click **New Prescription** to write a prescription. The drug picker
checks the patient's allergies and current medications and warns about
interactions.

* **Prescriptions History** opens every prescription this patient has
  ever received — useful for refill questions.

##### 8. Print the receipt and the bill

* Click **New Receipt** to take a payment (cash, card, insurance
  co-pay). Pick the method, enter the amount, save. A printable
  receipt opens.
* Click **New Bill** to print the full itemised bill (useful when the
  patient asks for one for insurance reimbursement).

##### 9. Schedule the recall

Click **New Recall** to book the next routine appointment (cleaning,
follow-up). The recall is added to the patient's schedule and a
reminder is queued for the configured channel (SMS, e-mail, or both).

##### 10. Done

The patient leaves. The banner stays on them until the next patient
scans a fingerprint — useful if you forgot to print something on the
way out.

 See the per-action detail pages under **Workflows** in the left
sidebar.

\newpage

###### Finding a Patient

There are three ways to put a patient into the banner — pick the
fastest one available for the person in front of you.

###### Finger Print Scan

Place the patient's finger on the reader and click **Finger Print
Scan**. The system looks the print up in the central biometric store
and, on a match, fills the banner with that patient.

If the reader returns *No match*:

* The patient has never registered a print — see **Patient Toolbox 
  Enrol Fingerprint** to capture it on the spot.
* The print quality was poor — wipe the reader and try a different
  finger.

###### Select Patient

Opens the patient picker. Search by:

* **Name** — first, middle, last, or any partial match.
* **File number** — the printed badge / card number.
* **Mobile** — last 4 digits is usually enough.
* **National ID / Passport**.
* **Date of birth**.

Tip: filter by **Branch** at the top of the picker to limit the list to
your clinic.

###### Walk-in / unknown patient

If the person has never visited any branch before, skip straight to
**[New Patient](new-patient.md)** — the first save creates the file and
selects them in the banner in one step.

###### What "selecting a patient" actually does

Every other toolbar button operates on **the patient currently in the
banner**. Selecting a new patient:

* Updates the banner.
* Pre-fills patient-context fields on every form you open afterwards.
* Refreshes the **Patient Toolbox** on the right with this patient's
  alerts, attachments, and quick actions.

It does **not** open any patient screen on its own — that needs an
explicit toolbar click (Edit, Open File, Dental Chart, …).

\newpage

###### New Patient

Click **New Patient** to register someone visiting for the first time.

###### What you fill in

###### Personal

* Full name (English and Arabic where applicable).
* Date of birth, gender, marital status.
* Nationality, religion.
* Photo (optional — drag any image into the photo box).

###### Contact

* Mobile, e-mail, address, P.O. Box.
* Emergency contact (name, relation, phone).

###### Medical

* Allergies (drug and non-drug).
* Chronic conditions.
* Current medications.
* Notes the dentist should see (recent surgery, pregnancy, anticoagulants).

###### Insurance

If the patient has a card from a payer the clinic contracts with, add
the card number, validity, and co-pay tier here. The payer becomes the
default guarantor on every bill until you change it.

###### After save

* The new patient is selected in the banner — you can go straight to
  **New Visit**, **Dental Chart**, or **New Appointment**.
* A file number is allocated automatically.
* The patient is now searchable across all clinic front desks.

###### Edit Patient

After save, **Edit Patient** opens the same form back up to correct
anything. The original creation date and the user who created it are
kept in the audit trail.

\newpage

###### New Visit

A **Visit** represents one in-person attendance at the clinic. It is
the container that holds the chart entries, prescriptions, lab
referrals and the bill for that day.

###### Open

Click **New Visit** with the patient already in the banner.

###### What you fill in

* **Date / time** — defaults to now.
* **Visit type** — Consultation, Follow-up, Emergency, Cleaning, Check-up,
  Cosmetic.
* **Dentist** — the treating doctor.
* **Room** — the chair / operatory.
* **Referred by** — if the patient was sent by another clinic.
* **Chief complaint** — short free-text on why they are there today.

###### Save

Saving the visit:

* Creates a bill header against this visit.
* Makes the visit selectable in the Dental Chart's *Visit* dropdown.
* Adds the visit to the dentist's daily roster.

###### What happens during the visit

The dentist works in the **Dental Chart** (next page). Every procedure
they tick on a tooth flows into:

* The chart history (visible from now on).
* The visit's bill (price taken from the price-list).
* The treatment plan if it is part of one.

###### Closing the visit

When the patient is finished, the receptionist takes payment via **New
Receipt** and (optionally) prints the bill via **New Bill**. There is
no separate *Close Visit* button — the visit is implicitly closed when
no more procedures are added to it.

\newpage

###### Dental Chart

The **Dental Chart** is the dentist's main working surface. Click
**Dental Chart** on the front-desk toolbar to open it for the patient
in the banner.

###### Layout

The chart shows the patient's mouth as **two arches** (upper and
lower), each with adult and deciduous teeth. Around the chart:

| Area | What it does |
|---|---|
| Top toolbar | Switches the active visit, switches between Adult / Child / Perio / Ortho views, prints, sends to imaging. |
| Left tool palette | Conditions (caries, fracture, missing, …), treatments (filling, extraction, crown, root canal, …), notes. |
| Right side panel | Material picker — selects amalgam, composite shade, alloy, etc. for whichever treatment was last picked. |
| Bottom history strip | A scrollable timeline of every previous entry on the selected tooth. |

###### Working a tooth

1. Click the tooth (or a specific surface — mesial, distal, occlusal,
   buccal, lingual).
2. From the left palette pick a **condition** (what is wrong) or a
   **treatment** (what you are doing about it).
3. Pick the **material** from the right panel if the treatment needs
   one.
4. The chart updates immediately — coloured marks show the new state,
   and the entry is added to the visit's procedure list.

###### What flows where

Every chart entry creates:

* A clinical note on the tooth (visible in the bottom history strip and
  on every future chart open).
* A line on the **current visit's bill** at the price-list rate.
* A line on the **Treatment Plan** if the treatment is part of one.

###### Special views

* **Adult chart** — 32 permanent teeth.
* **Child chart** — 20 deciduous teeth.
* **Perio chart** — pocket-depth, bleeding, recession, mobility.
* **Ortho chart** — bracket / wire / appliance tracking.

Switch views with the toolbar buttons; the underlying patient is the
same.

\newpage

###### Treatment Plans

A **Treatment Plan** is the longer-term care roadmap for a patient —
the set of procedures the dentist agreed to do over the coming
weeks or months. Click **Treatment Plans** on the front-desk toolbar to
open it.

###### What you see

A single screen split into three areas:

| Area | What it shows |
|---|---|
| **Header** | Patient, plan name, total estimated cost, total paid so far, status. |
| **Procedures grid** | One row per planned procedure — tooth, treatment, dentist, planned date, estimated cost, status. |
| **Status panel** | Counts of Planned / In-Progress / Completed / Cancelled, and a progress bar. |

###### Statuses

* **Planned** — agreed with the patient; not yet started.
* **In-Progress** — partly done over more than one visit (e.g. root
  canal + post + crown).
* **Completed** — finished and signed off.
* **Cancelled** — declined by the patient or no longer indicated.

###### How rows get there

Treatments are usually added from the **Dental Chart**: when the
dentist ticks a procedure the chart asks *Add to plan?* If they say
yes, the row appears here. They can also be typed in directly from the
plan grid.

###### Acceptance & consent

* Print the plan from the **Print** button as a patient-facing quote.
* Once the patient signs, mark the plan **Accepted** — the header
  status changes and the plan total locks in (price changes after
  acceptance need an override).

###### Tip

Use **Treatment Plans** before quoting a major case (full-mouth
rehabilitation, implants, orthodontics) so the patient sees the whole
journey and the total cost up front — it cuts last-minute drop-outs.

\newpage

###### Appointments & Recalls

Two toolbar buttons drive the booking diary: **New Appointment** and
**New Recall**.

###### New Appointment

Click **New Appointment** when the patient wants a specific date and
time for the next visit.

* Pick the **dentist**.
* The diary pops up showing that dentist's free slots — green = free,
  red = booked, grey = blocked / out.
* Click a slot. Set **duration**, **room**, **reason**.
* Save — the slot turns blue and an SMS / e-mail confirmation goes out
  if the patient has consented to reminders.

The appointment is now visible on:

* The dentist's daily roster.
* The patient's file (Appointments tab).
* The front-desk wall display (if configured).

###### New Recall

A **Recall** is a softer booking — *come back in 6 months for a
cleaning* — without committing to a specific slot yet. Click **New
Recall**.

* Pick the **reason** (Cleaning, Follow-up, Annual check-up,
  Orthodontic check, …).
* Pick the **due month** (or due date if you want to be precise).
* Pick the **reminder channel** (SMS, e-mail, both, none).
* Save.

When the due date approaches, the recall list (in the Recalls module)
shows the patient. The receptionist then turns the recall into a real
appointment with **New Appointment** above.

###### Cancelling / rescheduling

Open the appointment from the diary, click **Cancel** or drag it to a
new slot. The patient gets a fresh notification automatically.

\newpage

###### Prescriptions

Two toolbar buttons handle prescribing: **New Prescription** to write
one, **Prescriptions History** to review what was prescribed before.

###### New Prescription

Click **New Prescription**.

* The drug picker shows the clinic's standard formulary first
  (configurable). Type to search by trade name, generic name, or class.
* Pick **strength**, **frequency**, **duration**, **route**.
* Add as many drug lines as needed.
* Save.

###### Safety checks that run automatically

* **Allergy check** — warns if any of the patient's recorded allergies
  match the active ingredient.
* **Interaction check** — warns if any prescribed drug interacts with
  the patient's currently-active medications.
* **Pregnancy / paediatric** — warns if the drug is contraindicated
  for the patient's age or pregnancy status.
* **Dose check** — warns if the daily dose is outside the typical
  range for the patient's weight.

You can override any warning with a note, but the override is recorded.

###### Printing & sending

* **Print** produces the paper prescription.
* If the clinic has an integrated pharmacy, the prescription is also
  pushed electronically (pharmacy sees it on their queue immediately).

###### Prescriptions History

Click **Prescriptions History** to see every prescription this patient
has ever received — from any branch, any dentist, any date.

Columns: date, dentist, drugs (count + first one), status (Issued,
Refilled, Cancelled), printed Yes/No.

Click any row to open the full prescription, or click **Refill** to
copy it forward into a new prescription with today's date.

\newpage

###### Billing & Payments

Two toolbar buttons close out the visit financially: **New Receipt**
to take a payment, **New Bill** to print the itemised bill.

###### New Receipt

Click **New Receipt** to record a payment. Choose:

* **Method** — Cash, Card, Bank transfer, Insurance co-pay, Credit
  note.
* **Amount** — defaults to the visit's outstanding balance; can be
  partial.
* **Reference** — card slip number, transfer reference (when not cash).
* **Notes** — free text.

Save. A printable receipt opens — print one copy for the patient and
keep the digital copy on file.

###### How the payment is applied

* If the visit is **fully covered by insurance**, the receipt only
  collects the co-pay; the rest stays on the payer's claim.
* If the patient is **self-pay**, the receipt is applied to the
  oldest outstanding bill first, then the current visit's bill.
* If the receipt is for **more than the balance**, the surplus stays
  as a **credit** on the patient's account and is applied to future
  bills automatically.

###### New Bill

Click **New Bill** to open the itemised bill for today's visit. From
here you can:

* **Print** — gives the patient the formal invoice with line-by-line
  procedures and charges.
* **Email** — sends the same as a PDF to the patient's e-mail on file.
* **Re-price** a line (with override permission) — useful for staff
  discounts and goodwill adjustments. Each override is logged.
* **Apply discount** — % off the line, off the bill total, or a fixed
  amount.
* **Split** — split between two payers (e.g. insurance + self-pay).

###### Bill status

* **Draft** — still being built; you can keep adding lines.
* **Finalised** — fully priced, ready for payment / claim submission.
* **Paid** — payment receipts cover the total.
* **Submitted** — sent to the insurance payer.

###### Tip

For routine visits the receptionist usually skips **New Bill** entirely
— **New Receipt** is enough because the patient just wants the
receipt. Open **New Bill** only when the patient asks for an itemised
invoice, or when you need to apply a discount or split between payers.

\newpage

###### Administration

Clinic Reception has very little to configure on its own —
it just orchestrates pieces that live in other modules. As the clinic
administrator your job is mainly to make sure those pieces are set up.

| Setting | Where it lives |
|---|---|
| Branches & rooms | Data Setup  Organisation  Branches / Rooms |
| Dentists and their schedules | Data Setup  Staff  Doctors / Schedules |
| Visit types | Data Setup  Clinical  Visit Types |
| Price list (procedure prices) | Data Setup  Billing  Price List |
| Insurance payers and contracts | Data Setup  Billing  Payers |
| Drug formulary | Pharmacy module  Formulary |
| Fingerprint reader | See **[Patient Toolbox & Fingerprint](patient-toolbox.md)** |
| SMS / e-mail templates | Data Setup  Communications |

###### Per-user settings

For each receptionist user:

* **Default branch** — pre-selects the branch on every picker.
* **Default dentist** — pre-fills the dentist on new visits / appointments.
* **Permission to override prices** — needed before *Re-price* and
  *Discount* on the bill are clickable.
* **Permission to cancel a paid visit** — needed before the bill can be
  cancelled after a receipt has been issued.

See the system administrator's manual for setting these (they live on
the user record, not in this workspace).

\newpage

###### Patient Toolbox & Fingerprint

###### Patient Toolbox

The **Patient Toolbox** is the slim panel on the right edge of Clinic
Reception. It shows context-aware shortcuts for the
patient currently in the banner — the buttons that appear depend on
what the patient has on file.

Common shortcuts:

* **Allergies** — pops the allergy list (red highlight if any).
* **Active alerts** — any clinical or administrative alert flagged
  on the patient.
* **Attachments** — upload / view ID copy, insurance card scan,
  consent forms, X-rays brought from elsewhere.
* **Account balance** — outstanding amount across all branches.
* **Enrol Fingerprint** — capture a fingerprint for a patient who has
  none on file (or add a second / third finger).
* **Last visit** — jumps straight to the most recent visit's
  procedures and notes.
* **Insurance eligibility check** — pings the payer's API to confirm
  the card is still valid before the visit starts.

The administrator decides which buttons appear and in what order, per
clinic profile.

###### Fingerprint reader

The front desk supports any reader that exposes a standard biometric
service.

###### One-time setup

1. Plug the reader into the workstation.
2. From the front desk, click **Patient Toolbox  Test Reader** — the
   panel should flash green when the reader is reachable.
3. If the reader is not detected, install the vendor driver and the
   biometric service from the IT bundle, restart the browser, and
   re-test.

###### Enrolling a finger

1. Select the patient (any way — picker, ID number).
2. Click **Patient Toolbox  Enrol Fingerprint**.
3. Pick the finger from the on-screen hand.
4. Place the finger on the reader. The capture takes three reads to
   build a template.
5. Save. The finger is now linked to that patient across every branch.

###### Day-to-day use

The receptionist clicks **Finger Print Scan** on the toolbar and asks
the patient to place a finger. Match  banner fills. No match  fall
back to **Select Patient**.

###### Tips

* Wipe the reader between patients.
* Enrol **two** fingers per patient (typically both index fingers) — if
  one is bandaged or injured the other still works.
* The biometric template is hashed; the raw print is never stored.

\newpage

###### Metasoft Communicator

###### Introduction

**metasSoft Communicator** is an integrated HMS tool that enables clinics
to send WhatsApp messages, documents, reports, invoices, prescriptions,
and image attachments directly to patients, suppliers, and other
contacts from within HMS.

Unlike traditional WhatsApp Business integrations, Communicator does
not depend on third-party messaging gateways, API configurations, or
template approval processes. This reduces implementation complexity,
lowers operational costs, and simplifies ongoing maintenance.

###### Key Benefits

* Send WhatsApp messages directly from HMS.
* Attach documents, reports, images, invoices, and prescriptions.
* Eliminate dependency on third-party WhatsApp gateway providers.
* No template creation, submission, or approval requirements.
* Reduce recurring subscription and messaging fees.
* Faster deployment and easier administration.
* Minimise development and support effort across customer installations.
* Simplify localisation and customisation for different clinics and
  regions.
* Ideal for small and medium-sized clinics seeking a cost-effective
  communication solution.
* Provides a flexible foundation for future SaaS deployments while
  remaining simple to operate in on-premises environments.

By eliminating the need to configure and maintain message templates
for each customer, service provider, appointment reminder, or
localised installation, metasSoft Communicator significantly reduces
implementation and support overhead while delivering a seamless
communication experience directly from HMS.
###### How it works

The Communicator sends WhatsApp messages on behalf of HMS —
appointment reminders, confirmations, prescriptions, documents, and
ad-hoc messages — by driving WhatsApp Web in the background. It lives
in the Windows system tray on a dedicated PC and runs around the
clock.

###### What it does

* **Watches the HMS message queue.** When HMS adds a WhatsApp row
  (status *Pending*), the Communicator picks it up, sends it through
  WhatsApp Web, and writes the result back (*Sent* or *Failed*).
* **Lets staff send by hand** from a small in-app screen — pick a
  contact, type the text, attach a file, send.
* **Lists every message** with its delivery status, lets you resend,
  edit, pause, or delete the ones that haven't gone yet.
* **Protects the WhatsApp account** with safety guardrails — pacing,
  per-number caps, per-day cap, duplicate window, sending hours,
  surge break.
* **Stays alive** — auto-starts with Windows, lives in the tray, a
  watchdog relaunches it, a health monitor restarts the sender if it
  stops, session loss is recovered automatically.

###### When you need it

* Your HMS server is **outside the WhatsApp Business API** programme,
  or you want to keep using the personal/business WhatsApp account on
  a phone.
* You want **bulk-friendly pacing** and per-recipient limits without
  paying for an API.
* You want HMS staff to be able to send the **odd manual message**
  through the same path that handles the automated traffic.

###### Quick map

* **[Getting Started](getting-started.md)** — install, scan the QR
  once, send your first message.
* **[Features](features.md)** — categorised feature list.
* **Screens** — Sender (Start/Stop + manual send + log) and Message
  Queue (every message with actions).
* **[Everyday Use](everyday-use.md)** — common tasks and quick
  troubleshooting.
* **Settings** — the 7 settings tabs.
* **Administration** — architecture, installation, safety guardrails,
  alerts, reliability internals, logs, uninstall.

 Continue to **[Getting Started](getting-started.md)**.

\newpage

###### Getting Started

From a fresh PC to first WhatsApp message — about 10 minutes.

###### 1. Pick the service PC

* Windows 10 / 11 that **stays powered on** (the *service* machine).
* **Google Chrome** installed.
* **.NET 6 Desktop Runtime (x64)** installed.
* Network access to the HMS SQL Server and to WhatsApp Web.
* A phone with **WhatsApp** to scan the QR code once.

###### 2. Deploy the Communicator

Copy the Communicator into the HMS web app folder — typically into a
**Communicator** subfolder alongside the running HMS — and double-click
the executable to launch.

On startup it walks up the folder tree to find the HMS application
settings — so it picks up the same database the running HMS uses.

###### 3. Quick Setup wizard

The very first time it runs, the **Quick Setup** dialog appears. It
does everything in one step.

1. Click **Set up now**.
2. A Chrome window opens **WhatsApp Web**. **Scan the QR code** with
   the phone — once. The login is remembered.
3. Wait for the message *"WhatsApp Web is logged in and ready."*

After setup, the Chrome window hides itself and the Communicator
continues in the system tray.

###### 4. Install as a service (recommended)

Open **Settings  Deployment  Install Communicator**. One click sets
up the whole "always on" behaviour:

* Per-user **auto-start** entry — the Communicator starts when Windows
  logs in.
* **Watchdog** scheduled task — relaunches the app every few minutes if
  it isn't running.
* **Safety guardrails** turned on with sensible defaults.
* **Start hidden to tray** — no window pops up on login.
* Tells HMS to route WhatsApp through the Communicator — the master
  switch is flipped to **on**.
* Starts the sender immediately.

###### Optional: Windows auto-login

For an unattended server that has no human present after a reboot, run
**Settings  Deployment  Configure auto-login**. UAC asks for
admin rights, then Windows signs in automatically next time the
machine reboots. The password is stored encrypted in the Windows
secret store — never in plain text.

Use only on dedicated, physically secured machines.

###### 5. Send your first message by hand

1. Click the tray icon to open the window.
2. Go to **Sender**.
3. If status reads **Stopped**, press **Start** and wait for
   **Running** (green dot).
4. **Contact** — type a name (or pick a saved one).
5. **Phone** — digits, country code, no spaces.
6. **Message** — the text (Arabic is supported).
7. (Optional) **Attachment** — Browse to an image, PDF, or document.
8. Press **Send**.

The message lands in the Message Queue and is sent in turn. You can
watch the **Log** panel on the right side of the Sender screen for
live, colour-coded activity.

###### 6. Verify HMS messages are flowing

Trigger a normal HMS event that produces a WhatsApp — book an
appointment, issue a prescription, send a reminder — and switch to the
Communicator's **Message Queue**. The new row should appear with
status **Pending**, flip to **Sending**, then **Sent**.

 Continue to **[Features](features.md)** for the full catalogue.

\newpage

###### Features

Every Metasoft Communicator feature, grouped by what it lets you do.
###### 1. Message sending

* **Automatic sending** — picks up Pending rows from the HMS message
  queue and sends them over WhatsApp Web.
* **Manual sending** — pick a contact (or type one), write text, attach
  a file, click Send.
* **Text in any language** — Arabic, emoji, multiline; pasted via the
  clipboard so unicode is reliable.
* **Attachments** — images, PDFs, Word, Excel, any document. Optional
  caption alongside the attachment.
* **Same path for HMS + manual** — both sources go through the queue,
  the same safety rules, the same logging.

###### 2. Address book

* **Remembers every contact** ever used (name  phone).
* **Auto-saved after each send** — no separate "add contact" step.
* **Autocomplete** in the manual-send Contact field.
* **Country-code-aware** — strips `+`, spaces, dashes before sending.

###### 3. Sender screen

* **Start / Stop** the automatic sender.
* **Status pill** — Running (green), Stopped (grey) with the current
  queue depth.
* **Manual send block** — Contact, Phone, Message, Attachment, Send.
* **Live activity log** — colour-coded (blue info, amber warning, red
  error).
* **Clear log** — empties the on-screen view (file log keeps growing).

###### 4. Message Queue screen

* **Four summary cards** — Pending / Sending / Sent / Failed counts at
  the top of the screen.
* **Status chips** — *All / Pending / Sending / Sent / Failed / Held*
  to narrow the list with one click.
* **Date filter** — From / To dates with a Clear button.
* **Per-row badge + recipient + text + attachment chip + failure
  reason + time + reference number**.
* **Right-to-left rendering** — Arabic messages render correctly.
* **Per-row actions** — Send (retry), Edit (change text), Pause (hold),
  Delete.
* **Send all unsent** — re-queue every failed / paused / stuck message
  in one click.

###### 5. Statuses

* **Pending** — waiting in the queue.
* **Sending** — being sent right now.
* **Sent** — delivered to WhatsApp successfully.
* **Failed** — could not be sent; reason shown inline.
* **Held / Paused** — held on purpose (by user or by a safety rule);
  releases automatically when the rule clears, or via Send.

###### 6. Always-on operation

* **System-tray application** — lives by the Windows clock, click to
  open.
* **Single instance** — second launches focus the existing window
  instead of starting a duplicate.
* **Closing the window only hides it** — Quit from the tray menu is
  the only way to fully exit.
* **Auto-starts with Windows** at user login.
* **Watchdog scheduled task** — relaunches the app within minutes if
  it isn't running.
* **Health monitor** — restarts the sender within ~1 minute if it
  stops while processing is on.
* **Single-instance mutex** — watchdog cannot create duplicates.

###### 7. Crash resistance

* **Unhandled exception handlers** for UI, background, and task code —
  exceptions are logged and recovered without process exit.
* **Session recovery** — a lost WhatsApp session is detected and
  reconnected automatically.
* **True logout detection** — if WhatsApp has actually logged out
  (needs a fresh QR scan), an alert fires.

###### 8. Safety guardrails

* **Minimum gap between sends** + random jitter — paces sending to
  avoid bursts.
* **Per-number / per-hour** cap.
* **Per-number / per-day** cap.
* **Total per-day** cap (circuit-breaker).
* **Duplicate window** — drops the same message to the same number
  inside the window.
* **Sending hours** — e.g. 08:00 – 20:00; outside the window messages
  are held.
* **Sending days of week** — e.g. skip weekends.
* **Surge protection** — too many messages in a short window auto-pauses
  the sender.

Each rule can be set to 0 to disable just that rule.

###### 9. Alerts & monitoring

* **Sender-down threshold** — alert if the sender has been down for
  more than X minutes.
* **Surge trip alert** — alert when surge protection auto-pauses
  sending.
* **WhatsApp logout alert** — alert when a true logout is detected.
* **Email (SMTP)** — host, port, SSL, credentials, From / To. Works
  even when WhatsApp is down.
* **WhatsApp alert** — queue a message to an admin number; delivered
  once WhatsApp comes back.
* **Test alert** button — fires a sample alert through both channels.

###### 10. WhatsApp engine options

* **Engine selector** — WhatsApp Web (default, supports attachments)
  or WhatsApp Desktop (text only, simpler).
* **Hide Chrome / console** after launch.
* **Auto-hide after login** — Chrome disappears once the QR is scanned.
* **Persistent Chrome profile** — QR scanned once; login remembered
  across restarts.

###### 11. Database hookup

* **Single source of truth** — reads the same HMS application settings
  file the HMS web app uses; no separate connection string.
* **Polling interval** — how often to check the queue.
* **Attachment retention** — how long sent attachments are kept.
* **Default country code** — used when a number has no country code.
* **Test connection** button — proves the database hookup before
  enabling sending.
* **Heartbeat** — the app writes a heartbeat row so HMS can detect a
  dead Communicator.
* **Stuck reaper** — unsticks messages that have been in *Sending* too
  long.

###### 12. Startup behaviour

* **Start with Windows** toggle.
* **Start sender** on launch — yes / no.
* **Start hidden** — no window pops up, only the tray icon.

###### 13. Deployment tools (Settings  Deployment)

* **Install Communicator** — one click; sets up auto-start, watchdog,
  safety, hidden start, flips the HMS master switch on, starts sending.
* **Uninstall Communicator** — reverses everything on this PC, flips
  the HMS master switch off so HMS resumes its legacy sending path.
  Never touches data or schema.
* **Configure Windows auto-login** — encrypted credential in the
  Windows secret store; for unattended servers.
* **Run Quick Setup** — re-runs the first-time wizard.

###### 14. Logging

* **Rolling main log** next to the executable — full activity log;
  auto-rotates at ~5 MB, keeps the last few generations.
* **Not-found-phones log** — separate file of every number WhatsApp
  could not find.
* **Live log panel** on the Sender screen — same data, colour-coded.
* **Per-message reason** — failed rows carry their failure reason
  inline.

###### 15. In-app Help

* **Help tab** in the sidebar — short, plain-language guide built into
  the app.
* **Kept in sync** with every feature change as part of the release.

###### 16. HMS integration

* **Master switch** in HMS — when on, HMS routes WhatsApp to the
  Communicator queue; when off, HMS uses its legacy WhatsApp path.
* **Idempotent** — disabling the Communicator does not disrupt HMS;
  the legacy path resumes automatically.
* **Same database** — the Communicator and HMS read / write the same
  message queue rows, so HMS always sees the latest status.

 Continue to **[Sender Screen](screens/sender.md)** or
**[Message Queue](screens/message-queue.md)** for the day-to-day UI.

\newpage

###### Sender Screen

The **Sender** screen has three areas, top to bottom: **Status**,
**Manual send**, and **Log**.

![Sender screen](../img/sender.png)

###### Status

| Control | What it does |
|---|---|
| **Start** | Turns the automatic sender on. |
| **Stop** | Pauses sending — Pending rows stay in the queue. |
| Coloured dot | **Running** (green) or **Stopped** (grey). |
| **Queue** | How many messages are waiting to be sent. |

Press **Start**; if it is the first time after a reboot the Chrome
window may pop up briefly while the WhatsApp session checks in. It
hides itself once it is logged in.

###### Manual send

The block that lets staff send a message by hand from the Communicator
itself (the same path HMS messages take — so the same safety rules
apply).

| Field | Notes |
|---|---|
| **Contact** | Pick a saved contact, or type a name. The dropdown autocompletes from the address book. |
| **Phone** | Digits only — country code first, no spaces or dashes. |
| **Message** | The text. Arabic is supported and renders right-to-left. |
| **Attachment** | Optional. Click **Browse** to attach an image, PDF, Word, Excel, or any document. |
| **Send** | Queues the message. It then flows through the same queue and safety guardrails as HMS messages. |

The contact + phone you used are auto-added to the address book on
first send, so they autocomplete next time.

###### Log

The right-hand panel shows live, colour-coded activity:

* **Blue** — informational (started, queued, sent).
* **Amber** — warning (retry, throttled, recovered).
* **Red** — error (failed, logout, unreachable).

**Clear log** empties the on-screen view only — the file log on disk
keeps growing and rotating.

###### Tips

* Keep the Sender screen open on a small monitor at the front desk so
  problems surface quickly — the log spells them out as they happen.
* If the status reads *Stopped* and Pending is growing, the most
  likely cause is the WhatsApp session — press **Start** and watch
  for the QR scan request.

 Continue to **[Message Queue](message-queue.md)**.

\newpage

###### Message Queue Screen

Every WhatsApp message — automatic or manual — flows through this
screen. Use it to monitor the queue, act on stuck messages, and answer
"did it actually send?" questions.

![Message Queue screen](../img/message-queue.png)

###### Summary cards

Four cards across the top count the messages in each state:

* **Pending** — waiting to be sent.
* **Sending** — being sent right now.
* **Sent** — delivered to WhatsApp successfully.
* **Failed** — could not be sent.

Click any card to jump the list to that state.

###### Filters

| Filter | What it does |
|---|---|
| **Status chips** — *All / Pending / Sending / Sent / Failed / Held* | Narrow the list to one state. |
| **From / To dates** | Limit to a date range. |
| **Clear** | Resets every filter. |

Filters compose — Failed + last 7 days, for example.

###### Each message row shows

* A coloured **status badge**.
* The **recipient** — phone number plus name (from the address book if
  known).
* The **message text** (Arabic renders right-to-left).
* A **paperclip chip** if an attachment is included.
* The **failure reason** underneath if the row is Failed (e.g.
  *Invalid number*, *Chat did not open*, *Throttled*).
* The **time** and a **reference number** (e.g. `#16`).

###### Per-row actions (on un-sent messages)

| Action | Effect |
|---|---|
| **Send** | Re-queue immediately. The row flips to Sending. |
| **Edit** | Open the editor; change the text; Save. The corrected row is queued. |
| **Pause** | Hold the row — it stays in the queue but is skipped until Send is pressed again. |
| **Delete** | Remove the row from the queue. |

Sent messages are read-only — they cannot be edited or re-sent (HMS
audit assumes Sent rows are immutable).

###### Bulk action

**Send all unsent** at the top of the screen re-queues *everything*
that hasn't gone yet — Failed, Paused, Held, plus any rows stuck in
Sending. Useful after fixing the cause of a batch failure (e.g.
WhatsApp logged out for an hour).

###### Statuses cheat-sheet

| Status | Meaning | What to do |
|---|---|---|
| Pending | Waiting in the queue. | Nothing — it will send in turn. |
| Sending | Being sent right now. | Nothing — wait a moment. |
| Sent | Delivered to WhatsApp. | Done. |
| Failed | Could not be sent (reason shown). | Fix the issue (e.g. number), press Send. |
| Held / Paused | Held by you, or by a safety rule (throttle, schedule, surge, duplicate). | Releases automatically when the rule clears, or press Send. |

 Continue to **[Everyday Use](../everyday-use.md)**.

\newpage

###### Everyday Use

The Communicator is designed to disappear into the background — most
days nobody opens it. Here is what to know for the days you do.

###### How it behaves on its own

* It **starts with Windows** and runs hidden in the system tray.
* If you close the window, it only **hides** — the service is still
  running.
* If the app is ever killed, the **watchdog relaunches** it within a
  few minutes.
* If sending stops while processing is enabled, the **health monitor
  restarts** it within about a minute.
* If WhatsApp Web drops the session, it **reconnects** automatically.
* A true WhatsApp logout (needs a fresh QR) fires an **alert**.

###### Common tasks

| I want to… | Do this |
|---|---|
| Resend a failed message | Message Queue  find the row  **Send**. |
| Fix a wrong message before it sends | Message Queue  **Edit**  change  Save. |
| Stop one message going out | Message Queue  **Pause** (or Delete). |
| Retry everything that failed | Message Queue  **Send all unsent**. |
| Find an old message | Use the status chips and From / To dates. |
| Send a document | Sender  **Browse** to the file  **Send**. |
| Pause all sending | Sender  **Stop**. Press Start to resume. |
| Open the window after closing it | Click the Communicator tray icon (near the clock). |
| Fully exit | Right-click the tray icon  **Quit**. |

###### Quick troubleshooting

| Symptom | Likely cause & fix |
|---|---|
| *"Chat did not open"* in the log | WhatsApp isn't logged in — press **Start** and scan the QR. |
| Messages stay **Pending** and nothing sends | Sender is **Stopped** — press Start. Or check internet / WhatsApp login. |
| A message shows **"Invalid number"** | The phone number is wrong — **Edit** it (or fix it in HMS) and press Send. |
| A message is **"Held (Throttled)"** | A safety limit (per-number, per-day, or sending hours) is in effect — it sends automatically later. |
| **Surge** notice appears | Surge protection auto-paused the sender — wait, or raise the limit in Safety. |
| I can't see the window | Click the Communicator icon in the system tray. The window opens; closing it hides it again. |
| Sent messages still arrive in HMS as Pending | The HMS master switch may be off — check Settings  Database and confirm the connection is to the right database. |

###### When to call IT

* The QR scan keeps reappearing after every reboot.
* The watchdog seems to be relaunching the app constantly.
* Email alerts say sender-down repeatedly.
* The whole machine froze / blue-screened.

These are admin / installation problems — see **Administration** in
the sidebar.

 Or continue to **Settings  Overview** for the configuration
reference.

\newpage

###### Settings

Open from the sidebar. The settings window is split into seven tabs.

![Settings — Engine tab](img/settings-engine.png)

###### Engine

How the Communicator drives WhatsApp.

| Setting | Notes |
|---|---|
| **Engine** | *WhatsApp Web* (default — supports attachments) or *WhatsApp Desktop* (text only, simpler). |
| **Hide Chrome window** | Chrome doesn't appear in the taskbar. |
| **Hide console window** | Hides any background console window. |
| **Auto-hide after login** | Chrome shows just long enough for the QR scan, then hides automatically. |

###### Sending

How retries and notifications behave.

| Setting | Notes |
|---|---|
| **Retry attempts** | How many times a failed send is retried before being marked Failed. |
| **Retry delay** | Wait between retries (seconds). |
| **Tray notifications** | Show a Windows toast for sent / failed messages. |

###### Database

The HMS hookup.

| Setting | Notes |
|---|---|
| **Queue polling** | How often the queue is checked (seconds). Smaller = faster pickup, more DB load. |
| **Attachment retention** | How long sent attachments are kept on disk. |
| **Default country code** | Applied when a number has no country code. |
| **Test connection** | Proves the database hookup. Always run this after a config change. |
| **Heartbeat** | The Communicator writes a heartbeat row so HMS can detect a dead Communicator. |
| **Stuck reaper** | Unsticks messages that have been in *Sending* for too long. |

###### Safety

The guardrails that protect the WhatsApp account from being banned and
recipients from being spammed. See **[Safety
Guardrails](admin/safety-guardrails.md)** for a deep dive.

| Guardrail | Default | What it does |
|---|---|---|
| **Min gap + jitter** | 8 s + 0–4 s | Paces sending. |
| **Max per number / hour** | 3 | Holds further messages to the same number until next hour. |
| **Max per number / day** | 5 | Holds until next day. |
| **Max total per day** | 100 | Circuit breaker — holds everything until next day. |
| **Duplicate window** | 1 hour | Drops the same message to the same number inside the window. |
| **Sending window** | off (08–20) | Hold outside the configured hours. |
| **Sending days** | every day | Skip specified weekdays. |
| **Surge protection** | 200 in 10 min | Auto-pauses the sender; holds the queue. |

Set any individual value to **0** to disable just that rule.

###### Alerts

When something is wrong, tell someone.

| Setting | Notes |
|---|---|
| **Triggers** | Sender down beyond X minutes · Surge protection trips · WhatsApp logged out. |
| **Email (SMTP)** | Host, port, SSL, username, password, From, To. Works even when WhatsApp is down. |
| **WhatsApp alert** | Queue a message to an admin number — delivered once WhatsApp resumes. |
| **Test alert** | Fires a sample alert through both channels — verify the wiring before relying on it. |

###### Startup

| Setting | Notes |
|---|---|
| **Start with Windows** | Add / remove the per-user auto-start entry. |
| **Start sender** on launch | If on, sending begins automatically; if off, the app opens but stays paused until you press Start. |
| **Start hidden** | The window does not appear on launch — only the tray icon. |

###### Deployment

One-click tools for the support team.

| Button | What it does |
|---|---|
| **Install Communicator** | Sets up auto-start, watchdog, safety guardrails, start hidden, flips the HMS master switch on, and starts the sender. |
| **Uninstall Communicator** | Reverses every change on this PC; flips the HMS master switch off; never touches data or schema. |
| **Configure Windows auto-login** | UAC-elevated; stores credentials encrypted in the Windows secret store; for unattended servers only. |
| **Run Quick Setup** | Re-runs the first-time wizard — for QR re-scans or fresh starts. |

 Continue to **[Administration  Architecture](admin/architecture.md)**.

\newpage

###### Architecture

A one-page tour of how the Communicator and HMS work together.

###### Message flow

```
HMS event (appointment, reminder, prescription, manual click)
                       │
                       
        HMS inserts a row into the message queue
                       │  (status = Pending)
                       
        Communicator polls the queue
                       │
              ┌────────┴────────┐
                               
   Manual send (Sender)   Auto pickup
              │                 │
              └────────┬────────┘
                       
   Atomically claim the row (status = Sending)
                       │
                       
        Drive WhatsApp Web in background Chrome
                       │
              ┌────────┴────────┐
                               
        Sent                 Failed
              └────────┬────────┘
                       
        Write result back to the queue row
```

###### Components

| Component | What it is | Where it runs |
|---|---|---|
| **HMS** | The hospital application that produces WhatsApp messages. | The HMS web server. |
| **Message queue** | A set of rows in the HMS database. | The HMS SQL Server. |
| **Communicator app** | A tray application that polls the queue and drives WhatsApp Web. | A dedicated Windows PC. |
| **Background Chrome** | The browser instance the Communicator pilots; persistent user-data profile remembers the WhatsApp login. | The same Windows PC. |
| **Watchdog** | A Windows Task Scheduler job that relaunches the Communicator if it isn't running. | The same Windows PC. |
| **WhatsApp Web** | The web client running inside Chrome; speaks to WhatsApp's servers. | Internet. |

###### Master switch

HMS only routes WhatsApp to the queue when its master switch is **on**.
When it is off, HMS uses its own legacy WhatsApp path. The
*Install Communicator* / *Uninstall Communicator* buttons flip this
switch for you — no manual config edits.

| Master switch | HMS behaviour |
|---|---|
| **On** | HMS writes new WhatsApp messages to the queue. The Communicator delivers them. |
| **Off** | HMS sends WhatsApp through its legacy code path. The queue is ignored. |

###### What the Communicator does *not* do

* It does **not** modify the HMS database schema.
* It does **not** delete data on uninstall.
* It does **not** call WhatsApp's official API — it drives the web
  client of a real WhatsApp account.
* It does **not** parse the HMS payload — text and attachment go to
  WhatsApp as the queue says.

###### Why a tray application, not a true Windows service

A real Windows service runs in Session 0 with no interactive desktop
— it cannot drive a browser, scan a QR, or show a tray icon. The
Communicator is therefore a **tray application that auto-starts at
user login** and behaves like a service for every practical purpose
(auto-start, watchdog, hidden window, single instance).

For unattended servers, **[Windows auto-login](install-and-uninstall.md#windows-auto-login)**
plus the watchdog gives true "no human present" operation.

 Continue to **[Install & Uninstall](install-and-uninstall.md)**.

\newpage

###### Install & Uninstall

###### System requirements

* Windows 10 / 11 that **stays powered on**.
* **Google Chrome** installed.
* **.NET 6 Desktop Runtime (x64)**.
* Network access to the HMS SQL Server and to WhatsApp Web.
* A phone with WhatsApp for the one-time QR scan.

###### Deployment layout

The Communicator is deployed into a **Communicator** subfolder inside
the HMS web application — typically alongside the HMS runtime
(something like `…\HMS_Web\Communicator\`). It walks up the folder
tree on launch to find the HMS application settings file, so the
database connection is auto-discovered.

###### One-click install

**Settings  Deployment  Install Communicator** does all of this in
one step:

* Adds a **per-user auto-start** entry.
* Installs the **watchdog scheduled task** (relaunches the app every
  few minutes if it isn't running).
* Enables the **safety guardrails** with sensible defaults.
* Sets **Start hidden** — the window does not pop up on login.
* Sets the HMS **master switch to on** — HMS routes WhatsApp through
  the Communicator.
* **Starts the sender**, opening WhatsApp Web for the QR scan if
  there isn't a stored session yet.

After this, the Communicator is in "always on" mode — it will be
running every time the PC is on, even if no human logs in
(combine with auto-login below).

###### Windows auto-login

For an unattended server PC, **Settings  Deployment  Configure
auto-login** asks Windows to sign in automatically after a reboot
without a human present.

* UAC prompts for administrator rights.
* The password is stored **encrypted in the Windows secret store** —
  never in plain text or in a config file.
* On the next reboot, Windows logs in, the auto-start entry launches
  the Communicator, the watchdog confirms it is running.

**Use only on dedicated, physically secured machines.** A PC that
auto-logs in is a PC anyone with physical access has logged-in
access to.

###### Uninstall

**Settings  Deployment  Uninstall Communicator** reverses everything
on this PC:

* Stops the sender and **closes the app**.
* Removes the auto-start entry.
* Removes the watchdog scheduled task.
* Removes Windows auto-login (if set).
* Sets the HMS **master switch to off** — HMS resumes its legacy
  WhatsApp path immediately.

It does **not**:

* Delete any data.
* Touch the database schema.
* Remove the executable folder or the logs.

So re-installing later just means running the executable again and
clicking **Install Communicator** — the previous config and logs are
all still there.

###### Moving to another PC

1. Install the Communicator on the new PC (copy folder + Install
   Communicator).
2. Scan the QR code on the new PC (the WhatsApp session on the old PC
   is automatically signed out — WhatsApp only allows one Web
   session at a time).
3. Confirm messages start flowing on the new PC.
4. **Uninstall Communicator** on the old PC.

Both PCs cannot run at the same time pointing at the same database —
the queue rows would be claimed twice. Always finish the move within
the same maintenance window.

 Continue to **[Safety Guardrails](safety-guardrails.md)**.

\newpage

###### Safety Guardrails

The guardrails protect the WhatsApp account from being banned and
recipients from being spammed. They run on every message — both
automatic and manual.

###### The eight guardrails

| Guardrail | Default | What it does when exceeded |
|---|---|---|
| **Min gap + jitter between sends** | 8 s + 0–4 s | Waits — paces sending, looks human. |
| **Max per number, per hour** | 3 | Holds further messages to that number; auto-retried next hour. |
| **Max per number, per day** | 5 | Holds; auto-retried next day. |
| **Max total, per day** | 100 | Circuit-breaker — holds everything; auto-retried next day. |
| **Duplicate window** | 1 hour | Drops the same message text to the same number inside the window (flagged on the queue). |
| **Sending hours window** | off (e.g. 08:00 – 20:00) | Holds outside the window; sends when it re-opens. |
| **Sending days** | every day | Skip configured weekdays. |
| **Surge protection** | 200 in 10 minutes | Auto-pauses the sender; holds the queue; fires an alert. |

###### Setting any rule to 0 = disabled

Each rule has its own zero-disables behaviour. For example, setting
**Max per number, per hour = 0** disables only that one rule — the
daily cap, total cap, and surge protection still apply.

###### What "Held" looks like

A row in the **Held / Paused** status with the **reason** under the
text — e.g. *Held (Per-number daily cap)*, *Held (Sending hours)*,
*Held (Surge)*. The row stays in the queue and is automatically
re-evaluated when the guardrail clears.

###### Manual override

The receptionist can press **Send** on a held row in the Message
Queue — that one row is force-released. The guardrail still counts
the send (the daily cap is now closer to its ceiling). Use sparingly.

###### Tuning recommendations

* **New WhatsApp account** — leave defaults; they are deliberately
  conservative.
* **Established business account, low complaint history** — you can
  raise the daily total cap to 200 – 300 once you've watched the
  account for a few weeks.
* **High-frequency single-recipient flows** (e.g. appointment +
  preparation + reminder for the same patient in one day) — raise
  *Max per number, per day* from 5  8 or so.
* **After-hours quiet hours** — set Sending hours to your
  reception's working hours. Reminders generated overnight are
  queued and go out when the clinic opens.

###### When to widen vs. when to fix the source

* If the queue is constantly piling up at the daily total cap, that
  is the system telling you the WhatsApp account is being used like
  a bulk-marketing channel. Either widen the cap *and* watch for
  account warnings, or look at the HMS automation that is producing
  the messages and trim duplicates.
* If **Surge protection** trips, look at HMS first — usually a batch
  job kicked off all at once. Stagger it.

 Continue to **[Alerts & Monitoring](alerts-and-monitoring.md)**.

\newpage

###### Alerts & Monitoring

The Communicator can be left running unattended — alerts are the
mechanism that wakes someone up when it can't fix itself.

###### Triggers

| Trigger | When it fires |
|---|---|
| **Sender down beyond X minutes** | The sender has been Stopped (or unable to recover) for more than the configured threshold. |
| **Surge protection trips** | Too many messages in a short window — the sender auto-paused itself. |
| **WhatsApp logged out** | A true logout was detected — the session needs a fresh QR scan from a human. |

###### Channels

###### Email (SMTP)

Settings  Alerts  Email block:

* **Host / Port** — e.g. `smtp.gmail.com` / `587`.
* **SSL / StartTLS** — typically on for port 587.
* **Username / Password** — service account credentials; prefer an
  app-specific password if your provider supports them.
* **From** — the sender shown to recipients.
* **To** — comma-separated list of admin e-mail addresses.

Works **even when WhatsApp is down** — this is the primary channel
for the *WhatsApp logged out* alert.

###### WhatsApp

* Settings  Alerts  WhatsApp number — an admin's WhatsApp number.
* Alert messages are **queued** when an alert fires; they are
  delivered automatically once WhatsApp sending resumes.

Useful as a redundancy when e-mail is unreliable, less useful as the
sole channel for *WhatsApp logged out* alerts (you may never see it
until the session is back).

###### Test alert

The **Test alert** button fires a sample alert through both channels.
Run it after every config change — confirms the wiring works before
you need it to work.

###### What ends up in alerts

A short text — the trigger name, a timestamp, the host name, the
current queue depth, and any reason text the Communicator was able to
collect. No patient data, no message content.

###### Monitoring beyond alerts

* **Heartbeat row** — the Communicator writes a heartbeat row to the
  database every cycle. HMS dashboards can show "last heartbeat at
  …" as a live indicator.
* **Watchdog logs** — the Task Scheduler watchdog records every
  relaunch — useful for spotting flapping.
* **Log file** — see [Logs](logs.md) for what is logged and where.

###### Recommended monitoring stack

1. **Email alerts** to the IT admin's inbox for serious events.
2. **WhatsApp alerts** to a clinic manager's phone for surge / pause.
3. A **dashboard tile** in HMS showing the last heartbeat (built-in if
   you use the HMS dashboards).
4. **Weekly review** of the *not-found-phones* log to clean up bad
   numbers at source.

 Continue to **[Reliability](reliability.md)**.

\newpage

###### Reliability

Five mechanisms keep the Communicator running 24 × 7 without a human
in the room.

###### 1. Watchdog (relaunch)

A Windows Task Scheduler job runs every few minutes. If the
Communicator isn't running, the watchdog launches it.

* A single-instance mutex prevents duplicates — if the app *is*
  running, the watchdog's launch is a no-op.
* If the watchdog itself is removed (e.g. by an over-zealous admin),
  the *Install Communicator* button re-creates it.

###### 2. Health monitor (sender restart)

A background loop inside the app checks once a minute that the sender
is running when it should be. If processing is enabled but the
sender has stopped (browser crash, lost session, unhandled stall),
the health monitor restarts the sender within ~1 minute.

The user sees a small entry in the log; no manual action needed.

###### 3. Crash handlers

The app wires global crash handlers in three places:

* **UI thread** — unhandled exceptions in window code.
* **Background tasks** — unobserved task exceptions.
* **App domain** — anything not caught by the first two.

Every catch logs the exception and **does not exit the process** —
the watchdog + health monitor would relaunch / restart anyway, but
not exiting keeps the queue moving.

###### 4. Session recovery

The browser layer watches for the "you are no longer logged in"
state. Two cases:

* **Soft disconnect** (e.g. network blip) — Chrome reconnects to
  WhatsApp; the Communicator continues. No alert.
* **True logout** (e.g. WhatsApp force-signed-out from another
  device, or the QR session expired) — needs a human to scan a QR.
  An alert fires; the sender stops; the queue holds.

###### 5. Single-instance mutex

The watchdog can trigger a second launch attempt at any time. The
mutex ensures only one instance owns the database queue and the
Chrome profile — duplicates exit immediately.

The same mutex makes "click the icon to bring it forward" reliable
— a second launch focuses the existing window instead of starting
a duplicate.

###### What this means in practice

| Failure mode | What happens |
|---|---|
| App killed by Task Manager | Watchdog relaunches in <5 min. |
| App crashed | Crash handler logs and recovers; if the process did exit, watchdog relaunches. |
| Sender stopped without a crash | Health monitor restarts within ~1 min. |
| WhatsApp Web session dropped | Auto-reconnect; user-invisible. |
| WhatsApp truly logged out | Alert; needs a human QR scan. |
| Windows reboot | Auto-login (if configured)  auto-start entry  app running again. |
| HMS database down | Sender goes idle, retries on next polling cycle. No data lost — pending rows stay pending. |
| Chrome killed | App relaunches Chrome on the next cycle. |
| Disk full | Crash handler catches log-write failures; app continues; alert fires. |

 Continue to **[Logs](logs.md)**.

\newpage

###### Logs

Two log files sit next to the executable. Both rotate automatically.

###### Main activity log

Every notable event is recorded:

* App start / stop / config change.
* Sender start / stop.
* Each queue pickup (row reference, recipient, type).
* Each send attempt and its outcome (Sent, Failed, Held + reason).
* WhatsApp session events — connected, disconnected, logged-out.
* Watchdog / health-monitor actions.
* Exceptions (with stack trace).

Rotation: the file grows to ~5 MB then is rolled; the last few
generations are kept. Old files are removed automatically.

###### Not-found-phones log

A separate file lists every phone number WhatsApp could not find
(*"Phone number shared via url is invalid"* and friends). It is
append-only — no rotation — because clinics want to be able to bulk-
clean these numbers in HMS.

Workflow: open the file weekly, copy the numbers, search them in HMS,
fix or remove. The file does not delete itself when entries are
fixed.

###### Live log panel

The Sender screen mirrors the main log in real time, colour-coded
(blue / amber / red). **Clear log** empties the on-screen view only —
the file on disk is untouched and keeps growing.

###### What is *not* logged

* Message body of WhatsApp messages (privacy).
* Patient identifiers beyond what is already visible in the queue
  row (reference number, recipient name from the address book).
* Passwords or SMTP credentials.

###### Sharing logs with support

If support asks for logs:

* The main log file — the active one and the most recent rotated
  generation are enough for most issues.
* The not-found-phones log — only if the complaint is about specific
  numbers.

Logs can be zipped and e-mailed safely — they do not contain message
content.

###### Permanent archiving

Logs are designed for short-term troubleshooting (days to weeks). If
a longer audit trail is required, set up a scheduled task to copy
the rotated generations to a NAS or log-aggregation tool nightly.

 Continue to **[Architecture](architecture.md)** if you arrived
here directly.

\newpage

###### metasoft NPHIES BridgeProxy

**BridgeProxy** is a small Windows service + tray dashboard that lets
HMS talk to **NPHIES** (Saudi Arabia's national health-information
platform) when the HMS server cannot reach NPHIES directly.

###### Why it exists

NPHIES authorises providers by **source IP address**. It accepts FHIR
traffic only from IP addresses that:

* Have been white-listed by NPHIES, **and**
* Are located **inside Saudi Arabia**.

When HMS runs outside KSA (for example, in Lebanon), or from a network
whose public IP is not whitelisted, HMS cannot communicate with
NPHIES directly.

BridgeProxy is installed on a small Windows machine **inside KSA**
with a whitelisted IP. HMS sends its NPHIES traffic to the proxy; the
proxy forwards it to NPHIES from the whitelisted IP and returns the
response verbatim.

###### What it does — and what it does not do

| Does | Does not |
|---|---|
| Listens for HMS requests on a TCP port. | Parse the FHIR payload. |
| Forwards bytes to NPHIES. | Modify the request or response. |
| Returns the response verbatim. | Cache, log, or store FHIR data. |
| Counts requests / OK / errors. | Authenticate the HMS caller — it relies on network reach + a shared API key. |
| Tests connectivity to Sandbox / Production. | Replace the NPHIES SSL or certificate handshake — both sides remain end-to-end TLS. |

As a result, **HMS behaviour is unchanged** regardless of its physical
location.

###### Two components

| Component | What it is | Runs as |
|---|---|---|
| **BridgeProxy.Service.exe** | The proxy itself. Listens on a TCP port, forwards to NPHIES. | Windows service, auto-start. |
| **BridgeProxy.Tray.exe** | The dashboard — system-tray icon + management window for Start/Stop, configuration, diagnostics. | Per-user, auto-starts at login. |

###### Quick map

* **[Getting Started](getting-started.md)** — install, first connection
  test, point HMS at it.
* **[Features](features.md)** — categorised feature list.
* **Dashboard** — one page per tab (Status, Configuration, Send to
  NPHIES).
* **Administration** — installation, uninstall, HMS-side configuration,
  diagnostics.

 Continue to **[Getting Started](getting-started.md)**.

\newpage

###### Getting Started

Install BridgeProxy, verify it reaches NPHIES, and point HMS at it.

###### 1. Pick the host machine

* It must be **inside Saudi Arabia**.
* Its **public IP** must be one of the IPs already whitelisted with
  NPHIES (or about to be whitelisted).
* **Windows Server** or Windows 10/11 with admin rights.
* Always-on — the HMS server depends on it for every NPHIES call.

###### 2. Install

1. Copy the BridgeProxy folder to `C:\BridgeProxy\`.
2. Run **INSTALL.cmd** and accept the UAC prompt.

During first launch the installer:

* Asks for the listening port (default: **5500**).
* Installs and starts the Windows service.
* Creates an inbound Windows Firewall rule.
* Configures the tray application to start automatically at login.
* Displays the tray icon (a shield).

###### 3. Open the dashboard

Double-click the shield tray icon. The dashboard window opens on the
**Status** tab.

Confirm:

* **Service** shows *Running*.
* **Port** shows the port you chose.
* **Server IP** lists the host's local IP addresses.

###### 4. Test connectivity to NPHIES

Click **Test Sandbox** — verifies the host can reach the NPHIES
sandbox gateway. Should turn green.

Click **Test Production** — same for the production gateway.

If either fails:

* Open **Diagnostics** (next button) for a full network report.
* Confirm the host's **public IP** is whitelisted with NPHIES.

###### 5. Configure HMS to use the bridge

On the HMS application server:

1. Open **NPHIES Settings  Bridge**.
2. **Use Bridge**  enable. (Enable this when HMS runs outside KSA or
   its IP is not static / whitelisted.)
3. Set the **Bridge URL** to the BridgeProxy host
   (e.g. `http://203.0.113.10:5500`).
4. Click **Test Connection** — HMS should be able to reach the proxy.
5. (Optional) Click **Configure Firewall (Outbound)** to open the
   outbound port from HMS to the bridge automatically.

###### 6. First real submission

Send any normal NPHIES message from HMS — eligibility check,
pre-authorization, claim. The proxy forwards it; HMS gets the same
response it would have received talking to NPHIES directly.

On the dashboard, the **Requests / OK / Errors** counters tick up.

###### 7. Verify from the bridge side

Click **Inbound Check** in the dashboard — confirms HMS can still
reach the bridge.

Use **Send to NPHIES** (third dashboard tab) to send a manual test
request from the bridge itself — handy when troubleshooting whether
the issue is HMS or the bridge.

 Continue to **[Features](features.md)** for the complete catalogue,
or **[Dashboard  Status](dashboard/status.md)** for day-to-day use.

\newpage

###### Features

Every BridgeProxy feature, grouped by what it lets you do.
###### 1. Network bridging

* **Source-IP relay** — every outbound call to NPHIES leaves from the
  bridge's whitelisted IP, regardless of where HMS is located.
* **Verbatim forwarding** — bytes in, bytes out. No payload parsing, no
  rewriting, no caching.
* **TLS pass-through** — end-to-end TLS between HMS and NPHIES is
  preserved.
* **No FHIR coupling** — works for any NPHIES message version without
  upgrades; the proxy is content-agnostic.
* **Allowed-hosts whitelist** — refuses to forward to anywhere other
  than the configured destination hosts.
* **API key** — shared secret between HMS and the bridge; rejects
  unauthorised callers.

###### 2. Deployment

* **Single-folder install** — copy `C:\BridgeProxy\`, run
  `INSTALL.cmd`.
* **Auto-installed Windows service** — `BridgeProxy.Service.exe` runs
  on boot as a system service.
* **Auto-installed tray dashboard** — `BridgeProxy.Tray.exe` starts on
  login for every interactive user.
* **Configurable listening port** — chosen during install, changeable
  later from the dashboard.
* **Automatic inbound firewall rule** — installer opens the chosen
  TCP port.
* **Clean uninstall** — `UNINSTALL.cmd` removes the service, firewall
  rules, and scheduled task. Configuration and logs are preserved for
  audit / reinstall.

###### 3. Service management (Dashboard  Status)

* **Service state** — Running / Stopped / Starting at a glance.
* **Listening port** — current TCP port.
* **Server IP** — every local IP address of the host (so you know what
  NPHIES sees as your source).
* **Uptime** — time since the service last restarted.
* **Live counters** — Requests / OK / Errors since service start.
* **Start / Stop / Restart** buttons — control the Windows service
  without opening the Services console.

###### 4. Connectivity tests

* **Test Sandbox** — TCP + TLS reach to the NPHIES sandbox gateway.
* **Test Production** — same for the production gateway.
* **Diagnostics** — full network diagnostic sweep (DNS, route, TLS
  handshake, gateway reach) in one click.
* **Inbound Check** — verifies HMS can reach the bridge (useful when
  diagnosing whether the issue is HMS-to-bridge or bridge-to-NPHIES).

###### 5. Configuration (Dashboard  Configuration)

* **Port** — listening TCP port (changeable; service restarts on save).
* **Timeout** — request timeout in seconds.
* **Allowed Hosts** — comma-separated whitelist of destination hosts
  the proxy will forward to.
* **API Key** — read-only display of the shared secret (rotated via the
  configuration file).
* **Save & Restart Service** — applies any change and restarts the
  service in one click.
* **Open Firewall Port** — re-creates the inbound firewall rule if
  someone has removed it.

###### 6. Manual testing (Dashboard  Send to NPHIES)

* **Target selector** — Sandbox / Production / Custom URL.
* **Custom URL** — send a hand-typed request to any whitelisted host
  (useful for testing new endpoints before HMS supports them).
* **Sends from the bridge** — proves the host's NPHIES reach without
  needing HMS to be involved.

###### 7. HMS-side configuration (HMS  NPHIES Settings  Bridge)

* **Use Bridge** toggle — switch HMS between *direct* and *bridged*
  NPHIES traffic without restart.
* **Test Connection** — from HMS to the bridge.
* **Configure Firewall (Outbound)** — opens the outbound port from
  the HMS server to the bridge automatically.

###### 8. Safety & operations

* **Configuration & logs preserved on uninstall** — re-install is a
  drop-in.
* **No data persistence** — FHIR payloads are not stored anywhere on
  the bridge.
* **Counter-only telemetry** — only Requests / OK / Errors are tracked.

 Continue to **[Dashboard  Status](dashboard/status.md)** for
day-to-day operations.

\newpage

###### Status Tab

The **Status** tab is the dashboard's home page — live service
information and one-click control of the service.

###### Live service information

| Field | What it shows |
|---|---|
| **Service** | Running, Stopped, or Starting. |
| **Port** | The TCP port the service is listening on. |
| **Server IP** | Every local IP address the host has — what NPHIES sees as your source IP. |
| **Uptime** | Time since the service was last restarted. |
| **Requests / OK / Errors** | Live counters since service start. |

The counters give you a real-time pulse — if Requests is climbing but
OK is flat, something downstream is broken; if Requests is flat,
something between HMS and the bridge is broken.

###### Action buttons

| Button | What it does |
|---|---|
| **Start** | Starts the Windows service. |
| **Stop** | Stops the Windows service. Use sparingly — HMS NPHIES traffic halts immediately. |
| **Restart** | Stop + Start, useful after a configuration change saved without the *Save & Restart Service* button. |
| **Test Sandbox** | TCP + TLS reach to the NPHIES sandbox gateway. Green = good. |
| **Test Production** | Same as Test Sandbox, against the production NPHIES gateway. |
| **Diagnostics** | Runs a full network diagnostic sweep — DNS resolution, route, TLS handshake, gateway reach. Output appears in a results pane. |
| **Inbound Check** | Verifies HMS can reach the bridge — answers *"is the problem on the HMS side?"* in one click. |

###### Reading the test results

* **Green** = success. The bridge has full reach.
* **Yellow / orange** = degraded. Partial reach (TCP fine, TLS fails;
  or one gateway reachable, the other not).
* **Red** = failure. Open **Diagnostics** for the detailed report and
  fix from the bottom up: DNS  route  TLS  gateway.

 Continue to **[Configuration](configuration.md)**.

\newpage

###### Configuration Tab

Settings the bridge service uses. Changes apply on **Save & Restart
Service**.

###### Settings

| Setting | What it does |
|---|---|
| **Port** | The listening TCP port. Default 5500. Change if the chosen port is already in use; the firewall rule is updated automatically. |
| **Timeout** | Request timeout in seconds. Increase only if NPHIES is intermittently slow — long timeouts hold connections open and can hide real outages. |
| **Allowed Hosts** | Comma-separated whitelist of destination hosts the proxy will forward to. Requests for anything outside this list are rejected. Pre-populated with the sandbox and production NPHIES hosts. |
| **API Key** | Read-only display of the shared secret between HMS and the bridge. Rotate by editing the configuration file directly on the host. |

###### Buttons

| Button | Effect |
|---|---|
| **Save & Restart Service** | Persists changes to the configuration file and restarts the service so the new values take effect. There is a brief window where the proxy is unavailable — schedule for low-traffic times. |
| **Open Firewall Port** | Re-creates the inbound Windows Firewall rule for the current port. Use this if someone manually removed the rule, or after changing the port. |

###### Allowed Hosts — what to put in

Only the NPHIES hosts you legitimately need:

* `nphies.sa` and any production sub-domains.
* `sandbox.nphies.sa` for testing.

Do **not** widen the list to include arbitrary internet hosts — the
whitelist is the only place that limits what the proxy can reach.

###### Port — picking a safe value

* Default **5500** works for most clinics.
* Avoid common ports (80, 443, 3389, 5432, 1433, 1521) — they
  collide with web servers, RDP, databases.
* Pick from the registered range (1024 – 49151).
* Whatever you pick, the HMS *Bridge URL* on the HMS side has to
  match — change one, change both.

 Continue to **[Send to NPHIES](send-to-nphies.md)**.

\newpage

###### Send to NPHIES Tab

A manual-testing utility — send a request straight from the bridge to
NPHIES without HMS being involved. Useful when you need to isolate
whether a failure is on the HMS side or the bridge side.

###### Target options

| Target | What it does |
|---|---|
| **Sandbox** | Sends the request to the NPHIES sandbox gateway. Safe — no real claims are created. |
| **Production** | Sends to the production gateway. Use with care — real submissions count. |
| **Custom URL** | Send to any URL within the **Allowed Hosts** whitelist. Useful for testing new endpoints before HMS supports them. |

###### When to use this tab

* **HMS reports a NPHIES failure** — replay the same payload from
  here. If the bridge succeeds, the issue is on the HMS side; if it
  fails the same way, the issue is bridge or NPHIES.
* **A new NPHIES endpoint** — verify the bridge can reach it before
  upgrading HMS to use it.
* **Connectivity drill** — quick check from a fresh install before
  pointing HMS at the bridge.

###### What does *not* belong here

* **Real clinical submissions** — those should always come from HMS so
  the response is captured against the right patient / claim record.
* **Load tests** — the manual tool sends one request at a time and is
  not designed for performance work.

\newpage

###### Installation

The installer is a single command. It registers the Windows service,
opens the firewall, configures auto-start, and shows the tray icon.

###### Prerequisites

* **Windows Server / Windows 10 / 11** with administrator rights.
* The host is **inside Saudi Arabia**.
* The host's **public IP is whitelisted with NPHIES** (or will be).
* The chosen TCP port is **free**.

###### Install

1. Copy the BridgeProxy folder to `C:\BridgeProxy\`.
2. Right-click **INSTALL.cmd**  **Run as administrator** (or simply
   double-click and accept the UAC prompt).
3. When asked, enter the listening port. The default **5500** is fine
   for most clinics.
4. Wait for the installer to finish — the tray icon (a shield) appears
   when it's done.

The installer:

* Registers `BridgeProxy.Service.exe` as a Windows service set to
  auto-start at boot.
* Creates an inbound Windows Firewall rule for the listening port.
* Sets `BridgeProxy.Tray.exe` to auto-start at login (Scheduled Task).
* Launches the tray application.

###### Post-install checklist

| Step | Where |
|---|---|
| Confirm **Service = Running** | Dashboard  Status |
| Confirm **Test Sandbox** is green | Dashboard  Status |
| Confirm **Test Production** is green | Dashboard  Status |
| Confirm **Allowed Hosts** lists the right NPHIES hosts | Dashboard  Configuration |
| Configure HMS to use the bridge | HMS  NPHIES Settings  Bridge |
| Send a test eligibility check from HMS | HMS |
| Verify counters tick up | Dashboard  Status |

###### Where things go

| Item | Location |
|---|---|
| Service binary | `C:\BridgeProxy\BridgeProxy.Service.exe` |
| Tray binary | `C:\BridgeProxy\BridgeProxy.Tray.exe` |
| Configuration file | `C:\BridgeProxy\` (alongside the binaries) |
| Logs | `C:\BridgeProxy\logs\` |
| Firewall rule | Windows Firewall  Inbound Rules  *BridgeProxy* |
| Scheduled Task | Task Scheduler  *BridgeProxy Tray* |

###### Multi-user host

The tray dashboard auto-starts at login **per user**. The service is
shared. If several Windows users sign in to the host, each sees their
own tray icon; clicking either opens the same dashboard pointing at
the same service.

\newpage

###### Uninstall

Run **UNINSTALL.cmd** as Administrator.

It removes:

* The Windows service.
* The inbound Windows Firewall rule.
* The Scheduled Task that auto-starts the tray dashboard.

It **preserves**:

* The configuration file.
* The logs folder.
* The binaries themselves under `C:\BridgeProxy\`.

This makes re-install a drop-in — run `INSTALL.cmd` again on the same
folder and the previous configuration and logs are picked up.

###### Fully removing the install

If you need to wipe the host clean:

1. Run **UNINSTALL.cmd** as Administrator.
2. Delete `C:\BridgeProxy\` (folder + everything inside).
3. (Optional) Archive the `logs\` folder first if you need the audit
   trail.

###### Reverting HMS to direct mode

Before you stop the bridge, switch HMS back to direct NPHIES:

1. Open **HMS  NPHIES Settings  Bridge**.
2. **Use Bridge**  off.
3. **Test Connection** — confirms HMS can reach NPHIES directly.

Otherwise HMS keeps trying to send through a bridge that no longer
exists.

###### Moving the bridge to another host

The cleanest path:

1. Install BridgeProxy on the new host. Verify Test Sandbox /
   Production both go green.
2. Update **HMS  NPHIES Settings  Bridge  Bridge URL** to point at
   the new host.
3. Click **Test Connection** in HMS — confirms it switched.
4. Uninstall BridgeProxy on the old host.

Both hosts can coexist for a few minutes — the old one simply stops
receiving traffic once HMS is repointed.

\newpage

###### HMS Configuration

The bridge does nothing useful until HMS is told to route NPHIES
traffic through it.

###### Where

In HMS, open **NPHIES Settings  Bridge**.

###### Settings

| Setting | Meaning |
|---|---|
| **Use Bridge** | The master switch. Enable when HMS runs outside KSA or its IP is not static / whitelisted. Disable to send NPHIES traffic directly. |
| **Bridge URL** | The TCP endpoint of the bridge — e.g. `http://203.0.113.10:5500`. Must match the bridge host's reachable IP and listening port. |
| **API Key** | The shared secret. Must match the **API Key** shown on the bridge's *Configuration* tab. |
| **Timeout** | Optional override for the request timeout. |

###### Buttons

| Button | What it does |
|---|---|
| **Test Connection** | Sends a no-op to the bridge and verifies the round-trip. Use after any change. |
| **Configure Firewall (Outbound)** | Asks Windows to open the outbound port from the HMS server to the bridge — saves a trip to IT. |

###### When to enable

| Situation | Enable Bridge? |
|---|---|
| HMS server inside KSA on a whitelisted static IP. | No — use direct. |
| HMS server outside KSA. | **Yes**. |
| HMS server inside KSA on a dynamic / consumer IP. | **Yes** — until the IP is whitelisted. |
| HMS server inside KSA on a static IP awaiting whitelisting. | **Yes** as a temporary bridge. |
| Multi-site HMS where some sites need bridging and some don't. | Per-site setting — toggle at the right tenant. |

###### After enabling

* All existing NPHIES configuration (provider IDs, payer codes,
  eligibility forms) keeps working. The bridge is transparent.
* Response times can go up by a few hundred milliseconds (extra
  network hop). If you see seconds of added latency, the bridge host
  may be on a slow link.

###### Switching back to direct

Disable **Use Bridge** and click **Test Connection**. HMS connects to
NPHIES directly again. Any pending submissions in the HMS queue
re-try on the new path.

###### Verifying the round-trip

After **Use Bridge** is on:

1. **HMS  Test Connection** turns green.
2. Submit any real NPHIES check (eligibility for any patient).
3. On the bridge **Dashboard  Status**, the **Requests** counter
   ticks up by one and **OK** ticks up by one shortly after.

If Requests ticks but OK does not, the bridge reached HMS but NPHIES
rejected the call — open Diagnostics on the bridge.

\newpage

###### Diagnostics

When connectivity isn't green, **Diagnostics** is the one-click sweep
that tells you which layer is broken.

###### How to run it

Dashboard  **Status** tab  click **Diagnostics**. The results pane
fills with a tiered report.

###### What it tests, in order

The sweep walks the network stack bottom-up so you can fix from the
root.

| Tier | Checks | Failure means |
|---|---|---|
| **DNS** | Can the host resolve `nphies.sa` and the sandbox host name? | DNS server unreachable or misconfigured — fix `ipconfig /all` first. |
| **Route** | Is there an IP route to the gateway? | Default gateway or routing table problem. |
| **TCP** | Three-way handshake to port 443 on the NPHIES host. | Firewall (host or network) blocking outbound 443. |
| **TLS** | Successful TLS 1.2/1.3 handshake. | Outdated TLS stack on the host, or a TLS-intercepting proxy in the way. |
| **Gateway** | Sends a no-op probe to the NPHIES gateway and gets a response. | NPHIES side is up but rejecting — most often, the host's public IP is not whitelisted. |

###### Reading the output

* Every tier ends in **OK** or a specific error line.
* Stop at the first failure — fixing it usually clears the ones below.
* The report is plain text — copy it into a support ticket if you
  escalate.

###### Adjacent buttons

* **Inbound Check** — separate sweep that verifies HMS can reach
  *this* host (i.e. the bridge from HMS's point of view). Useful when
  bridge  NPHIES is green but HMS still can't submit.
* **Test Sandbox** / **Test Production** — quick green / red on the
  gateway specifically, without running the full DNS/route/TCP/TLS
  walk. Use these for the fast pulse; use Diagnostics when something
  is actually broken.

###### Common failures and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| DNS fails. | Wrong DNS server on the host. | Set a working DNS server (Cloudflare 1.1.1.1, Google 8.8.8.8, or your ISP's). |
| Route fails. | Default gateway missing. | Check NIC configuration. |
| TCP fails. | Outbound 443 blocked. | Open the firewall — host AND network. |
| TLS fails. | Old Windows / TLS-intercepting proxy. | Update Windows; bypass the corporate proxy for NPHIES hosts. |
| Gateway fails. | Source IP not whitelisted with NPHIES. | Confirm the host's public IP, contact NPHIES to whitelist. |
| Inbound Check fails. | HMS server can't reach the bridge. | Check the path *from HMS to the bridge*: firewall on bridge, network route, HMS *Bridge URL* value. |

\newpage

#### Human Resources Module

The **Human Resources** module manages the full employee lifecycle in HMS:
from recruitment, hiring and contracting, through day-to-day personnel
actions (transfers, promotions, appraisals, leaves, sick leave, document
expiry), all the way to end-of-service settlement. The **Payroll**
sub-module turns this data into monthly salaries, deductions, loans and
pay slips.

##### What you can do in HR

* **Maintain an employee master file** — personal data, contact, documents
  (passport, residence, visa, council certificates), bank, dependants,
  qualifications, experience.
* **Manage the organisation chart** — branches, departments, positions and
  vacancies, salary packages, periodic allowances.
* **Run recruitment** — register candidates, link them to vacancies and
  recruitment agencies, convert candidates into employees.
* **Issue and renew contracts** — fixed-term, part-time, renewable, with
  automatic alerts 30 and 180 days before expiry.
* **Record personnel actions** — termination, promotion / demotion,
  transfer, salary change, with a three-level approval workflow
  (Department Head  Project Director  Hospital Director).
* **Process leaves** — annual vacation requests, sick leave, educational
  leave, travel authorisation, leave extensions, dependant tickets.
* **Run appraisals** and link them to re-contracting and salary raises.
* **Track expiring documents** — passports, residences, visas, S.C.C.
  certificates — with built-in alerts.
* **Process payroll** — pay codes, pay runs, registers, pay slips, loans.
* **Print 25+ HR reports** — staff lists by nationality / sponsor /
  religion, salary registers, due vacations, recruitment, Saudization,
  termination, turnover, …

##### How to open the module

From the HMS main menu open **Human Resources** (and **Payroll** for the
pay-cycle pages). The module is registered in `MAIN_Menu` as:

| Menu entry | Module code | Launched by |
|---|---|---|
| Human Resources | `HR` | `Admin.exe` |
| Payroll | `PR` | `Admin.exe` |

##### Module map

```
HR
├── Master files
│   ├── Employees ............ HR_Employee.FT    search via HR_Employee_Fast.ST
│   ├── Departments .......... HR_Department.FT
│   ├── Positions ............ HR_POSITION.FT
│   ├── Packages (salary) .... HR_PACKAGE.FT
│   ├── Periodic Allowances .. HR_PRDALW.FT
│   ├── Agencies ............. HR_Agency.FT
│   └── Certificates ......... HR_Certificate.FT
├── Recruitment
│   ├── Vacancies ............ HR_VACANCY.FT
│   └── Candidates ........... HR_Candidate.FT
├── Contracts ................ HR_Contract.ft
├── Personnel Actions ........ HR_Action.FT
├── Appraisals ............... HR_Appraisal.FT
├── Leaves
│   ├── Vacation request ..... HR_Vacation.FT
│   ├── Travel auth .......... HR_VAUTH.FT
│   └── Extension ............ HR_Extension.FT
├── Documents
│   ├── Visa ................. HR_VISA.FT
│   └── Sick leave ........... MF_SickLeave.FT  /  MF_SickLeave2.FT
├── Overview dashboard ....... HR_Overview.ST  (branch-filtered)
└── Reports .................. ~25 RPT/INI under  Report template/

PR (Payroll)
├── Pay Codes ................ PR_PayCode.FT
├── Pay Runs ................. PR_PayRun.FT
├── Registers & slips ........ PR_Register
└── Loans .................... PR_Loan
```

 Continue to **[Getting Started](getting-started.md)** or jump straight to
**[Employees](employees/index.md)**.

\newpage

#### Getting Started with HR

This walkthrough takes you from a freshly-installed HMS to your first
fully-paid employee in **10 steps**. Allow about 30 minutes for the first
employee; subsequent employees take 2–3 minutes.

!!! tip "Before you start"
    Make sure the **HR Administrator** role is assigned to your user, and
    that the **Branches** lookup contains at least one branch (Abha,
    Dammam, Riyadh, Qassem, Jeddah are the factory defaults shipped with
    the demo).

##### 1. Set up the organisation

1. Open **Data Setup  HR  Branches** and add your hospital branches.
2. Open **Data Setup  HR  Departments** (`HR_Department.FT`) and add
   each department. Set the **Cost Centre** (`HRD_CstCtr`) — it is used
   by Payroll for GL postings.
3. Open **Data Setup  HR  Positions** (`HR_POSITION.FT`) and add the
   job titles you use. The **Vacation Days per Year** field becomes the
   default annual leave for any contract on this position.

##### 2. Create salary packages

Open **HR  Packages** (`HR_PACKAGE.FT`) and define each standard salary
package (e.g. *Consultant — Saudi*, *Nurse — Expat*). A package is a
template for basic + allowances that you reuse on contracts.

##### 3. Define periodic allowances

Open **HR  Periodic Allowances** (`HR_PRDALW.FT`) for fixed monthly
add-ons that are not part of the package (e.g. *Mobile*, *Schooling*,
*Housing top-up*).

##### 4. Open vacancies

Open **HR  Vacancies** (`HR_VACANCY.FT`) and add the open positions
you are recruiting for. A vacancy ties together **Branch + Department +
Position + Required nationality / gender + Recruitment source**.

##### 5. Register candidates

For each applicant open **HR  Candidates** (`HR_Candidate.FT`) and
record personal data, passport, residence, expected arrival (ETA) and
the **Vacancy** they applied for. Candidates can be linked to a
**Recruitment Agency** (`HR_Agency.FT`).

##### 6. Hire — convert candidate to employee

Open the candidate and use **Actions  Hire** (or open the employee
form directly via **HR  Employees** `HR_Employee.FT`). The candidate's
personal data is copied into the new `HR_Employee` record and an
**Employee ID** is auto-generated by the `HR_Employee` counter.

##### 7. Issue the first contract

On the employee form go to the **Contracts** tab and add a new
contract (`HR_Contract.ft`):

* Start / end dates
* Package (auto-fills basic + housing + transportation + mobile)
* Tickets per year (employee / family)
* Vacation days
* Type (married/single, permanent/part-time)

##### 8. Add allowances & dependants

Use the **Allowances**, **Dependants**, **Qualifications** and
**Experience** tabs of the employee form to complete the file.

##### 9. Configure payroll codes

Open **Payroll  Pay Codes** (`PR_PayCode.FT`) and verify that the
shipped factory codes (BAS, HOU, TRA, MOB, GOSI, …) match your
chart-of-accounts. Add custom deduction codes (e.g. *Loan repayment*,
*Salary advance*).

##### 10. Run the first payroll

Open **Payroll  Pay Run** (`PR_PayRun.FT`):

1. Set the **Period Start** (first of month).
2. Choose **Branch** and (optionally) **Department** to restrict the run.
3. Click **Generate**. A **PR_Register** is created with one
   **PR_RegDet** line per employee × pay code.
4. Review, post to GL, and print pay slips (`PR_PaySlip.rpt`).

 Continue to **[Employees  Personal Info](employees/personal.md)**.

\newpage

###### Employees

The **Employee** record is the heart of the HR module. Every other
HR object (contract, salary, action, leave, payroll register) hangs
off an `HR_Employee.Id`.

###### How to open

* **HR menu  Employees** — opens the searchable list
  (`HR_Employee_Fast.ST`, also reachable from any picker via the
  *Employee* lookup).
* From a vacancy or candidate — the **Hire** action creates a new
  employee linked back to the source candidate.

###### The Employee form (`HR_Employee.FT`)

The form is organised into **16 tabs**:

| # | Tab | What it holds |
|---|---|---|
| 1 | **Personal** | Name (EN/AR), date & place of birth, gender, nationality, religion, marital status, ID photo |
| 2 | **Employment** | Branch, department, position, vacancy, status, joining date, attendance card |
| 3 | **Contracts** | List of contracts (`HR_Contract.ft`) — start/end, package, basic, ticket entitlement |
| 4 | **Qualifications** | Degrees, certifications, S.C.C. (Saudi Council) certificate number / expiry / profession |
| 5 | **Salary** | Salary history (`HR_Salary`) — every package or action change creates one row |
| 6 | **Allowances** | Per-employee allowances (`hr_employee_allawence`) |
| 7 | **Tickets** | Travel tickets owed and used (`hr_employee_ticket`) |
| 8 | **Leaves** | Vacation entries (`hr_employee_vacation`), accrued / taken / remaining |
| 9 | **Overtime** | Overtime hours (`hr_employee_overtime`) |
| 10 | **Dependants** | Spouse and children (`HR_Employee_child`) |
| 11 | **End of Service** | EOS settlement — last working day, years of service, EOS amount |
| 12 | **Notes** | Free-text notes |
| 13 | **Contact** | Address, phone, mobile, email, P.O. Box, ZIP, emergency contact (SOS) |
| 14 | **Experience** | Prior work history (`HR_EMPLOYEE_Experience`) |
| 15 | **Earned Leaves** | Computed earned leave balance |
| 16 | **Incentives** | Performance / spot bonuses (`HR_Incentive`) |

###### Banner

A green **banner** at the top of the form (procedure `HR_EMPLOYEE_BANNER`)
shows at a glance: full name, employee number, position, department,
branch, and contract status.

###### Alerts

Two alert strips scroll at the top:

* **HR_EMP_Alert** — expiring documents (passport, residence, S.C.C.,
  contract end, visa) within the next 30 days.
* **HR_EMP_Note_Alert** — any free-text note flagged as alert.

###### Underlying tables

| Table | Use |
|---|---|
| `HR_Employee` | Master record |
| `HR_PKT_Employee` | Edit-buffer (ghost table) — your unsaved changes live here until **Save** |
| `HR_Employee_child` | Dependants |
| `HR_EMPLOYEE_Experience` | Prior employment |
| `hr_employee_qualification` | Diplomas / certificates |
| `hr_employee_vacation` | Vacation history |
| `hr_employee_ticket` | Tickets |
| `hr_employee_overtime` | Overtime hours |
| `hr_employee_allawence` | Personal allowances |
| `HR_Salary` | Salary history (one row per change) |
| `HR_PKALW` | Package allowance breakdown |

 Next: **[Personal Info](personal.md)**

\newpage

###### Personal Info (Tab 1)

The **Personal** tab captures the legal identity of the employee.

###### Fields

| Group | Field | Notes |
|---|---|---|
| Name (EN) | First / Father / Grand-Father / Family | Required. Used on contracts, pay slips, certificates. |
| Name (AR) | الاسم / الأب / العائلة | Stored in `HR_EMP_First_A`, `HR_EMP_Father_A`, `HR_EMP_Family_A`. Required for Saudi labour-office filings. |
| Birth | Date of Birth, Place of Birth | |
| Identity | Gender, Nationality, Religion, Marital Status, Blood Group | All come from look-up tables (Data Setup). |
| Impairment | Impaired (yes / no) | Drives the *Disability* line in regulatory reports. |

###### Tips

* The **full name** field (`HR_EMP_NAME` / `HR_EMP_NAME_A`) is computed
  automatically from the four name parts on save — never edit it
  directly.
* Use the **photo** placeholder on the right to attach an ID picture
  (drag-and-drop or click *Browse*). Photos are stored under
  `wwwroot/upload/` per the **Imaging** settings.
* The **Saudi Council Certificate** block on the *Qualifications* tab
  uses the *Nationality* set here to enable / disable validation.

\newpage

###### Employment (Tab 2)

The **Employment** tab is what links a person to a job inside the
hospital.

###### Fields

| Field | DB column | Purpose |
|---|---|---|
| Employee Number | `Main_Number` | The number printed on the ID badge. Auto-allocated via the `HR_Employee` counter; can be overridden. |
| Previous Number | `Previous_Number` | Legacy code from your previous HR system, for cross-reference. |
| Accounting Number | `Accounting_Number` | The supplier code in the GL; used by Payroll to post salary to the correct vendor. |
| Insurance Number | `Insurance_Number` | GOSI / national insurance reference. |
| Attendance Card | `Attendance_Card_Number` | Card / badge number — fed by the time-and-attendance device. |
| Branch | `HR_EMP_Branch` | Required. Drives all branch-filtered reports. |
| Department | `HR_EMP_Department` | Required. Drives the cost-centre on payroll. |
| Position | `HR_EMP_Position` | Required. Determines default vacation / package. |
| Vacancy | `HR_EMP_VACANCY` | The specific opening this employee occupies. |
| Status | `Status` | Active / On Leave / Suspended / Terminated. |
| Category | `Category` | Free-form grouping (e.g. *Clinical*, *Admin*, *Support*). |

###### Behaviour

* Changing **Branch + Department + Position** does **not** automatically
  create a `HR_PosHist` history row — use the **Transfer** personnel
  action (see [Transfer](../actions/transfer.md)) so the change is
  audited.
* The **Vacancy** field is validated against `HR_Vacancy`. An employee
  cannot occupy a vacancy that is inactive or already filled — use the
  **Clear Vacancy** action (`HR_Employee_Clear_Vacancy`) to release it.

\newpage

###### Contracts (Tab 3)

Every employee has one **active contract** and (optionally) a history
of expired or terminated contracts. The contract drives **basic salary,
allowances, ticket entitlement, vacation days** and the **end-of-service
formula**.

###### Contract form (`HR_Contract.ft`)

The form has two tabs: **Information** and **Position Vacancy History**.

###### Information tab

| Field | DB column | Notes |
|---|---|---|
| Contract Number | `Contract_Number` | Auto-incremented serial. |
| Start / End Date | `Start_date`, `End_date` | End-of-service is calculated from these. |
| Married / Single | `Type_Married_single` | Affects family-ticket entitlement. |
| Permanent / Part-time | `Type_permanent_parttime`, `Parttime` | Part-time contracts skip GOSI deduction. |
| Tickets for Employee | `Tickets_for_employee` | Free yearly tickets. |
| Tickets for Family | `Tickets_for_Family` | |
| Basic Salary | `Basic` | The base for EOS and all *based-on-basic* allowances. |
| Housing | `Housing` | |
| Transportation | `Transportation` | |
| Mobile | `Mobile` | |
| Schooling | `Schooling` | |
| Year / Model of Car | `Year_Model_Car` | If the contract includes a company car. |
| Additional Allowances | `Addionnal_allowances` | Free-text amount. |
| Job Type | `Job_Type` | Free-text. |
| Title | `Title` | Job title printed on the contract document. |
| Overtime allowed | `Overtime_allowed` | Yes / No. |
| Vacation Days | `Vacation_days` | Annual leave entitlement. |
| Period before vacation | `Period_before_vacation` | Months of service required before the employee can claim leave. |
| Package | `PACKAGE` | Reference to `HR_Package`. If set, basic/housing/transport/mobile are copied from the package and grey-locked. |

###### Position Vacancy History tab

Displays the grid `HR_PosHist.GT` — every transfer / promotion shown
chronologically: branch, department, position, vacancy, start, end.

###### Renewal & extension

| SP | When fired |
|---|---|
| `HR_Contract_Renew` | Creates a brand-new contract record carrying forward the same package. |
| `HR_Contract_Extend` | Extends the **End_date** of the current contract without creating a new one. Sets `CT_Extended = 1`. |
| `HR_APRContract` | Triggered from an Appraisal — auto-renews the contract using the appraisal's recommended package. |
| `HR_EXTContract` | Background SP that processes the *Extension* personnel action. |

###### Alerts

Two stored procedures populate the dashboard alerts:

* `HR_Action_ContractPending_Alert` — contracts pending approval.
* The two views `HR_Contract_30d` / `HR_Contract_6m` feed the
  *Expiring contracts* drill-down list in the HR Overview.

###### Status values (`HR_Contract_Status`)

`A` Active &nbsp;·&nbsp; `E` Expired &nbsp;·&nbsp; `T` Terminated &nbsp;·&nbsp; `R` Renewed &nbsp;·&nbsp; `X` Extended

\newpage

###### Salary & Allowances (Tabs 5 + 6)

###### Salary history (`HR_Salary`)

Every time the basic salary changes — through a new contract, a
personnel action, or an appraisal raise — a row is inserted into
`HR_Salary`. The tab shows the full timeline.

| Column | Meaning |
|---|---|
| Effective Date | When the new salary starts. |
| Basic Salary | Base amount. |
| Housing / Transportation / Mobile | Standard allowances from the package. |
| Additional Allowances | Free amount. |
| SL_Appraisal | FK to the appraisal that triggered the raise (if any). |
| SL_Action | FK to the personnel action that triggered the change. |
| SL_Fixed | If checked, the row is locked and Payroll uses **exactly** these amounts (no further proration). |
| SL_InActive | Hide from active calculations (kept for audit). |

Stored procedures that write into `HR_Salary`:

* `HR_ACTION_Salary_Add` — fired by *Promotion / Demotion*.
* `HR_APRS_Salary_Add` — fired by an appraisal raise.
* `HR_APRS_Salary_FIX` — locks the row after the appraisal cycle closes.

###### Allowances grids

| Tab | Grid file | Table | Purpose |
|---|---|---|---|
| Allowances | `HR_Alw.GT` | `hr_employee_allawence` | Personal one-off or recurring add-ons. |
| Package allowances | `HR_PKALW.GT` | `HR_PKALW` | Standard allowance breakdown from the **Package**. |
| Periodic | `HR_PRDALW.GT` | `HR_PRDALW` | Recurring monthly allowances (Mobile top-up, schooling). Loaded into Payroll automatically. |
| Incentives | `HR_Incentive.GT` | `HR_Incentive` | Performance / spot bonuses. Linked to `HR_IncentiveType`. |

###### How Payroll consumes these tables

When you click **Generate** on a Pay Run, the procedure
`HR_MonthlySalaries` does roughly the following for every employee in
the selected branch / department:

1. Read the current `HR_Salary` row whose Effective Date ≤ Period End.
2. Add every active `hr_employee_allawence` row (one-shot if start/end
   matches the period; recurring otherwise).
3. Add every active `HR_PRDALW` row.
4. Add the current month's `HR_Incentive` rows.
5. Subtract deductions (`HR_Deductions`, loan repayments
   `PR_Loan_Payments`).
6. Write one line per pay code into `PR_RegDet` and update the totals
   on `PR_Register`.

\newpage

###### Leaves & Tickets (Tabs 7 + 8)

###### Leaves tab

The **Leaves** tab shows the employee's lifetime leave ledger
(`hr_employee_vacation`).

| Column | Meaning |
|---|---|
| Vacation Type | Annual, Sick, Educational, Hajj, Compassionate, Unpaid, … (look-up `HR_VacationType`). |
| From / To | The leave window. |
| Days | Calendar days; weekends/holidays excluded via `HR_Holiday`. |
| Status | Pending  Approved  Taken  Reversed. |
| Travel Auth | FK to `HR_VAUTH` if the employee is travelling abroad. |
| Actual Leave | Real return date — may differ from planned. |

The summary box on the right shows the formula:

> **Accrued + Earned − Used = Total Days**

— a live read-out of `HR_EMP_VacDue`, `HR_EMP_VacTaken`,
`HR_EMP_VacRemain`. It is recomputed by `HR_SP_VAC_CALC` whenever the
form opens.

###### Tickets tab

`hr_employee_ticket` — one row per yearly ticket the employee is owed.

| Column | Meaning |
|---|---|
| Year | Entitlement year. |
| Type | Employee / Family. |
| Issued | Yes if a ticket has been issued. |
| Amount | Cash value (when paid as cash-in-lieu). |
| Vacation | FK to the `hr_employee_vacation` row the ticket was used on. |

###### Holidays

`HR_Holiday` stores official paid holidays. The day-count for vacation
requests uses these to skip weekends / public holidays. Maintain it
once a year under **Data Setup  HR  Holidays**.

###### Earned leaves (Tab 15)

A read-only view that runs `HR_ACTION_ACCRUED_LEAVE_CALC` to show:

```
(Contract Days − Unpaid Leaves >14 days − Holidays) / 365 × Annual Leave = Accrued Days
```

\newpage

###### End of Service (Tab 11)

The **End of Service** tab shows the EOS settlement that will be paid
if the employee leaves today. The figures are *computed live* and
refreshed every time you open the form.

###### Fields

| Field | DB column |
|---|---|
| End-of-Service Type | `HR_EMP_EOS_Type` (`HR_EOS` look-up) |
| Last working day | `HR_EMP_EOS_LastDay` |
| Basic salary used | `HR_EMP_EOS_BasicSalary` |
| Years of service | `HR_EMP_EOS_Years` |
| Months per year of service | `HR_EMP_EOS_MonthForYear` (Saudi labour law: ½ month for the first 5 years, full month afterwards) |
| EOS amount | `HR_EMP_EOS_Amount` |
| Service-Award difference | `ServiceAward_Difference` (manual top-up) |

###### Procedures

| Procedure | When |
|---|---|
| `HR_SP_EOS_CALC` | Live recompute on form open. |
| `HR_EOS_DIF_CALC` | Compute the difference between contract-period award and accumulated reserve for a single employee. |
| `HR_EOS_DIF_CALC_ALL` | Same, batch for every active employee. Run nightly. |

###### Termination flow

The EOS amount is **finalised** when a *Termination* personnel action is
applied:

1. Open the employee  **Actions** tab  **New**  Type *Termination*.
2. Fill in the *Termination* sub-tab (resignation, end-of-contract,
   Article 80, medical, etc.).
3. Fill the **Entitlements** lines (`TERM_ENT_AccruedLeaves`,
   `TERM_ENT_DaysPay_Emp`, `TERM_ENT_Tickets`, …).
4. Send for **three-level approval** (Department Head  Project
   Director  Hospital Director).
5. On final approval `HR_Action_Apply` runs:
   * marks `HR_Employee.Resigned = 1`
   * closes the active contract
   * locks `HR_Salary` rows
   * generates the final pay-slip line in the next Pay Run.

\newpage

###### Recruitment

The Recruitment pipeline turns an **open vacancy** into a **hired
employee** in three stages:

```
Vacancy    Candidate    Hire (Employee)
```

Optionally backed by a **Recruitment Agency**.

###### Pages

* **[Vacancies](vacancies.md)** — define what you are hiring for.
* **[Candidates](candidates.md)** — track applicants from CV to arrival.
* **[Agencies](agencies.md)** — manage external recruiters and their
  commissions.

###### Related lookups

| Table | Purpose |
|---|---|
| `HR_CandidateStatus` | New / Screened / Interviewed / Offered / Rejected / Hired |
| `HR_Vacancy_Status` | Open / On Hold / Filled / Cancelled |
| `HR_RecSource` | LinkedIn, Bayt, Walk-in, Agency, Referral, … |
| `HR_VACClass` | Vacancy classification (Critical / Standard / Replacement) |
| `HR_POSCATEG` | Position category — used for headcount budget reporting |

\newpage

###### Vacancies

A **Vacancy** is an approved opening — branch + department + position +
requirements — that recruitment will fill.

###### Vacancy form (`HR_VACANCY.FT`)

Four tabs: **Information**, **History**, **Actions**, **Note**.

###### Information tab

| Field | DB column |
|---|---|
| Code | `HVC_CODE` (auto-incremented from `HVC_CODE_TMP`) |
| Name (EN / AR) | `Name`, `HVC_Name_A` |
| Branch / Department / Position | `Branch`, `Department`, `Position` |
| Count | `Count` — number of identical seats this vacancy represents |
| Required Gender | `HVC_Gender` |
| Required Nationality | `HVC_Nationality` |
| Salary | `HVC_Salary` (target salary) |
| Recruitment Source | `HVC_RecSource` |
| Classification | `HVC_CLASS` (Critical / Standard / Replacement) |
| Status | `HVC_Status` (Open / Filled / On Hold / Cancelled) |
| ETA | `HVC_ETA` — expected fill date |
| Target Vacancy | `HVC_TargetVacancy` — used when one vacancy is being replaced by another |
| Transient | `HVC_Transient` — a temporary vacancy auto-created by a transfer |

###### Transient vacancies

When you transfer an employee, the *Source* position momentarily has an
employee leaving and the *Destination* position has an employee
arriving. To keep headcount accounting clean, HMS auto-creates a
**transient** vacancy on each side. Three SPs manage them:

* `hr_Vacancy_Create_Transient` — create.
* `hr_Vacancy_Transient_Process` — link to the originating action.
* `hr_Vacancy_Transient_Process_All` — nightly sweep.

###### Vacancy load

`HR_Vacancy_Load` is the SP that powers vacancy pickers everywhere
(Employee form, Candidate form, Personnel Action transfer tab). It
excludes filled / cancelled vacancies.

###### Reports

* **HR Vacancies** (`HR_Vacancies.ini`  `HR_Recruitment.rpt`) — open
  vacancies grouped by branch & department.
* **HR Recruitment** — same, with pipeline counts of candidates per
  vacancy.

\newpage

###### Candidates

A **Candidate** is anyone you are considering for a vacancy. The
record carries 95 % of the data an `HR_Employee` carries — so that on
**Hire** the data simply copies across.

###### Candidate form (`HR_Candidate.FT`)

Five tabs: **Personal**, **Employment**, **Contact**, **Notes**, **Note
List**.

###### Personal tab

| Field | DB column | Notes |
|---|---|---|
| Number | `Number` | Candidate reference (CV-001…). |
| Name (EN/AR) | `First`, `Father`, `Grand_Father`, `Family`, `First_A`, `Father_A`, `Family_A` | |
| Date / Place of Birth | `Date_of_Birth`, `Place_of_Birth` | |
| Gender / Nationality / Religion | `Gender`, `Nationality`, `Religion` | |
| Marital | `Marital` | |
| Address / Phone / Mobile / Email / PO Box / ZIP | `Address`, `Phone`, `Mobile`, `Email`, `POBOX`, `ZIP` | |
| Origin Country Address / Phone | `Origin_Country_Address`, `Origin_Country_Phone` | |
| Spouse / Children | `Spouse_name`, `Children_number` | |
| Impaired | `Impaired` | |
| Photo | image | |

###### Employment tab

| Field | DB column |
|---|---|
| Vacancy | `VACANCY` |
| Position / Department / Branch | `Position`, `Department`, `Branch` |
| Category | `Category` |
| Status | `Status` (`HR_CandidateStatus`) |
| Agency | `Agency` (`HR_Agency`) |
| ETA / PTA | `ETA`, `PTA` (expected / planned travel arrival) |
| Current sponsor name | `Current_sponsor_name` |
| Passport (Number / Place / Expiry / Issue date) | `Passport_*` |
| Residence (Number / Place / Expiry) | `Residence_*` |

###### Hire workflow

1. Move the candidate's **Status** to *Offered* and obtain acceptance.
2. Click **Actions  Hire**. The system:
   * Inserts a row into `HR_Employee` (new `Id`, auto Main_Number).
   * Copies all personal/contact/passport/residence fields.
   * Sets `HR_Employee.HR_EMP_Candidate` = source candidate `Id` (audit
     link, also exposed as `EmployeeID` on the candidate row).
   * Closes the **Vacancy** (`HR_Vacancy.HVC_Status`  *Filled*) if the
     vacancy count drops to 0.
3. Open the new employee record and issue the first **Contract**
   (see [Contracts](../employees/contracts.md)).

\newpage

###### Recruitment Agencies

External recruiters (manpower agencies) are recorded in
`HR_Agency` and edited via `HR_Agency.FT`.

###### Fields

* Name, country, contact person, phone, e-mail.
* Commission rate (per hire or per month of salary).
* Active flag.

###### Where the link appears

* On a **Candidate** (Employment tab  *Agency*).
* On an **Employee** (`HR_EMP_Agency`) — useful for tracking which
  agency originally supplied the staff member.
* On the **Recruitment** report grouped by Agency.

\newpage

###### Organisation

The **Organisation** group contains the four reference structures that
every employee and contract hangs off:

| Page | What it is |
|---|---|
| [Departments](departments.md) | The cost-centres under each branch. |
| [Positions](positions.md) | Job titles with default vacation days. |
| [Packages](packages.md) | Standard salary templates re-used on contracts. |
| [Periodic Allowances](periodic-allowances.md) | Recurring monthly add-ons fed straight into Payroll. |

These pages are normally maintained by an **HR Administrator** —
front-line HR users only *consume* them via pickers.

\newpage

###### Departments

`HR_Department` is the cost-centre dimension of the hospital.

###### Form (`HR_Department.FT`)

| Field | DB column | Notes |
|---|---|---|
| Code | `HRD_Code` | Short alpha-numeric code (used on pay slips). |
| Name (EN) | `Name` | Required. |
| Name (AR) | `HRD_Name_Arabic` | |
| Cost Centre | `HRD_CstCtr` | FK to the GL cost-centre table; drives the salary GL line. |
| ID2 | `ID2` | Secondary code for legacy interfaces. |

###### Where it appears

* Mandatory on every **Employee** (`HR_EMP_Department`).
* Mandatory on every **Vacancy** (`HR_Vacancy.Department`).
* Selectable on **Pay Runs** (`PR_Register.PRR_Department`) so payroll
  can be run department-by-department.
* Reported on every HR roster (by-department staffing, by-department
  salary cost, etc.).

###### Tips

* Do not delete a department once an employee has been linked to it —
  inactivate it instead (add an `Inactive` lookup row in the local
  status setup).
* The **Cost Centre** value is read by `HR_MonthlySalaries` when the
  pay run posts to GL — make sure it matches an existing GL CC, or the
  journal will fail with a *missing CC* warning.

\newpage

###### Positions

`HR_POSITION` is the catalogue of job titles available in the
hospital.

###### Form (`HR_POSITION.FT`)

| Field | DB column | Notes |
|---|---|---|
| Code | `HRPOS_CODE` | Short code printed on staffing-schedule reports. |
| Name (EN) | `Name` | Required. |
| Name (AR) | `HRPOS_Name_Arabic` | |
| Category | `HRPOS_Category` | FK to `HR_POSCATEG` (Medical / Nursing / Tech / Admin / Support). |
| Vacation Days per Year | `VacDaysPerYear` | The factory annual leave for any contract created on this position. |
| ID2 | `ID2` | Secondary code. |

###### Where it appears

* On every **Employee** (`HR_EMP_Position`) and **Vacancy**
  (`HR_Vacancy.Position`).
* On every **Candidate** (`HR_Candidate.Position`).
* On the **Staffing Schedule** report (`HR_StaffingSchedule.rpt`).
* The **Saudisation** report groups by `HRPOS_Category` to compute
  national / non-national ratios.

\newpage

###### Packages

A **Package** is a re-usable salary template. Instead of typing basic
+ housing + transport on every contract, you create the package once
and pick it on the contract.

###### Form (`HR_PACKAGE.FT`)

| Field | DB column |
|---|---|
| Name (EN) | `Name` |
| Name (AR) | `NAME_A` |
| Print Name (AR) | `HRP_PrintName_A` (short label printed on slips when space is tight) |
| Notes | `Note` |

###### Allowance breakdown

Each package has child rows in `HR_PKALW` (one row per allowance
type — basic, housing, transportation, mobile, schooling, …):

| Column | Meaning |
|---|---|
| Type | FK to `HR_ALWTYPE`. |
| Amount | Fixed amount, or |
| Percent | % of basic (Type-Married, Type-Single — both possible). |
| Currency | Currency of the package. |

Maintained from the **Allowances** grid on the package form
(`HR_PKALW.GT`).

###### Refresh propagation

When you change a package's amounts, **existing contracts are NOT
updated automatically** — the change applies only to new contracts
and to contracts when they are renewed via `HR_Contract_Renew`.

To push a package change to every active contract use the helper SP
`HR_PACKAGE_UPDATE` (run from a SQL prompt with the package ID as
parameter).

\newpage

###### Periodic Allowances

Periodic allowances (`HR_PRDALW`) are recurring monthly amounts that
are paid *outside* the salary package — typically *Mobile reimbursement*,
*Schooling top-up*, *Housing increment*, *Acting allowance*, …

###### Form (`HR_PRDALW.FT`)

| Field | DB column |
|---|---|
| Employee | `EmployeeID` (picker `HR_Employee_Fast.ST`) |
| Allowance Type | `Type` (FK to `HR_PRDALWType`) |
| Amount | money |
| Frequency | Monthly / Quarterly / Yearly |
| Start Date / End Date | activity window |
| Active | yes/no |
| Banner | `HR_PRDALW_BANNER` SP populates the header |

###### How payroll consumes them

`HR_MonthlySalaries` includes every `HR_PRDALW` row whose period overlaps
the pay-run period and whose Active flag = 1. The amount lands on
`PR_RegDet` under the matching pay code.

###### Tip

Use `HR_PKALW_ORG_Add` (admin helper) to bulk-add the same
allowance to every employee in a department — e.g. when the board
approves a *Critical-care allowance* for all ICU nurses.

\newpage

###### Personnel Actions

A **Personnel Action** (`HR_Action.FT`) is the auditable record of any
change to an employee's job that is not a routine data edit. Every
action goes through a **three-level approval workflow** before it is
applied.

###### Action types

| Type | Tab | What it changes |
|---|---|---|
| **Termination** | Tab 2 | Closes the contract, computes EOS, blocks future pay. |
| **Promotion / Demotion** | Tab 3 | Title + salary change. Writes a new `HR_Salary` row. |
| **Transfer** | Tab 4 | Branch / department / position change. Writes a `HR_PosHist` row and updates vacancies. |
| **Salary Change** | shares Promotion tab | Salary only, no title change. |
| **Contract Renewal** | (auto from Appraisal) | Inserts a new contract. |
| **Extension** | shares Promotion tab | Extends current contract `End_date`. |

###### Approval workflow

```
Created  Department Head approval  Project Director approval  Hospital Director approval  Applied
```

* Each approval level stamps its **User + Date** on `HR_Action`
  (`APRV_DepHead`, `APRV_ProjDir`, `APRV_HospDir`).
* Approval levels can be **skipped** by an admin override (see *Policy
  Verification* tab).
* `HR_Action_Apply` is the SP that performs the final mutation once
  *all* required approvals are in.

###### Banner & alerts

* `HR_Action_BANNER` — top strip on the form showing employee name,
  current position, action serial, status.
* `HR_Action_Alert` — dashboard alert for actions pending **your**
  approval (filtered by `HR_ActionApproval`).

###### Form tabs

1. **Information** — type, date, employee, basic action data.
2. **Termination** — reason flags, last working day, entitlements.
3. **Promotion / Demotion** — new title, new vacancy, new basic.
4. **Transfer** — source vs destination branch / department / vacancy.
5. **Dept-Head Approval** — note, signature, date.
6. **Project-Dir Approval** — note, signature, date.
7. **Hospital-Dir Approval** — note, signature, date.
8. **Policy Verification** — admin override.

 Details on the most-used actions:

* [Termination](termination.md)
* [Promotion / Demotion](promotion.md)
* [Transfer](transfer.md)
* [Appraisals](appraisals.md)

\newpage

###### Termination

A **Termination** action ends the employment relationship and triggers
the final EOS settlement.

###### Termination reasons (Tab 2 flags)

| Flag | Meaning |
|---|---|
| `TERM_Resignation` | Employee resigned voluntarily. |
| `TERM_ReContractNotOffered` | Hospital decided not to renew. |
| `TERM_ReContractNotWished` | Employee declined to renew. |
| `TERM_MedicalReason` | Medical incapacity. |
| `TERM_Article80` | Saudi Labour Law Art. 80 — termination for cause. |
| `TERM_DuringProbation` | Within the probation period — reduced entitlements. |
| `TERM_SCCFailed` | Failure to obtain / renew the Saudi Council certificate. |
| `TERM_Others` | Free-text reason. |
| `HAC_TermReason` | FK to `HR_TermReason` look-up (free taxonomy you maintain). |

###### Entitlements block

Filled by the HR officer before the action is submitted:

| Field | Meaning |
|---|---|
| `TERM_ENT_AccruedLeaves` | Unused leave days to pay out. |
| `TERM_ENT_TotalLeaves` | Total leave balance (informational). |
| `TERM_ENT_ServiceAward_TotalPeriod` / `_CompletedTerms` | Which formula to use for end-of-service award. |
| `TERM_ENT_Tickets` | Pending tickets to cash out. |
| `TERM_ENT_DaysPay_Emp` | Days of salary owed to employee. |
| `TERM_ENT_DaysPay_Hosp` | Days the *employee* owes the hospital (notice not served). |
| `HAC_TicketToDeduct` | Cost of un-served-notice ticket. |
| `HAC_VisaToDeduct` | Visa cost to deduct if employee resigns before threshold. |
| `HAC_LastWorkingDay` | The last day the employee physically works. |
| `HAC_TermLetterDate` | When the termination letter was issued. |

###### On apply

When the *Hospital Director* approval is stamped, `HR_Action_Apply`:

1. Sets `HR_Employee.Resigned = 1`, `Date_of_resignation = HAC_LastWorkingDay`.
2. Closes the active contract (`HR_contract.Status = 'T'`,
   `CT_Effective_End_Date = HAC_LastWorkingDay`).
3. Inserts a `PR_RegDet` settlement line in the next pay run (one line
   per entitlement: accrued leave, tickets, EOS, notice).
4. Releases the **Vacancy** (`HR_Vacancy.HVC_Status`  *Open*) unless
   `HVC_Transient = 1`.
5. Locks all `HR_Salary` rows for this employee.

###### Reports

* **HR Termination** (`HR_Termination.ini`).
* **HR Turnover** (`HR_Turnover.ini`).

\newpage

###### Promotion / Demotion

A **Promotion / Demotion** action changes the employee's title and/or
basic salary.

###### Fields (Tab 3)

| Field | Meaning |
|---|---|
| `DPROM_NewTitle` | New job title (free-text or from `HR_POSITION`). |
| `DPROM_NewVacancy` | New vacancy the employee will occupy. |
| `DPROM_Department` | Optional department change. |
| `Cur_Basic` | Current basic salary (read-only, copied from contract). |
| `New_Basic` | New basic salary the HR officer is proposing. |
| `Recom_IncDec` | Calculated absolute increase / decrease. |
| `Recom_IncDecPerc` | Calculated %. |

###### On apply

`HR_Action_PROMOD_Apply` runs:

1. Inserts a new row in `HR_Salary` with `SL_Action = <this action ID>`
   and `Effective_date = HAC_Effective_Date`.
2. Updates `HR_Employee.HR_EMP_Position` and the contract title.
3. If a new vacancy was supplied, occupies it and frees the previous
   one (transient vacancies are created if branch / dept changes — see
   [Vacancies](../recruitment/vacancies.md)).
4. Stamps `HAC_Action_Applied = 1`.

###### Reversal

If a promotion is later reversed, create a **new** action with
`HAC_ReverseAction = <ID of original>` and select *Demotion*. The SP
`HR_Action_PROMOD_Apply` detects the reversal flag, restores the
previous salary row and inactivates the original raise.

\newpage

###### Transfer

A **Transfer** moves an employee from one *Branch + Department +
Vacancy* to another, without changing salary.

###### Fields (Tab 4)

| Field | Source / Destination |
|---|---|
| `HRTR_S_Branch` | Source branch |
| `HRTR_S_Department` | Source department |
| `HRTR_S_Vacancy` | Source vacancy |
| `HRTR_S_Main_Number` | Source employee badge number (audit) |
| `HRTR_D_Branch` | Destination branch |
| `HRTR_D_Department` | Destination department |
| `HRTR_D_Vacancy` | Destination vacancy |
| `HRTR_D_Main_Number` | Destination badge number |

###### On apply

`HR_Action_TRANS_Apply`:

1. Updates `HR_Employee.HR_EMP_Branch / _Department / _VACANCY`.
2. Inserts a row in `HR_PosHist` recording the move.
3. Creates a **transient** source vacancy via
   `hr_Vacancy_Create_Transient` if the source vacancy was the only
   one of its kind — guarantees headcount accounting balances.
4. Marks destination vacancy as filled.
5. Stamps `HAC_Action_Applied = 1`.

###### Bulk historical import

Use `HR_Action_HIST_Apply_All` to reapply every historical transfer
when you migrate from a legacy HR system (one-shot batch tool).

\newpage

###### Appraisals

Appraisals (`HR_Appraisal.FT`) are the formal performance review
issued at the end of each contract term. The outcome drives
**Re-contracting** and the **annual raise**.

###### Form tabs

1. **Appraisal** — scoring.
2. **Re-Contracting** — the decision to renew / extend / not renew.

###### Scoring fields

| Field | Lookup | Notes |
|---|---|---|
| Job Knowledge | `HR_APRFactor` | A / B / C / D / E rating. |
| Work Quality | `HR_APRFactor` | |
| Work Quantity | `HR_APRFactor` | |
| Overall Appraisal | `HR_APROverall` | Computed from the three factors (configurable in `HR_APRFactor.Weight`). |
| Appraisal Status | `HR_APRStatus` | Draft / Submitted / Approved / Cancelled. |
| Raise (amount) | `Raise` | Approved raise to be added to the next `HR_Salary` row. |
| Recontracting Status | `HR_RecontractingStatus` | Renew / Extend / Do not renew. |
| Employee Approval | `HR_EmpApproval` | Whether the employee has counter-signed. |

###### On submit

`HR_Appraisal_Apply` runs:

1. If **Renew**  fires `HR_APRContract` to insert a new contract.
2. If **Extend**  fires `HR_Contract_Extend` to push out the end date.
3. If a **Raise** is approved  fires `HR_APRS_Salary_Add` to insert
   a new `HR_Salary` row with `SL_Appraisal = <appraisal ID>`.
4. Sets `APRS_Applied = 1`.

`HR_APRS_Salary_FIX` is a nightly tidy-up SP that locks the raise
rows once their effective date is reached.

###### Banner

`HR_Appraisal_BANNER` shows: employee, current contract end, scoring
summary, recommended raise.

\newpage

###### Leaves & Travel

HMS handles three closely-related leave objects:

| Page | Form | What it is |
|---|---|---|
| [Vacation Requests](vacation.md) | `HR_Vacation.FT` | The day-by-day annual / sick / educational leave request. |
| [Travel Authorisation](travel-auth.md) | `HR_VAUTH.FT` | Authorisation for an employee to travel abroad while on leave (used for ticket entitlement & re-entry visa). |
| [Vacation Extensions](extensions.md) | `HR_Extension.FT` | Extend an in-progress leave. |

###### Leave types (`HR_VacationType`)

* **Annual** — counted against `HR_EMP_VacRemain`.
* **Sick** — counted separately; 30 full-pay + 60 half-pay days/year per Saudi labour law.
* **Educational** — exam / study leave.
* **Hajj** — once-in-employment.
* **Compassionate** — bereavement.
* **Unpaid** — does not accrue salary; days >14 reduce service period.
* **Maternity / Paternity**.

\newpage

###### Vacation Requests

###### Form (`HR_Vacation.FT`)

Six tabs: **Request  Educational Leave  Supervisor Approval 
Director Approval  Actual Leave  Dependants Eligibility**.

###### Request tab

| Field | Notes |
|---|---|
| Employee | Picker (`HR_Employee_Fast.ST`) |
| Vacation Type | `HR_VacationType` look-up |
| From / To | Planned dates — must not overlap an existing approved leave. |
| Days | Auto-calculated, holidays from `HR_Holiday` excluded. |
| Reason | Free text. |
| Travel Authorisation | Optional FK to `HR_VAUTH` if travelling abroad. |
| Replacement | Employee covering during the absence (optional). |

###### Approval tabs

Two-level approval: **Supervisor  Director**. Each tab stamps user +
date. Status flows `Pending  SupervisorApproved  Approved  Taken 
Reversed` (lookup `HR_VacReqStatus`).

###### Actual Leave tab

When the employee returns, HR fills:

* Actual From / To dates.
* Days actually taken.
* Notes (e.g. early return, extension granted).

`HR_VacReq_CALC` recomputes the employee's accrued / used / remaining
totals (`HR_EMP_VacDue / VacTaken / VacRemain`).

###### Validation procedures

| SP | What it checks |
|---|---|
| `HR_DueVacations` | Drives the *Due Vacations* report and alert. |
| `HR_Vacation_Alert` | Dashboard alert: leaves starting in 7 days. |
| `HR_Vacation_Alert_Residence` | Cross-checks the employee's residence permit covers the leave + 14 days. |
| `HR_Vacation_TravelALW_Validate` | Validates travel allowance entitlement on the leave row. |
| `HR_Vacation_RPT` | Computes the figures on the *Vacation Statistics* family of reports (VacStat 1-8). |

###### Reports

* **Due Vacations** — `hr_DueVacations.rpt`
* **Vacation Stats** — 8 ready-to-print pivots (`HR_VacSTAT.rpt` …
  `HR_VacSTAT4.rpt` and `hr_vacstat7/8.ini`).

\newpage

###### Travel Authorisation

`HR_VAUTH.FT` records the authorisation for an employee to travel
abroad — needed for **re-entry visa**, **ticket entitlement** and
**residence-permit validity** checks.

###### Key fields

* Employee, From / To dates.
* Destination country / city.
* Re-entry validity date (must be > To).
* Ticket entitlement: cash-in-lieu or in-kind (employee / family).
* Status (`HR_VAUTHStatus`): Pending / Approved / Cancelled / Used.

###### Linked actions

* `HR_VacAction` records the *VacAction* event when the auth is used.
* `HR_VacAction_Apply` consumes the ticket entitlement from
  `hr_employee_ticket`.
* `HR_VacAction_Submit` / `HR_VacAction_AutoApply` drive the approval
  workflow.

###### Reports

* **Employee Tickets** (`hr_EmployeeTickets.rpt`) — outstanding ticket
  ledger.
* **Expiring Documents** (`hr_ExpiringDocs.rpt`) includes residence
  expiry vs travel-auth dates.

\newpage

###### Vacation Extensions

`HR_Extension.FT` is used when an employee on leave requests to
**extend** the leave beyond the originally approved To-date.

###### Workflow

1. Open the *active* vacation row from the employee's Leaves tab.
2. Click **Actions  New Extension**.
3. Fill the new To-date, reason, and any additional unpaid days.
4. Supervisor / Director approval, then `HR_EXTContract` applies the
   change — `hr_employee_vacation` row is updated and accrual is
   recomputed via `HR_VacReq_REQUEST_CALC`.

###### Validation

* The extension cannot push the leave end-date past the **contract
  end-date** (unless the contract is also extended via
  `HR_Contract_Extend`).
* The extension is rejected if the employee's residence expires
  before the new end-date.

\newpage

###### Visas

`HR_VISA.FT` records work-visa applications and renewals for expat
staff.

###### Fields

| Field | Notes |
|---|---|
| Employee | Picker. |
| Visa Type | `HR_VisaType` (Work / Family / Visit / Re-entry). |
| Status | `HR_VISAStatus` (Requested / Approved / Issued / Cancelled / Used). |
| Validity Start | Visa issue date. |
| Validity End | Expiry. |
| Note | Free text. |

`HR_VISA_BANNER` shows the visa lifecycle at the top of the form.

###### Reports

* **Expiring Documents** (`hr_ExpiringDocs.rpt`) — includes visas
  expiring in the next 30/60/90 days.

\newpage

###### Certificates

`HR_Certificate.FT` records professional certificates the employee
holds — and most importantly the **Saudi Council Certificate** (SCC)
which is mandatory for licensed clinical staff.

###### SCC fields (on the Employee form, Qualifications tab)

| Field | DB column |
|---|---|
| Certificate Number | `HR_EMP_SaudiCouncilCert_NO` |
| Issue Date | `HR_EMP_SaudiCouncilCert_DATE` |
| Exam Date | `HR_EMP_SaudiCouncilCert_ExamDATE` |
| Valid (flag) | `HR_EMP_SaudiCouncilCert_Valid` |
| Expiry Date | `HR_EMP_SaudiCouncilCert_EXPDATE` |
| Profession | `HR_EMP_SaudiCouncilCert_Profession` |
| Status | `HR_EMP_SaudiCouncilCert_Status` |
| Not Applicable | `HR_EMP_SaudiCouncilCert_NA` (set for non-clinical staff) |
| Notes | `HR_EMP_SaudiCouncilCert_Note` |

`HR_CCI_UPDATE` is the SP that refreshes SCC validity for all employees
nightly. `hr_Certificate_ADD` is the helper that inserts a certificate
row from the certificate form into the employee's qualifications.

###### Reports

* **Employee Certificates** (`HR_Emp_Certificate.rpt`) — three layouts
  (F1, F2, F3) for different licensing authorities.
* **SaudiCC** (`HR_SaudiCC.ini`) — staff list with current SCC status.

\newpage

###### Sick Leave

Sick leave is recorded on two slightly different forms:

| Form | Use case |
|---|---|
| `MF_SickLeave.FT` | Quick single-day sick leave entered by the employee's manager. |
| `MF_SickLeave2.FT` | Full medical sick-leave certificate issued by the hospital clinic — includes diagnosis, treating physician, ICD code, attachments. The `MF_SickLeave2_SO` and `wMF_SickLeave2_CDC` variants are used in clinics with a different print layout. |

###### Fields

* Employee, From, To, Days.
* Diagnosis / ICD-10 (on the full version).
* Issuing physician (picker into the physician table).
* Attachments (lab results, prescriptions).
* Approved by HR (yes/no), notes.

###### Effect on payroll

* **Up to 30 days** in a service year  full-pay sick leave; no
  payroll deduction.
* **Days 31–90**  75 % pay; the *Sick-deduction* pay code is added to
  the next pay run by `HR_MonthlySalaries`.
* **Days 91+**  unpaid; reduces the period used for end-of-service
  computation.

\newpage

###### Payroll

The **Payroll (PR)** module turns HR data into monthly salaries.

###### Pages

* [Pay Codes](pay-codes.md) — the chart of earnings & deductions.
* [Pay Runs](pay-runs.md) — the monthly batch.
* [Registers & Pay Slips](registers.md) — the resulting transactions
  and the printable pay slip.
* [Loans](loans.md) — staff loans repaid through payroll.

###### Pipeline at a glance

```
HR_Salary  ┐
HR_PRDALW  │
HR_PKALW   ├──  HR_MonthlySalaries  ──  PR_Register
HR_Incentive│                              ├── PR_RegDet (one row per code × employee)
HR_Holiday │                               └── totals
PR_Loan    ┘
                                            │
                                            ├──  PaySlip print  (PR_PaySlip.rpt)
                                            └──  GL posting     (Vglbatch)
```

###### Key tables

| Table | Use |
|---|---|
| `PR_PayCode` | Earning / deduction codes (BAS, HOU, GOSI, LOAN, …). |
| `PR_PayRun` | Header — period, generated by, message. |
| `PR_Register` | One per pay run × department (when run by department). |
| `PR_RegDet` | Line items — one per employee × pay code. |
| `PR_Loan` | Staff loans; repayment lines are inserted into `PR_RegDet`. |
| `PR_PCPeriod` / `PR_PCType` | Pay-code period & type look-ups. |

\newpage

###### Pay Codes

A **Pay Code** is one line on the pay slip. Maintain them under
**Payroll  Pay Codes** (`PR_PayCode.FT`).

###### Fields

| Field | DB column | Meaning |
|---|---|---|
| Code | `Code` | Short alpha code (BAS, HOU, TRA, MOB, OT, GOSI, LOAN, …). |
| Internal Code | `iCode` | Used for system codes — never shown on slips. |
| Name | `Name` | Printed on the pay slip. |
| Type | `Type` (`PR_PCType`) | Earning / Deduction / Reimbursement / Informational. |
| Period | `Period` (`PR_PCPeriod`) | Monthly / Quarterly / Annual / One-shot. |
| Based On | `BasedOn` | Fixed / % of Basic / Formula. |
| Factor | `Factor` | % or multiplier when *Based On* needs it. |
| Account | `Account` | GL account this code posts to. |
| Class | `Class` | A / B / C grouping for summary reports. |
| TransRequired | `TransRequired` | If true, the code only appears when a corresponding HR transaction exists (e.g. *Overtime* only if `hr_employee_overtime` rows exist for the period). |
| Benefit Code | `PRP_BenefitCode` | Treated as a non-cash benefit for tax computations. |

###### Tips

* Do **not delete** a code that has any `PR_RegDet` lines — older pay
  slips will lose their description. Inactivate by setting the *Status*
  flag instead.
* The order codes appear on the slip is driven by `PR_PayCode.Class +
  ID` — choose codes carefully to keep slips readable.

\newpage

###### Pay Runs

A **Pay Run** is one monthly batch. Open **Payroll  Pay Run**
(`PR_PayRun.FT`).

###### Fields

| Field | DB column |
|---|---|
| Period Start | `PeriodStart` (first day of the month) |
| Period | `Period` (e.g. `2026-06`) |
| GL Batch | `Vglbatch` (filled when posted to GL) |
| Created By | `CreatedBy` |
| Created On | `CreatedON` |
| Message | `MSG` (free-text log) |

###### Workflow

1. Open Pay Run, click **New**.
2. Set Period Start, choose Branch and (optionally) Department, EOS
   status, vacation status, contract-start window, package filters.
   These map to `PR_Register.PRR_*` columns.
3. Click **Generate** — `HR_MonthlySalaries` runs:
   * Selects every active employee matching the filters.
   * Inserts one `PR_Register` per Branch (or per Department, depending
     on settings).
   * Inserts one `PR_RegDet` per employee × pay code.
   * Updates Totals on `PR_Register` (`Total`, `TotalPay`,
     `TotalDeduction`).
4. Review the **Registers** tab — drill into any line to see the
   computation.
5. Click **Post to GL** — `Vglbatch` is filled and the batch becomes
   read-only.
6. Print pay slips (`PR_PaySlip.rpt`) — one PDF per employee or
   batched.

###### Re-running

If you need to regenerate, **delete the un-posted register** first
(or use the *Reverse* command on a posted register, which inserts a
contra batch in GL). A new generation always creates a fresh
`PR_Register` — never overwrites.

\newpage

###### Registers & Pay Slips

###### `PR_Register`

The register is the **header** of a pay batch.

| Column | Meaning |
|---|---|
| `Description` | Free-text title (e.g. *June 2026 – Riyadh*). |
| `Period`, `PeriodStart` | Pay period. |
| `Date` | Generation date. |
| `Total`, `TotalPay`, `TotalDeduction` | Sums. |
| `Vglbatch` | GL batch ID once posted. |
| `GenSource` | `M` = monthly, `S` = settlement, `A` = adjustment, `T` = termination. |
| `PRR_Branch`, `PRR_Department` | Filters used during generation. |
| `PRR_Exlbranch`, `PRR_EXLPackage` | Exclusion filters. |
| `PRR_EOS_STATUS`, `PRR_VAC_STATUS` | Include / exclude employees on EOS / on vacation. |
| `MSG` | Generation log. |

###### `PR_RegDet`

One row per employee × pay code. Columns include `Employee`, `PayCode`,
`Amount`, `Note` (e.g. *Proration: 18/30 days*).

###### Pay slip report

`PR_PaySlip.rpt` (with template `PR_PaySlip.ini`) — the printable
slip. Layout sections:

* Header — employee name, number, department, period.
* Earnings block — every `Type = Earning` pay code.
* Deductions block — every `Type = Deduction` pay code.
* Net pay — `TotalPay − TotalDeduction`.
* Footer — payment method (bank), bank IBAN, sign-off lines.

The slip uses the employee's `HR_EMP_NAME_A` (Arabic) when the *Print
in Arabic* parameter is set.

###### Register transactions report

`PR_Register_Trans.rpt` — flat list of every `PR_RegDet` row for the
register, sortable by department / pay code. Useful for audit and GL
reconciliation.

\newpage

###### Loans

Staff loans are managed in `PR_Loan` and repaid automatically through
payroll.

###### Fields

| Field | Meaning |
|---|---|
| Employee | FK to `HR_Employee`. |
| Loan Type | `PR_LoanType` (Personal / Emergency / Housing / Car / Education). |
| Status | `PR_LoanStatus` (Requested / Approved / Active / Paid / Cancelled). |
| Amount | Principal. |
| Instalments | Number of monthly repayments. |
| Start Period | First payroll period to deduct. |
| Repayment / month | Computed, can be overridden. |
| Outstanding | Recomputed after each payroll run. |

###### Workflow

1. HR creates a loan row, status *Requested*.
2. Finance / Director approves  status *Active*.
3. Each Pay Run reads active loans (`PR_Loan_Load`), computes the
   instalment, inserts a *LOAN* `PR_RegDet` line, and inserts a row
   into `PR_PKT_Loan` history.
4. When *Outstanding = 0* the loan is auto-marked *Paid*.
5. The dashboard `PR_Loan_Alert` flags loans whose deduction failed
   because the employee's net pay would go below zero.

###### Banner

`PR_Loan_BANNER` shows: employee, principal, outstanding, % paid,
months remaining.

\newpage

#### HR Reports

All reports are stored under `<HMS>/Report template/` as `.ini`
parameter files and `.rpt` Crystal layouts. They are launched from the
**Reports** ribbon button on each HR form.

##### Staff lists

| Report | File | Purpose |
|---|---|---|
| All Employees | `HR_Employees.rpt` | Full active roster. |
| Employees (alt layout) | `HR_Employees2.rpt` | Compact one-line-per-employee. |
| Employees by Nationality | `hr_EmployeeByNationality.rpt` | Headcount grouped by passport country. |
| Employees by Religion | `hr_employeebyreligion.rpt` | |
| Employees by Sponsor | `hr_EmployeeBySponsor.rpt` | For multi-sponsor groups. |
| Employees by Agency | `HR_Employees_Agency.rpt` | Group by recruitment agency. |
| Insured staff | `HR_Insurance.rpt`, `hr_Insured.rpt` | GOSI / private insurance roster. |
| Saudisation | `hr_saoudization.rpt` | Saudi vs non-Saudi ratios per position category. |
| Staffing Schedule | `HR_StaffingSchedule.rpt` | Required vs filled per dept. |
| New Employees | `HR_NewEmployees.rpt` | Joiners in a date range. |
| End-of-Service | `hr_endservice.rpt` | EOS register, with computed amounts. |
| Termination | `HR_Termination.ini` | Leavers in a period. |
| Turnover | `HR_Turnover.ini` | Hires vs leavers ratio. |

##### Vacations

| Report | File |
|---|---|
| Due Vacations | `hr_DueVacations.rpt` |
| Vacation Statistics 1-8 | `HR_VacSTAT.rpt`, `HR_VacSTAT2-4.rpt`, `hr_vacstat7.ini`, `hr_vacstat8.ini` |

##### Salary

| Report | File |
|---|---|
| Current Salaries | `hr_CurrentSalaries.ini` |
| Salary Change Log | `HR_SalaryChange.rpt` |
| Salaries (long) | `HR_Salaries.rpt`, `HR_SalaryEXT.rpt` |
| Pay Slip | `PR_PaySlip.rpt` |
| Register Transactions | `PR_Register_Trans.rpt` |

##### Tickets & Documents

| Report | File |
|---|---|
| Employee Tickets | `hr_EmployeeTickets.rpt` |
| Expiring Documents | `hr_ExpiringDocs.rpt` |
| Sponsoring Employee | `RP_SponsoringEmployee.rpt` |
| Saudi Council Certificate | `HR_SaudiCC.ini` |
| Certificate (3 formats) | `HR_Emp_Certificate.rpt`, `_F2.rpt`, `_F3.rpt` |

##### Recruitment & Appraisals

| Report | File |
|---|---|
| Vacancies | `HR_Vacancies.ini` |
| Recruitment Pipeline | `HR_Recruitment.rpt` |
| Appraisals | `HR_Appraisals.ini` |
| Recontracting | `HR_Recontracting.ini` |

\newpage

###### Administration

The Administration sub-section is for the **HR Administrator** —
the person who configures look-ups, security, alerts and dashboards.

* [Lookup Tables](lookups.md) — the 30+ reference tables that drive HR
  pickers.
* [Security & Approvals](security.md) — who can do what.
* [Alerts & Banners](alerts.md) — dashboard alert configuration.

###### The HR Overview dashboard (`HR_Overview.ST`)

The **HR  Overview** search pad is the manager's home page:

* Driving SP: `SPD_SP_HR_Overview`.
* Default filter: **All branches** — switchable to Abha, Dammam,
  Riyadh, Qassem, Jeddah.
* QuickFilter field: *Position* — type in the position name to narrow
  the list.
* Default toolbar buttons: **Edit** the selected employee, **New**
  employee.
* Alert highlighting: any row whose status contains *Expired* is
  shown red/bold (residence, passport, contract, SCC).

\newpage

###### Lookup Tables

All HR look-ups are maintained under **Data Setup  HR**. They are
ordinary tables that the picker dropdowns read from at form-open time
(no service restart needed).

###### Master look-ups

| Table | Used by |
|---|---|
| `HR_Branch` | Employee, Vacancy, Pay Run filter |
| `HR_Department` | Employee, Vacancy, Pay Run filter |
| `HR_POSITION` | Employee, Vacancy, Candidate |
| `HR_POSCATEG` | Position category (Saudisation report) |
| `HR_Package` | Contract |
| `HR_ALWTYPE` | Package allowance type |
| `HR_PRDALWType` | Periodic allowance type |
| `HR_IncentiveType` | Incentive type |
| `HR_VacationType` | Vacation request |
| `HR_VACClass` | Vacancy classification |
| `HR_RecSource` | Recruitment source |
| `HR_RepFormat` | Report format selector |
| `HR_ValueType` | Value-type look-up for action fields |
| `HR_Holiday` | Public holidays (vacation day-count) |
| `HR_Category` | Free employee grouping (Clinical / Admin / Support) |
| `HR_EntryPort` | Port of entry (immigration) |
| `HR_Destination` | Country of travel (TravelAuth) |
| `HR_VisaType` | Visa types |
| `HR_TermReason` | Termination reason taxonomy |
| `HR_RecontractingStatus` | Re-contract decision |
| `HR_EOS` | EOS type |
| `HR_LU_Vacations` | Vacation reason library |
| `HR_LU_Deductions` | Deduction library |
| `HR_Agency` | Recruitment agencies |

###### Status look-ups (small code tables)

| Table | Code values |
|---|---|
| `HR_Status` | Employee status (A/L/S/T) |
| `HR_Contract_Status` | A / E / T / R / X |
| `HR_Vacancy_Status` | O / F / H / C |
| `HR_CandidateStatus` | N / S / I / O / R / H |
| `HR_APRStatus` | Draft / Submitted / Approved / Cancelled |
| `HR_APROverall` | A / B / C / D / E ratings |
| `HR_APRFactor` | Per-factor rating with weight |
| `HR_VAUTHStatus`, `HR_VISAStatus` | Document workflow |
| `HR_VACActionStatus`, `HR_VACActionStage`, `HR_VACActionType` | Vacation action workflow |
| `HR_VacReqStatus` | Vacation request flow |
| `PYR_Stage`, `PYR_Status` | Payroll cycle status |

###### Tip

Most look-ups have a `Name_A` Arabic column — fill it in if you print
slips or contracts in Arabic, otherwise the English value is used as a
fall-back.

\newpage

###### Security & Approvals

HR security is enforced at two layers.

###### 1. HMS user roles

The standard HMS user / group / role system gates access to **forms**
and **menu entries** — typically the four HR roles shipped by default:

| Role | Sees | Can edit |
|---|---|---|
| HR Administrator | Everything | Everything |
| HR Officer | Everything except *Salary* tab on employees outside own branch | Employees, candidates, vacancies, leaves |
| Department Manager | Only own department's employees | Approves first-level actions |
| Employee Self-Service | Own profile, own leave history | Submit leave & travel requests |

Form-level access is bound at install time by mapping each `.FT` and
`.ST` to a *security code* in the HMS admin tools.

###### 2. Personnel-Action approval workflow

Even with full edit rights, a personnel action is **not applied**
until the three approval levels stamp it:

```
HR Officer creates 
        Department Head approves       (APRV_DepHead + Date)
        Project Director approves      (APRV_ProjDir + Date)
        Hospital Director approves     (APRV_HospDir + Date)
                  
        HR_Action_Apply runs the actual mutation
```

* Approvers are configured per-branch in `HR_ActionApproval` /
  `HR_EmpApproval`.
* The dashboard alert `HR_Action_Alert` lists every action pending
  *your* approval — clicking it opens the action ready to sign.
* Approvals are append-only — they cannot be removed once stamped,
  only superseded by an *Override* on the *Policy Verification* tab
  (admin only, audited).

\newpage

###### Alerts & Banners

Every HR form has a **Banner** (the static green strip at the top)
and one or more **Alerts** (scrolling marquee strips below).

###### Banner procedures

| Form | Banner SP |
|---|---|
| Employee | `HR_EMPLOYEE_BANNER` |
| Contract | `HR_Contract_BANNER` |
| Personnel Action | `HR_Action_BANNER` |
| Appraisal | `HR_Appraisal_BANNER` |
| Candidate | `HR_Candidate_BANNER` |
| Vacation | `HR_VACATION_BANNER` |
| VacAction | `HR_VacAction_BANNER` |
| Visa | `HR_VISA_BANNER` |
| Travel Auth | `HR_VAUTH_BANNER` |
| Periodic Allowance | `HR_PRDALW_BANNER` |
| Agency | `HR_Agency_BANNER` |

A banner SP returns a small result-set the HMS framework renders as a
read-only header (employee photo + name + key facts).

###### Alert procedures

Alerts pop on the dashboard *and* on the employee form when something
needs attention.

| SP | Triggers when |
|---|---|
| `HR_EMP_Alert` | Any document on this employee expires within 30 days. |
| `HR_EMP_Note_Alert` | Free-text employee note flagged as alert. |
| `HR_EMP_Note_Alert_APRS` | Appraisal-related employee note. |
| `HR_Vacation_Alert` | A leave is starting within 7 days. |
| `HR_Vacation_Alert_Residence` | Leave cross-checks residence validity. |
| `HR_Action_Alert` | A personnel action is pending **your** approval. |
| `HR_Action_ContractPending_Alert` | A contract renewal action is pending. |
| `PR_Loan_Alert` | A loan instalment failed because net pay would go negative. |
| `HR_ExpiringDocs` | Drives the *Expiring Documents* drill-down list. |

###### How alerts are configured

Each form's `.FT` file has one or more `[Alert]`, `[Alert2]`, …
sections specifying:

* `Show` — on/off.
* `Procedure` — which SP to call.
* `Count` — how many rows to scroll.
* `Every` — seconds between scroll steps.
* `Duration` — seconds each row is visible.
* `Width` — px width of the strip.

\newpage

###### Data Model

Reference list of every HR / Payroll table shipped with HMS. All IDs
are `int`. Every editable table has a matching **`HR_PKT_*` ghost
table** (PKT = Pending Keyed Transaction) which holds the user's
unsaved buffer; on **Save** the framework copies the PKT row into the
live table.

###### Core master tables

| Table | Purpose |
|---|---|
| `HR_Employee` | Master employee record. |
| `HR_PKT_Employee` | Edit buffer. |
| `HR_Employee_child` | Dependants (spouse + children). |
| `HR_EMPLOYEE_Experience` | Prior employment history. |
| `hr_employee_qualification` | Diplomas and certificates. |
| `hr_employee_vacation` | Vacation ledger. |
| `hr_employee_ticket` | Ticket entitlement & usage. |
| `hr_employee_overtime` | Overtime hours by date. |
| `hr_employee_allawence` | Personal allowances. |
| `HR_Salary` | Salary timeline (one row per change). |
| `HR_PKALW` | Package allowance breakdown. |
| `HR_PRDALW` | Periodic monthly allowances. |
| `HR_Incentive` | Performance / spot bonuses. |

###### Organisation

| Table | Purpose |
|---|---|
| `HR_Branch` | Branches / sites. |
| `HR_Department` | Departments (cost-centres). |
| `HR_POSITION` | Job titles. |
| `HR_POSCATEG` | Position category. |
| `HR_Category` | Generic employee grouping. |
| `HR_Package` | Salary package template. |
| `HR_PosHist` | Position history (audit). |

###### Recruitment

| Table | Purpose |
|---|---|
| `HR_Vacancy` | Open positions. |
| `HR_Candidate` | Applicants. |
| `HR_Agency` | Recruitment agencies. |

###### Contracts & actions

| Table | Purpose |
|---|---|
| `HR_contract` | Contracts. |
| `HR_Action` | Personnel actions. |
| `HR_ActionType` | Action-type look-up. |
| `HR_ActionApproval` | Per-branch approver matrix. |
| `HR_Appraisal` | Performance appraisals. |
| `HR_EmpApproval` | Employee-side approver matrix. |
| `HR_EOS` | End-of-service type lookup. |
| `HR_TermReason` | Termination reason taxonomy. |
| `HR_VACAction`, `HR_VACActionStage/Status/Type` | Vacation action workflow. |

###### Documents

| Table | Purpose |
|---|---|
| `HR_VISA`, `HR_VisaType`, `HR_VISAStatus` | Visa applications. |
| `HR_VAUTH`, `HR_VAUTHStatus` | Travel authorisations. |
| `HR_Certificate` | Generic certificate catalogue. |
| `HR_ELeave` | Educational-leave linked to vacation. |
| `HR_LU_Vacations`, `HR_LU_Deductions` | Reason libraries. |

###### Payroll (PR)

| Table | Purpose |
|---|---|
| `PR_PayCode` | Pay codes (earnings & deductions). |
| `PR_PayRun` | Pay-run header. |
| `PR_Register` | One per pay-run × branch. |
| `PR_RegDet` | Pay-slip line items. |
| `PR_Loan` | Staff loans. |
| `PR_LoanType`, `PR_LoanStatus` | Loan lookups. |
| `PR_PCPeriod`, `PR_PCType` | Pay-code lookups. |
| `PR_PKT_*` | Edit-buffer ghosts. |
| `PYR_Stage`, `PYR_Status` | Payroll cycle status. |

###### Lookups (status & rating)

`HR_Status`, `HR_Contract_Status`, `HR_Vacancy_Status`,
`HR_CandidateStatus`, `HR_APRStatus`, `HR_APROverall`, `HR_APRFactor`,
`HR_RecontractingStatus`, `HR_VacReqStatus`, `HR_ALWTYPE`,
`HR_PRDALWType`, `HR_IncentiveType`, `HR_VacationType`, `HR_RecSource`,
`HR_RepFormat`, `HR_ValueType`, `HR_Holiday`, `HR_Branch`,
`HR_Destination`, `HR_EntryPort`, `HR_Deductions`, `HR_VACClass`.

\newpage

###### Templates (FT / ST / GT)

The HMS UI is metadata-driven. Each window is one of three template
files under `<HMS>/Forms` (legacy) or `<HMS>/FTP`, `<HMS>/STP`,
`<HMS>/GTP` (current).

| Suffix | Kind | Example |
|---|---|---|
| `.FT` | Form — single record edit window | `HR_Employee.FT` |
| `.ST` | Search pad / list window | `HR_Employee_Fast.ST` |
| `.GT` | Grid — child table embedded in a form | `HR_Salary.GT` |
| `.BND` | Binder — full-screen workspace | (no dedicated HR binder; opened via main menu) |

###### HR forms (`FTP/`)

| File | Purpose |
|---|---|
| `HR_Employee.FT` | Employee master form (16 tabs). |
| `HR_Contract.ft` | Contract edit. |
| `HR_Action.FT` | Personnel action. |
| `HR_Appraisal.FT` | Appraisal. |
| `HR_Candidate.FT` | Candidate. |
| `HR_Vacation.FT` | Vacation request. |
| `HR_VacAction.FT` | Vacation action / consumption. |
| `HR_VACANCY.FT` | Vacancy. |
| `HR_Department.FT` | Department. |
| `HR_POSITION.FT` | Position. |
| `HR_PACKAGE.FT` | Salary package. |
| `HR_PRDALW.FT` | Periodic allowance. |
| `HR_VAUTH.FT` | Travel authorisation. |
| `HR_VISA.FT` | Visa. |
| `HR_Extension.FT` | Leave extension. |
| `HR_Agency.FT` | Recruitment agency. |
| `HR_Certificate.FT` | Certificate. |
| `MF_SickLeave.FT`, `MF_SickLeave2.FT` | Sick-leave certificates. |
| `PR_PayRun.FT` | Payroll run. |
| `PR_PayCode.FT` | Pay code. |

###### HR list windows (`STP/`)

| File | Purpose |
|---|---|
| `HR_Overview.ST` | Manager dashboard (branch-filtered, QuickFilter on Position). |
| `HR_Employee.ST` | Standard employee search. |
| `HR_Employee_Fast.ST` | Fast picker (used everywhere a *select employee* dropdown is shown). |
| `HR_Employee_LB.ST` | Lebanon-specific layout. |
| `HR_DataEntry.ST` | Mass-edit grid. |
| `HR_Department.ST`, `HR_Position.ST`, `HR_Package.ST`, `HR_Candidate.ST` | List per master table. |
| `HR_Contract.ST`, `HR_Contract_30d.ST`, `HR_Contract_6m.ST` | Contract list + expiry-window drill-downs. |
| `HR_ContractReview.ST` | Contracts to review. |
| `HR_Action.ST`, `HR_Action_DRL.ST`, `HR_Action_STS.ST` | Actions list & drill-downs. |
| `HR_Salary_DRL.ST` | Salary drill-down (from Employee). |
| `HR_Appraisal.ST` | Appraisals list. |
| `HR_Agency.ST`, `HR_Certificate.ST` | Lookups. |
| `HR_Extension.ST`, `HR_Incentive.ST`, `HR_Passport.ST`, `HR_Residence.ST` | Per-document lists. |
| `HR_SalaryReview.ST` | Salary review batch. |
| `HR_SCC.ST` | S.C.C. status list. |
| `HR_VAUTH.ST`, `HR_VISA.ST` | Document lists. |
| `HR_VACATION_Family.ST` | Vacations with family-ticket info. |
| `HR_Package.ST`, `HR_PRDALW.ST` | Package & periodic-allowance lookups. |
| `Employer_DRL.ST` | Sponsor drill-down. |

###### HR child grids (`GTP/`)

| File | Embedded in | Purpose |
|---|---|---|
| `HR_PKALW.GT` | Package & Contract | Package allowance breakdown. |
| `HR_Alw.GT` | Employee Allowances tab | Personal allowances. |
| `HR_Salary.GT` | Employee Salary tab | Salary history (read-only). |
| `HR_PosHist.GT` | Contract & Employee | Position history. |
| `HR_Contract.GT` | Employee Contracts tab | Contract list. |
| `HR_APRContract.GT` | Appraisal Re-Contracting tab | New contract preview. |
| `HR_EXTContract.GT` | Action Extension | Extension preview. |
| `HR_vacation.GT` | Employee Leaves tab | Vacation history. |
| `HR_Eleave.GT` | Vacation Educational-Leave tab | |
| `HR_Quals.GT` | Employee Qualifications tab | Diplomas & licences. |
| `HR_Childs.GT` | Employee Dependants tab | |
| `HR_Experience.GT` | Employee Experience tab | |
| `HR_Ticket.GT` | Employee Tickets tab | |
| `HR_Overtime.GT` | Employee Overtime tab | |
| `HR_Incentive.GT` | Employee Incentives tab | |
| `HR_Contract.GT` | Employee Contracts tab | |

\newpage

###### Stored Procedures

The HR module ships ~70 stored procedures. They fall into seven
families.

###### 1. Banners (read-only header strips)

`HR_EMPLOYEE_BANNER`, `HR_Contract_BANNER`, `HR_Action_BANNER`,
`HR_Appraisal_BANNER`, `HR_Candidate_BANNER`, `HR_VACATION_BANNER`,
`HR_VacAction_BANNER`, `HR_VISA_BANNER`, `HR_VAUTH_BANNER`,
`HR_PRDALW_BANNER`, `HR_Agency_BANNER`, `PR_Loan_BANNER`.

###### 2. Alerts (dashboard / form notifications)

`HR_EMP_Alert`, `HR_EMP_Note_Alert`, `HR_EMP_Note_Alert_APRS`,
`HR_Vacation_Alert`, `HR_Vacation_Alert_Residence`, `HR_Action_Alert`,
`HR_Action_ContractPending_Alert`, `HR_ExpiringDocs`, `PR_Loan_Alert`.

###### 3. Lookup-population helpers (used by the *Data Setup* installer)

`HR_Branch_Add`, `HR_EntryPort_Add`, `HR_Position_Add`,
`HR_POSCATEG_Add`, `HR_ValueType_Add`, `HR_PKALW_Add`,
`HR_PKALW_ORG_Add`, `hr_Certificate_ADD`, `HR_ACTION_Salary_Add`,
`HR_APRS_Salary_Add`, `HR_PosHist_Initialize`, `HR_PosHist_ADD`,
`HR_EMP_NewNumber`, `HR_PACKAGE_UPDATE`, `HR_CCI_UPDATE`.

###### 4. Calculations

`HR_SP_VAC_CALC`, `HR_VacReq_CALC`, `HR_VacReq_REQUEST_CALC`,
`HR_SP_EOS_CALC`, `HR_EOS_DIF_CALC`, `HR_EOS_DIF_CALC_ALL`,
`HR_ACTION_ACCRUED_LEAVE_CALC`, `HR_ACTION_TOTAL_LEAVE_CALC`,
`HR_APRS_Salary_FIX`.

###### 5. Workflow appliers (the SP that actually mutates state)

| SP | Used by |
|---|---|
| `HR_Action_Apply` | Generic personnel-action apply (dispatches to one of the below). |
| `HR_Action_PROMOD_Apply` | Promotion / Demotion. |
| `HR_Action_RETRA_Apply` | Re-transfer (returning an employee to the original branch). |
| `HR_Action_TRANS_Apply` | Transfer. |
| `HR_Action_HIST_Apply_All` | Bulk re-apply of historical actions (migration tool). |
| `HR_Action_Submit_Type` | Submit a draft action with a specific type. |
| `HR_Action_AutoApply` | Nightly sweep that applies fully-approved actions. |
| `HR_Appraisal_Apply` | Appraisal apply (raise + recontract). |
| `HR_Appraisal_AutoApply` | Nightly sweep for fully-approved appraisals. |
| `HR_Contract_Renew` | Issue a new contract from the current one. |
| `HR_Contract_Extend` | Extend the current contract's end-date. |
| `HR_APRContract` | Renew triggered from an appraisal. |
| `HR_EXTContract` | Background extension processor. |
| `HR_VacAction_Submit` | Submit a vacation action. |
| `HR_VacAction_Apply` | Apply a vacation action (consume tickets). |
| `HR_VacAction_AutoApply` | Nightly sweep. |

###### 6. Reports / batch

`HR_Employee_RPT`, `HR_Vacation_RPT`, `HR_Account_Employees`,
`HR_MonthlySalaries`, `HR_DueVacations`, `HR_ReContractingLetter`,
`HR_EmpAcct_Gen`, `HR_EMPACCT_NEW`, `HR_Vacation_TravelALW_Validate`.

###### 7. Plumbing (framework hooks)

* `HR_SP_FT_Process` — generic process hook called by every HR form.
* `HR_SP_Employee_Vacancy_PostProcess` — post-save hook for the
  Employee form, keeps `HR_Vacancy` in sync.
* `hr_Vacancy_Create_Transient`, `hr_Vacancy_Transient_Process`,
  `hr_Vacancy_Transient_Process_All` — transient vacancy lifecycle.
* `HR_Vacancy_Load` — picker SP for all *Vacancy* dropdowns.
* `HR_Employee_Clear_Vacancy` — release an employee's vacancy without
  a personnel action (admin tool).
* `PR_Loan_Load` — picker SP for loan dropdowns.
* `PR_Loan_Payments` — generates the next instalment line in a pay run.

\newpage

###### Glossary

| Term | Definition |
|---|---|
| **Accrued leave** | Leave days the employee has earned but not yet used. Computed by `HR_ACTION_ACCRUED_LEAVE_CALC`. |
| **Action** | A formal change to an employee's job (transfer, promotion, termination, …) that goes through three-level approval — see [Personnel Actions](../actions/index.md). |
| **Appraisal** | End-of-term performance review — see [Appraisals](../actions/appraisals.md). |
| **Banner** | Static green strip at the top of an HMS form; rendered by a `*_BANNER` SP. |
| **Binder (BND)** | Full-screen workspace template (toolbar + side menu). HR has no dedicated binder — it is opened from the main menu. |
| **Candidate** | An applicant — see [Candidates](../recruitment/candidates.md). |
| **Contract** | Time-bound employment contract — see [Contracts](../employees/contracts.md). |
| **EOS** | End of Service award (gratuity) paid on leaving, per Saudi labour law — see [End of Service](../employees/eos.md). |
| **Form (FT)** | Single-record edit window — e.g. `HR_Employee.FT`. |
| **Ghost / PKT** | The edit-buffer table (`HR_PKT_*`). User changes live here until **Save**. |
| **Grid (GT)** | Child-table view embedded in a form — e.g. `HR_Salary.GT`. |
| **HR Officer** | Day-to-day HR user — creates employees, leaves, candidates. |
| **HR Administrator** | Configures look-ups, packages, periodic allowances, security. |
| **Package** | Salary template — see [Packages](../organization/packages.md). |
| **Pay Code** | One line on the pay slip — see [Pay Codes](../payroll/pay-codes.md). |
| **Pay Run** | One monthly payroll batch — see [Pay Runs](../payroll/pay-runs.md). |
| **Periodic Allowance** | Recurring monthly amount paid outside the package — see [Periodic Allowances](../organization/periodic-allowances.md). |
| **PKT table** | See *Ghost*. |
| **Register** | Result of one pay run — see [Registers](../payroll/registers.md). |
| **S.C.C.** | Saudi Council Certificate — licensure for clinical staff — see [Certificates](../documents/certificates.md). |
| **Search pad (ST)** | List / search window — e.g. `HR_Employee_Fast.ST`. |
| **Sponsor** | Legal employer on the residence permit. Tracked in `HR_Employee.Current_sponsor_name`. |
| **Transient vacancy** | Auto-created temporary vacancy that keeps headcount balanced during a transfer — see [Vacancies](../recruitment/vacancies.md). |
| **VacAction** | Vacation action — a step in the vacation workflow (request, approve, take, return). |
| **Vacancy** | Approved opening to be filled — see [Vacancies](../recruitment/vacancies.md). |
| **Vglbatch** | GL batch number written on `PR_Register.Vglbatch` once a payroll is posted to general ledger. |

