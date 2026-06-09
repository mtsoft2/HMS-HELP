# Schedule

The day's appointment grid in dashboard form — what's booked, what
arrived, what was missed, who is on duty.

## Date navigator

A small bar at the top:

* **Previous day** — step back one day.
* **Today** — jump to today (also titled *Jump to today*).
* **Next day** — step forward.
* **Refresh** — re-pull the data.

The date drives every counter and the heat-strip below.

## Status counters

A row of compact tiles, each with an icon and the count for the
selected day:

| Counter | Hover tooltip | Meaning |
|---|---|---|
| **Booked** | *Total booked today* | Every appointment, all statuses included. |
| **Scheduled** | *Newly scheduled, not yet confirmed* | Just-booked, awaiting confirmation. |
| **Confirmed** | *Confirmed bookings* | Patient confirmed (e.g. by SMS reply). |
| **Arrived** | *Patients who have arrived* | Checked-in at reception. |
| **Attended** | *Completed visits* | Patient seen and visit closed. |
| **Cancelled** | *Cancelled / deleted* | Cancelled or removed. |
| **No-show** | *No-shows* | Patient did not turn up. |
| **Free** | — | Slots still open for new bookings. |

## Heat-strip

A horizontal strip representing the whole day, one cell per booking
slot:

* **Cell colour** = status (matches the status counters).
* **Cell content** = patient's initial.
* **Hover tooltip** = patient name + physician + time + status.
* **Click a cell** = open that appointment.

This is the fastest way to see "where are the gaps" or "who is in
chair 3 at 11:00".

## Physicians on duty

A side panel listing the physicians working that day:

* Each row shows the physician's name + a compact mini-counter
  (booked / attended / no-show).
* **Show less / Show more** when the list is long.
* **Click a physician** → opens their full record.

## What you do with it

* **Morning huddle** — open the heat-strip on the wall, walk the team
  through the day in 30 seconds.
* **Mid-morning sanity check** — *Arrived* counter should be tracking
  *Confirmed*; large gap → someone is slow at check-in.
* **End of day** — *No-show* count is your hit-list for next-day
  reminder calls.

➡ Continue to **[Census](census.md)**.
