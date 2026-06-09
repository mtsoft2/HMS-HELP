# Upload & Import

Four ways to get files into DM2.

## 1. Drag & drop

The fastest path. Drag any file (or several files at once) from your
file explorer onto the gallery surface. Upload starts immediately, a
progress bar appears on each new tile. When done, the **Edit** dialog
opens so you can fill in title / category / tags.

## 2. Add document

Click **Add document** in the toolbar — opens a standard file picker.
Useful when drag-and-drop is blocked by the OS or you are uploading
from a network share you have already navigated to.

## 3. Import multiple

Click **Import multiple** when you want to upload **many files** and
apply the **same metadata** to all of them (e.g. 20 X-rays from the
same study session).

The Import dialog has:

* A file picker that accepts as many files as you want.
* **Title** template — used for every file (or fall back to the file
  name if empty).
* **Description** — applied to all.
* **Category** — applied to all.
* **Tags** — comma-separated, applied to all.
* **Keywords** — comma-separated, applied to all.
* **Skip duplicate uploads (by content hash)** — recommended on. When
  ticked, files that are already in the patient's gallery (same
  content, regardless of file name) are skipped.

Click **Import** to upload them all, or **Cancel** to abort.

## 4. Camera capture

For live capture see **[Camera Capture](camera-capture.md)** — works
with intraoral cameras and any UVC USB device.

## Duplicate detection

DM2 hashes every file on upload. If the hash matches a file already in
**this** patient's gallery, the upload is skipped (when *Skip
duplicates* is on) or warned about (when it is off). The check is by
**file content**, not file name — renamed copies are still detected.

## Supported file types

DM2 accepts anything; specifically tested viewers exist for:

* Images: JPG, PNG, GIF, BMP, TIFF, WebP.
* PDF.
* Microsoft Office: DOC, DOCX, XLS, XLSX, PPT, PPTX.
* Video: MP4, WebM, MOV.
* Audio: MP3, WAV, OGG.
* DICOM (single and multi-frame).
* Archives: ZIP (peek inside without extracting).

Other file types upload fine and show a generic file icon with a
**Download original** button.

## Permission gates

* If the embedding context is **read-only**, the *Add / Import /
  Capture* buttons are hidden entirely.
* Per-user permission can restrict upload size (set in HMS user
  config).
* Per-user permission controls **hard delete** vs **soft delete**.

➡ Continue to **[Camera Capture](camera-capture.md)**.
