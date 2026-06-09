# Hours & Days

The clinic's standard working hours, days, and grid sizing.

## Hours

| Setting | Meaning |
|---|---|
| **Clinic opens at (hour, 0–23)** | First bookable hour of the day. |
| **Clinic closes at (hour, 0–24)** | Last bookable hour of the day. Use 24 for midnight. |
| **Booking step (minutes)** | The increment for booking — 15, 20, 30. Every cell in the grid is one step. |
| **Scroll-to hour on open (start)** | What hour the grid scrolls to when you first open the scheduler. |
| **Scroll-to hour on open (end)** | The bottom of the initial scroll window. |
| **Lunch / midday gap 1 (minutes)** | A visual gap inserted at the lunch hour — purely cosmetic. |
| **Lunch / midday gap 2 (minutes)** | Optional second gap for clinics with two midday breaks (e.g. prayer + lunch). |
| **Show all working hours** | When ticked, the grid shows every hour from open → close on first load (overrides the *Scroll-to* settings). |

## Working days of the week

A row of seven day toggles — Sat, Sun, Mon, Tue, Wed, Thu, Fri (order
depends on locale). Tick the days the clinic is open. Non-working days
are greyed out and refuse bookings.

## Calendar options

| Setting | Meaning |
|---|---|
| **Number of physicians to show at once** | How many physician columns fit on screen in Day view. Use **Previous / Next physicians** to page through the rest. |
| **Number of day columns to show in Week view** | Usually 5 (work-week) or 7 (full week). |

## Tips

* If the receptionist regularly scrolls back to early morning slots,
  set **Scroll-to hour on open (start)** to the earliest expected
  booking — saves a daily scroll.
* The **Booking step** also controls how drag-and-drop snaps. Smaller
  step = finer precision; larger step = harder to mis-click.
