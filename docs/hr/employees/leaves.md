# Leaves & Tickets (Tabs 7 + 8)

## Leaves tab

The **Leaves** tab shows the employee's lifetime leave ledger
(`hr_employee_vacation`).

| Column | Meaning |
|---|---|
| Vacation Type | Annual, Sick, Educational, Hajj, Compassionate, Unpaid, … (look-up `HR_VacationType`). |
| From / To | The leave window. |
| Days | Calendar days; weekends/holidays excluded via `HR_Holiday`. |
| Status | Pending → Approved → Taken → Reversed. |
| Travel Auth | FK to `HR_VAUTH` if the employee is travelling abroad. |
| Actual Leave | Real return date — may differ from planned. |

The summary box on the right shows the formula:

> **Accrued + Earned − Used = Total Days**

— a live read-out of `HR_EMP_VacDue`, `HR_EMP_VacTaken`,
`HR_EMP_VacRemain`. It is recomputed by `HR_SP_VAC_CALC` whenever the
form opens.

## Tickets tab

`hr_employee_ticket` — one row per yearly ticket the employee is owed.

| Column | Meaning |
|---|---|
| Year | Entitlement year. |
| Type | Employee / Family. |
| Issued | Yes if a ticket has been issued. |
| Amount | Cash value (when paid as cash-in-lieu). |
| Vacation | FK to the `hr_employee_vacation` row the ticket was used on. |

## Holidays

`HR_Holiday` stores official paid holidays. The day-count for vacation
requests uses these to skip weekends / public holidays. Maintain it
once a year under **Data Setup → HR → Holidays**.

## Earned leaves (Tab 15)

A read-only view that runs `HR_ACTION_ACCRUED_LEAVE_CALC` to show:

```
(Contract Days − Unpaid Leaves >14 days − Holidays) / 365 × Annual Leave = Accrued Days
```
