# Snapshots & Compare

Snapshots let you **freeze the chart on any date** and then
**compare two snapshots side-by-side** later — invaluable for
follow-up visits, before/after presentations, insurance claims,
and medico-legal records.

## Saving a snapshot

Click **Save snapshot** in the toolbar.

* A confirmation appears: *"Save a snapshot of the chart as of
  today? A new snapshot point is created so you can use Compare
  later to see what changed."*
* Click **OK** — a snapshot marker is created for **today's date**.
* The new date appears in the **Snapshot dropdown**.
* A toast confirms: *"Snapshot saved for today."*

The snapshot is a **marker**, not a copy of the chart — it
references the procedures dated up to that day. So deleting a
snapshot does not delete procedures (see below).

## Viewing a snapshot

Open the **Snapshot dropdown** in the toolbar. Pick any date:

* **Today** — live chart with every procedure including ones added
  today.
* **Any past snapshot date** — chart as it was on that date.

The chart redraws with only the procedures recorded up to (and
including) the picked date.

## Comparing two snapshots

Click **Compare**:

* The Compare view opens with two arch-pair panels side-by-side —
  pick a *Left* date and a *Right* date from snapshot dropdowns
  on each panel.
* Procedures **added** between Left and Right are highlighted
  **green**.
* Procedures **removed** between Left and Right are highlighted
  **red**.
* Procedures that exist on both panels are drawn normally.

A tooltip on each diff shows what changed (procedure name,
surfaces, date).

## Deleting a snapshot

Click **Delete snapshot** with a snapshot date selected.

> **Removes the snapshot MARKER for the currently-selected date.
> Real procedures dated the same day are NOT deleted.**

The confirmation popup makes the distinction explicit. If the date
was *only* a marker (no procedures dated that day), the date
disappears from the dropdown. If real procedures exist for that
day, those procedures are kept and the dropdown loses just the
marker.

This is by design — snapshot markers are organising hooks, not
data — and protects against accidentally deleting clinical
records.

## Reload

After importing procedures from another system, or if something
looks off, click **Reload** — the chart recalculates from saved
procedures and re-applies the snapshot view.

## Use cases

* **Follow-up appointments** — save a snapshot at the end of each
  major visit. Compare to the previous snapshot at the start of
  the next visit and explain to the patient what was done.
* **Ortho progress** — snapshot at every adjustment visit and
  compare across the entire treatment to show progression.
* **Insurance audit** — point in time evidence of what was
  recorded vs what was billed.
* **Patient handover** — when a patient transfers to another
  dentist, the snapshot list shows the chart history without
  needing the full procedure log.

## Tips

* Save a snapshot at the **end** of each significant visit — it
  takes a second and gives you a clean before/after later.
* Use the **Print** button while viewing a past snapshot to print
  the chart as it was on that date.
* The snapshot dropdown is colour-coded by recency — today on
  top, older below.
