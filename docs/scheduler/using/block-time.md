# Block Time

A **Block** is a stretch of time on a physician's calendar that is
**not bookable** — meetings, theatre, surgery slots, training,
leave-of-absence. They show as striped grey bands on the grid and the
booking dialog refuses to place a patient inside them.

## Add a block

Right-click an empty cell → **Block this time** (or open the Block
dialog from the kebab menu → **Breaks**).

Fill in:

| Field | Meaning |
|---|---|
| **Physician** | Whose calendar the block applies to. |
| **Room** | (Optional) Block only one room — leave blank to block all rooms. |
| **Date from / Date to** | The block's date range (use the same date in both for a single-day block). |
| **Time from / Time to** | The hours within each day that are blocked. |
| **Reason** | Free text shown in the cell tooltip — e.g. *Theatre*, *Conference*. |

Save. The block appears immediately as a grey striped band.

## Edit / Remove a block

Open the kebab menu → **Breaks**. Every block is listed with Edit and
Remove links. Editing reopens the same dialog; removing deletes the
block (existing appointments inside the same hours are not touched —
just no longer striped).

## Recurring blocks

For weekly recurring blocks (e.g. *every Wednesday 14:00 – 16:00:
team meeting*):

* Set Date from to the first Wednesday and Date to to a long horizon
  (e.g. end of year).
* The system applies the block on **every** weekday that falls in the
  range and matches the time window — for a true weekly recurrence
  combine this with the working-day toggles in **Hours & Days**.

## Difference vs Breaks

* A **Break** is the same idea but configured globally under
  **Scheduler settings → Breaks** — typically lunch, prayer time. It
  applies to *all* physicians automatically.
* A **Block** is one physician's calendar entry that you add ad-hoc
  from this dialog.

## Difference vs Holidays

* A **Holiday** blocks the entire clinic on that date — no physician
  works. Configured under **Scheduler settings → Holidays**.

➡ Continue to **[Event Info Panel](event-info.md)**.
