# Features

Every Clinic Dashboard feature, grouped by what it lets you do.
Exhaustive but plain-English — no system internals.

---

## 1. Layout & Navigation

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
* **Card hide / show** — right-click any card → *Hide this card*; bring
  hidden cards back from the controls menu.
* **Click anything to drill down** — KPI tiles, list rows, chart
  segments all open the underlying records.

## 2. Overview sub-tab

Six headline KPI tiles plus a 30-day revenue sparkline.

### KPI tiles

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

### Revenue trend card

* **30-day daily revenue sparkline** with axis labels (date and value).
* **Hover any data point** for the exact daily total.
* Auto-handles **empty period** — friendly *"no billing activity in
  the last 30 days"* message.

## 3. Schedule sub-tab

Today's appointment grid in dashboard form.

* **Today's schedule heat-strip** — each cell coloured by status
  (Booked / Confirmed / Arrived / Attended / Cancelled / No-show /
  Free) with the patient initial.
* **Hover tooltip** — patient + physician + time + status.
* **Click a cell** → opens that appointment.
* **Status counters** — Booked, Confirmed, Arrived, Attended,
  Cancelled, No-show, Free.
* **Date navigator** — Previous day, Today (jump back), Next day.
* **Physicians on duty** side panel — who is working today.
* **Show less / Show more** for the physician list when it overflows.

## 4. Census sub-tab

Inpatient occupancy and discharge planning.

### Cards

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
* **Click "Open admission"** on any row → opens the full admission
  record.

## 5. Billing sub-tab

Cash flow, A/R, claims, and top items.

### Cards

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

## 6. Physicians sub-tab

Per-physician productivity, today and month-to-date.

### Per-physician card

* **Physician name** + click-through to their full record.
* **Today's counters**: Booked, Pending, Arrived, Done, Cxl, No-show.
* **Utilization** % — what share of the physician's bookable hours
  are filled today.
* **Patients MTD** — count of distinct patients seen this month.
* **Revenue MTD** — money invoiced under this physician this month.

### Other features

* **Sort by** — utilization, revenue MTD, or patients MTD.
* **Show less / Show more** when the physician list is long.
* **Date navigator** — Previous day, Today, Next day.
* **Empty-state** — *"No appointments today"* on physician cards with
  a fully open calendar.

## 7. Inventory sub-tab

Stock visibility for the clinic.

### Cards

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

## 8. Quality sub-tab

Outcomes, incidents, and patient satisfaction.

### Cards

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

## 9. CRM sub-tab

Acquisition and growth.

### Cards

* **Opportunity funnel** — funnel chart from Lead → Contact → Quote →
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

## 10. Common card features (every sub-tab)

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

## 11. Customisation

* **Card show / hide** per user, per sub-tab.
* **Sub-tab order** — fixed; cannot be re-ordered.
* **Auto-refresh interval** — configurable per clinic.
* **Currency** — drives the unit chip on monetary KPIs; falls back to
  SAR.
* **Sub-tab visibility** — administrators can hide entire sub-tabs
  for users whose role does not need them (e.g. hide CRM from
  clinical staff).

## 12. Permissions

* **View access** — controlled per sub-tab on the user role
  (Overview / Schedule / Census / Billing / Physicians / Inventory /
  Quality / CRM).
* **Drill access** — a user can see a KPI without necessarily
  having permission to open the underlying record; in that case the
  click is suppressed.
* **Hide-card preferences** are per-user and do not affect anyone
  else.

## 13. Performance & freshness

* KPIs and lists come from **live aggregates** — no batch wait.
* **Auto-refresh** keeps the dashboard current without reloading the
  page.
* **Heavy charts** (sparklines, funnels) re-render only on data change
  to keep the page responsive.
* **Live data fall-back** — if a feed isn't provisioned yet, the
  dashboard renders sensible placeholder values instead of breaking,
  with a small note.

## 14. Quality-of-life

* **Single-page** — no nested screens; everything fits in one
  scroll.
* **Tooltips everywhere** — hover any chart point, KPI value, or
  delta chip to see the formal definition.
* **Show less / Show more** on long lists.
* **Language follows login** — every label and tooltip is translated
  to your interface language.
* **Wall-display friendly** — the dashboard runs full-screen on a
  TV without UI clipping.

➡ Continue to **[Overview sub-tab](sub-tabs/overview.md)** or jump to
any other sub-tab in the left nav.
