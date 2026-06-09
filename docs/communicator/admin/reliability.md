# Reliability

Five mechanisms keep the Communicator running 24 × 7 without a human
in the room.

## 1. Watchdog (relaunch)

A Windows Task Scheduler job runs every few minutes. If the
Communicator isn't running, the watchdog launches it.

* A single-instance mutex prevents duplicates — if the app *is*
  running, the watchdog's launch is a no-op.
* If the watchdog itself is removed (e.g. by an over-zealous admin),
  the *Install Communicator* button re-creates it.

## 2. Health monitor (sender restart)

A background loop inside the app checks once a minute that the sender
is running when it should be. If processing is enabled but the
sender has stopped (browser crash, lost session, unhandled stall),
the health monitor restarts the sender within ~1 minute.

The user sees a small entry in the log; no manual action needed.

## 3. Crash handlers

The app wires global crash handlers in three places:

* **UI thread** — unhandled exceptions in window code.
* **Background tasks** — unobserved task exceptions.
* **App domain** — anything not caught by the first two.

Every catch logs the exception and **does not exit the process** —
the watchdog + health monitor would relaunch / restart anyway, but
not exiting keeps the queue moving.

## 4. Session recovery

The browser layer watches for the "you are no longer logged in"
state. Two cases:

* **Soft disconnect** (e.g. network blip) — Chrome reconnects to
  WhatsApp; the Communicator continues. No alert.
* **True logout** (e.g. WhatsApp force-signed-out from another
  device, or the QR session expired) — needs a human to scan a QR.
  An alert fires; the sender stops; the queue holds.

## 5. Single-instance mutex

The watchdog can trigger a second launch attempt at any time. The
mutex ensures only one instance owns the database queue and the
Chrome profile — duplicates exit immediately.

The same mutex makes "click the icon to bring it forward" reliable
— a second launch focuses the existing window instead of starting
a duplicate.

## What this means in practice

| Failure mode | What happens |
|---|---|
| App killed by Task Manager | Watchdog relaunches in <5 min. |
| App crashed | Crash handler logs and recovers; if the process did exit, watchdog relaunches. |
| Sender stopped without a crash | Health monitor restarts within ~1 min. |
| WhatsApp Web session dropped | Auto-reconnect; user-invisible. |
| WhatsApp truly logged out | Alert; needs a human QR scan. |
| Windows reboot | Auto-login (if configured) → auto-start entry → app running again. |
| HMS database down | Sender goes idle, retries on next polling cycle. No data lost — pending rows stay pending. |
| Chrome killed | App relaunches Chrome on the next cycle. |
| Disk full | Crash handler catches log-write failures; app continues; alert fires. |

➡ Continue to **[Logs](logs.md)**.
