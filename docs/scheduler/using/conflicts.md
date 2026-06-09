# Conflicts

When you drop an appointment onto a time that already has bookings, the
scheduler does **not** silently overwrite — the **Conflict** dialog
opens and shows you exactly what would clash.

## What the dialog shows

A card for each conflicting appointment, with:

* Patient name + MRN
* Time (from – to)
* Physician
* Room
* Status
* Reason

The card at the top is the appointment **you are placing**. The cards
below are what is already in those slots.

## Your choices

| Action | Effect |
|---|---|
| **Cancel** | Closes the dialog. Nothing changes. The clipboard is preserved if you cut. |
| **Overwrite** | Deletes the conflicting appointments and places yours. Use sparingly — those patients are now unbooked. |
| **Move both** *(when possible)* | Puts yours in and bumps the conflicting one(s) to the next free slot. |

## Bulk paste conflicts

If you paste several appointments in a row and one of them conflicts,
the dialog shows that *one* conflict. Resolve it and the paste
continues automatically.

## Why the dialog appears even when slots "look" free

* The slot might be a **break** or **blocked time** the physician
  configured.
* The slot might be inside a **holiday**.
* Another receptionist might have booked it 5 seconds before you (the
  scheduler refreshes on every action).

In all three cases the conflict dialog tells you exactly which kind of
conflict it is.

➡ Continue to **[Bulk reschedule](bulk-reschedule.md)**.
