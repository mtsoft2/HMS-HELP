# Bulk Reschedule

When a physician runs late, gets called away, or wants to flip rooms,
moving the day's appointments one by one is painful. **Bulk
reschedule** does it in one operation.

## Open

Click **Bulk** in the toolbar.

## What you choose

| Field | Meaning |
|---|---|
| **From physician** | Whose appointments to move. |
| **On date** | Which day's appointments to consider. |
| **Move to physician** | (Optional) The other physician to take the patients. Leave blank to keep the same physician. |
| **Shift by** | Minutes to shift each appointment forward (positive) or back (negative). E.g. `+30` pushes the whole day half an hour later. |
| **Shift to date** | (Optional) Move the day's appointments to a different date entirely. |

## Run

Click **Save**. The scheduler:

1. Validates each move against breaks, holidays, and existing
   appointments.
2. If any of the moves would conflict, opens the **Conflict** dialog
   listing every clash. You can cancel, overwrite, or skip per row.
3. Applies the rest atomically — either every appointment moves or
   none of them do.

## Use cases

* **Doctor is 30 minutes late** → Shift by `+30`.
* **Doctor swapping rooms with a colleague** → set *Move to physician*
  to the other physician. The day moves columns.
* **Public holiday declared on short notice** → Shift to date = next
  open day. Patients are notified by the standard reminder flow.

## Tip

Bulk reschedule respects the **status filter** at the bottom of the
grid — hide *Cancelled* and *No-show* statuses first if you only want
to move appointments that are still live.

➡ Continue to **[Block Time](block-time.md)**.
