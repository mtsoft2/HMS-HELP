# Filters & Statuses

Controls which appointments appear in the grid based on their status.

## Show appointments with status…

A list of every appointment status with a checkbox. Tick to show, untick to hide. The legend at the bottom of the grid is the same list — clicking a legend swatch toggles the matching checkbox.

Typical statuses:

* **Pending** — booked but not yet confirmed.
* **Confirmed** — patient confirmed (often by SMS reply).
* **Arrived** — patient has checked in at reception.
* **In-Service** — patient is currently with the physician.
* **Completed** — visit finished.
* **No-show** — patient did not turn up.
* **Cancelled** — appointment cancelled.

!!! tip
    Hide **Completed**, **No-show**, and **Cancelled** to keep the grid
    focused on what's still live today.

## Reset to default visible statuses

Click **Reset to default visible statuses** to bring back the
out-of-the-box visibility (typically: Pending, Confirmed, Arrived,
In-Service).

## Filter mode (read-only)

Shown for reference only — it tells you which filter logic the clinic
is using globally (e.g. *Hide cancelled by default*, *Show everything*).
The setting itself is in the clinic's global configuration, not editable
from here.
