# Termination

A **Termination** action ends the employment relationship and triggers
the final EOS settlement.

## Termination reasons (Tab 2 flags)

| Flag | Meaning |
|---|---|
| `TERM_Resignation` | Employee resigned voluntarily. |
| `TERM_ReContractNotOffered` | Hospital decided not to renew. |
| `TERM_ReContractNotWished` | Employee declined to renew. |
| `TERM_MedicalReason` | Medical incapacity. |
| `TERM_Article80` | Saudi Labour Law Art. 80 — termination for cause. |
| `TERM_DuringProbation` | Within the probation period — reduced entitlements. |
| `TERM_SCCFailed` | Failure to obtain / renew the Saudi Council certificate. |
| `TERM_Others` | Free-text reason. |
| `HAC_TermReason` | FK to `HR_TermReason` look-up (free taxonomy you maintain). |

## Entitlements block

Filled by the HR officer before the action is submitted:

| Field | Meaning |
|---|---|
| `TERM_ENT_AccruedLeaves` | Unused leave days to pay out. |
| `TERM_ENT_TotalLeaves` | Total leave balance (informational). |
| `TERM_ENT_ServiceAward_TotalPeriod` / `_CompletedTerms` | Which formula to use for end-of-service award. |
| `TERM_ENT_Tickets` | Pending tickets to cash out. |
| `TERM_ENT_DaysPay_Emp` | Days of salary owed to employee. |
| `TERM_ENT_DaysPay_Hosp` | Days the *employee* owes the hospital (notice not served). |
| `HAC_TicketToDeduct` | Cost of un-served-notice ticket. |
| `HAC_VisaToDeduct` | Visa cost to deduct if employee resigns before threshold. |
| `HAC_LastWorkingDay` | The last day the employee physically works. |
| `HAC_TermLetterDate` | When the termination letter was issued. |

## On apply

When the *Hospital Director* approval is stamped, `HR_Action_Apply`:

1. Sets `HR_Employee.Resigned = 1`, `Date_of_resignation = HAC_LastWorkingDay`.
2. Closes the active contract (`HR_contract.Status = 'T'`,
   `CT_Effective_End_Date = HAC_LastWorkingDay`).
3. Inserts a `PR_RegDet` settlement line in the next pay run (one line
   per entitlement: accrued leave, tickets, EOS, notice).
4. Releases the **Vacancy** (`HR_Vacancy.HVC_Status` → *Open*) unless
   `HVC_Transient = 1`.
5. Locks all `HR_Salary` rows for this employee.

## Reports

* **HR Termination** (`HR_Termination.ini`).
* **HR Turnover** (`HR_Turnover.ini`).
