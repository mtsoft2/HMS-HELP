# Event Info Panel

Click any booked cell to open the **Appointment Information** panel on
the right. It is the single place that pulls together everything the
front desk needs to know before the patient walks in.

## What it shows

* **Patient** — name, MRN, photo (if on file).
* **Time** — from / to, duration.
* **Physician**.
* **Room**.
* **Category** with its colour swatch.
* **Reason** (short label).
* **Comment** (longer note from whoever booked it).
* **Status** — Pending, Confirmed, Arrived, In-Service, Completed,
  No-show, Cancelled.

## Flags & alerts

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

## Quick actions

The panel's footer has the same actions as the right-click menu:

* **Edit** — opens the booking dialog.
* **Cancel edit** — discards changes.
* **Delete** — removes the appointment after a confirm.
* **Status** — quick-set Arrived / In-Service / Completed / No-show
  without opening the full editor.

➡ Continue to **[Scheduler Settings](../configuration/index.md)**.
