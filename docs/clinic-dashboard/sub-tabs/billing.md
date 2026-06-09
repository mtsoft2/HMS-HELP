# Billing

Cash flow at a glance — revenue, A/R, claims, top items.

## Headline counters

* **Revenue today** — same KPI as the Overview tab, repeated here so
  you don't have to leave Billing.
* **MTD average bill** ("Avg ticket") — average bill size month-to-date.
* **A/R outstanding** — total amount currently owed by patients and
  payers.
* **Severely overdue** — A/R aged past the configured threshold —
  this is the at-risk number.

Every monetary value uses the configured clinic currency (defaults to
**SAR** if not set).

## Cards

### Revenue · last 30 days

A daily-totals sparkline with hover tooltips, identical in style to
the Overview tab — drawn here in larger size with extra detail.

### A/R aging

Four buckets — **0–30**, **31–60**, **61–90**, **90+ days** —
shown as horizontal bars with the exact amounts. A **Outstanding
only** toggle hides bills that have already been settled to keep the
chart focused on the at-risk piece.

### Top revenue items · 90d

A leaderboard of the highest-revenue service codes over the past 90
days:

| Column | Meaning |
|---|---|
| **Item** | Service / procedure name. |
| **Volume** | Number of times invoiced. |
| **Revenue** | Total money under this code. |

Each row has an **Open <item>** link → opens the item / service
record.

### Claim status · 60d

A breakdown of insurance claims submitted in the last 60 days:

* **Accepted** — paid in full.
* **Pending** — awaiting payer decision.
* **Rejected** — declined; needs resubmission or write-off.
* **Re-submitted** — second pass currently in review.

Each segment is clickable → opens the claim list pre-filtered to that
status.

## What you do with it

* **Daily cash check** — Revenue today + Avg ticket give you the
  daily cash-velocity in five seconds.
* **Receivables triage** — A/R aging + Severely overdue identify the
  bills that need a phone call this week.
* **Service-mix view** — Top revenue items shows what is *actually*
  paying the clinic's bills, vs what management *thinks* is.
* **Claims chase** — Claim status flags how many claims are stuck in
  Pending and how many got Rejected.

➡ Continue to **[Physicians](physicians.md)**.
