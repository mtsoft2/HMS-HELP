# Patient Toolbox & Fingerprint

## Patient Toolbox

The **Patient Toolbox** is the slim panel on the right edge of the
Dental Clinic Front Desk. It shows context-aware shortcuts for the
patient currently in the banner — the buttons that appear depend on
what the patient has on file.

Common shortcuts:

* **Allergies** — pops the allergy list (red highlight if any).
* **Active alerts** — any clinical or administrative alert flagged
  on the patient.
* **Attachments** — upload / view ID copy, insurance card scan,
  consent forms, X-rays brought from elsewhere.
* **Account balance** — outstanding amount across all branches.
* **Enrol Fingerprint** — capture a fingerprint for a patient who has
  none on file (or add a second / third finger).
* **Last visit** — jumps straight to the most recent visit's
  procedures and notes.
* **Insurance eligibility check** — pings the payer's API to confirm
  the card is still valid before the visit starts.

The administrator decides which buttons appear and in what order, per
clinic profile.

## Fingerprint reader

The front desk supports any reader that exposes a standard biometric
service.

### One-time setup

1. Plug the reader into the workstation.
2. From the front desk, click **Patient Toolbox → Test Reader** — the
   panel should flash green when the reader is reachable.
3. If the reader is not detected, install the vendor driver and the
   biometric service from the IT bundle, restart the browser, and
   re-test.

### Enrolling a finger

1. Select the patient (any way — picker, ID number).
2. Click **Patient Toolbox → Enrol Fingerprint**.
3. Pick the finger from the on-screen hand.
4. Place the finger on the reader. The capture takes three reads to
   build a template.
5. Save. The finger is now linked to that patient across every branch.

### Day-to-day use

The receptionist clicks **Finger Print Scan** on the toolbar and asks
the patient to place a finger. Match → banner fills. No match → fall
back to **Select Patient**.

### Tips

* Wipe the reader between patients.
* Enrol **two** fingers per patient (typically both index fingers) — if
  one is bandaged or injured the other still works.
* The biometric template is hashed; the raw print is never stored.
