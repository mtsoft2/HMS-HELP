# Loans

Staff loans are managed in `PR_Loan` and repaid automatically through
payroll.

## Fields

| Field | Meaning |
|---|---|
| Employee | FK to `HR_Employee`. |
| Loan Type | `PR_LoanType` (Personal / Emergency / Housing / Car / Education). |
| Status | `PR_LoanStatus` (Requested / Approved / Active / Paid / Cancelled). |
| Amount | Principal. |
| Instalments | Number of monthly repayments. |
| Start Period | First payroll period to deduct. |
| Repayment / month | Computed, can be overridden. |
| Outstanding | Recomputed after each payroll run. |

## Workflow

1. HR creates a loan row, status *Requested*.
2. Finance / Director approves → status *Active*.
3. Each Pay Run reads active loans (`PR_Loan_Load`), computes the
   instalment, inserts a *LOAN* `PR_RegDet` line, and inserts a row
   into `PR_PKT_Loan` history.
4. When *Outstanding = 0* the loan is auto-marked *Paid*.
5. The dashboard `PR_Loan_Alert` flags loans whose deduction failed
   because the employee's net pay would go below zero.

## Banner

`PR_Loan_BANNER` shows: employee, principal, outstanding, % paid,
months remaining.
