# Demo Mode

**Demo mode** loads a realistic showcase case onto the chart so
you can present the system's full range — caries, restorations,
crowns, RCTs, extractions, implants, plus active treatment-plan
items — without touching any real patient data.

Click **Demo** in the toolbar to enable; click again to exit.

## What loads

A representative case with **one of every procedure type** — so
the chart shows every icon and overlay element in a sensible
clinical context.

A confirmation toast appears:

> *"Loaded showcase case with one of each procedure type
> (no DB writes). Click Demo again to exit."*

While Demo mode is on, the chart's **alert area** displays a
*"Demo mode on"* badge so nobody mistakes the showcase chart for
a real patient.

## Exiting

Click **Demo** again. The chart reverts to the real patient's
procedures and a toast confirms:

> *"Demo mode off — real patient procedures restored."*

## Nothing is saved

* The showcase procedures **never touch the database**.
* The real patient's procedures are **never altered**.
* Snapshot dates are **not** modified by Demo mode.
* Closing the chart while Demo is on still leaves the real patient
  intact next time you open it.

## Per-overlay Demo modes

Two overlays have their **own** Demo data:

* **[Periodontal](overlays/perio.md#demo-mode)** — Stage II
  generalised periodontitis with severe lower-posterior pocketing,
  BoP, mobility, furcation.
* **[Orthodontic](overlays/ortho.md#demo-mode)** — mock brackets,
  elastics, encounters, checklists, tasks, headgear, status flags.

Each overlay's Demo toggle is independent of the chart-wide Demo
button — you can demo perio without the chart-wide showcase, for
example.

## Use cases

* **Sales presentation** — open the chart on any patient, hit
  Demo, walk the customer through the icons.
* **Training** — junior dentists practise on the showcase case
  without polluting real records.
* **Bug verification** — designers and engineers can reproduce
  layout / colour / overlay issues on the same canonical data set
  in every clinic.
* **Marketing material** — screenshots of the Demo case are safe
  to publish (no real patient).

## What Demo does *not* hide

* The patient banner still shows the **real patient's** name and
  photo. Demo modifies the chart contents only — not the patient
  context.
* The toolbar / overlays / drawer still function exactly as they
  would on a real case.

So Demo is for **what the chart can show**, not for *"a different
patient"*.
