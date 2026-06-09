# Find a Patient & Book

The fastest path from "patient calls" to "appointment in the grid" is
two clicks.

## Find

Click **Find** in the toolbar (or press the keyboard shortcut your
admin configured). The patient picker opens with a single search box.

Search by any of:

* **Name** — first, family, or partial match.
* **MRN** — the patient's HMS file number (often the badge number).
* **Phone** — last 4 digits is usually unique enough.

The list narrows as you type. Pick the patient.

### What if the patient isn't there?

* They've never visited the clinic → book the slot as a **walk-in**
  (skip the picker, just click the slot — the booking dialog lets you
  type the patient's name without linking to a file). The receptionist
  attaches a real file later via **Edit appointment**.
* They've visited a different branch — clear any branch filter at the
  top of the picker; the search runs across all branches.

### Patient context shown in the picker

Each row shows: name, MRN, date of birth, mobile, last visit. Special
flags appear as small icons:

| Icon | Meaning |
|---|---|
| Heart | VIP patient — handle gently. |
| Triangle | Pending balance over the configured threshold — flag for the cashier before the visit. |
| Allergen symbol | Has documented allergies — the receptionist should remind the physician. |
| Person-x | High no-show count — consider asking for a deposit. |

## Book

After picking the patient, click the empty cell you want — in the
right physician's column at the right time. The booking dialog opens
pre-filled.

Fill in:

* **From / To** — start and end time. The dialog snaps to the booking
  step set in **Scheduler settings → Hours & Days → Booking step**.
* **Room** — defaults to the physician's room if one is set.
* **Category** — Consultation, Follow-up, Cleaning, Emergency, ….
  Categories drive the appointment colour. List configured in
  **Scheduler settings → Categories**.
* **Reason** — short label that appears on the appointment card.
* **Comment** — longer free text the physician sees in event info.

Save.

## What you see after save

The cell is filled and coloured by category. Hovering shows a
tooltip; clicking shows the full **Appointment Information** panel
with allergy / balance / VIP / no-show flags. Right-click for
Edit / Copy / Cut / Delete.

➡ Continue to **[Move, Copy, Paste](move-and-paste.md)**.
