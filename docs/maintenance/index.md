# Maintenance Module

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
/// caption
The Maintenance dashboard on the **KPIs** tab — live database health
overview, backup status, and licensing in one screen.
///

## How to open it

From the HMS main menu pick **Maintenance**. The module is restricted
to the **Maintenance / Supervisor** role; the *supervisor* badge in
the top-right confirms which role you're using.

## The screen

* **Top strip** — Database, Server, Data File, Log File, Backup
  Folder, Last Scan.
* **Action toolbar** — *Backup Now · Backup Schedule · Send Log ·
  Settings*.
* **Sidebar** — Desktop · Backup (Backup Log) · Storage (Table Sizes,
  Backup Log Report, Table Sizes Report).
* **Main pane** — two tabs: **KPIs** and **Checklist**, with **Edit /
  Refresh / Export** controls on the right.

## Two tabs

| Tab | What it shows |
|---|---|
| **KPIs** | Live database health, live activity, backup state, licensing — all as coloured tiles. |
| **Checklist** | The 48-point scored health checklist with one-click fixes. |

➡ Continue to **[Getting Started](getting-started.md)** or jump to
**[Features](features.md)**.
