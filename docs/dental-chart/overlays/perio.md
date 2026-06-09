# Periodontal Overlay & Sheet

The periodontal layer covers everything a perio exam needs —
six-point pocket charting, bleeding on probing, recession,
mobility, furcation, suppuration — painted on the same arches the
GP uses.

## Two parts

The perio layer has **two independent controls**:

| Control | What it does |
|---|---|
| **Perio overlay** | Toggles the periodontal *visualisation* on the chart — pocket polylines, BoP diamonds, recession spikes. Read-only. |
| **Perio sheet** | Opens the perio *data-entry drawer* on the right of the chart. Read-write. |

You can leave the overlay visible while the sheet is closed —
useful chairside when the visualisation is enough and the dentist
doesn't want the drawer covering the chart.

## The visualisation (overlay)

Drawn on top of the base chart:

* **Pocket polylines** — six points per tooth connected, the line
  height showing pocket depth.
* **BoP diamonds** — red diamonds where bleeding-on-probing was
  recorded.
* **Recession spikes** — downward spikes on the buccal / lingual
  showing recession depth.
* **Mobility** — small marker on teeth with mobility recorded
  (degree shown next to it).
* **Furcation** — marker between roots when furcation involvement
  is recorded.
* **Suppuration** — distinct icon where pus was observed.

Colour intensity scales with severity — deeper pockets, more
recession, all show stronger.

## The sheet (data entry)

The perio sheet opens as a right-side drawer with:

* **Header** — patient, exam date, recorded-by.
* **Per-tooth grid** — six sites per tooth (DB, B, MB, DL, L, ML for upper / DL, L, ML, DB, B, MB for lower), each with pocket depth and BoP toggle.
* **Mobility row** — degree I / II / III per tooth.
* **Furcation row** — class I / II / III per tooth.
* **Recession row** — buccal + lingual values per tooth.
* **Suppuration toggle** per site.
* **Notes** field for the overall exam.

On narrow screens the sheet **covers the chart**; on wide screens
it sits beside it.

## Closing the exam case

* **Close case** marks this perio exam read-only — chart frozen,
  no further edits.
* **Reopen** re-activates it and deactivates any other active
  perio exam, ensuring only one is current at a time.

## Demo mode

The **Perio Demo** button loads a realistic *generalised Stage II
periodontitis* case — severe localised lower-posterior pocketing,
BoP, mobility, furcation involvement — to showcase the chart's
range. Nothing is saved to the database. Click Demo again to exit
and reload the real exam.

## Tips

* Toggle the **overlay on and the sheet off** when you want to
  *show* the patient their perio status without entering data.
* The overlay redraws automatically when you save the sheet — no
  need to close-and-reopen.
* Pocket depth values 0–12 are accepted; out-of-range entries are
  rejected with a small inline warning.
