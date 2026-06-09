# Personnel Actions

A **Personnel Action** (`HR_Action.FT`) is the auditable record of any
change to an employee's job that is not a routine data edit. Every
action goes through a **three-level approval workflow** before it is
applied.

## Action types

| Type | Tab | What it changes |
|---|---|---|
| **Termination** | Tab 2 | Closes the contract, computes EOS, blocks future pay. |
| **Promotion / Demotion** | Tab 3 | Title + salary change. Writes a new `HR_Salary` row. |
| **Transfer** | Tab 4 | Branch / department / position change. Writes a `HR_PosHist` row and updates vacancies. |
| **Salary Change** | shares Promotion tab | Salary only, no title change. |
| **Contract Renewal** | (auto from Appraisal) | Inserts a new contract. |
| **Extension** | shares Promotion tab | Extends current contract `End_date`. |

## Approval workflow

```
Created → Department Head approval → Project Director approval → Hospital Director approval → Applied
```

* Each approval level stamps its **User + Date** on `HR_Action`
  (`APRV_DepHead`, `APRV_ProjDir`, `APRV_HospDir`).
* Approval levels can be **skipped** by an admin override (see *Policy
  Verification* tab).
* `HR_Action_Apply` is the SP that performs the final mutation once
  *all* required approvals are in.

## Banner & alerts

* `HR_Action_BANNER` — top strip on the form showing employee name,
  current position, action serial, status.
* `HR_Action_Alert` — dashboard alert for actions pending **your**
  approval (filtered by `HR_ActionApproval`).

## Form tabs

1. **Information** — type, date, employee, basic action data.
2. **Termination** — reason flags, last working day, entitlements.
3. **Promotion / Demotion** — new title, new vacancy, new basic.
4. **Transfer** — source vs destination branch / department / vacancy.
5. **Dept-Head Approval** — note, signature, date.
6. **Project-Dir Approval** — note, signature, date.
7. **Hospital-Dir Approval** — note, signature, date.
8. **Policy Verification** — admin override.

➡ Details on the most-used actions:

* [Termination](termination.md)
* [Promotion / Demotion](promotion.md)
* [Transfer](transfer.md)
* [Appraisals](appraisals.md)
