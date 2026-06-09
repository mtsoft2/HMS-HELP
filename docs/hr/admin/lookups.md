# Lookup Tables

All HR look-ups are maintained under **Data Setup → HR**. They are
ordinary tables that the picker dropdowns read from at form-open time
(no service restart needed).

## Master look-ups

| Table | Used by |
|---|---|
| `HR_Branch` | Employee, Vacancy, Pay Run filter |
| `HR_Department` | Employee, Vacancy, Pay Run filter |
| `HR_POSITION` | Employee, Vacancy, Candidate |
| `HR_POSCATEG` | Position category (Saudisation report) |
| `HR_Package` | Contract |
| `HR_ALWTYPE` | Package allowance type |
| `HR_PRDALWType` | Periodic allowance type |
| `HR_IncentiveType` | Incentive type |
| `HR_VacationType` | Vacation request |
| `HR_VACClass` | Vacancy classification |
| `HR_RecSource` | Recruitment source |
| `HR_RepFormat` | Report format selector |
| `HR_ValueType` | Value-type look-up for action fields |
| `HR_Holiday` | Public holidays (vacation day-count) |
| `HR_Category` | Free employee grouping (Clinical / Admin / Support) |
| `HR_EntryPort` | Port of entry (immigration) |
| `HR_Destination` | Country of travel (TravelAuth) |
| `HR_VisaType` | Visa types |
| `HR_TermReason` | Termination reason taxonomy |
| `HR_RecontractingStatus` | Re-contract decision |
| `HR_EOS` | EOS type |
| `HR_LU_Vacations` | Vacation reason library |
| `HR_LU_Deductions` | Deduction library |
| `HR_Agency` | Recruitment agencies |

## Status look-ups (small code tables)

| Table | Code values |
|---|---|
| `HR_Status` | Employee status (A/L/S/T) |
| `HR_Contract_Status` | A / E / T / R / X |
| `HR_Vacancy_Status` | O / F / H / C |
| `HR_CandidateStatus` | N / S / I / O / R / H |
| `HR_APRStatus` | Draft / Submitted / Approved / Cancelled |
| `HR_APROverall` | A / B / C / D / E ratings |
| `HR_APRFactor` | Per-factor rating with weight |
| `HR_VAUTHStatus`, `HR_VISAStatus` | Document workflow |
| `HR_VACActionStatus`, `HR_VACActionStage`, `HR_VACActionType` | Vacation action workflow |
| `HR_VacReqStatus` | Vacation request flow |
| `PYR_Stage`, `PYR_Status` | Payroll cycle status |

## Tip

Most look-ups have a `Name_A` Arabic column — fill it in if you print
slips or contracts in Arabic, otherwise the English value is used as a
fall-back.
