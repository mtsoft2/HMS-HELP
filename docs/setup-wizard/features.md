# Features

Every Setup Wizard v2 feature, grouped by what it lets you do.

---

## 1. Guided five-step flow

* **Welcome → Patch → Database → Apply → Finish** — progress visible
  at the top of every screen.
* **Previous / Next / Cancel** on every step (cancel safe up to
  Apply).
* **Get started** card on Welcome shows patch number, date, size,
  and a reminder to close open HMS clients first.
* **Patching History** is one click away from Welcome — no need to
  start the patch to know whether the database is up to date.

## 2. Config-free install

* **Works without `Config.ini`** — no pre-configuration required.
* **Auto-loads `Config.ini`** if present — re-installs are still
  one-click.
* No registry footprint.

## 3. Database targeting

* **SQL Server instance dropdown** — every instance discovered on
  the network.
* **Free-text typing** — host name, IP, or named instance
  (`HOST\SQLEXPRESS`).
* **Authentication selector** — Windows or SQL Server.
* **Connect button** — validates the choice before letting the
  wizard proceed.
* **Database dropdown** — populates from the connected instance
  with the count of databases found.
* **Green / red badge** confirms connection status with the specific
  error if it fails.

## 4. Patch information

* **Install folder** — pre-filled with the standard path, override
  with Browse.
* **What's new** preview — scrollable inside the wizard, **Open**
  pops the notes out into Notepad.

## 5. Safe application

* **Two-phase apply** — SQL scripts first, then file copy.
* **Per-script status row** — DONE / VERIFIED / Error visible during
  the run.
* **Show only errors** filter to focus on what failed.
* **Stops on first hard failure** — the wizard surfaces the error
  instead of soldiering on.
* **Idempotent scripts** — re-applying is safe.

## 6. Post-install verification

* **Object count** — *"N of N expected objects verified in
  sys.objects"* shown when the patch completes.
* **Re-Verify** button — re-inspects the database without re-running
  scripts.
* **Re-Apply** button — full re-run (idempotent).

## 7. Patch validation & history

* **Patching History** dialog — every recorded patch from the last
  cumulative (-CM) onwards.
* **Entries + MISSING counter** — one-line health summary
  (*"112 entries · 55 MISSING"*).
* **Per-patch status** — Applied / Error / MISSING with date and HMS
  version.
* **Prerequisite check** — the wizard refuses to apply a patch when a
  prerequisite cumulative patch is missing.

## 8. Comprehensive error reporting

* **Single error file** — every setup and validation error from the
  run is written to one text file next to the wizard. Attach to
  support tickets in one click.
* **Per-script error text** inline on the Apply screen.
* **Database version mismatch** detection — flagged in the error
  file with the expected vs found version.

## 9. Modern UI

* Clean dark-blue header on every step.
* Light step body with consistent spacing.
* Step numbers on the right (*"STEP N OF 5"*).
* metaSOFT HMS branding panel on the Welcome screen.

---

➡ Continue to **[Walkthrough](walkthrough.md)** for the step-by-step
run, or **[Patching History](patching-history.md)** for the patch
report.
