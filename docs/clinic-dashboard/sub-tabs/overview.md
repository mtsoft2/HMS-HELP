# Overview

The default sub-tab — the manager's "everything in one glance" view.

## What you see

Two cards stacked vertically:

### Headline KPIs

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

### Revenue · last 30 days

A daily-totals sparkline:

* Filled area under a line for visual trend.
* **Dots** on the first day, last day, and every 7th day, with a hover
  tooltip showing date + amount.
* **Y-axis** labels — min and max values.
* **X-axis** labels — start date, mid date, end date.
* **Empty state** — *"No billing activity in the last 30 days."*

## What you do with it

* **First check** of the morning — five seconds tells you whether
  today is on track.
* **Hover the deltas** for the formal comparison period.
* **Click any KPI tile** to drill into the underlying list (the
  appointments, the no-shows, the beds, the claims).
* **Hover any sparkline dot** to read the exact day's revenue.

➡ Continue to **[Schedule](schedule.md)**.
