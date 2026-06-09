# Promotion / Demotion

A **Promotion / Demotion** action changes the employee's title and/or
basic salary.

## Fields (Tab 3)

| Field | Meaning |
|---|---|
| `DPROM_NewTitle` | New job title (free-text or from `HR_POSITION`). |
| `DPROM_NewVacancy` | New vacancy the employee will occupy. |
| `DPROM_Department` | Optional department change. |
| `Cur_Basic` | Current basic salary (read-only, copied from contract). |
| `New_Basic` | New basic salary the HR officer is proposing. |
| `Recom_IncDec` | Calculated absolute increase / decrease. |
| `Recom_IncDecPerc` | Calculated %. |

## On apply

`HR_Action_PROMOD_Apply` runs:

1. Inserts a new row in `HR_Salary` with `SL_Action = <this action ID>`
   and `Effective_date = HAC_Effective_Date`.
2. Updates `HR_Employee.HR_EMP_Position` and the contract title.
3. If a new vacancy was supplied, occupies it and frees the previous
   one (transient vacancies are created if branch / dept changes — see
   [Vacancies](../recruitment/vacancies.md)).
4. Stamps `HAC_Action_Applied = 1`.

## Reversal

If a promotion is later reversed, create a **new** action with
`HAC_ReverseAction = <ID of original>` and select *Demotion*. The SP
`HR_Action_PROMOD_Apply` detects the reversal flag, restores the
previous salary row and inactivates the original raise.
