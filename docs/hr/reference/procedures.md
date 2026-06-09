# Stored Procedures

The HR module ships ~70 stored procedures. They fall into seven
families.

## 1. Banners (read-only header strips)

`HR_EMPLOYEE_BANNER`, `HR_Contract_BANNER`, `HR_Action_BANNER`,
`HR_Appraisal_BANNER`, `HR_Candidate_BANNER`, `HR_VACATION_BANNER`,
`HR_VacAction_BANNER`, `HR_VISA_BANNER`, `HR_VAUTH_BANNER`,
`HR_PRDALW_BANNER`, `HR_Agency_BANNER`, `PR_Loan_BANNER`.

## 2. Alerts (dashboard / form notifications)

`HR_EMP_Alert`, `HR_EMP_Note_Alert`, `HR_EMP_Note_Alert_APRS`,
`HR_Vacation_Alert`, `HR_Vacation_Alert_Residence`, `HR_Action_Alert`,
`HR_Action_ContractPending_Alert`, `HR_ExpiringDocs`, `PR_Loan_Alert`.

## 3. Lookup-population helpers (used by the *Data Setup* installer)

`HR_Branch_Add`, `HR_EntryPort_Add`, `HR_Position_Add`,
`HR_POSCATEG_Add`, `HR_ValueType_Add`, `HR_PKALW_Add`,
`HR_PKALW_ORG_Add`, `hr_Certificate_ADD`, `HR_ACTION_Salary_Add`,
`HR_APRS_Salary_Add`, `HR_PosHist_Initialize`, `HR_PosHist_ADD`,
`HR_EMP_NewNumber`, `HR_PACKAGE_UPDATE`, `HR_CCI_UPDATE`.

## 4. Calculations

`HR_SP_VAC_CALC`, `HR_VacReq_CALC`, `HR_VacReq_REQUEST_CALC`,
`HR_SP_EOS_CALC`, `HR_EOS_DIF_CALC`, `HR_EOS_DIF_CALC_ALL`,
`HR_ACTION_ACCRUED_LEAVE_CALC`, `HR_ACTION_TOTAL_LEAVE_CALC`,
`HR_APRS_Salary_FIX`.

## 5. Workflow appliers (the SP that actually mutates state)

| SP | Used by |
|---|---|
| `HR_Action_Apply` | Generic personnel-action apply (dispatches to one of the below). |
| `HR_Action_PROMOD_Apply` | Promotion / Demotion. |
| `HR_Action_RETRA_Apply` | Re-transfer (returning an employee to the original branch). |
| `HR_Action_TRANS_Apply` | Transfer. |
| `HR_Action_HIST_Apply_All` | Bulk re-apply of historical actions (migration tool). |
| `HR_Action_Submit_Type` | Submit a draft action with a specific type. |
| `HR_Action_AutoApply` | Nightly sweep that applies fully-approved actions. |
| `HR_Appraisal_Apply` | Appraisal apply (raise + recontract). |
| `HR_Appraisal_AutoApply` | Nightly sweep for fully-approved appraisals. |
| `HR_Contract_Renew` | Issue a new contract from the current one. |
| `HR_Contract_Extend` | Extend the current contract's end-date. |
| `HR_APRContract` | Renew triggered from an appraisal. |
| `HR_EXTContract` | Background extension processor. |
| `HR_VacAction_Submit` | Submit a vacation action. |
| `HR_VacAction_Apply` | Apply a vacation action (consume tickets). |
| `HR_VacAction_AutoApply` | Nightly sweep. |

## 6. Reports / batch

`HR_Employee_RPT`, `HR_Vacation_RPT`, `HR_Account_Employees`,
`HR_MonthlySalaries`, `HR_DueVacations`, `HR_ReContractingLetter`,
`HR_EmpAcct_Gen`, `HR_EMPACCT_NEW`, `HR_Vacation_TravelALW_Validate`.

## 7. Plumbing (framework hooks)

* `HR_SP_FT_Process` — generic process hook called by every HR form.
* `HR_SP_Employee_Vacancy_PostProcess` — post-save hook for the
  Employee form, keeps `HR_Vacancy` in sync.
* `hr_Vacancy_Create_Transient`, `hr_Vacancy_Transient_Process`,
  `hr_Vacancy_Transient_Process_All` — transient vacancy lifecycle.
* `HR_Vacancy_Load` — picker SP for all *Vacancy* dropdowns.
* `HR_Employee_Clear_Vacancy` — release an employee's vacancy without
  a personnel action (admin tool).
* `PR_Loan_Load` — picker SP for loan dropdowns.
* `PR_Loan_Payments` — generates the next instalment line in a pay run.
