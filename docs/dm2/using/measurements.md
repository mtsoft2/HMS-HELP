# Measurements

Measurements are quantitative annotations — distances, angles, areas.
They share the same layer as annotations and are saved to the patient
record the same way.

## Open the measurement tools

Click **Measurement tools** in the viewer toolbar. The tool palette
slides open.

## Tools

| Tool | What it does |
|---|---|
| **Ruler** | Click start point, click end point — shows the straight-line distance with units (mm if scale is known, px otherwise). |
| **Combined ruler** | Multi-segment ruler — click each waypoint; double-click to finish. Shows the total length. |
| **Angle** | Three-point angle — vertex point in the middle; the tool shows the angle in degrees. Useful for orthodontic analysis. |
| **Crosshairs** | Quick centre-cross for symmetry checks; no numbers, just visual reference. |
| **Polygon area** | Click each vertex; double-click to close. Shows the enclosed area. |

## Units & scale

* **DICOM** — pixel-spacing is read from the DICOM header. Measurements
  are reported in **millimetres** automatically.
* **Other images** — by default measurements are in **pixels**. Use
  **Calibrate** to teach DM2 the real-world scale.

### Calibrate

If the image has a known reference (a ruler in the photo, a calibrated
gauge, a structure of known size):

1. Pick the **Ruler** tool.
2. Draw a line between two points of known real-world distance.
3. Click **Calibrate** on the measurement palette.
4. Type the real distance (e.g. *10 mm*).
5. All subsequent measurements on this image use that scale.

The calibration is saved with the annotation layer so it sticks.

## Editing & deleting

* **Click** a measurement to select it; drag the end-points to adjust.
* **Eraser** (in the Annotation tool palette) removes a single
  measurement.
* **Reset view** does **not** delete measurements — it only resets
  rotation / mirror / zoom / pan.

## Save

Same as annotations — click **Save annotations to the patient record**.
Distances, angles, areas, and calibration are all persisted.

➡ Continue to **[Compare](compare.md)**.
