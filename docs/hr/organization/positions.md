# Positions

`HR_POSITION` is the catalogue of job titles available in the
hospital.

## Form (`HR_POSITION.FT`)

| Field | DB column | Notes |
|---|---|---|
| Code | `HRPOS_CODE` | Short code printed on staffing-schedule reports. |
| Name (EN) | `Name` | Required. |
| Name (AR) | `HRPOS_Name_Arabic` | |
| Category | `HRPOS_Category` | FK to `HR_POSCATEG` (Medical / Nursing / Tech / Admin / Support). |
| Vacation Days per Year | `VacDaysPerYear` | The factory annual leave for any contract created on this position. |
| ID2 | `ID2` | Secondary code. |

## Where it appears

* On every **Employee** (`HR_EMP_Position`) and **Vacancy**
  (`HR_Vacancy.Position`).
* On every **Candidate** (`HR_Candidate.Position`).
* On the **Staffing Schedule** report (`HR_StaffingSchedule.rpt`).
* The **Saudisation** report groups by `HRPOS_Category` to compute
  national / non-national ratios.
