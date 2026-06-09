# Transfer

A **Transfer** moves an employee from one *Branch + Department +
Vacancy* to another, without changing salary.

## Fields (Tab 4)

| Field | Source / Destination |
|---|---|
| `HRTR_S_Branch` | Source branch |
| `HRTR_S_Department` | Source department |
| `HRTR_S_Vacancy` | Source vacancy |
| `HRTR_S_Main_Number` | Source employee badge number (audit) |
| `HRTR_D_Branch` | Destination branch |
| `HRTR_D_Department` | Destination department |
| `HRTR_D_Vacancy` | Destination vacancy |
| `HRTR_D_Main_Number` | Destination badge number |

## On apply

`HR_Action_TRANS_Apply`:

1. Updates `HR_Employee.HR_EMP_Branch / _Department / _VACANCY`.
2. Inserts a row in `HR_PosHist` recording the move.
3. Creates a **transient** source vacancy via
   `hr_Vacancy_Create_Transient` if the source vacancy was the only
   one of its kind — guarantees headcount accounting balances.
4. Marks destination vacancy as filled.
5. Stamps `HAC_Action_Applied = 1`.

## Bulk historical import

Use `HR_Action_HIST_Apply_All` to reapply every historical transfer
when you migrate from a legacy HR system (one-shot batch tool).
