# Logs

Two log files sit next to the executable. Both rotate automatically.

## Main activity log

Every notable event is recorded:

* App start / stop / config change.
* Sender start / stop.
* Each queue pickup (row reference, recipient, type).
* Each send attempt and its outcome (Sent, Failed, Held + reason).
* WhatsApp session events — connected, disconnected, logged-out.
* Watchdog / health-monitor actions.
* Exceptions (with stack trace).

Rotation: the file grows to ~5 MB then is rolled; the last few
generations are kept. Old files are removed automatically.

## Not-found-phones log

A separate file lists every phone number WhatsApp could not find
(*"Phone number shared via url is invalid"* and friends). It is
append-only — no rotation — because clinics want to be able to bulk-
clean these numbers in HMS.

Workflow: open the file weekly, copy the numbers, search them in HMS,
fix or remove. The file does not delete itself when entries are
fixed.

## Live log panel

The Sender screen mirrors the main log in real time, colour-coded
(blue / amber / red). **Clear log** empties the on-screen view only —
the file on disk is untouched and keeps growing.

## What is *not* logged

* Message body of WhatsApp messages (privacy).
* Patient identifiers beyond what is already visible in the queue
  row (reference number, recipient name from the address book).
* Passwords or SMTP credentials.

## Sharing logs with support

If support asks for logs:

* The main log file — the active one and the most recent rotated
  generation are enough for most issues.
* The not-found-phones log — only if the complaint is about specific
  numbers.

Logs can be zipped and e-mailed safely — they do not contain message
content.

## Permanent archiving

Logs are designed for short-term troubleshooting (days to weeks). If
a longer audit trail is required, set up a scheduled task to copy
the rotated generations to a NAS or log-aggregation tool nightly.

➡ Continue to **[Architecture](architecture.md)** if you arrived
here directly.
