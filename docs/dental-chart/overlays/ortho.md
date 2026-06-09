# Orthodontic Overlay & Sheet

Everything orthodontics needs — bracket / band placement, archwire,
elastics, status flags, headgear — on the same arches, plus a
right-side drawer for full case management.

## Two parts

| Control | What it does |
|---|---|
| **Ortho overlay** | Draws brackets, archwire, elastics, status flags, headgear arrows on the chart. |
| **Ortho sheet** | Opens the orthodontic editor drawer on the right. |

Independent — overlay can be on while the sheet is closed.

## The visualisation (overlay)

* **Brackets** — drawn on the buccal of each banded tooth, colour
  reflecting bracket type (metal, ceramic, self-ligating).
* **Bands** — drawn on the appropriate molars.
* **Archwire** — drawn through every bonded tooth on the relevant
  arch.
* **Elastics** — drawn between teeth showing direction and class
  (II, III, cross-elastic, vertical, …).
* **Status flags** — small icons for *to-bond*, *to-reposition*,
  *to-debond*, *holding*.
* **Headgear arrows** — outward arrows indicating headgear forces.

## The sheet (case management)

The drawer is split into tabs:

### Case header

Active case, appliance type, current phase, archwire upper / lower,
start date, expected end, treating orthodontist.

### Tooth grid

One row per tooth — bracket / band, attachment, status flag,
auxiliary, notes.

### Elastics

A table of every elastic on this case — from/to teeth, class,
size, wear pattern, start date, end date.

### Encounters

Per-visit log — what was done at each ortho visit (wire change,
spring placed, IPR, reposition).

### Checklists

Phase-specific checklists (e.g. *initial alignment complete*,
*levelling complete*, *finishing*) so the case can be progressed
deliberately.

### Tasks

To-do items for the next visit (*"check 14 binding"*, *"order new
elastics"*, *"order retainer"*).

## Quick-fit brackets

A single click "puts brackets on incisors / canines / premolars
(1–28) and bands on the second / third molars" — typical starting
point right after bonding. Fine-tune tooth-by-tooth afterwards.

## Wipe ortho appliance

Wipes brackets / bands / attachments / elastics for **every** tooth
on the current case. The **case header** (appliance, phase, wires)
is preserved. Useful at debond.

The chart asks for confirmation before wiping.

## Start new case / Close / Reopen

* **Start new case** — closes the currently active case (kept for
  history) and creates a fresh active case.
* **Close case** — marks the case read-only (chart frozen, no
  further edits).
* **Reopen** — re-activates the case and deactivates any other
  active case so only one is current at a time.

## Delete ortho case

**Permanently deletes** this case **and** all its tooth lines,
elastics, encounters, checklists, and tasks. *Cannot be undone.*

Asks for explicit confirmation. Use only when a case was created in
error.

## Demo mode

The **Ortho Demo** button loads mock brackets, elastics,
encounters, checklists, tasks, headgear, status flags so every
feature appears. Nothing saved to the database. Click again to
exit and restore the real case.

## Tips

* Open the **sheet** for case management; leave just the **overlay**
  on for chairside review.
* Use the **Encounters** tab as your visit journal — it makes the
  next adjustment visit faster.
* The **Tasks** tab is where you list everything you want to do
  next time — checked off when finished.
