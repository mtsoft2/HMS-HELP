# Alerts & Banners

Every HR form has a **Banner** (the static green strip at the top)
and one or more **Alerts** (scrolling marquee strips below).

## Banner procedures

| Form | Banner SP |
|---|---|
| Employee | `HR_EMPLOYEE_BANNER` |
| Contract | `HR_Contract_BANNER` |
| Personnel Action | `HR_Action_BANNER` |
| Appraisal | `HR_Appraisal_BANNER` |
| Candidate | `HR_Candidate_BANNER` |
| Vacation | `HR_VACATION_BANNER` |
| VacAction | `HR_VacAction_BANNER` |
| Visa | `HR_VISA_BANNER` |
| Travel Auth | `HR_VAUTH_BANNER` |
| Periodic Allowance | `HR_PRDALW_BANNER` |
| Agency | `HR_Agency_BANNER` |

A banner SP returns a small result-set the HMS framework renders as a
read-only header (employee photo + name + key facts).

## Alert procedures

Alerts pop on the dashboard *and* on the employee form when something
needs attention.

| SP | Triggers when |
|---|---|
| `HR_EMP_Alert` | Any document on this employee expires within 30 days. |
| `HR_EMP_Note_Alert` | Free-text employee note flagged as alert. |
| `HR_EMP_Note_Alert_APRS` | Appraisal-related employee note. |
| `HR_Vacation_Alert` | A leave is starting within 7 days. |
| `HR_Vacation_Alert_Residence` | Leave cross-checks residence validity. |
| `HR_Action_Alert` | A personnel action is pending **your** approval. |
| `HR_Action_ContractPending_Alert` | A contract renewal action is pending. |
| `PR_Loan_Alert` | A loan instalment failed because net pay would go negative. |
| `HR_ExpiringDocs` | Drives the *Expiring Documents* drill-down list. |

## How alerts are configured

Each form's `.FT` file has one or more `[Alert]`, `[Alert2]`, …
sections specifying:

* `Show` — on/off.
* `Procedure` — which SP to call.
* `Count` — how many rows to scroll.
* `Every` — seconds between scroll steps.
* `Duration` — seconds each row is visible.
* `Width` — px width of the strip.
