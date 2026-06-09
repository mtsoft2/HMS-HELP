# Glossary

| Term | Definition |
|---|---|
| **Accrued leave** | Leave days the employee has earned but not yet used. Computed by `HR_ACTION_ACCRUED_LEAVE_CALC`. |
| **Action** | A formal change to an employee's job (transfer, promotion, termination, …) that goes through three-level approval — see [Personnel Actions](../actions/index.md). |
| **Appraisal** | End-of-term performance review — see [Appraisals](../actions/appraisals.md). |
| **Banner** | Static green strip at the top of an HMS form; rendered by a `*_BANNER` SP. |
| **Binder (BND)** | Full-screen workspace template (toolbar + side menu). HR has no dedicated binder — it is opened from the main menu. |
| **Candidate** | An applicant — see [Candidates](../recruitment/candidates.md). |
| **Contract** | Time-bound employment contract — see [Contracts](../employees/contracts.md). |
| **EOS** | End of Service award (gratuity) paid on leaving, per Saudi labour law — see [End of Service](../employees/eos.md). |
| **Form (FT)** | Single-record edit window — e.g. `HR_Employee.FT`. |
| **Ghost / PKT** | The edit-buffer table (`HR_PKT_*`). User changes live here until **Save**. |
| **Grid (GT)** | Child-table view embedded in a form — e.g. `HR_Salary.GT`. |
| **HR Officer** | Day-to-day HR user — creates employees, leaves, candidates. |
| **HR Administrator** | Configures look-ups, packages, periodic allowances, security. |
| **Package** | Salary template — see [Packages](../organization/packages.md). |
| **Pay Code** | One line on the pay slip — see [Pay Codes](../payroll/pay-codes.md). |
| **Pay Run** | One monthly payroll batch — see [Pay Runs](../payroll/pay-runs.md). |
| **Periodic Allowance** | Recurring monthly amount paid outside the package — see [Periodic Allowances](../organization/periodic-allowances.md). |
| **PKT table** | See *Ghost*. |
| **Register** | Result of one pay run — see [Registers](../payroll/registers.md). |
| **S.C.C.** | Saudi Council Certificate — licensure for clinical staff — see [Certificates](../documents/certificates.md). |
| **Search pad (ST)** | List / search window — e.g. `HR_Employee_Fast.ST`. |
| **Sponsor** | Legal employer on the residence permit. Tracked in `HR_Employee.Current_sponsor_name`. |
| **Transient vacancy** | Auto-created temporary vacancy that keeps headcount balanced during a transfer — see [Vacancies](../recruitment/vacancies.md). |
| **VacAction** | Vacation action — a step in the vacation workflow (request, approve, take, return). |
| **Vacancy** | Approved opening to be filled — see [Vacancies](../recruitment/vacancies.md). |
| **Vglbatch** | GL batch number written on `PR_Register.Vglbatch` once a payroll is posted to general ledger. |
