# Pay Runs

A **Pay Run** is one monthly batch. Open **Payroll → Pay Run**
(`PR_PayRun.FT`).

## Fields

| Field | DB column |
|---|---|
| Period Start | `PeriodStart` (first day of the month) |
| Period | `Period` (e.g. `2026-06`) |
| GL Batch | `Vglbatch` (filled when posted to GL) |
| Created By | `CreatedBy` |
| Created On | `CreatedON` |
| Message | `MSG` (free-text log) |

## Workflow

1. Open Pay Run, click **New**.
2. Set Period Start, choose Branch and (optionally) Department, EOS
   status, vacation status, contract-start window, package filters.
   These map to `PR_Register.PRR_*` columns.
3. Click **Generate** — `HR_MonthlySalaries` runs:
   * Selects every active employee matching the filters.
   * Inserts one `PR_Register` per Branch (or per Department, depending
     on settings).
   * Inserts one `PR_RegDet` per employee × pay code.
   * Updates Totals on `PR_Register` (`Total`, `TotalPay`,
     `TotalDeduction`).
4. Review the **Registers** tab — drill into any line to see the
   computation.
5. Click **Post to GL** — `Vglbatch` is filled and the batch becomes
   read-only.
6. Print pay slips (`PR_PaySlip.rpt`) — one PDF per employee or
   batched.

## Re-running

If you need to regenerate, **delete the un-posted register** first
(or use the *Reverse* command on a posted register, which inserts a
contra batch in GL). A new generation always creates a fresh
`PR_Register` — never overwrites.
