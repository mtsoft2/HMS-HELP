# Rooms

The list of physical treatment rooms / consultation rooms / chairs the
clinic books patients into. Every appointment carries a room so the
patient (and the cleaner) know where to go.

## What you see

A list, one row per room. Above the list a counter — *Treatment
rooms — N configured*.

## Add a room

Click **New Room**. The editor opens with:

| Field | Meaning |
|---|---|
| **Room #** | The room number. Must be unique. |
| **Name (EN)** | The room's English name (printed on the appointment slip). |
| **الاسم** | The room's Arabic name. |
| **Doc ID** | (Optional) Default physician for this room — appointments booked in this room default to this physician. |
| **Type** | (Optional) Room type code — used in some reports. |
| **Day-of-week toggles** | A row of seven day buttons — tick the days this specific room is in use. Leave them all on for a "always available" room. |

Save. The room is immediately available on the booking dialog and in
the rooms picker.

## Edit / Delete

Each row has **Edit** and **Delete** links. Editing reopens the same
editor. Delete asks for confirm — rooms that have past appointments
are kept in the database for audit but no longer appear on the
booking dialog.

## Tips

* Set **Doc ID** for chairs that are *always* used by one dentist —
  every booking in that chair pre-selects them.
* Use the day toggles for a room that is only available on certain
  days (e.g. a mobile X-ray that comes in twice a week).
