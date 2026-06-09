# Salary & Allowances (Tabs 5 + 6)

## Salary history (`HR_Salary`)

Every time the basic salary changes — through a new contract, a
personnel action, or an appraisal raise — a row is inserted into
`HR_Salary`. The tab shows the full timeline.

| Column | Meaning |
|---|---|
| Effective Date | When the new salary starts. |
| Basic Salary | Base amount. |
| Housing / Transportation / Mobile | Standard allowances from the package. |
| Additional Allowances | Free amount. |
| SL_Appraisal | FK to the appraisal that triggered the raise (if any). |
| SL_Action | FK to the personnel action that triggered the change. |
| SL_Fixed | If checked, the row is locked and Payroll uses **exactly** these amounts (no further proration). |
| SL_InActive | Hide from active calculations (kept for audit). |

Stored procedures that write into `HR_Salary`:

* `HR_ACTION_Salary_Add` — fired by *Promotion / Demotion*.
* `HR_APRS_Salary_Add` — fired by an appraisal raise.
* `HR_APRS_Salary_FIX` — locks the row after the appraisal cycle closes.

## Allowances grids

| Tab | Grid file | Table | Purpose |
|---|---|---|---|
| Allowances | `HR_Alw.GT` | `hr_employee_allawence` | Personal one-off or recurring add-ons. |
| Package allowances | `HR_PKALW.GT` | `HR_PKALW` | Standard allowance breakdown from the **Package**. |
| Periodic | `HR_PRDALW.GT` | `HR_PRDALW` | Recurring monthly allowances (Mobile top-up, schooling). Loaded into Payroll automatically. |
| Incentives | `HR_Incentive.GT` | `HR_Incentive` | Performance / spot bonuses. Linked to `HR_IncentiveType`. |

## How Payroll consumes these tables

When you click **Generate** on a Pay Run, the procedure
`HR_MonthlySalaries` does roughly the following for every employee in
the selected branch / department:

1. Read the current `HR_Salary` row whose Effective Date ≤ Period End.
2. Add every active `hr_employee_allawence` row (one-shot if start/end
   matches the period; recurring otherwise).
3. Add every active `HR_PRDALW` row.
4. Add the current month's `HR_Incentive` rows.
5. Subtract deductions (`HR_Deductions`, loan repayments
   `PR_Loan_Payments`).
6. Write one line per pay code into `PR_RegDet` and update the totals
   on `PR_Register`.
