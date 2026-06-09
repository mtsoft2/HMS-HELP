# Safety Guardrails

The guardrails protect the WhatsApp account from being banned and
recipients from being spammed. They run on every message — both
automatic and manual.

## The eight guardrails

| Guardrail | Default | What it does when exceeded |
|---|---|---|
| **Min gap + jitter between sends** | 8 s + 0–4 s | Waits — paces sending, looks human. |
| **Max per number, per hour** | 3 | Holds further messages to that number; auto-retried next hour. |
| **Max per number, per day** | 5 | Holds; auto-retried next day. |
| **Max total, per day** | 100 | Circuit-breaker — holds everything; auto-retried next day. |
| **Duplicate window** | 1 hour | Drops the same message text to the same number inside the window (flagged on the queue). |
| **Sending hours window** | off (e.g. 08:00 – 20:00) | Holds outside the window; sends when it re-opens. |
| **Sending days** | every day | Skip configured weekdays. |
| **Surge protection** | 200 in 10 minutes | Auto-pauses the sender; holds the queue; fires an alert. |

## Setting any rule to 0 = disabled

Each rule has its own zero-disables behaviour. For example, setting
**Max per number, per hour = 0** disables only that one rule — the
daily cap, total cap, and surge protection still apply.

## What "Held" looks like

A row in the **Held / Paused** status with the **reason** under the
text — e.g. *Held (Per-number daily cap)*, *Held (Sending hours)*,
*Held (Surge)*. The row stays in the queue and is automatically
re-evaluated when the guardrail clears.

## Manual override

The receptionist can press **Send** on a held row in the Message
Queue — that one row is force-released. The guardrail still counts
the send (the daily cap is now closer to its ceiling). Use sparingly.

## Tuning recommendations

* **New WhatsApp account** — leave defaults; they are deliberately
  conservative.
* **Established business account, low complaint history** — you can
  raise the daily total cap to 200 – 300 once you've watched the
  account for a few weeks.
* **High-frequency single-recipient flows** (e.g. appointment +
  preparation + reminder for the same patient in one day) — raise
  *Max per number, per day* from 5 → 8 or so.
* **After-hours quiet hours** — set Sending hours to your
  reception's working hours. Reminders generated overnight are
  queued and go out when the clinic opens.

## When to widen vs. when to fix the source

* If the queue is constantly piling up at the daily total cap, that
  is the system telling you the WhatsApp account is being used like
  a bulk-marketing channel. Either widen the cap *and* watch for
  account warnings, or look at the HMS automation that is producing
  the messages and trim duplicates.
* If **Surge protection** trips, look at HMS first — usually a batch
  job kicked off all at once. Stagger it.

➡ Continue to **[Alerts & Monitoring](alerts-and-monitoring.md)**.
