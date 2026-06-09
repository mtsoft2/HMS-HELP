# Vacation Requests

## Form (`HR_Vacation.FT`)

Six tabs: **Request → Educational Leave → Supervisor Approval →
Director Approval → Actual Leave → Dependants Eligibility**.

### Request tab

| Field | Notes |
|---|---|
| Employee | Picker (`HR_Employee_Fast.ST`) |
| Vacation Type | `HR_VacationType` look-up |
| From / To | Planned dates — must not overlap an existing approved leave. |
| Days | Auto-calculated, holidays from `HR_Holiday` excluded. |
| Reason | Free text. |
| Travel Authorisation | Optional FK to `HR_VAUTH` if travelling abroad. |
| Replacement | Employee covering during the absence (optional). |

### Approval tabs

Two-level approval: **Supervisor → Director**. Each tab stamps user +
date. Status flows `Pending → SupervisorApproved → Approved → Taken →
Reversed` (lookup `HR_VacReqStatus`).

### Actual Leave tab

When the employee returns, HR fills:

* Actual From / To dates.
* Days actually taken.
* Notes (e.g. early return, extension granted).

`HR_VacReq_CALC` recomputes the employee's accrued / used / remaining
totals (`HR_EMP_VacDue / VacTaken / VacRemain`).

## Validation procedures

| SP | What it checks |
|---|---|
| `HR_DueVacations` | Drives the *Due Vacations* report and alert. |
| `HR_Vacation_Alert` | Dashboard alert: leaves starting in 7 days. |
| `HR_Vacation_Alert_Residence` | Cross-checks the employee's residence permit covers the leave + 14 days. |
| `HR_Vacation_TravelALW_Validate` | Validates travel allowance entitlement on the leave row. |
| `HR_Vacation_RPT` | Computes the figures on the *Vacation Statistics* family of reports (VacStat 1-8). |

## Reports

* **Due Vacations** — `hr_DueVacations.rpt`
* **Vacation Stats** — 8 ready-to-print pivots (`HR_VacSTAT.rpt` …
  `HR_VacSTAT4.rpt` and `hr_vacstat7/8.ini`).
