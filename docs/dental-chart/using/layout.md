# Layout & Toolbar

The dental-chart screen is organised so the dentist's eyes spend
99 % of the visit on the arches in the centre, and 1 % on the
controls around them.

## Top bar (toolbar)

Across the very top:

| Control | Purpose |
|---|---|
| **Sidebar toggle** | Collapses / expands the left rail and the patient banner. Useful on small screens. |
| **Adult / Pedo** | Switches between the permanent and primary dentitions. Adult is default. |
| **Plan overlay** | Toggles the treatment-plan band visualisation. |
| **Perio overlay** | Toggles the periodontal overlay. |
| **Perio sheet** | Opens / closes the periodontal sheet drawer. |
| **Ortho overlay** | Toggles the orthodontic overlay. |
| **Ortho sheet** | Opens / closes the orthodontic sheet drawer. |
| **Multi-select** | Enters multi-select mode. |
| **Mirror** | Mirrors today's procedures from selected teeth to the contralateral side. |
| **Apply** | Applies the armed tool to every selected tooth. |
| **Snapshot dropdown** | Picks the snapshot date to view. |
| **Save snapshot** | Captures the chart as of today. |
| **Compare** | Opens the side-by-side compare view. |
| **Delete snapshot** | Removes the snapshot marker for the selected date. |
| **Reload** | Recalculates the chart from saved procedures. |
| **Demo** | Loads a chart-wide showcase case. |
| **Print** | Opens the clean chart-only print layout. |
| **Documents** | Opens the patient's document gallery. |
| **Legend** | Opens the procedure legend popup. |
| **Maximise / Exit zoom** | Toggle the chart fullscreen. |
| **Close** | Close the dental chart. |

A **kebab menu** (left rail) holds advanced / debug-style entries
that aren't part of routine chairside use.

## Patient banner

Below the toolbar:

* Patient photo.
* Name (English + Arabic if both are on file).
* File number.
* Date of birth + age + gender.
* Clinical alerts (allergies, VIP, special-needs flags) when
  present.

The banner is always visible — the dentist never has to wonder
whose chart they are working on.

## Left rail (toolbox)

The toolbox holds the tools the dentist clicks to record what they
find or do:

* **Status group** — sound, caries (per surface), missing,
  fractured, mobility, restorations.
* **Operation group** — filling, extraction, crown, bridge, RCT,
  scaling, sealant, implant, …
* **Root group** — RCT completed / incomplete, post & core,
  periapical lesion, internal resorption.
* **Class list** — surface class picker (M, D, O / I, B / F, L / P)
  for procedures that take a class.
* **Hints** — small reminder labels under each button explaining
  what the icon means. **Hide hints** turns them off once the team
  is fluent.
* **Hide toolbox** collapses the whole rail when it isn't needed.

## Centre — the chart

Two arches, anatomically arranged. Each tooth shows:

* The procedure icons stacked on the relevant surface.
* The treatment-plan band underneath.
* Small markers when there are clinical notes, images, endodontic
  findings, or radiographic findings recorded.
* The tooth number (in the active numbering system).

## Right drawer (overlays' sheets)

When **Perio sheet** or **Ortho sheet** is open, it slides in from
the right and occupies a third of the screen (or covers the chart
on narrow screens). On wide monitors the drawer + chart coexist.

## Status / Alert area

A thin band above the chart shows non-blocking alerts (e.g.
*"Patient context not loaded yet"*, *"Mirror failed"*, *"Demo mode
on — real procedures hidden"*).

➡ Continue to **[Tools](tools.md)** or **[Selecting Teeth](selecting-teeth.md)**.
