# Settings

Open from the sidebar. The settings window is split into seven tabs.

## Engine

How the Communicator drives WhatsApp.

| Setting | Notes |
|---|---|
| **Engine** | *WhatsApp Web* (default — supports attachments) or *WhatsApp Desktop* (text only, simpler). |
| **Hide Chrome window** | Chrome doesn't appear in the taskbar. |
| **Hide console window** | Hides any background console window. |
| **Auto-hide after login** | Chrome shows just long enough for the QR scan, then hides automatically. |

## Sending

How retries and notifications behave.

| Setting | Notes |
|---|---|
| **Retry attempts** | How many times a failed send is retried before being marked Failed. |
| **Retry delay** | Wait between retries (seconds). |
| **Tray notifications** | Show a Windows toast for sent / failed messages. |

## Database

The HMS hookup.

| Setting | Notes |
|---|---|
| **Queue polling** | How often the queue is checked (seconds). Smaller = faster pickup, more DB load. |
| **Attachment retention** | How long sent attachments are kept on disk. |
| **Default country code** | Applied when a number has no country code. |
| **Test connection** | Proves the database hookup. Always run this after a config change. |
| **Heartbeat** | The Communicator writes a heartbeat row so HMS can detect a dead Communicator. |
| **Stuck reaper** | Unsticks messages that have been in *Sending* for too long. |

## Safety

The guardrails that protect the WhatsApp account from being banned and
recipients from being spammed. See **[Safety
Guardrails](admin/safety-guardrails.md)** for a deep dive.

| Guardrail | Default | What it does |
|---|---|---|
| **Min gap + jitter** | 8 s + 0–4 s | Paces sending. |
| **Max per number / hour** | 3 | Holds further messages to the same number until next hour. |
| **Max per number / day** | 5 | Holds until next day. |
| **Max total per day** | 100 | Circuit breaker — holds everything until next day. |
| **Duplicate window** | 1 hour | Drops the same message to the same number inside the window. |
| **Sending window** | off (08–20) | Hold outside the configured hours. |
| **Sending days** | every day | Skip specified weekdays. |
| **Surge protection** | 200 in 10 min | Auto-pauses the sender; holds the queue. |

Set any individual value to **0** to disable just that rule.

## Alerts

When something is wrong, tell someone.

| Setting | Notes |
|---|---|
| **Triggers** | Sender down beyond X minutes · Surge protection trips · WhatsApp logged out. |
| **Email (SMTP)** | Host, port, SSL, username, password, From, To. Works even when WhatsApp is down. |
| **WhatsApp alert** | Queue a message to an admin number — delivered once WhatsApp resumes. |
| **Test alert** | Fires a sample alert through both channels — verify the wiring before relying on it. |

## Startup

| Setting | Notes |
|---|---|
| **Start with Windows** | Add / remove the per-user auto-start entry. |
| **Start sender** on launch | If on, sending begins automatically; if off, the app opens but stays paused until you press Start. |
| **Start hidden** | The window does not appear on launch — only the tray icon. |

## Deployment

One-click tools for the support team.

| Button | What it does |
|---|---|
| **Install Communicator** | Sets up auto-start, watchdog, safety guardrails, start hidden, flips the HMS master switch on, and starts the sender. |
| **Uninstall Communicator** | Reverses every change on this PC; flips the HMS master switch off; never touches data or schema. |
| **Configure Windows auto-login** | UAC-elevated; stores credentials encrypted in the Windows secret store; for unattended servers only. |
| **Run Quick Setup** | Re-runs the first-time wizard — for QR re-scans or fresh starts. |

➡ Continue to **[Administration → Architecture](admin/architecture.md)**.
