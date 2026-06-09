# Appraisals

Appraisals (`HR_Appraisal.FT`) are the formal performance review
issued at the end of each contract term. The outcome drives
**Re-contracting** and the **annual raise**.

## Form tabs

1. **Appraisal** — scoring.
2. **Re-Contracting** — the decision to renew / extend / not renew.

## Scoring fields

| Field | Lookup | Notes |
|---|---|---|
| Job Knowledge | `HR_APRFactor` | A / B / C / D / E rating. |
| Work Quality | `HR_APRFactor` | |
| Work Quantity | `HR_APRFactor` | |
| Overall Appraisal | `HR_APROverall` | Computed from the three factors (configurable in `HR_APRFactor.Weight`). |
| Appraisal Status | `HR_APRStatus` | Draft / Submitted / Approved / Cancelled. |
| Raise (amount) | `Raise` | Approved raise to be added to the next `HR_Salary` row. |
| Recontracting Status | `HR_RecontractingStatus` | Renew / Extend / Do not renew. |
| Employee Approval | `HR_EmpApproval` | Whether the employee has counter-signed. |

## On submit

`HR_Appraisal_Apply` runs:

1. If **Renew** → fires `HR_APRContract` to insert a new contract.
2. If **Extend** → fires `HR_Contract_Extend` to push out the end date.
3. If a **Raise** is approved → fires `HR_APRS_Salary_Add` to insert
   a new `HR_Salary` row with `SL_Appraisal = <appraisal ID>`.
4. Sets `APRS_Applied = 1`.

`HR_APRS_Salary_FIX` is a nightly tidy-up SP that locks the raise
rows once their effective date is reached.

## Banner

`HR_Appraisal_BANNER` shows: employee, current contract end, scoring
summary, recommended raise.
