# Alternative Hours

Some clinics shift their hours for a few weeks or months (Ramadan,
summer, winter break). Instead of editing the main hours and remembering
to put them back, use **Alternative Hours** — a parallel schedule that
takes over for a date range, then automatically reverts.

## Fields

| Setting | Meaning |
|---|---|
| **Use alternative hours** | Master switch. Off = ignore everything below. |
| **Alternative hours — start date** | First day the alt schedule applies. |
| **Alternative hours — end date** | Last day the alt schedule applies. |
| **Alt-opens at (hour, 0–23)** | Open hour during the alt window. |
| **Alt-closes at (hour, 0–24)** | Close hour during the alt window. |
| **Alt-gap 1 (minutes)** | Lunch / midday gap during the alt window. |
| **Alt-gap 2 (minutes)** | Optional second alt gap. |

## How it interacts with regular hours

* Inside the alt window → alt hours win, regular hours are ignored.
* Outside the alt window → regular hours apply, alt settings are
  ignored.
* Working-day toggles (Sat, Sun, …) come from **Hours & Days** in both
  cases — there is no separate alt day-of-week list.
* Booking step comes from **Hours & Days** in both cases.

## Use cases

* **Ramadan** — open 21:00 – 01:00 for one month.
* **Summer school break** — earlier opening (07:00 – 14:00) for July /
  August.
* **Winter Holidays** — shortened day (10:00 – 16:00) for a week.

## Tip

Set up the next Ramadan schedule at the start of the year and leave
it in place — the **Use alternative hours** master switch lets you
toggle the whole thing on and off without re-entering dates.
