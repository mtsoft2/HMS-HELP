# Install & Uninstall

## System requirements

* Windows 10 / 11 that **stays powered on**.
* **Google Chrome** installed.
* **.NET 6 Desktop Runtime (x64)**.
* Network access to the HMS SQL Server and to WhatsApp Web.
* A phone with WhatsApp for the one-time QR scan.

## Deployment layout

The Communicator is deployed into a **Communicator** subfolder inside
the HMS web application — typically alongside the HMS runtime
(something like `…\HMS_Web\Communicator\`). It walks up the folder
tree on launch to find the HMS application settings file, so the
database connection is auto-discovered.

## One-click install

**Settings → Deployment → Install Communicator** does all of this in
one step:

* Adds a **per-user auto-start** entry.
* Installs the **watchdog scheduled task** (relaunches the app every
  few minutes if it isn't running).
* Enables the **safety guardrails** with sensible defaults.
* Sets **Start hidden** — the window does not pop up on login.
* Sets the HMS **master switch to on** — HMS routes WhatsApp through
  the Communicator.
* **Starts the sender**, opening WhatsApp Web for the QR scan if
  there isn't a stored session yet.

After this, the Communicator is in "always on" mode — it will be
running every time the PC is on, even if no human logs in
(combine with auto-login below).

## Windows auto-login

For an unattended server PC, **Settings → Deployment → Configure
auto-login** asks Windows to sign in automatically after a reboot
without a human present.

* UAC prompts for administrator rights.
* The password is stored **encrypted in the Windows secret store** —
  never in plain text or in a config file.
* On the next reboot, Windows logs in, the auto-start entry launches
  the Communicator, the watchdog confirms it is running.

**Use only on dedicated, physically secured machines.** A PC that
auto-logs in is a PC anyone with physical access has logged-in
access to.

## Uninstall

**Settings → Deployment → Uninstall Communicator** reverses everything
on this PC:

* Stops the sender and **closes the app**.
* Removes the auto-start entry.
* Removes the watchdog scheduled task.
* Removes Windows auto-login (if set).
* Sets the HMS **master switch to off** — HMS resumes its legacy
  WhatsApp path immediately.

It does **not**:

* Delete any data.
* Touch the database schema.
* Remove the executable folder or the logs.

So re-installing later just means running the executable again and
clicking **Install Communicator** — the previous config and logs are
all still there.

## Moving to another PC

1. Install the Communicator on the new PC (copy folder + Install
   Communicator).
2. Scan the QR code on the new PC (the WhatsApp session on the old PC
   is automatically signed out — WhatsApp only allows one Web
   session at a time).
3. Confirm messages start flowing on the new PC.
4. **Uninstall Communicator** on the old PC.

Both PCs cannot run at the same time pointing at the same database —
the queue rows would be claimed twice. Always finish the move within
the same maintenance window.

➡ Continue to **[Safety Guardrails](safety-guardrails.md)**.
