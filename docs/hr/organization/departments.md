# Departments

`HR_Department` is the cost-centre dimension of the hospital.

## Form (`HR_Department.FT`)

| Field | DB column | Notes |
|---|---|---|
| Code | `HRD_Code` | Short alpha-numeric code (used on pay slips). |
| Name (EN) | `Name` | Required. |
| Name (AR) | `HRD_Name_Arabic` | |
| Cost Centre | `HRD_CstCtr` | FK to the GL cost-centre table; drives the salary GL line. |
| ID2 | `ID2` | Secondary code for legacy interfaces. |

## Where it appears

* Mandatory on every **Employee** (`HR_EMP_Department`).
* Mandatory on every **Vacancy** (`HR_Vacancy.Department`).
* Selectable on **Pay Runs** (`PR_Register.PRR_Department`) so payroll
  can be run department-by-department.
* Reported on every HR roster (by-department staffing, by-department
  salary cost, etc.).

## Tips

* Do not delete a department once an employee has been linked to it —
  inactivate it instead (add an `Inactive` lookup row in the local
  status setup).
* The **Cost Centre** value is read by `HR_MonthlySalaries` when the
  pay run posts to GL — make sure it matches an existing GL CC, or the
  journal will fail with a *missing CC* warning.
