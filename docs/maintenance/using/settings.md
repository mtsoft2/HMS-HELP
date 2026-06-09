# Settings

Click **Settings** in the toolbar to open the Maintenance Settings
dialog. Three short fields that affect every other screen.

## Backup Folder (single source of truth)

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

## Audit retention (days)

The maximum age (in days) of audit rows before the *Audit / log
overage* check on the **Checklist** considers them excess.

* Affects two tables: **SEC_Log** and **SEC_PasswordLog**.
* The matching safe fix purges rows older than this limit.

## Log retention (days)

Same concept for application-log rows.

* Affects two tables: **DBHealth_History** and **Backup_Run**.

## Save / Close

* **Save** persists the settings to the central configuration file and
  refreshes every dependent KPI tile.
* **Close** abandons changes.

## Where these settings live

The settings are stored centrally — change them once and every
schedule, every backup, every KPI tile and every checklist row picks
up the new values without a restart.

➡ Continue to **[Backup Log](backup-log.md)**.
