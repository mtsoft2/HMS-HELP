# Everyday Use

The Communicator is designed to disappear into the background — most
days nobody opens it. Here is what to know for the days you do.

## How it behaves on its own

* It **starts with Windows** and runs hidden in the system tray.
* If you close the window, it only **hides** — the service is still
  running.
* If the app is ever killed, the **watchdog relaunches** it within a
  few minutes.
* If sending stops while processing is enabled, the **health monitor
  restarts** it within about a minute.
* If WhatsApp Web drops the session, it **reconnects** automatically.
* A true WhatsApp logout (needs a fresh QR) fires an **alert**.

## Common tasks

| I want to… | Do this |
|---|---|
| Resend a failed message | Message Queue → find the row → **Send**. |
| Fix a wrong message before it sends | Message Queue → **Edit** → change → Save. |
| Stop one message going out | Message Queue → **Pause** (or Delete). |
| Retry everything that failed | Message Queue → **Send all unsent**. |
| Find an old message | Use the status chips and From / To dates. |
| Send a document | Sender → **Browse** to the file → **Send**. |
| Pause all sending | Sender → **Stop**. Press Start to resume. |
| Open the window after closing it | Click the Communicator tray icon (near the clock). |
| Fully exit | Right-click the tray icon → **Quit**. |

## Quick troubleshooting

| Symptom | Likely cause & fix |
|---|---|
| *"Chat did not open"* in the log | WhatsApp isn't logged in — press **Start** and scan the QR. |
| Messages stay **Pending** and nothing sends | Sender is **Stopped** — press Start. Or check internet / WhatsApp login. |
| A message shows **"Invalid number"** | The phone number is wrong — **Edit** it (or fix it in HMS) and press Send. |
| A message is **"Held (Throttled)"** | A safety limit (per-number, per-day, or sending hours) is in effect — it sends automatically later. |
| **Surge** notice appears | Surge protection auto-paused the sender — wait, or raise the limit in Safety. |
| I can't see the window | Click the Communicator icon in the system tray. The window opens; closing it hides it again. |
| Sent messages still arrive in HMS as Pending | The HMS master switch may be off — check Settings → Database and confirm the connection is to the right database. |

## When to call IT

* The QR scan keeps reappearing after every reboot.
* The watchdog seems to be relaunching the app constantly.
* Email alerts say sender-down repeatedly.
* The whole machine froze / blue-screened.

These are admin / installation problems — see **Administration** in
the sidebar.

➡ Or continue to **Settings → Overview** for the configuration
reference.
