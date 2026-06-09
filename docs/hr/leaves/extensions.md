# Vacation Extensions

`HR_Extension.FT` is used when an employee on leave requests to
**extend** the leave beyond the originally approved To-date.

## Workflow

1. Open the *active* vacation row from the employee's Leaves tab.
2. Click **Actions → New Extension**.
3. Fill the new To-date, reason, and any additional unpaid days.
4. Supervisor / Director approval, then `HR_EXTContract` applies the
   change — `hr_employee_vacation` row is updated and accrual is
   recomputed via `HR_VacReq_REQUEST_CALC`.

## Validation

* The extension cannot push the leave end-date past the **contract
  end-date** (unless the contract is also extended via
  `HR_Contract_Extend`).
* The extension is rejected if the employee's residence expires
  before the new end-date.
