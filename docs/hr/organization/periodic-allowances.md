# Periodic Allowances

Periodic allowances (`HR_PRDALW`) are recurring monthly amounts that
are paid *outside* the salary package — typically *Mobile reimbursement*,
*Schooling top-up*, *Housing increment*, *Acting allowance*, …

## Form (`HR_PRDALW.FT`)

| Field | DB column |
|---|---|
| Employee | `EmployeeID` (picker `HR_Employee_Fast.ST`) |
| Allowance Type | `Type` (FK to `HR_PRDALWType`) |
| Amount | money |
| Frequency | Monthly / Quarterly / Yearly |
| Start Date / End Date | activity window |
| Active | yes/no |
| Banner | `HR_PRDALW_BANNER` SP populates the header |

## How payroll consumes them

`HR_MonthlySalaries` includes every `HR_PRDALW` row whose period overlaps
the pay-run period and whose Active flag = 1. The amount lands on
`PR_RegDet` under the matching pay code.

## Tip

Use `HR_PKALW_ORG_Add` (admin helper) to bulk-add the same
allowance to every employee in a department — e.g. when the board
approves a *Critical-care allowance* for all ICU nurses.
