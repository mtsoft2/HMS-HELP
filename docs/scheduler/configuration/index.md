# Scheduler Settings

Open **Scheduler settings** by clicking the **kebab menu** (three dots,
top-left of the scheduler) → **Scheduler settings**.

The settings dialog is organised into ten tabs. Use this overview to
pick the right tab; each one has its own page below.

| Tab | What it sets | Stored where | Page |
|---|---|---|---|
| **Display** | Theme, density, full-screen | Per user | [Display](display.md) |
| **Filters** | Which appointment statuses are visible | Per user | [Filters & Statuses](filters-and-statuses.md) |
| **Hours & Days** | Clinic open / close times, booking step, working days, columns | Per clinic | [Hours & Days](hours-and-days.md) |
| **Alternative** | Special hours during a date range (Ramadan, summer) | Per clinic | [Alternative Hours](alternative-hours.md) |
| **Rooms** | Treatment rooms with per-room day-of-week availability | Per clinic | [Rooms](rooms.md) |
| **Breaks** | Recurring or one-off breaks blocked across the day | Per clinic | [Breaks](breaks.md) |
| **Holidays** | Fixed and annual closures | Per clinic | [Holidays](holidays.md) |
| **Categories** | Appointment categories with their colours | Per clinic | [Categories & Colours](categories-and-colors.md) |
| **Alerts** | Wait threshold + no-show banding + balance threshold | Per clinic | [Alerts](alerts.md) |
| **System** | Release, version, app name, current user (read-only) | — | — |

!!! tip "Per-user vs per-clinic"
    The **Display** and **Filters** tabs save automatically and only
    affect your own screen. Every other tab saves to the clinic
    configuration — your changes apply to **everyone in the clinic**
    the next time their scheduler loads.

!!! warning "Permission"
    Saving anything outside **Display** and **Filters** needs the
    *Scheduler administrator* permission. Without it, those tabs open
    in read-only mode.
