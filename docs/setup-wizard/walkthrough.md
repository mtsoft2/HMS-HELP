# Walkthrough — Applying a Patch

The wizard is **five steps**, shown in the progress bar at the top of
every screen: **Welcome → Patch → Database → Apply → Finish**.

The lower-left corner shows the wizard version (e.g. *Version 1.1.0*).
The lower-right corner has **Cancel** at every step — safe to press
until step 4.

---

## Step 1 — Welcome

![Welcome step](img/01-welcome.png)

The welcome card shows the patch the wizard is about to apply:

* **Patch #** — the patch number.
* **Date** — the patch's release date.
* **Size** — the patch payload size.

A reminder line under the card asks you to **close any open HMS
clients** before continuing — uncommitted edits on the patient form
or any other live screen are at risk during the patch.

The **Patching History** button at the bottom-left opens the patch-status
report against the current database — see
**[Patching History](patching-history.md)**.

Click **Get started** to move to Step 2.

---

## Step 2 — Patch information

![Patch step](img/02-patch.png)

Two fields:

* **Install folder** — the on-disk HMS installation the patch is
  targeting (the wizard pre-fills the standard install path; click
  **Browse** to point at a different one).
* **What's new** — a scrollable preview of the release notes shipped
  with the patch. **Open** pops the same notes out into Notepad
  for easier reading.

Confirm the folder is correct and click **Next**.

---

## Step 3 — Database connection

![Database step](img/03-database.png)

* **Install path** — read-only, carried forward from Step 2.
* **Server** — the SQL Server instance to patch. Pick from the
  dropdown (auto-discovered network instances) or type a host name
  / IP / named instance.
* **Authentication** — Windows or SQL Server. If SQL Server, the
  wizard expands to ask for user name and password.
* **Connect** — pings the server. On success the wizard fills the
  **Database** dropdown with every database found on that instance
  and shows a green badge — *"Connected — N databases found"*.
* **Database** — pick the customer database to patch.

The wizard refuses to leave this step until the connection is
green — preventing half-applied patches.

Click **Next** to move to the Apply step.

---

## Step 4 — Apply patch

![Apply step](img/05-apply.png)

The wizard runs the patch in two phases:

1. **Run SQL scripts** — every script in the patch executes in order
   against the chosen database. Each script appears as a row in the
   table with its status — **DONE**, **VERIFIED**, or an error pill if
   it failed.
2. **Copy files to the HMS install folder** — DLLs, templates,
   reports.

When everything completes, a green summary at the top reads:

> ✓ **Patch applied successfully.**
> All scripts executed and files copied. *N of N expected objects
> verified in sys.objects.*

The number reflects the post-install integrity check.

### Filter the table

* **Show only errors** checkbox — hides every DONE / VERIFIED row so
  you can focus on what failed.

### Action buttons (bottom of the screen)

* **← Previous** — go back to the Database step (only before Apply
  starts; once scripts are running the patch must finish or be
  cancelled).
* **Re-Verify** — re-inspect `sys.objects` against the expected list
  without re-running any scripts. Useful when a verification glitch
  was caused by a temporary lock.
* **Re-Apply** — re-runs the SQL scripts and re-copies the files.
  Safe — scripts are written to be idempotent.
* **Next →** — only enabled once the patch is successful.
* **Cancel** — abandons the patch.

Click **Next** to move to Step 5.

---

## Step 5 — Finish

A short confirmation card shows the patch is applied and the wizard
exits. The customer database now reports the new patch in **Patching
History**.

---

## What if a script fails?

The wizard does **not** silently continue.

* The failing row shows in red on the Apply table with the SQL error
  text inline.
* **Show only errors** lets you list every failure in one view.
* The comprehensive error file (saved next to the wizard) holds the
  full output for the support team.
* Press **Re-Apply** after fixing the underlying issue (permissions,
  missing prerequisite, etc.) — the wizard re-runs idempotently and
  moves past previously-applied scripts.

If the failure is a missing prerequisite cumulative patch, the
Patching History will surface that — see
**[Patching History](patching-history.md)**.
