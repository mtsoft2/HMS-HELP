# Viewer

The DM2 viewer is a single surface that knows how to render every
common file type — images, PDF, Office documents, video, audio, DICOM,
ZIP archives. It opens when you click a document in the gallery.

## The toolbar

The toolbar groups buttons into four areas — they show or hide
depending on what the file supports.

| Group | Buttons |
|---|---|
| **Cursor** | Cursor mode (pan / select), annotation tools, measurement tools, image filters, more tools |
| **Transform** | Rotate left, Rotate right, Mirror horizontal, Mirror vertical, Reset view |
| **Save** | Save annotations to the patient record |
| **Output** | Print, Download original, Open in new tab |

Plus navigation arrows on the left / right edge for **Previous (←)** and
**Next (→)** — they walk through every document in the current
selection.

## Cursor mode — click for menu

The default mode. Click **Cursor** in the toolbar (or just click on
empty viewer space) to switch back to it from any tool. In cursor mode:

* **Drag** = pan the image.
* **Mouse wheel** = zoom (or scroll frames, in DICOM stack mode).
* **Pinch** on touch screens = zoom.
* **Click a tool from the toolbar** to enter annotation, measurement,
  or filter mode.

## Image transforms

| Button | Effect |
|---|---|
| **Rotate left** | 90° anti-clockwise. |
| **Rotate right** | 90° clockwise. |
| **Mirror horizontal** | Flip left ↔ right. Lights up when active. |
| **Mirror vertical** | Flip top ↔ bottom. Lights up when active. |
| **Reset view** | Removes all rotation, mirroring, zoom, and pan — back to default. |

Transforms are **non-destructive** — the original file is untouched.

## Frame navigation (DICOM and multi-frame)

When the document has multiple frames (DICOM stacks, multi-page TIFF):

* **Frame strip** along the bottom — click any frame thumbnail.
* **Mouse-wheel mode** — toggle between *zoom* and *scroll frames*.
  The current mode is shown in the toolbar info line:
  *Mouse-wheel: zoom* or *Mouse-wheel: scroll frames*.
* **Play / pause (cine)** — auto-advance through frames at a
  configurable speed.

## File-type quick reference

| Type | Tools available |
|---|---|
| Image | All annotation, measurement, filter, transform, compare |
| DICOM | All of the above + Window/Level + cine + DICOM metadata panel |
| PDF | Page navigation, text selection, print |
| Word / Excel / PowerPoint | In-browser preview, page / sheet navigation |
| Video | Play / pause, scrub, volume, fullscreen |
| Audio | Play / pause, scrub, volume |
| ZIP | Browse contents, extract any file to viewer |
| Other | Generic icon + Download original |

➡ Continue to **[Annotations](annotations.md)** or
**[Measurements](measurements.md)**.
