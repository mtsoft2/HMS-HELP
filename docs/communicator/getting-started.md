# Getting Started

From a fresh PC to first WhatsApp message — about 10 minutes.

## 1. Pick the service PC

* Windows 10 / 11 that **stays powered on** (the *service* machine).
* **Google Chrome** installed.
* **.NET 6 Desktop Runtime (x64)** installed.
* Network access to the HMS SQL Server and to WhatsApp Web.
* A phone with **WhatsApp** to scan the QR code once.

## 2. Deploy the Communicator

Copy the Communicator into the HMS web app folder — typically into a
**Communicator** subfolder alongside the running HMS — and double-click
the executable to launch.

On startup it walks up the folder tree to find the HMS application
settings — so it picks up the same database the running HMS uses.

## 3. Quick Setup wizard

The very first time it runs, the **Quick Setup** dialog appears. It
does everything in one step.

1. Click **Set up now**.
2. A Chrome window opens **WhatsApp Web**. **Scan the QR code** with
   the phone — once. The login is remembered.
3. Wait for the message *"WhatsApp Web is logged in and ready."*

After setup, the Chrome window hides itself and the Communicator
continues in the system tray.

## 4. Install as a service (recommended)

Open **Settings → Deployment → Install Communicator**. One click sets
up the whole "always on" behaviour:

* Per-user **auto-start** entry — the Communicator starts when Windows
  logs in.
* **Watchdog** scheduled task — relaunches the app every few minutes if
  it isn't running.
* **Safety guardrails** turned on with sensible defaults.
* **Start hidden to tray** — no window pops up on login.
* Tells HMS to route WhatsApp through the Communicator — the master
  switch is flipped to **on**.
* Starts the sender immediately.

### Optional: Windows auto-login

For an unattended server that has no human present after a reboot, run
**Settings → Deployment → Configure auto-login**. UAC asks for
admin rights, then Windows signs in automatically next time the
machine reboots. The password is stored encrypted in the Windows
secret store — never in plain text.

Use only on dedicated, physically secured machines.

## 5. Send your first message by hand

1. Click the tray icon to open the window.
2. Go to **Sender**.
3. If status reads **Stopped**, press **Start** and wait for
   **Running** (green dot).
4. **Contact** — type a name (or pick a saved one).
5. **Phone** — digits, country code, no spaces.
6. **Message** — the text (Arabic is supported).
7. (Optional) **Attachment** — Browse to an image, PDF, or document.
8. Press **Send**.

The message lands in the Message Queue and is sent in turn. You can
watch the **Log** panel on the right side of the Sender screen for
live, colour-coded activity.

## 6. Verify HMS messages are flowing

Trigger a normal HMS event that produces a WhatsApp — book an
appointment, issue a prescription, send a reminder — and switch to the
Communicator's **Message Queue**. The new row should appear with
status **Pending**, flip to **Sending**, then **Sent**.

➡ Continue to **[Features](features.md)** for the full catalogue.
