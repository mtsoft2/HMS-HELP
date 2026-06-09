# Alerts

Thresholds that drive the **flags on the event info panel** and the
**icons on appointment cards**. Tune these once for the clinic and
every receptionist sees consistent warnings.

## Wait threshold

How long a patient is considered "waiting" before the scheduler shows
a warning band. Typical values: 15 – 20 minutes.

If a patient has status **Arrived** and the configured wait threshold
elapses without moving to **In-Service**, the cell gets a warning band
and the patient appears on the front-desk *patients waiting*
dashboard.

## No-show banding

Patients with a history of missing appointments get a coloured band
that scales with the count. Configure the bands:

| Band | Default range | Meaning |
|---|---|---|
| **None** | 0 missed | No flag. |
| **Yellow** | 1 – 2 | Cautionary — receptionist may want to send a reminder the day before. |
| **Orange** | 3 – 4 | Strong — consider asking for confirmation. |
| **Red** | 5+ | High-risk — clinic policy may require a deposit. |

Edit the cut-off counts to match the clinic's policy.

## Pending balance threshold

The amount above which an outstanding patient balance triggers the
*Pending balance over threshold* flag on the event info panel. Set this
to the value where the receptionist should hand the patient to the
cashier **before** the visit (rather than after).

The flag also adds a small icon on the appointment card so the
receptionist sees it without opening the panel.

## How alerts and flags work together

| Source | Where it shows |
|---|---|
| **Allergy** flag | Pulled from the patient's chart. Card icon + panel banner. |
| **VIP** flag | Patient profile flag. Card icon + panel banner. |
| **Pending balance** | Set by the threshold here. Card icon + panel banner. |
| **No-show band** | Computed from past appointments + bands above. Panel band only. |
| **Wait threshold** | Computed from arrival time + threshold above. Card band only. |
| **Procedure has instructions** | Pulled from the booked procedure (if it carries prep instructions). Panel banner only. |
