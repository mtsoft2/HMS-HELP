# Administration

The Dental Clinic Front Desk has very little to configure on its own —
it just orchestrates pieces that live in other modules. As the clinic
administrator your job is mainly to make sure those pieces are set up.

| Setting | Where it lives |
|---|---|
| Branches & rooms | Data Setup → Organisation → Branches / Rooms |
| Dentists and their schedules | Data Setup → Staff → Doctors / Schedules |
| Visit types | Data Setup → Clinical → Visit Types |
| Price list (procedure prices) | Data Setup → Billing → Price List |
| Insurance payers and contracts | Data Setup → Billing → Payers |
| Drug formulary | Pharmacy module → Formulary |
| Fingerprint reader | See **[Patient Toolbox & Fingerprint](patient-toolbox.md)** |
| SMS / e-mail templates | Data Setup → Communications |

## Per-user settings

For each receptionist user:

* **Default branch** — pre-selects the branch on every picker.
* **Default dentist** — pre-fills the dentist on new visits / appointments.
* **Permission to override prices** — needed before *Re-price* and
  *Discount* on the bill are clickable.
* **Permission to cancel a paid visit** — needed before the bill can be
  cancelled after a receipt has been issued.

See the system administrator's manual for setting these (they live on
the user record, not in this workspace).
