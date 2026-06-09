# Employees

The **Employee** record is the heart of the HR module. Every other
HR object (contract, salary, action, leave, payroll register) hangs
off an `HR_Employee.Id`.

## How to open

* **HR menu → Employees** — opens the searchable list
  (`HR_Employee_Fast.ST`, also reachable from any picker via the
  *Employee* lookup).
* From a vacancy or candidate — the **Hire** action creates a new
  employee linked back to the source candidate.

## The Employee form (`HR_Employee.FT`)

The form is organised into **16 tabs**:

| # | Tab | What it holds |
|---|---|---|
| 1 | **Personal** | Name (EN/AR), date & place of birth, gender, nationality, religion, marital status, ID photo |
| 2 | **Employment** | Branch, department, position, vacancy, status, joining date, attendance card |
| 3 | **Contracts** | List of contracts (`HR_Contract.ft`) — start/end, package, basic, ticket entitlement |
| 4 | **Qualifications** | Degrees, certifications, S.C.C. (Saudi Council) certificate number / expiry / profession |
| 5 | **Salary** | Salary history (`HR_Salary`) — every package or action change creates one row |
| 6 | **Allowances** | Per-employee allowances (`hr_employee_allawence`) |
| 7 | **Tickets** | Travel tickets owed and used (`hr_employee_ticket`) |
| 8 | **Leaves** | Vacation entries (`hr_employee_vacation`), accrued / taken / remaining |
| 9 | **Overtime** | Overtime hours (`hr_employee_overtime`) |
| 10 | **Dependants** | Spouse and children (`HR_Employee_child`) |
| 11 | **End of Service** | EOS settlement — last working day, years of service, EOS amount |
| 12 | **Notes** | Free-text notes |
| 13 | **Contact** | Address, phone, mobile, email, P.O. Box, ZIP, emergency contact (SOS) |
| 14 | **Experience** | Prior work history (`HR_EMPLOYEE_Experience`) |
| 15 | **Earned Leaves** | Computed earned leave balance |
| 16 | **Incentives** | Performance / spot bonuses (`HR_Incentive`) |

### Banner

A green **banner** at the top of the form (procedure `HR_EMPLOYEE_BANNER`)
shows at a glance: full name, employee number, position, department,
branch, and contract status.

### Alerts

Two alert strips scroll at the top:

* **HR_EMP_Alert** — expiring documents (passport, residence, S.C.C.,
  contract end, visa) within the next 30 days.
* **HR_EMP_Note_Alert** — any free-text note flagged as alert.

## Underlying tables

| Table | Use |
|---|---|
| `HR_Employee` | Master record |
| `HR_PKT_Employee` | Edit-buffer (ghost table) — your unsaved changes live here until **Save** |
| `HR_Employee_child` | Dependants |
| `HR_EMPLOYEE_Experience` | Prior employment |
| `hr_employee_qualification` | Diplomas / certificates |
| `hr_employee_vacation` | Vacation history |
| `hr_employee_ticket` | Tickets |
| `hr_employee_overtime` | Overtime hours |
| `hr_employee_allawence` | Personal allowances |
| `HR_Salary` | Salary history (one row per change) |
| `HR_PKALW` | Package allowance breakdown |

➡ Next: **[Personal Info](personal.md)**
