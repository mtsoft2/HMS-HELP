# Data Model

Reference list of every HR / Payroll table shipped with HMS. All IDs
are `int`. Every editable table has a matching **`HR_PKT_*` ghost
table** (PKT = Pending Keyed Transaction) which holds the user's
unsaved buffer; on **Save** the framework copies the PKT row into the
live table.

## Core master tables

| Table | Purpose |
|---|---|
| `HR_Employee` | Master employee record. |
| `HR_PKT_Employee` | Edit buffer. |
| `HR_Employee_child` | Dependants (spouse + children). |
| `HR_EMPLOYEE_Experience` | Prior employment history. |
| `hr_employee_qualification` | Diplomas and certificates. |
| `hr_employee_vacation` | Vacation ledger. |
| `hr_employee_ticket` | Ticket entitlement & usage. |
| `hr_employee_overtime` | Overtime hours by date. |
| `hr_employee_allawence` | Personal allowances. |
| `HR_Salary` | Salary timeline (one row per change). |
| `HR_PKALW` | Package allowance breakdown. |
| `HR_PRDALW` | Periodic monthly allowances. |
| `HR_Incentive` | Performance / spot bonuses. |

## Organisation

| Table | Purpose |
|---|---|
| `HR_Branch` | Branches / sites. |
| `HR_Department` | Departments (cost-centres). |
| `HR_POSITION` | Job titles. |
| `HR_POSCATEG` | Position category. |
| `HR_Category` | Generic employee grouping. |
| `HR_Package` | Salary package template. |
| `HR_PosHist` | Position history (audit). |

## Recruitment

| Table | Purpose |
|---|---|
| `HR_Vacancy` | Open positions. |
| `HR_Candidate` | Applicants. |
| `HR_Agency` | Recruitment agencies. |

## Contracts & actions

| Table | Purpose |
|---|---|
| `HR_contract` | Contracts. |
| `HR_Action` | Personnel actions. |
| `HR_ActionType` | Action-type look-up. |
| `HR_ActionApproval` | Per-branch approver matrix. |
| `HR_Appraisal` | Performance appraisals. |
| `HR_EmpApproval` | Employee-side approver matrix. |
| `HR_EOS` | End-of-service type lookup. |
| `HR_TermReason` | Termination reason taxonomy. |
| `HR_VACAction`, `HR_VACActionStage/Status/Type` | Vacation action workflow. |

## Documents

| Table | Purpose |
|---|---|
| `HR_VISA`, `HR_VisaType`, `HR_VISAStatus` | Visa applications. |
| `HR_VAUTH`, `HR_VAUTHStatus` | Travel authorisations. |
| `HR_Certificate` | Generic certificate catalogue. |
| `HR_ELeave` | Educational-leave linked to vacation. |
| `HR_LU_Vacations`, `HR_LU_Deductions` | Reason libraries. |

## Payroll (PR)

| Table | Purpose |
|---|---|
| `PR_PayCode` | Pay codes (earnings & deductions). |
| `PR_PayRun` | Pay-run header. |
| `PR_Register` | One per pay-run × branch. |
| `PR_RegDet` | Pay-slip line items. |
| `PR_Loan` | Staff loans. |
| `PR_LoanType`, `PR_LoanStatus` | Loan lookups. |
| `PR_PCPeriod`, `PR_PCType` | Pay-code lookups. |
| `PR_PKT_*` | Edit-buffer ghosts. |
| `PYR_Stage`, `PYR_Status` | Payroll cycle status. |

## Lookups (status & rating)

`HR_Status`, `HR_Contract_Status`, `HR_Vacancy_Status`,
`HR_CandidateStatus`, `HR_APRStatus`, `HR_APROverall`, `HR_APRFactor`,
`HR_RecontractingStatus`, `HR_VacReqStatus`, `HR_ALWTYPE`,
`HR_PRDALWType`, `HR_IncentiveType`, `HR_VacationType`, `HR_RecSource`,
`HR_RepFormat`, `HR_ValueType`, `HR_Holiday`, `HR_Branch`,
`HR_Destination`, `HR_EntryPort`, `HR_Deductions`, `HR_VACClass`.
