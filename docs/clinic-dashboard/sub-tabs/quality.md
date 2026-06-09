# Quality

Outcomes, incidents, and patient satisfaction — the soft side of
clinical operations.

## Cards

### Readmission · 30-day

A radial / percentage card showing the share of discharged patients
who came back as inpatients within 30 days.

* The lower, the better.
* A short caption explains the formula.
* Click the card → opens the list of readmitted patients.

### Satisfaction proxy · 90d

A derived satisfaction score using the **attended / no-show /
cancelled mix** as a proxy for whether the clinic is delivering what
patients showed up for.

* A higher attended rate and a lower no-show + cancel rate → higher
  proxy score.
* The card carries the explanatory tag *"Built from attended /
  no-show / cancelled mix"* so users know what they are looking at.
* **Attendance** breakdown shown alongside.

### Quality alerts

A list of currently-open quality alerts:

| Column | Meaning |
|---|---|
| **Title** | Short description. |
| **Severity** | High / Medium / Low. |
| **Age** | How long the alert has been open. |
| **Status** | Open / Acknowledged / Resolved. |

Click **Open <alert title>** → opens the alert detail.

### Incidents · last 90 days

The clinical-incident register for the last 90 days:

| Column | Meaning |
|---|---|
| **Date** | When the incident happened. |
| **Severity** | Severity rating. |
| **Category** | Incident category (Medication, Fall, Equipment, …). |
| **Type** | Sub-type within the category. |
| **Subject** | Short title. |
| **Tracking #** | The incident reference number. |
| **Stage** | Where it is in the workflow (Reported, Under review, Closed). |

Click **Open incident #<id>** → opens the incident record.

Plus a top-line **Open incidents** counter.

## What you do with it

* **Weekly quality huddle** — Readmission rate + Open incidents +
  Quality alerts is the agenda.
* **Trend watch** — sudden change in the satisfaction proxy is your
  first leading indicator that something is off (often before patient
  complaints reach you).
* **Incident triage** — sort by severity, click into anything red.

➡ Continue to **[CRM](crm.md)**.
