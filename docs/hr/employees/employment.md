# Employment (Tab 2)

The **Employment** tab is what links a person to a job inside the
hospital.

## Fields

| Field | DB column | Purpose |
|---|---|---|
| Employee Number | `Main_Number` | The number printed on the ID badge. Auto-allocated via the `HR_Employee` counter; can be overridden. |
| Previous Number | `Previous_Number` | Legacy code from your previous HR system, for cross-reference. |
| Accounting Number | `Accounting_Number` | The supplier code in the GL; used by Payroll to post salary to the correct vendor. |
| Insurance Number | `Insurance_Number` | GOSI / national insurance reference. |
| Attendance Card | `Attendance_Card_Number` | Card / badge number — fed by the time-and-attendance device. |
| Branch | `HR_EMP_Branch` | Required. Drives all branch-filtered reports. |
| Department | `HR_EMP_Department` | Required. Drives the cost-centre on payroll. |
| Position | `HR_EMP_Position` | Required. Determines default vacation / package. |
| Vacancy | `HR_EMP_VACANCY` | The specific opening this employee occupies. |
| Status | `Status` | Active / On Leave / Suspended / Terminated. |
| Category | `Category` | Free-form grouping (e.g. *Clinical*, *Admin*, *Support*). |

## Behaviour

* Changing **Branch + Department + Position** does **not** automatically
  create a `HR_PosHist` history row — use the **Transfer** personnel
  action (see [Transfer](../actions/transfer.md)) so the change is
  audited.
* The **Vacancy** field is validated against `HR_Vacancy`. An employee
  cannot occupy a vacancy that is inactive or already filled — use the
  **Clear Vacancy** action (`HR_Employee_Clear_Vacancy`) to release it.
