# Categories & Colours

Up to **12 appointment categories**, each with its own colour. The
colour is what fills the cell on the grid — so the receptionist
recognises an emergency vs a routine cleaning at a glance.

## What you see

A 12-row table. Each row has the category **name** and a **colour
swatch**.

## Editing

The table is **read-only** in the standard settings dialog — the
clinic configuration team sets the categories and colours during
implementation. To request a change:

* Add a new category → contact the system administrator (they update
  the master clinic configuration).
* Change a colour → same — the swatch palette is managed centrally so
  every clinic in a group uses the same colour for the same category.

## Choosing colours

Some guidance from clinics that have shipped this for years:

* **Reserve red for Emergency** — receptionists instinctively look for
  it.
* **Use a muted colour for the most common category** — *Routine
  follow-up* in pale blue keeps the grid calm.
* **Pick distinct colours for adjacent categories** — pale-blue
  follow-up next to pale-green check-up is hard to tell apart on a
  small screen.
* **Don't use grey** — grey is reserved for breaks and blocks.

## Where the colour shows up

* Cell fill on the grid.
* Swatch on the **event info panel**.
* Swatch in the booking dialog's category picker.
* Legend at the bottom of the grid (clicking the swatch toggles
  visibility — see [Filters & Statuses](filters-and-statuses.md)).
