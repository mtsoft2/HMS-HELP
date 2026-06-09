# KPIs Dashboard

The default tab in Maintenance — every important number about the
database, on a single screen, refreshed live.

![Maintenance KPIs dashboard](../screenshots/01-kpis-dashboard.png)
/// caption
The KPIs tab. Top strip pins the database identity; the toolbar
exposes Backup Now / Backup Schedule / Send Log / Settings; the
sidebar offers Backup Log and the storage reports.
///

## How it is organised

Three colour-coded bands:

### Live activity & performance

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

### Backup

| Tile | What it means |
|---|---|
| **Last backup** | Time since the most recent backup (e.g. *8m ago*). |
| **Next scheduled** | When the next scheduled backup will run, or *no schedules*. |
| **Backup folder size** | Total size of files currently in the backup folder. |
| **Backup files** | Number of backup files in that folder. |
| **Policy (clinical)** | Whether the backup setup meets the clinical-use policy. *Inadequate* shows the reason. |
| **Full schedule** | *Configured* or *Missing*. |
| **Log schedule** | *Configured* / *Missing* / *N/A* (when the database uses SIMPLE recovery, log backups are not applicable). |

### Licensing

| Tile | What it means |
|---|---|
| **Licensed users** | Used vs total seats. |
| **License serial** | The product key currently active. |
| **License expiry** | The renewal date. |
| **Connected now** | Distinct sessions logged in right now. |
| **Active users** | Enabled user accounts. |
| **Total users** | Including disabled. |
| **Last user login** | Most recent successful login. |

## Reading the colours

* **Green** — healthy / within target.
* **Yellow** — degraded but not failing (e.g. backup disk close to
  full).
* **Red** — failing / policy non-compliant.

## Actions on this tab

Top-right:

* **Edit** — open the dashboard template editor (admin only).
* **Refresh** — re-pull the KPI values.
* **Export** — export the current dashboard as a printable report.

## Drill-down

Click any tile to open the underlying detail — most tiles jump to the
matching row in the **Checklist** tab; the licensing tiles jump to the
users / licenses screen.

➡ Continue to **[Health Checklist](health-checklist.md)**.
