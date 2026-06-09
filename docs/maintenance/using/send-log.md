# Send Log

Click **Send Log** in the toolbar to generate a shareable maintenance
report and upload it to Google Drive.

## What it generates

A self-contained HTML file with everything an off-site auditor or
head-office DBA needs to review the site's health — all on one
scrollable page.

![Generated maintenance-log report](../screenshots/05-maintenance-log.png)
/// caption
The **Maintenance Log** as rendered on Drive. Sections from top to
bottom: identity strip, KPIs (Database Health Overview), Live activity
& performance, Backup, Licensing, Health by topic, and the full
Database Health Checklist.
///

### Sections

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

## Flow

1. Click **Send Log**. The button shows *Generating and uploading…*.
2. The system writes the HTML file and uploads it to the Google Drive
   folder configured in **Maintenance → Settings**.
3. On success — *Uploaded to Google Drive* — the result panel shows:
    * **Open in Drive** — opens the file in a new browser tab.
    * **Copy link** — copies the share-link to your clipboard.
4. Share that link in the ticket / e-mail thread.

## When it fails

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

## When to use it

* **Routine reporting** — weekly / monthly snapshot for head office.
* **Incident ticket** — send the log link with the ticket so support
  sees the full health picture without dialling in.
* **Pre-upgrade** — generate before a major upgrade for an immutable
  record of the pre-change state.
* **Audit** — attach the link to the audit trail.

➡ Continue to **[Settings](settings.md)**.
