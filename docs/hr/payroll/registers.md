# Registers & Pay Slips

## `PR_Register`

The register is the **header** of a pay batch.

| Column | Meaning |
|---|---|
| `Description` | Free-text title (e.g. *June 2026 – Riyadh*). |
| `Period`, `PeriodStart` | Pay period. |
| `Date` | Generation date. |
| `Total`, `TotalPay`, `TotalDeduction` | Sums. |
| `Vglbatch` | GL batch ID once posted. |
| `GenSource` | `M` = monthly, `S` = settlement, `A` = adjustment, `T` = termination. |
| `PRR_Branch`, `PRR_Department` | Filters used during generation. |
| `PRR_Exlbranch`, `PRR_EXLPackage` | Exclusion filters. |
| `PRR_EOS_STATUS`, `PRR_VAC_STATUS` | Include / exclude employees on EOS / on vacation. |
| `MSG` | Generation log. |

## `PR_RegDet`

One row per employee × pay code. Columns include `Employee`, `PayCode`,
`Amount`, `Note` (e.g. *Proration: 18/30 days*).

## Pay slip report

`PR_PaySlip.rpt` (with template `PR_PaySlip.ini`) — the printable
slip. Layout sections:

* Header — employee name, number, department, period.
* Earnings block — every `Type = Earning` pay code.
* Deductions block — every `Type = Deduction` pay code.
* Net pay — `TotalPay − TotalDeduction`.
* Footer — payment method (bank), bank IBAN, sign-off lines.

The slip uses the employee's `HR_EMP_NAME_A` (Arabic) when the *Print
in Arabic* parameter is set.

## Register transactions report

`PR_Register_Trans.rpt` — flat list of every `PR_RegDet` row for the
register, sortable by department / pay code. Useful for audit and GL
reconciliation.
