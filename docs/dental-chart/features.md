# Features

Every Dental Chart feature, grouped by what it lets you do.

---

## 1. Chart layout

* **Two-arch view** — upper and lower, anatomically correct.
* **Adult dentition** — 32 permanent teeth.
* **Paediatric dentition** — 20 primary teeth; switch with the
  **Pedo** button in the toolbar.
* **Per-tooth, five-sector clicks** — mesial · distal · occlusal /
  incisal · buccal / facial · lingual / palatal — surface-specific
  procedures recorded with one click on the right sector.
* **Treatment-plan band** under each tooth — Existing (green) /
  Planned (red) / Completed (blue) / Referred (gray) — visible
  without opening the plan overlay.
* **Maximise / Exit zoom** — chart fills the whole window for
  detailed work; one click to come back.

## 2. Tools

* **Status tools** — record conditions (caries, missing, fractured,
  sound, mobility, …).
* **Operation tools** — record treatments (filling, extraction,
  crown, root canal, scaling, …).
* **Root tools** — root-specific findings (RCT completed / incomplete,
  post & core, periapical lesion, …).
* **Class list** — surface-class picker (M, D, O / I, B / F, L / P)
  for procedures that need a class.
* **Clear all selections** — resets armed tool + armed status +
  armed root + tooth selections in one click.
* **Show / hide toolbox** — collapsible panel; *Show toolbox* /
  *Hide toolbox* button.

## 3. Selecting teeth

* **Single-click** — apply the armed tool to one tooth.
* **Multi-select mode** — click multiple teeth (they highlight) and
  then **Apply** the tool to all of them at once. Confirmation
  toast shows the count.
* **Mirror** — copy today's procedures from selected teeth to the
  contralateral side. Reports *"Copied procedures from N teeth …
  M operation(s) created."*

## 4. Per-tooth depth

For each tooth (right-click or the details panel):

* **Clinical notes** — free text, dated, attached to the tooth.
* **Tooth notes** — short labels visible on the chart.
* **Image gallery** — attach photos, X-rays, scans for that specific
  tooth.
* **Endodontic findings** — recorded with a marker on the chart.
* **Radiographic findings** — recorded with a marker on the chart.
* Each set surfaces as a small icon on the tooth so the dentist
  knows what is recorded without opening the panel.

## 5. Snapshots & Compare

* **Save snapshot** — captures the chart state for the current date.
* **Snapshot dropdown** — pick any saved snapshot to view.
* **Compare** — side-by-side compare of any two snapshot dates.
  Highlights procedures added (green) or removed (red) between them.
* **Delete snapshot** — removes only the snapshot *marker* for the
  date; real procedures recorded on that day are not deleted.

## 6. Treatment Plan overlay

* **Existing / Planned / Completed / Referred** colour-coded band
  per tooth.
* Toggle on / off independently of the perio and ortho overlays.
* Drives the per-tooth band visible by default.

## 7. Periodontal overlay & sheet

* **Perio overlay** — pocket polylines, BoP (bleeding-on-probing)
  diamonds, recession spikes drawn directly on the chart.
* **Perio sheet** (right drawer) — per-tooth measurement entry
  (six sites per tooth) with mobility, furcation, suppuration.
* Overlay and sheet are independent — the overlay can stay visible
  while the sheet is closed.
* **Perio Demo mode** — loads a realistic Stage II generalized
  periodontitis case (with severe lower-posterior pocketing, BoP,
  mobility, furcation) for showcase / training. Nothing saved to
  the database.

## 8. Orthodontic overlay & sheet

* **Ortho overlay** — brackets, archwire, elastics, status flags,
  headgear arrows drawn on the chart.
* **Ortho sheet** (right drawer) — case header, tooth-by-tooth
  grid, elastics, encounters, checklists, tasks.
* Overlay and sheet are independent.
* **Start new ortho case** — closes the current active case (kept
  for history) and creates a fresh active case.
* **Close / Reopen case** — close marks a case read-only (chart
  frozen); reopen re-activates it and deactivates any other case
  so only one is current.
* **Quick-fit brackets** — one-click "brackets on incisors / canines
  / premolars + bands on second / third molars" — typical starting
  point after bonding. Fine-tune tooth-by-tooth afterwards.
* **Wipe ortho appliance** — clears brackets / bands / attachments
  / elastics across the whole case; preserves the case header
  (appliance / phase / wires). Useful at debond.
* **Delete ortho case** — permanently deletes the case plus every
  tooth line, elastic, encounter, checklist, and task. Cannot be
  undone.
* **Ortho Demo mode** — mock brackets, elastics, encounters,
  checklists, tasks, headgear, status flags so every feature
  shows up. Nothing saved.

## 9. Other clinical overlays

* **Caries overlay** — patient-level caries map for surface-by-surface
  caries planning.
* **Endodontic / Radiographic overlay** — markers for endo findings
  and radiographic findings projected on the arches.
* **Occlusion overlay** — occlusal-relationship visualisation.

Each overlay toggles independently — you can run, say, *Plan +
Perio overlay* at the same time, or all six at once.

## 10. Patient context

* **Patient banner** — name, file number, age, gender, photo at the
  top of the chart.
* **Patient documents shortcut** — opens the patient's full
  document gallery without leaving the chart.
* **Patient info header** — extra demographics and clinical alerts
  visible inline.

## 11. Numbering systems

* Universal / FDI / Palmer notation supported.
* The currently-active numbering system is shown on each tooth's
  label.
* Configured in administration; the same chart can switch on the
  fly without losing data (numbers re-label).

## 12. Voice capture

* **Voice capture component** — dictate notes / procedures hands-free
  during the exam.
* Transcribed text lands in the relevant note field for the
  dentist to confirm.

## 13. Demo mode (chart-wide)

* Loads a realistic showcase case — one of every procedure type —
  so the chart can be demonstrated to a customer or trainee.
* **No DB writes** — toggling Demo back off restores the real
  patient procedures.
* Separate Demo modes exist for the perio sheet and the ortho sheet
  (each loads its own showcase data set).

## 14. Reload & state

* **Reload chart** — recalculate everything from the saved
  procedures (useful if something looks off).
* **Multi-select** is preserved across overlay toggles.
* **Sidebar collapse** + **Toolbox hide** for chairside screen
  space.

## 15. Printing & export

* **Print chart** — opens the browser print dialog on a clean
  chart-only layout: no toolbar, no drawer, no menus — just the
  arches and the procedures.
* **Documents** opens the patient gallery — print / export
  individual files from there.

## 16. Legend

* **Procedure legend** popup — every chart icon's meaning in one
  place. Used by new staff and by patients who want to understand
  the marks on their printout.

## 17. Action confirmation & errors

* **Verification popup** for irreversible actions (delete
  snapshot, delete ortho case, wipe ortho appliance).
* **Alerts** (top of the chart) for non-blocking warnings.
* **Toast** messages for routine confirmations (snapshot saved,
  procedures mirrored, demo loaded).

## 18. Visit awareness

* Procedures created during the current visit are visible separately
  from historical procedures.
* The chart shows "this visit" deltas distinctly so the dentist sees
  what changed today.

## 19. Linked across HMS

* **Bills** — every chart procedure adds a line to the current
  visit's bill at the price-list rate.
* **Treatment plan** — planned procedures appear with the Planned
  status; completing them flips them to Completed.
* **Imaging gallery** — every per-tooth image is filed in
  [DM2](../dm2/index.md) with the tooth as a tag.
* **Prescriptions / Lab orders** — initiated from chairside through
  the same patient context.

➡ Continue to **[Layout & Toolbar](using/layout.md)**.
