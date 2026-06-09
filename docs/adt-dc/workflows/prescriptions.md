# Prescriptions

Two toolbar buttons handle prescribing: **New Prescription** to write
one, **Prescriptions History** to review what was prescribed before.

## New Prescription

Click **New Prescription**.

* The drug picker shows the clinic's standard formulary first
  (configurable). Type to search by trade name, generic name, or class.
* Pick **strength**, **frequency**, **duration**, **route**.
* Add as many drug lines as needed.
* Save.

### Safety checks that run automatically

* **Allergy check** — warns if any of the patient's recorded allergies
  match the active ingredient.
* **Interaction check** — warns if any prescribed drug interacts with
  the patient's currently-active medications.
* **Pregnancy / paediatric** — warns if the drug is contraindicated
  for the patient's age or pregnancy status.
* **Dose check** — warns if the daily dose is outside the typical
  range for the patient's weight.

You can override any warning with a note, but the override is recorded.

### Printing & sending

* **Print** produces the paper prescription.
* If the clinic has an integrated pharmacy, the prescription is also
  pushed electronically (pharmacy sees it on their queue immediately).

## Prescriptions History

Click **Prescriptions History** to see every prescription this patient
has ever received — from any branch, any dentist, any date.

Columns: date, dentist, drugs (count + first one), status (Issued,
Refilled, Cancelled), printed Yes/No.

Click any row to open the full prescription, or click **Refill** to
copy it forward into a new prescription with today's date.
