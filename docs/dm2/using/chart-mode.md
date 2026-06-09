# Chart Mode

When DM2 is embedded **inside the dental chart for a single tooth**,
it switches automatically into **chart mode** — a simplified gallery
that shows only that tooth's documents, with only the controls a
clinician needs at the chairside.

## What changes

| Removed in chart mode | Reason |
|---|---|
| Search bar | Only this tooth's files anyway. |
| Category filter | Same. |
| Type filter | Same. |
| Import multiple | Clinical capture is one-at-a-time. |
| List view toggle | Grid only — thumbnails are what matters. |
| Timeline view toggle | The chart already shows the timeline by visit. |

## What stays

* **Add document** — quick single-file upload.
* **Capture from camera** — intraoral / UVC capture (the main use).
* **Refresh** — re-pull after another user uploads.
* **Dark mode** — eye-friendly for radiology review.
* **Tile click → viewer** with annotations, measurements, compare.

## Header strip

A *Tooth N* header appears above the gallery so it is always clear
which tooth you are attaching files to. The number comes from the
chart's currently-selected tooth.

## Workflow at the chairside

1. Select a tooth in the dental chart.
2. Click the **Imaging** tab — DM2 opens in chart mode for that tooth.
3. Click **Capture from camera** — take the X-ray / photo.
4. Click the new tile to open the viewer.
5. Annotate / measure as needed; save.
6. Move on to the next tooth — DM2 follows the chart selection
   automatically.

## Multi-tooth view (regular DM2)

To see *every* document for the patient regardless of tooth, open the
patient's main **Documents** tab — that loads the full DM2 with all
filters available.
