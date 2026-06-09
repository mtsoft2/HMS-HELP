# Backup Schedules

Click **Backup Schedule** in the toolbar to open the schedules list.
A schedule fires a backup on a recurring cadence without anyone having
to click *Backup Now*.

## The list

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

## The editor

![New Schedule dialog](../screenshots/04-new-schedule.png)
/// caption
The **New Schedule** dialog. Five sections — Identity, What to back
up, When to run, frequency-specific fields, and the *Active* toggle.
///

### Identity

* **Name** — short label that appears in the list. Required.
* **Description** — free text.

### What to back up

* **Backup Type** — FULL / DIFF / LOG.
* **Backup Folder** — locked to the central folder from Settings.
  Single source of truth; all schedules use the same folder.

### When to run

* **Frequency** — Hourly · Daily · Weekly · Monthly.
* **Start Time** — HH:MM (24-hour clock).
* Frequency-specific extra:
    * **Weekly** → *Days of Week* — tick which weekdays.
    * **Monthly** → *Day of Month (1-31)*.
    * **Hourly** / **Daily** → no extra fields.

### Active (will run on schedule)

* Tick to enable. Untick to pause without deleting.

### Save / Cancel

Save commits the schedule and registers the corresponding SQL Server
Agent job (Daily / Weekly / Monthly) or in-app tick (Hourly). Cancel
abandons changes.

## Patterns

| Goal | Suggested schedules |
|---|---|
| Clinical database, low write volume | FULL daily 02:00 + LOG every 30 min during business hours |
| Clinical database, high write volume | FULL daily + DIFF every 6 h + LOG every 15 min |
| Reporting copy, off-hours updates | FULL weekly Sunday 03:00 |
| Pre-upgrade snapshot | Run **Backup Now** with FULL + a descriptive Description; no schedule needed |

## Common pitfalls

* **Active unticked** — schedules don't fire. Check the green dot.
* **Backup folder unwritable** — every run fails with the same error.
  Fix the OS permission on the folder.
* **No FULL backup yet** — DIFF and LOG schedules need a FULL baseline.
  Run **Backup Now** with FULL once before relying on DIFF/LOG
  schedules.
* **Recovery model is SIMPLE** — LOG schedules will be marked N/A.
  Switch the database to FULL recovery if you need log backups.

➡ Continue to **[Send Log](send-log.md)**.
