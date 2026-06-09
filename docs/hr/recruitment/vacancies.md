# Vacancies

A **Vacancy** is an approved opening — branch + department + position +
requirements — that recruitment will fill.

## Vacancy form (`HR_VACANCY.FT`)

Four tabs: **Information**, **History**, **Actions**, **Note**.

### Information tab

| Field | DB column |
|---|---|
| Code | `HVC_CODE` (auto-incremented from `HVC_CODE_TMP`) |
| Name (EN / AR) | `Name`, `HVC_Name_A` |
| Branch / Department / Position | `Branch`, `Department`, `Position` |
| Count | `Count` — number of identical seats this vacancy represents |
| Required Gender | `HVC_Gender` |
| Required Nationality | `HVC_Nationality` |
| Salary | `HVC_Salary` (target salary) |
| Recruitment Source | `HVC_RecSource` |
| Classification | `HVC_CLASS` (Critical / Standard / Replacement) |
| Status | `HVC_Status` (Open / Filled / On Hold / Cancelled) |
| ETA | `HVC_ETA` — expected fill date |
| Target Vacancy | `HVC_TargetVacancy` — used when one vacancy is being replaced by another |
| Transient | `HVC_Transient` — a temporary vacancy auto-created by a transfer |

## Transient vacancies

When you transfer an employee, the *Source* position momentarily has an
employee leaving and the *Destination* position has an employee
arriving. To keep headcount accounting clean, HMS auto-creates a
**transient** vacancy on each side. Three SPs manage them:

* `hr_Vacancy_Create_Transient` — create.
* `hr_Vacancy_Transient_Process` — link to the originating action.
* `hr_Vacancy_Transient_Process_All` — nightly sweep.

## Vacancy load

`HR_Vacancy_Load` is the SP that powers vacancy pickers everywhere
(Employee form, Candidate form, Personnel Action transfer tab). It
excludes filled / cancelled vacancies.

## Reports

* **HR Vacancies** (`HR_Vacancies.ini` → `HR_Recruitment.rpt`) — open
  vacancies grouped by branch & department.
* **HR Recruitment** — same, with pipeline counts of candidates per
  vacancy.
