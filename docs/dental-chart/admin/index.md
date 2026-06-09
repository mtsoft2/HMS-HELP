# Administration

The dental chart inherits most of its configuration from HMS itself
(procedure catalogue, price list, dentist list, room list). Only two
areas are configured at the chart level.

* **[Tooth Numbering](numbering.md)** — Universal vs FDI vs Palmer.
* **[Procedure Legend](legend.md)** — the catalogue of icons shown
  on the legend popup; what each one means.

## Other administration done elsewhere in HMS

| Setting | Where |
|---|---|
| Procedure catalogue (the tools available in the toolbox) | HMS → Data Setup → Clinical → Procedures |
| Price list (per-procedure prices) | HMS → Data Setup → Billing → Price List |
| Dentists + their schedules | HMS → Data Setup → Staff |
| Rooms (chairs / operatories) | HMS → Data Setup → Organisation → Rooms |
| User permissions to chart / edit / delete | HMS → User administration |
| Default overlays per user | Per-user preferences, saved on first use |

## Per-user preferences

Saved automatically on the chart:

* **Active overlays** at last close — re-opened in the same state.
* **Sidebar collapsed / expanded**.
* **Toolbox visible / hidden**.
* **Hints visible / hidden**.
* **Density / theme** preferences (light vs dark).

Nothing else needs to be configured per user — the chart picks up
defaults from HMS.

➡ Continue to **[Numbering](numbering.md)**.
