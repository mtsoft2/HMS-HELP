# Features

Every Metasoft Communicator feature, grouped by what it lets you do.

---

## 1. Message sending

* **Automatic sending** — picks up Pending rows from the HMS message
  queue and sends them over WhatsApp Web.
* **Manual sending** — pick a contact (or type one), write text, attach
  a file, click Send.
* **Text in any language** — Arabic, emoji, multiline; pasted via the
  clipboard so unicode is reliable.
* **Attachments** — images, PDFs, Word, Excel, any document. Optional
  caption alongside the attachment.
* **Same path for HMS + manual** — both sources go through the queue,
  the same safety rules, the same logging.

## 2. Address book

* **Remembers every contact** ever used (name ↔ phone).
* **Auto-saved after each send** — no separate "add contact" step.
* **Autocomplete** in the manual-send Contact field.
* **Country-code-aware** — strips `+`, spaces, dashes before sending.

## 3. Sender screen

* **Start / Stop** the automatic sender.
* **Status pill** — Running (green), Stopped (grey) with the current
  queue depth.
* **Manual send block** — Contact, Phone, Message, Attachment, Send.
* **Live activity log** — colour-coded (blue info, amber warning, red
  error).
* **Clear log** — empties the on-screen view (file log keeps growing).

## 4. Message Queue screen

* **Four summary cards** — Pending / Sending / Sent / Failed counts at
  the top of the screen.
* **Status chips** — *All / Pending / Sending / Sent / Failed / Held*
  to narrow the list with one click.
* **Date filter** — From / To dates with a Clear button.
* **Per-row badge + recipient + text + attachment chip + failure
  reason + time + reference number**.
* **Right-to-left rendering** — Arabic messages render correctly.
* **Per-row actions** — Send (retry), Edit (change text), Pause (hold),
  Delete.
* **Send all unsent** — re-queue every failed / paused / stuck message
  in one click.

## 5. Statuses

* **Pending** — waiting in the queue.
* **Sending** — being sent right now.
* **Sent** — delivered to WhatsApp successfully.
* **Failed** — could not be sent; reason shown inline.
* **Held / Paused** — held on purpose (by user or by a safety rule);
  releases automatically when the rule clears, or via Send.

## 6. Always-on operation

* **System-tray application** — lives by the Windows clock, click to
  open.
* **Single instance** — second launches focus the existing window
  instead of starting a duplicate.
* **Closing the window only hides it** — Quit from the tray menu is
  the only way to fully exit.
* **Auto-starts with Windows** at user login.
* **Watchdog scheduled task** — relaunches the app within minutes if
  it isn't running.
* **Health monitor** — restarts the sender within ~1 minute if it
  stops while processing is on.
* **Single-instance mutex** — watchdog cannot create duplicates.

## 7. Crash resistance

* **Unhandled exception handlers** for UI, background, and task code —
  exceptions are logged and recovered without process exit.
* **Session recovery** — a lost WhatsApp session is detected and
  reconnected automatically.
* **True logout detection** — if WhatsApp has actually logged out
  (needs a fresh QR scan), an alert fires.

## 8. Safety guardrails

* **Minimum gap between sends** + random jitter — paces sending to
  avoid bursts.
* **Per-number / per-hour** cap.
* **Per-number / per-day** cap.
* **Total per-day** cap (circuit-breaker).
* **Duplicate window** — drops the same message to the same number
  inside the window.
* **Sending hours** — e.g. 08:00 – 20:00; outside the window messages
  are held.
* **Sending days of week** — e.g. skip weekends.
* **Surge protection** — too many messages in a short window auto-pauses
  the sender.

Each rule can be set to 0 to disable just that rule.

## 9. Alerts & monitoring

* **Sender-down threshold** — alert if the sender has been down for
  more than X minutes.
* **Surge trip alert** — alert when surge protection auto-pauses
  sending.
* **WhatsApp logout alert** — alert when a true logout is detected.
* **Email (SMTP)** — host, port, SSL, credentials, From / To. Works
  even when WhatsApp is down.
* **WhatsApp alert** — queue a message to an admin number; delivered
  once WhatsApp comes back.
* **Test alert** button — fires a sample alert through both channels.

## 10. WhatsApp engine options

* **Engine selector** — WhatsApp Web (default, supports attachments)
  or WhatsApp Desktop (text only, simpler).
* **Hide Chrome / console** after launch.
* **Auto-hide after login** — Chrome disappears once the QR is scanned.
* **Persistent Chrome profile** — QR scanned once; login remembered
  across restarts.

## 11. Database hookup

* **Single source of truth** — reads the same HMS application settings
  file the HMS web app uses; no separate connection string.
* **Polling interval** — how often to check the queue.
* **Attachment retention** — how long sent attachments are kept.
* **Default country code** — used when a number has no country code.
* **Test connection** button — proves the database hookup before
  enabling sending.
* **Heartbeat** — the app writes a heartbeat row so HMS can detect a
  dead Communicator.
* **Stuck reaper** — unsticks messages that have been in *Sending* too
  long.

## 12. Startup behaviour

* **Start with Windows** toggle.
* **Start sender** on launch — yes / no.
* **Start hidden** — no window pops up, only the tray icon.

## 13. Deployment tools (Settings → Deployment)

* **Install Communicator** — one click; sets up auto-start, watchdog,
  safety, hidden start, flips the HMS master switch on, starts sending.
* **Uninstall Communicator** — reverses everything on this PC, flips
  the HMS master switch off so HMS resumes its legacy sending path.
  Never touches data or schema.
* **Configure Windows auto-login** — encrypted credential in the
  Windows secret store; for unattended servers.
* **Run Quick Setup** — re-runs the first-time wizard.

## 14. Logging

* **Rolling main log** next to the executable — full activity log;
  auto-rotates at ~5 MB, keeps the last few generations.
* **Not-found-phones log** — separate file of every number WhatsApp
  could not find.
* **Live log panel** on the Sender screen — same data, colour-coded.
* **Per-message reason** — failed rows carry their failure reason
  inline.

## 15. In-app Help

* **Help tab** in the sidebar — short, plain-language guide built into
  the app.
* **Kept in sync** with every feature change as part of the release.

## 16. HMS integration

* **Master switch** in HMS — when on, HMS routes WhatsApp to the
  Communicator queue; when off, HMS uses its legacy WhatsApp path.
* **Idempotent** — disabling the Communicator does not disrupt HMS;
  the legacy path resumes automatically.
* **Same database** — the Communicator and HMS read / write the same
  message queue rows, so HMS always sees the latest status.

➡ Continue to **[Sender Screen](screens/sender.md)** or
**[Message Queue](screens/message-queue.md)** for the day-to-day UI.
