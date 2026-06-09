# Templates (FT / ST / GT)

The HMS UI is metadata-driven. Each window is one of three template
files under `<HMS>/Forms` (legacy) or `<HMS>/FTP`, `<HMS>/STP`,
`<HMS>/GTP` (current).

| Suffix | Kind | Example |
|---|---|---|
| `.FT` | Form — single record edit window | `HR_Employee.FT` |
| `.ST` | Search pad / list window | `HR_Employee_Fast.ST` |
| `.GT` | Grid — child table embedded in a form | `HR_Salary.GT` |
| `.BND` | Binder — full-screen workspace | (no dedicated HR binder; opened via main menu) |

## HR forms (`FTP/`)

| File | Purpose |
|---|---|
| `HR_Employee.FT` | Employee master form (16 tabs). |
| `HR_Contract.ft` | Contract edit. |
| `HR_Action.FT` | Personnel action. |
| `HR_Appraisal.FT` | Appraisal. |
| `HR_Candidate.FT` | Candidate. |
| `HR_Vacation.FT` | Vacation request. |
| `HR_VacAction.FT` | Vacation action / consumption. |
| `HR_VACANCY.FT` | Vacancy. |
| `HR_Department.FT` | Department. |
| `HR_POSITION.FT` | Position. |
| `HR_PACKAGE.FT` | Salary package. |
| `HR_PRDALW.FT` | Periodic allowance. |
| `HR_VAUTH.FT` | Travel authorisation. |
| `HR_VISA.FT` | Visa. |
| `HR_Extension.FT` | Leave extension. |
| `HR_Agency.FT` | Recruitment agency. |
| `HR_Certificate.FT` | Certificate. |
| `MF_SickLeave.FT`, `MF_SickLeave2.FT` | Sick-leave certificates. |
| `PR_PayRun.FT` | Payroll run. |
| `PR_PayCode.FT` | Pay code. |

## HR list windows (`STP/`)

| File | Purpose |
|---|---|
| `HR_Overview.ST` | Manager dashboard (branch-filtered, QuickFilter on Position). |
| `HR_Employee.ST` | Standard employee search. |
| `HR_Employee_Fast.ST` | Fast picker (used everywhere a *select employee* dropdown is shown). |
| `HR_Employee_LB.ST` | Lebanon-specific layout. |
| `HR_DataEntry.ST` | Mass-edit grid. |
| `HR_Department.ST`, `HR_Position.ST`, `HR_Package.ST`, `HR_Candidate.ST` | List per master table. |
| `HR_Contract.ST`, `HR_Contract_30d.ST`, `HR_Contract_6m.ST` | Contract list + expiry-window drill-downs. |
| `HR_ContractReview.ST` | Contracts to review. |
| `HR_Action.ST`, `HR_Action_DRL.ST`, `HR_Action_STS.ST` | Actions list & drill-downs. |
| `HR_Salary_DRL.ST` | Salary drill-down (from Employee). |
| `HR_Appraisal.ST` | Appraisals list. |
| `HR_Agency.ST`, `HR_Certificate.ST` | Lookups. |
| `HR_Extension.ST`, `HR_Incentive.ST`, `HR_Passport.ST`, `HR_Residence.ST` | Per-document lists. |
| `HR_SalaryReview.ST` | Salary review batch. |
| `HR_SCC.ST` | S.C.C. status list. |
| `HR_VAUTH.ST`, `HR_VISA.ST` | Document lists. |
| `HR_VACATION_Family.ST` | Vacations with family-ticket info. |
| `HR_Package.ST`, `HR_PRDALW.ST` | Package & periodic-allowance lookups. |
| `Employer_DRL.ST` | Sponsor drill-down. |

## HR child grids (`GTP/`)

| File | Embedded in | Purpose |
|---|---|---|
| `HR_PKALW.GT` | Package & Contract | Package allowance breakdown. |
| `HR_Alw.GT` | Employee Allowances tab | Personal allowances. |
| `HR_Salary.GT` | Employee Salary tab | Salary history (read-only). |
| `HR_PosHist.GT` | Contract & Employee | Position history. |
| `HR_Contract.GT` | Employee Contracts tab | Contract list. |
| `HR_APRContract.GT` | Appraisal Re-Contracting tab | New contract preview. |
| `HR_EXTContract.GT` | Action Extension | Extension preview. |
| `HR_vacation.GT` | Employee Leaves tab | Vacation history. |
| `HR_Eleave.GT` | Vacation Educational-Leave tab | |
| `HR_Quals.GT` | Employee Qualifications tab | Diplomas & licences. |
| `HR_Childs.GT` | Employee Dependants tab | |
| `HR_Experience.GT` | Employee Experience tab | |
| `HR_Ticket.GT` | Employee Tickets tab | |
| `HR_Overtime.GT` | Employee Overtime tab | |
| `HR_Incentive.GT` | Employee Incentives tab | |
| `HR_Contract.GT` | Employee Contracts tab | |
