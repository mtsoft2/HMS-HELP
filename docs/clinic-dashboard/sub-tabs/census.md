# Census

Inpatient occupancy and discharge planning — the bed-side of the
clinic.

## Cards

### Occupancy

A radial / percentage card showing the % of beds full right now, with:

* The exact **Occupied** and **Free** bed counts.
* **Admits today** counter.
* **Discharges today** counter.
* **Free beds** total across all wards.

### Wards

A per-ward breakdown:

| Column | Meaning |
|---|---|
| **Ward** | Ward name. |
| **Occupied** | Beds currently in use. |
| **Free** | Beds available for admission. |
| **Available** | Free beds that are *also* clean and ready. |

Use this when reception calls asking *"do we have a bed in
paediatrics?"* — the answer is in this card.

### Bed map

A visual grid of every bed across every ward:

* **Cell colour** = bed status (occupied / free / cleaning / blocked).
* **Click a bed** = opens the admission record (if occupied) or a
  blank admission form (if free).
* The map respects ward groupings so adjacent beds in the same room
  stay adjacent in the map.

### Discharge queue · next 48h

A list of patients planned to leave in the next two days:

| Column | Meaning |
|---|---|
| **Patient** | Name. |
| **Ward** | Where they are now. |
| **LOS** | Length of stay so far. |
| **Discharge by** | Planned discharge date / time. |
| **Complaint / Note** | Reason for admission + any planning note. |

Each row has an **Open admission #<id>** link → opens the full
admission record. Use this list to drive the daily discharge huddle.

## What you do with it

* **Bed-managers** — the bed map answers "do we have a bed" in two
  seconds.
* **Discharge planners** — the queue is their work list for the next
  two days.
* **Clinical leads** — Occupancy + Admits/Discharges tell you whether
  the in/out flow is balanced.

➡ Continue to **[Billing](billing.md)**.
