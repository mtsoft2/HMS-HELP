# Patching History

Open from the **Patching History** button on the Welcome step. The
dialog shows the patch trail for the connected database — every
patch that has been recorded since the **last cumulative (-CM)
patch**.

![Patching History dialog](img/04-patching-history.png)

## Header

The grey banner at the top tells you at a glance:

* **Current patch** — the patch number of the wizard you launched
  (e.g. *"current patch 462"*).
* **Entries** — how many patch rows are tracked.
* **MISSING** count — how many of those rows are MISSING.

Example: *"112 entries · 55 MISSING"* — a database that has gone
through 112 patches' worth of script slots, but 55 of them never
recorded a successful install.

## Columns

| Column | Meaning |
|---|---|
| **Patch** | The patch number. Patches that are cumulative end in **`-CM`** (e.g. `350-CM`). |
| **Status** | *Applied* (green), *Error* (red), or **MISSING** (red, no date). |
| **Date** | When the patch ran (blank if MISSING). |
| **Version** | The HMS version the patch belongs to (e.g. *HMS 23.00*). |

## Status meanings

* **Applied** — the patch ran end-to-end successfully.
* **Error** — the patch ran but one or more scripts failed. The
  database is in an undefined state for that patch; rerun the
  wizard with that patch's installer.
* **MISSING** — the patch was never recorded as applied on this
  database. Either it has not been applied yet, or it was applied
  before the patch-tracking machinery existed.

## Reading the report

Scroll through the list looking for **red rows**:

* A line of consecutive *Applied* greens means the database is
  healthy in that range.
* An **Error** row means that specific patch needs to be re-applied
  before the database is fully in sync.
* A **MISSING** row means an earlier patch in the chain was never
  recorded — chase that one first, because subsequent patches may
  have depended on its schema changes.

## Why the report starts at the last CM

A cumulative patch consolidates every change up to its number into
a single, idempotent installer — running it brings any database up
to that version regardless of which intermediate patches were
applied or missed. So the history before the last `-CM` is
irrelevant: the `-CM` guarantees the baseline.

The report only lists patches **after** the last `-CM` because those
are the ones whose individual install status still matters.

## Acting on the report

* **Many MISSING rows + an old `-CM`** → apply the most recent `-CM`
  cumulative patch first. That clears almost every MISSING in one
  go.
* **A few Error rows scattered** → re-apply each errored patch
  individually. The patch installers are idempotent — re-applying
  is safe.
* **MISSING rows with no Error rows** → the customer skipped a few
  patches. Apply them in order; later patches may need their schema
  changes.

## Close

Click **Close** to return to the wizard's Welcome step. Nothing in
the report itself is editable — it is a read-only audit view.
