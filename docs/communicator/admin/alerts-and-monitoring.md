# Alerts & Monitoring

The Communicator can be left running unattended — alerts are the
mechanism that wakes someone up when it can't fix itself.

## Triggers

| Trigger | When it fires |
|---|---|
| **Sender down beyond X minutes** | The sender has been Stopped (or unable to recover) for more than the configured threshold. |
| **Surge protection trips** | Too many messages in a short window — the sender auto-paused itself. |
| **WhatsApp logged out** | A true logout was detected — the session needs a fresh QR scan from a human. |

## Channels

### Email (SMTP)

Settings → Alerts → Email block:

* **Host / Port** — e.g. `smtp.gmail.com` / `587`.
* **SSL / StartTLS** — typically on for port 587.
* **Username / Password** — service account credentials; prefer an
  app-specific password if your provider supports them.
* **From** — the sender shown to recipients.
* **To** — comma-separated list of admin e-mail addresses.

Works **even when WhatsApp is down** — this is the primary channel
for the *WhatsApp logged out* alert.

### WhatsApp

* Settings → Alerts → WhatsApp number — an admin's WhatsApp number.
* Alert messages are **queued** when an alert fires; they are
  delivered automatically once WhatsApp sending resumes.

Useful as a redundancy when e-mail is unreliable, less useful as the
sole channel for *WhatsApp logged out* alerts (you may never see it
until the session is back).

### Test alert

The **Test alert** button fires a sample alert through both channels.
Run it after every config change — confirms the wiring works before
you need it to work.

## What ends up in alerts

A short text — the trigger name, a timestamp, the host name, the
current queue depth, and any reason text the Communicator was able to
collect. No patient data, no message content.

## Monitoring beyond alerts

* **Heartbeat row** — the Communicator writes a heartbeat row to the
  database every cycle. HMS dashboards can show "last heartbeat at
  …" as a live indicator.
* **Watchdog logs** — the Task Scheduler watchdog records every
  relaunch — useful for spotting flapping.
* **Log file** — see [Logs](logs.md) for what is logged and where.

## Recommended monitoring stack

1. **Email alerts** to the IT admin's inbox for serious events.
2. **WhatsApp alerts** to a clinic manager's phone for surge / pause.
3. A **dashboard tile** in HMS showing the last heartbeat (built-in if
   you use the HMS dashboards).
4. **Weekly review** of the *not-found-phones* log to clean up bad
   numbers at source.

➡ Continue to **[Reliability](reliability.md)**.
