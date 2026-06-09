# Sick Leave

Sick leave is recorded on two slightly different forms:

| Form | Use case |
|---|---|
| `MF_SickLeave.FT` | Quick single-day sick leave entered by the employee's manager. |
| `MF_SickLeave2.FT` | Full medical sick-leave certificate issued by the hospital clinic — includes diagnosis, treating physician, ICD code, attachments. The `MF_SickLeave2_SO` and `wMF_SickLeave2_CDC` variants are used in clinics with a different print layout. |

## Fields

* Employee, From, To, Days.
* Diagnosis / ICD-10 (on the full version).
* Issuing physician (picker into the physician table).
* Attachments (lab results, prescriptions).
* Approved by HR (yes/no), notes.

## Effect on payroll

* **Up to 30 days** in a service year → full-pay sick leave; no
  payroll deduction.
* **Days 31–90** → 75 % pay; the *Sick-deduction* pay code is added to
  the next pay run by `HR_MonthlySalaries`.
* **Days 91+** → unpaid; reduces the period used for end-of-service
  computation.
