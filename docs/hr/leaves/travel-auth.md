# Travel Authorisation

`HR_VAUTH.FT` records the authorisation for an employee to travel
abroad — needed for **re-entry visa**, **ticket entitlement** and
**residence-permit validity** checks.

## Key fields

* Employee, From / To dates.
* Destination country / city.
* Re-entry validity date (must be > To).
* Ticket entitlement: cash-in-lieu or in-kind (employee / family).
* Status (`HR_VAUTHStatus`): Pending / Approved / Cancelled / Used.

## Linked actions

* `HR_VacAction` records the *VacAction* event when the auth is used.
* `HR_VacAction_Apply` consumes the ticket entitlement from
  `hr_employee_ticket`.
* `HR_VacAction_Submit` / `HR_VacAction_AutoApply` drive the approval
  workflow.

## Reports

* **Employee Tickets** (`hr_EmployeeTickets.rpt`) — outstanding ticket
  ledger.
* **Expiring Documents** (`hr_ExpiringDocs.rpt`) includes residence
  expiry vs travel-auth dates.
