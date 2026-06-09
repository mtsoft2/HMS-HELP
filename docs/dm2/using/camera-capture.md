# Camera Capture

Capture photos directly from an **intraoral camera** or any **UVC USB
device** (standard webcams included) without leaving HMS.

## Open

Click **Capture from camera (intraoral / UVC)** on the gallery
toolbar. The capture dialog opens, listing every camera the browser
can see.

## What you see

* **Camera picker** — every available capture device. Includes
  built-in laptop webcams, USB cameras, and intraoral wands.
* **Live preview** — the camera feed, scaled to fit the dialog.
* **Capture** button — grabs the current frame.
* **Retake** — discards the last capture and goes back to live.
* **Save** — keeps the captured frame and uploads it as a new document.

## Workflow

1. Click **Capture from camera**.
2. Pick the camera from the dropdown — the dialog remembers your last
   choice per user.
3. The live preview starts.
4. Position the patient / tooth in the frame, click **Capture**.
5. Inspect the captured frame. Click **Retake** if you missed it,
   **Capture** again to take another, or **Save** to upload it.
6. Fill in metadata (title, category, tags) — same as a normal upload.

You can capture and save several frames in one session — Save returns
you to the live preview ready for the next shot.

## Camera permissions

The browser asks for camera permission the first time you click
Capture. Allow it once and the prompt does not return for that
workstation.

If the camera does not appear in the dropdown:

* The driver isn't installed — install the vendor driver for the
  intraoral wand.
* The camera is in use by another application — close it first.
* The browser blocked the camera site-wide — toggle the camera icon in
  the browser's address bar.

## DICOM-aware capture

If the connected device is a DICOM-capable wand (some Sirona / Acteon
units), DM2 captures **with full DICOM metadata** so the resulting
file behaves like any other DICOM in the viewer (Window/Level, pixel
spacing for measurements).

## Chart mode

When DM2 is embedded in a single tooth's imaging tab, the captured
frame is automatically tagged to that tooth — no extra step needed.

➡ Continue to **[Viewer](viewer.md)**.
