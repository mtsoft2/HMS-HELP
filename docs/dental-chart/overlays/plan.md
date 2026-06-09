# Treatment Plan Overlay

The treatment-plan overlay paints a **colour-coded band** under
every tooth so the dentist sees at a glance what is *already
there*, what is *planned*, what has been *completed*, and what was
*referred out*.

## Colours

| Band colour | Meaning |
|---|---|
| **Green** | **Existing** — already present (old restorations, prostheses, missing teeth). |
| **Red** | **Planned** — agreed with the patient but not yet done. |
| **Blue** | **Completed** — finished during the current treatment plan. |
| **Gray** | **Referred** — sent to a specialist. |

## How rows get there

* When the dentist records a procedure with status *Planned*, the
  band on that tooth turns red.
* When the same procedure is later marked *Completed* — either
  from the chart or from the visit's procedure list — the band
  turns blue.
* **Existing** comes from the patient's history at first visit
  (intake) or from observations recorded with status tools.
* **Referred** is set by hand when the treatment was sent
  elsewhere.

## Why it matters

A glance at the band tells the receptionist whether to schedule a
follow-up (lots of red), the cashier whether to invoice now (blue
just appeared), and the patient whether their plan is progressing
(more blue than red over time).

The band is **always visible** by default — even when the Plan
overlay is toggled off, the band stays. The overlay toggle
controls extra plan-specific icons on the arches; the band itself
is a built-in part of the chart.

## Print

The print layout keeps the bands — a printed treatment plan from
the chart shows the patient exactly what was completed and what is
still planned, in colour.
