# Pay Codes

A **Pay Code** is one line on the pay slip. Maintain them under
**Payroll → Pay Codes** (`PR_PayCode.FT`).

## Fields

| Field | DB column | Meaning |
|---|---|---|
| Code | `Code` | Short alpha code (BAS, HOU, TRA, MOB, OT, GOSI, LOAN, …). |
| Internal Code | `iCode` | Used for system codes — never shown on slips. |
| Name | `Name` | Printed on the pay slip. |
| Type | `Type` (`PR_PCType`) | Earning / Deduction / Reimbursement / Informational. |
| Period | `Period` (`PR_PCPeriod`) | Monthly / Quarterly / Annual / One-shot. |
| Based On | `BasedOn` | Fixed / % of Basic / Formula. |
| Factor | `Factor` | % or multiplier when *Based On* needs it. |
| Account | `Account` | GL account this code posts to. |
| Class | `Class` | A / B / C grouping for summary reports. |
| TransRequired | `TransRequired` | If true, the code only appears when a corresponding HR transaction exists (e.g. *Overtime* only if `hr_employee_overtime` rows exist for the period). |
| Benefit Code | `PRP_BenefitCode` | Treated as a non-cash benefit for tax computations. |

## Tips

* Do **not delete** a code that has any `PR_RegDet` lines — older pay
  slips will lose their description. Inactivate by setting the *Status*
  flag instead.
* The order codes appear on the slip is driven by `PR_PayCode.Class +
  ID` — choose codes carefully to keep slips readable.
