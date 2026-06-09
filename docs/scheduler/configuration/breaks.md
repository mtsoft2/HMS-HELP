# Breaks

Recurring or one-off slots of time that are **not bookable** for the
whole clinic — typically lunch, prayer time, mandatory staff meetings.

A break is different from a [Block](../using/block-time.md): a Block
is one physician's calendar entry; a Break applies to every physician
in the clinic.

## What you see

A list with a counter at the top — *Breaks & blocked time — X of Y
shown* — and a filter box to narrow it down by physician or reason.

Each row shows: physician (or *All*), room (or *All*), date range,
time range, reason, Edit and Remove links.

## Add a break

Click **New Break**. Fill in:

| Field | Meaning |
|---|---|
| **Physician** | The physician the break applies to. Pick *All* for a clinic-wide break (lunch / prayer). |
| **Room** | (Optional) Only block a specific room — leave blank for all rooms. |
| **Date from / Date to** | The range of days the break is in effect. Use the same date in both for a one-off. |
| **Time from / Time to** | The hours within each day. |
| **Reason** | Free text shown in the cell tooltip — e.g. *Lunch*, *Prayer*, *Staff meeting*. |

Save. Cells inside the break are now striped grey and refuse bookings.

## Recurring weekly break

The classic *every weekday 13:00 – 14:00 = lunch* break:

* Pick *All* physicians, *All* rooms.
* Date from = today, Date to = end of year (or further).
* Time from = 13:00, Time to = 14:00.
* Reason = *Lunch*.

The break applies on every working day in the range (working days are
set in [Hours & Days](hours-and-days.md)).

## Edit / Remove

Use the per-row links. Removing a break frees up those slots
immediately for new bookings — existing appointments inside the
window are kept as-is.
