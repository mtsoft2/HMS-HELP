# Setup Wizard v2 — New HMS Setup Wizard (`Setup.exe`)

The **metaSOFT Setup Wizard v2** is the new, redesigned installer that
applies HMS patches to a customer database. It replaces the legacy
INI-driven installer with a guided five-step flow that validates the
database **before** touching it, applies the patch, and reports
every script with a per-script status.

![Welcome step](img/01-welcome.png)

## What's new in v2

### 1. Works without `Config.ini`

The wizard no longer requires `Config.ini` to be present. If a
`Config.ini` file *is* found in the install folder, the wizard
auto-loads the previous server / database / authentication values as
defaults — so re-installs are still one-click for support staff who
already configured the box.

### 2. SQL Server instance selection

The **Server** field on the Database step is a dropdown of every SQL
Server instance discovered on the network. Type a host name to pick
something not in the list — named instances (`HOST\SQLEXPRESS`) and IP
addresses are both accepted.

### 3. Authentication method selection

Pick either:

* **Windows Authentication** — uses the logged-in Windows account.
* **SQL Server Authentication** — enter a SQL login and password.

Stored procedures, tables, and trigger creation all use the chosen
account.

### 4. Verify database connection **before** proceeding

The wizard pings the chosen server + database and lists how many
databases were found before letting you click Next. A green
*"Connected — N databases found"* badge confirms reach.

If the connection fails, the wizard stays on the Database step with
the specific error displayed — no half-applied patch can result.

### 5. Verify required schema objects

After applying the patch, the wizard inspects `sys.objects` and
confirms that **every** expected procedure, function, table, and
trigger from the patch is present. The number shown on the Apply
screen — e.g. *"947 of 947 expected objects verified"* — is the
post-install integrity check.

### 6. Comprehensive error report

All setup and validation errors — script failures, missing objects,
permission denials, version mismatches — are written to a single
comprehensive text file alongside the wizard. One file to attach to
a support ticket; no log hunting.

### 7. Patch validation & reporting

The **Patching History** dialog opens from the Welcome step. It
shows every patch ever applied to the connected database **from the
last cumulative (-CM) patch onwards**, with per-patch:

* **Status** — *Applied*, *Error*, *MISSING*.
* **Date** — when the patch ran.
* **Version** — HMS version the patch belongs to.

A red banner at the top counts how many entries are tracked and how
many are **MISSING** — e.g. *"112 entries · 55 MISSING"* — instantly
showing whether the customer's database is up to date.

The wizard refuses to apply a new patch if a prerequisite cumulative
patch is missing, so the patch chain can never get out of order.

➡ Continue to **[Walkthrough](walkthrough.md)** for the five-step
guided run, or **[Patching History](patching-history.md)** for the
detail of the patch-status report.
