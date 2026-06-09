# Run Backup

Click **Backup Now** in the toolbar to open the Run Backup dialog.

![Run Backup dialog](../screenshots/03-run-backup.png)
/// caption
The **Run Backup** dialog — pick FULL, DIFF, or LOG, confirm the
backup folder, add a description, and click Run Backup.
///

## Fields

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

## Run

Click **Run Backup**. A progress strip appears: *Running backup,
please wait…*.

When the backup finishes:

* The file is written to the folder.
* The **Last Backup** KPI tile updates immediately.
* A new entry appears in the **Backup Log** sidebar item.
* A toast confirms success.

If the backup fails the dialog shows the SQL error and the *Last
Status* column on the Backup Log marks it **Failed**.

## When to use which type

| Type | When |
|---|---|
| **FULL** | At least once a day for clinical databases. Before a major upgrade. After a successful restore drill. |
| **DIFF** | Several times a day to shorten the restore chain. |
| **LOG** | Every 15-60 minutes when the database is in FULL recovery to limit RPO (data loss window). |

## Tips

* The folder must be writable by the **SQL Server account**, not just
  the user running HMS — if it can't write, the backup fails with a
  permission error.
* Use **Description** to mark special backups (*Pre-upgrade*,
  *End-of-month*, *Migration*) so they stand out in the Backup Log.
* Run **Backup Now** before a risky operation — restoring a DIFF that
  was taken five minutes ago beats restoring last night's FULL.

➡ Continue to **[Backup Schedules](backup-schedules.md)**.
