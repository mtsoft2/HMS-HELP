# Overlays

An **overlay** is a clinical view layered on top of the base
chart. Each overlay covers one specialty and can be turned on or
off independently — the dentist sees only what they need.

## The six overlays

| Overlay | Purpose | Has a sheet? |
|---|---|---|
| **[Treatment Plan](plan.md)** | Existing / Planned / Completed / Referred band per tooth. | No — band only. |
| **[Periodontal](perio.md)** | Pocket polylines, BoP diamonds, recession spikes. | Yes — right drawer with per-tooth measurement entry. |
| **[Orthodontic](ortho.md)** | Brackets, archwire, elastics, status flags, headgear. | Yes — right drawer with case header, tooth grid, elastics, encounters, checklists, tasks. |
| **[Caries](caries.md)** | Patient-level caries map for surface-by-surface planning. | No. |
| **[Endodontic / Radiographic](endo-rg.md)** | Endo and radiographic finding markers on the arches. | No. |
| **[Occlusion](occlusion.md)** | Occlusal-relationship visualisation. | No. |

## How they combine

* Overlays **stack** — you can have Plan + Perio + Ortho overlays
  all on at the same time. The chart is still readable; the
  overlay layer simply adds icons on top of the base chart.
* **Sheets** are the editor drawers for overlays that need
  per-tooth data entry (perio and ortho). The overlay and the
  sheet are independent — you can leave the overlay visible while
  the sheet is closed (i.e. read-only chairside view).
* On narrow screens, opening a sheet covers the chart; on wide
  monitors the sheet + chart sit side-by-side.

## Toggling

Each overlay has its own toolbar button. Click once to enable,
click again to disable. The button highlights to show the state.

## Demo modes

Two overlays carry their own showcase data sets:

* **Perio Demo mode** — loads a realistic Stage II generalised
  periodontitis case with severe localised lower-posterior
  pocketing, BoP, mobility, furcation involvement.
* **Ortho Demo mode** — loads mock brackets, elastics, encounters,
  checklists, tasks, headgear, status flags.

Both are non-destructive — toggle them off and the real case is
restored. Useful for training, customer demos, and verifying that
your screen and printer set-up look right.

➡ Pick an overlay from the list above to dive in.
