# End of Service (Tab 11)

The **End of Service** tab shows the EOS settlement that will be paid
if the employee leaves today. The figures are *computed live* and
refreshed every time you open the form.

## Fields

| Field | DB column |
|---|---|
| End-of-Service Type | `HR_EMP_EOS_Type` (`HR_EOS` look-up) |
| Last working day | `HR_EMP_EOS_LastDay` |
| Basic salary used | `HR_EMP_EOS_BasicSalary` |
| Years of service | `HR_EMP_EOS_Years` |
| Months per year of service | `HR_EMP_EOS_MonthForYear` (Saudi labour law: ½ month for the first 5 years, full month afterwards) |
| EOS amount | `HR_EMP_EOS_Amount` |
| Service-Award difference | `ServiceAward_Difference` (manual top-up) |

## Procedures

| Procedure | When |
|---|---|
| `HR_SP_EOS_CALC` | Live recompute on form open. |
| `HR_EOS_DIF_CALC` | Compute the difference between contract-period award and accumulated reserve for a single employee. |
| `HR_EOS_DIF_CALC_ALL` | Same, batch for every active employee. Run nightly. |

## Termination flow

The EOS amount is **finalised** when a *Termination* personnel action is
applied:

1. Open the employee → **Actions** tab → **New** → Type *Termination*.
2. Fill in the *Termination* sub-tab (resignation, end-of-contract,
   Article 80, medical, etc.).
3. Fill the **Entitlements** lines (`TERM_ENT_AccruedLeaves`,
   `TERM_ENT_DaysPay_Emp`, `TERM_ENT_Tickets`, …).
4. Send for **three-level approval** (Department Head → Project
   Director → Hospital Director).
5. On final approval `HR_Action_Apply` runs:
   * marks `HR_Employee.Resigned = 1`
   * closes the active contract
   * locks `HR_Salary` rows
   * generates the final pay-slip line in the next Pay Run.
