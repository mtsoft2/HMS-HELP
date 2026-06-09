# Human Resources Module

The **Human Resources** module manages the full employee lifecycle in HMS:
from recruitment, hiring and contracting, through day-to-day personnel
actions (transfers, promotions, appraisals, leaves, sick leave, document
expiry), all the way to end-of-service settlement. The **Payroll**
sub-module turns this data into monthly salaries, deductions, loans and
pay slips.

## What you can do in HR

* **Maintain an employee master file** — personal data, contact, documents
  (passport, residence, visa, council certificates), bank, dependants,
  qualifications, experience.
* **Manage the organisation chart** — branches, departments, positions and
  vacancies, salary packages, periodic allowances.
* **Run recruitment** — register candidates, link them to vacancies and
  recruitment agencies, convert candidates into employees.
* **Issue and renew contracts** — fixed-term, part-time, renewable, with
  automatic alerts 30 and 180 days before expiry.
* **Record personnel actions** — termination, promotion / demotion,
  transfer, salary change, with a three-level approval workflow
  (Department Head → Project Director → Hospital Director).
* **Process leaves** — annual vacation requests, sick leave, educational
  leave, travel authorisation, leave extensions, dependant tickets.
* **Run appraisals** and link them to re-contracting and salary raises.
* **Track expiring documents** — passports, residences, visas, S.C.C.
  certificates — with built-in alerts.
* **Process payroll** — pay codes, pay runs, registers, pay slips, loans.
* **Print 25+ HR reports** — staff lists by nationality / sponsor /
  religion, salary registers, due vacations, recruitment, Saudization,
  termination, turnover, …

## How to open the module

From the HMS main menu open **Human Resources** (and **Payroll** for the
pay-cycle pages). The module is registered in `MAIN_Menu` as:

| Menu entry | Module code | Launched by |
|---|---|---|
| Human Resources | `HR` | `Admin.exe` |
| Payroll | `PR` | `Admin.exe` |

## Module map

```
HR
├── Master files
│   ├── Employees ............ HR_Employee.FT  ▸  search via HR_Employee_Fast.ST
│   ├── Departments .......... HR_Department.FT
│   ├── Positions ............ HR_POSITION.FT
│   ├── Packages (salary) .... HR_PACKAGE.FT
│   ├── Periodic Allowances .. HR_PRDALW.FT
│   ├── Agencies ............. HR_Agency.FT
│   └── Certificates ......... HR_Certificate.FT
├── Recruitment
│   ├── Vacancies ............ HR_VACANCY.FT
│   └── Candidates ........... HR_Candidate.FT
├── Contracts ................ HR_Contract.ft
├── Personnel Actions ........ HR_Action.FT
├── Appraisals ............... HR_Appraisal.FT
├── Leaves
│   ├── Vacation request ..... HR_Vacation.FT
│   ├── Travel auth .......... HR_VAUTH.FT
│   └── Extension ............ HR_Extension.FT
├── Documents
│   ├── Visa ................. HR_VISA.FT
│   └── Sick leave ........... MF_SickLeave.FT  /  MF_SickLeave2.FT
├── Overview dashboard ....... HR_Overview.ST  (branch-filtered)
└── Reports .................. ~25 RPT/INI under  Report template/

PR (Payroll)
├── Pay Codes ................ PR_PayCode.FT
├── Pay Runs ................. PR_PayRun.FT
├── Registers & slips ........ PR_Register
└── Loans .................... PR_Loan
```

➡ Continue to **[Getting Started](getting-started.md)** or jump straight to
**[Employees](employees/index.md)**.
