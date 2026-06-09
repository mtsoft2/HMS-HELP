# Contracts (Tab 3)

Every employee has one **active contract** and (optionally) a history
of expired or terminated contracts. The contract drives **basic salary,
allowances, ticket entitlement, vacation days** and the **end-of-service
formula**.

## Contract form (`HR_Contract.ft`)

The form has two tabs: **Information** and **Position Vacancy History**.

### Information tab

| Field | DB column | Notes |
|---|---|---|
| Contract Number | `Contract_Number` | Auto-incremented serial. |
| Start / End Date | `Start_date`, `End_date` | End-of-service is calculated from these. |
| Married / Single | `Type_Married_single` | Affects family-ticket entitlement. |
| Permanent / Part-time | `Type_permanent_parttime`, `Parttime` | Part-time contracts skip GOSI deduction. |
| Tickets for Employee | `Tickets_for_employee` | Free yearly tickets. |
| Tickets for Family | `Tickets_for_Family` | |
| Basic Salary | `Basic` | The base for EOS and all *based-on-basic* allowances. |
| Housing | `Housing` | |
| Transportation | `Transportation` | |
| Mobile | `Mobile` | |
| Schooling | `Schooling` | |
| Year / Model of Car | `Year_Model_Car` | If the contract includes a company car. |
| Additional Allowances | `Addionnal_allowances` | Free-text amount. |
| Job Type | `Job_Type` | Free-text. |
| Title | `Title` | Job title printed on the contract document. |
| Overtime allowed | `Overtime_allowed` | Yes / No. |
| Vacation Days | `Vacation_days` | Annual leave entitlement. |
| Period before vacation | `Period_before_vacation` | Months of service required before the employee can claim leave. |
| Package | `PACKAGE` | Reference to `HR_Package`. If set, basic/housing/transport/mobile are copied from the package and grey-locked. |

### Position Vacancy History tab

Displays the grid `HR_PosHist.GT` — every transfer / promotion shown
chronologically: branch, department, position, vacancy, start, end.

## Renewal & extension

| SP | When fired |
|---|---|
| `HR_Contract_Renew` | Creates a brand-new contract record carrying forward the same package. |
| `HR_Contract_Extend` | Extends the **End_date** of the current contract without creating a new one. Sets `CT_Extended = 1`. |
| `HR_APRContract` | Triggered from an Appraisal — auto-renews the contract using the appraisal's recommended package. |
| `HR_EXTContract` | Background SP that processes the *Extension* personnel action. |

## Alerts

Two stored procedures populate the dashboard alerts:

* `HR_Action_ContractPending_Alert` — contracts pending approval.
* The two views `HR_Contract_30d` / `HR_Contract_6m` feed the
  *Expiring contracts* drill-down list in the HR Overview.

## Status values (`HR_Contract_Status`)

`A` Active &nbsp;·&nbsp; `E` Expired &nbsp;·&nbsp; `T` Terminated &nbsp;·&nbsp; `R` Renewed &nbsp;·&nbsp; `X` Extended
