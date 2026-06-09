# Security & Approvals

HR security is enforced at two layers.

## 1. HMS user roles

The standard HMS user / group / role system gates access to **forms**
and **menu entries** — typically the four HR roles shipped by default:

| Role | Sees | Can edit |
|---|---|---|
| HR Administrator | Everything | Everything |
| HR Officer | Everything except *Salary* tab on employees outside own branch | Employees, candidates, vacancies, leaves |
| Department Manager | Only own department's employees | Approves first-level actions |
| Employee Self-Service | Own profile, own leave history | Submit leave & travel requests |

Form-level access is bound at install time by mapping each `.FT` and
`.ST` to a *security code* in the HMS admin tools.

## 2. Personnel-Action approval workflow

Even with full edit rights, a personnel action is **not applied**
until the three approval levels stamp it:

```
HR Officer creates →
        Department Head approves       (APRV_DepHead + Date)
        Project Director approves      (APRV_ProjDir + Date)
        Hospital Director approves     (APRV_HospDir + Date)
                  ↓
        HR_Action_Apply runs the actual mutation
```

* Approvers are configured per-branch in `HR_ActionApproval` /
  `HR_EmpApproval`.
* The dashboard alert `HR_Action_Alert` lists every action pending
  *your* approval — clicking it opens the action ready to sign.
* Approvals are append-only — they cannot be removed once stamped,
  only superseded by an *Override* on the *Policy Verification* tab
  (admin only, audited).
