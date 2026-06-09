# Features

Every DM2 feature, grouped by what it lets you do. Use this page as a
checklist when training new users or evaluating gaps against another
DMS.

---

## 1. Browse & Find

* **Grid view** — large thumbnails laid out in a responsive grid.
* **List view** — dense one-line-per-document rows for fast scanning.
* **Timeline view** — documents grouped by date, newest first.
* **Search** — by title, tags, or keywords. Live filter as you type.
* **Sort** — by date, title, type, or size.
* **Show / hide soft-deleted** — surface or hide files in the recycle
  bin without permanently removing them.
* **Multi-select** — tick several rows for bulk actions (delete,
  download, move to compare).
* **Dark / light theme toggle**.
* **Maximise** — DM2 fills the whole window for focus work.
* **Chart mode** — when embedded in the dental chart, DM2 narrows to
  *this tooth, grid view, capture/refresh only*.

## 2. Add Documents

* **Drag and drop** — drop one or many files from Explorer / Finder.
* **Add document** — file picker for single-file upload.
* **Import multiple** — multi-file picker with metadata applied to all
  at once (title template, category, tags, keywords, description).
* **Skip duplicate uploads (by content hash)** — refuses to upload the
  same file twice, even if it has a different name.
* **Capture from camera** — works with intraoral cameras and any UVC
  USB device. Live preview, click to capture, retake or save.
* **DICOM import** — DICOM files keep their metadata (patient,
  modality, series, study date) on import.

## 3. View — any file type

A single viewer surface handles all of:

| Family | Formats |
|---|---|
| Images | JPG, PNG, GIF, BMP, TIFF, WebP |
| PDF | Native PDF rendering with text selection |
| Word | DOC, DOCX rendered in-browser |
| Excel | XLS, XLSX with sheet tabs |
| PowerPoint | PPT, PPTX slide preview |
| Video | MP4, WebM, MOV with play / pause / scrub |
| Audio | MP3, WAV, OGG with play / pause |
| DICOM | Single-frame, multi-frame (cine), 3D series |
| Archives | ZIP — peek inside without extracting |
| Other | Generic file icon + download |

## 4. Viewer — Navigation

* **Previous (←) / Next (→)** — page through every document in the
  current selection.
* **Frame strip** — for multi-frame DICOM, scroll or click any frame.
* **Cine play / pause** — auto-advance through DICOM frames at a
  configurable speed.
* **Mouse-wheel mode** — toggle between *zoom* and *scroll frames*.
* **Timeline** — pop the timeline overlay to jump back in chronological
  order without leaving the viewer.
* **Open in new tab** — pop the document out into its own browser tab.

## 5. Viewer — Transform

* **Rotate left / right** — 90° increments.
* **Mirror horizontal / vertical** — flip the image.
* **Zoom in / out** — wheel, pinch, or buttons.
* **Pan** — click-and-drag in cursor mode.
* **Reset view** — back to default rotation / zoom / pan.

## 6. Viewer — Annotations

* **Cursor mode** — click any annotation tool, then draw on the image.
* **Pen / freehand draw**.
* **Text labels**.
* **Shapes** — rectangle, circle, polygon, arrow.
* **Eraser** — remove a single annotation.
* **Save annotations to the patient record** — annotations are kept as
  a layer attached to the document; the original file is never
  modified.

## 7. Viewer — Measurements

* **Ruler** — straight-line distance, with auto-scale from DICOM
  pixel-spacing when available.
* **Combined ruler** — multi-segment measurement.
* **Angle** — three-point angle (e.g. for orthodontic analysis).
* **Crosshairs** — quick centre-cross for symmetry checks.
* **Polygon area** — closed-polygon area measurement.
* **Calibration** — re-calibrate pixels-per-mm if the source image has
  no DICOM scale.

## 8. Viewer — Image Filters

* **Brightness / contrast** sliders.
* **Inversion** — colour-invert (useful for X-rays).
* **Grayscale**.
* **Sharpen / blur** presets.
* **Window / Level** for DICOM — full radiology W/L control with
  modality presets (bone, soft tissue, lung).

## 9. Compare

* **Add to compare** — pin a document into a side-by-side compare
  panel.
* **Side-by-side or grid layout** — 2 / 3 / 4-pane comparison.
* **Synchronised zoom & pan** — move one image, the others move with it.
* **Remove from compare** — drop a document out of the compare set.
* **Common use case** — before-and-after orthodontic photos,
  baseline-vs-follow-up X-rays.

## 10. DICOM-specific

* **Multi-frame stack** — scroll through the whole series.
* **Cine playback** — play / pause / speed.
* **Mouse-wheel = scroll frames** mode.
* **DICOM metadata panel** — patient, modality, series, study date,
  acquisition parameters; toggle open/closed.
* **Window / Level** with modality presets.
* **Pixel spacing** auto-used for measurements.

## 11. Editor

The bundled in-browser editor lets you make light edits to common
document types without leaving HMS.

* **Word documents** — open `.docx` and edit text, formatting, tables.
  Save back into the patient record.
* **Cancel edit** — discard unsaved changes.
* **Editor host** — full-screen mode for focused editing.

## 12. Output & Sharing

* **Print** — current document (or the annotated overlay).
* **Download original** — the untouched file as uploaded.
* **Open in new tab** — pop-out viewer for a second-monitor setup.
* **Refresh** — re-pull the gallery from the server.

## 13. Cataloguing

Each document carries:

* **Title** — defaults to the file name if empty.
* **Description** — free text.
* **Category** — Consent form, Lab result, X-ray, Photo, …
  (configurable per clinic).
* **Tags** — comma-separated keywords, free-form.
* **Keywords** — extra searchable terms (often used for OCR'd content).

All five fields are searchable from the gallery search bar.

## 14. Safety

* **Soft delete** — deleted documents move to a recycle bin and can be
  restored. Hard delete needs admin permission.
* **Content-hash deduplication** — prevents accidental duplicate
  uploads of the same file.
* **Read-only mode** — when DM2 is embedded in a context the user has
  no write permission for, the upload / delete / edit controls are
  hidden entirely.
* **Annotations are non-destructive** — the original file is never
  modified.

## 15. UI quality-of-life

* **Keyboard shortcuts** — ← / → for prev/next, Esc to close.
* **Drag-and-drop everywhere** — drop into the gallery to upload, drag
  out of the gallery to download.
* **Density / theme** — comfortable vs compact rows; light vs dark.
* **Per-tooth chart mode** — automatic when embedded in the dental
  chart.
* **Loading spinners** for every async action.
* **Toast notifications** for save / delete / import results.

➡ Continue to **[Gallery](using/gallery.md)** for the day-to-day
browsing UI.
