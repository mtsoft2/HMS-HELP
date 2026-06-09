# Sender Screen

The **Sender** screen has three areas, top to bottom: **Status**,
**Manual send**, and **Log**.

![Sender screen](../img/sender.png)

## Status

| Control | What it does |
|---|---|
| **Start** | Turns the automatic sender on. |
| **Stop** | Pauses sending — Pending rows stay in the queue. |
| Coloured dot | **Running** (green) or **Stopped** (grey). |
| **Queue** | How many messages are waiting to be sent. |

Press **Start**; if it is the first time after a reboot the Chrome
window may pop up briefly while the WhatsApp session checks in. It
hides itself once it is logged in.

## Manual send

The block that lets staff send a message by hand from the Communicator
itself (the same path HMS messages take — so the same safety rules
apply).

| Field | Notes |
|---|---|
| **Contact** | Pick a saved contact, or type a name. The dropdown autocompletes from the address book. |
| **Phone** | Digits only — country code first, no spaces or dashes. |
| **Message** | The text. Arabic is supported and renders right-to-left. |
| **Attachment** | Optional. Click **Browse** to attach an image, PDF, Word, Excel, or any document. |
| **Send** | Queues the message. It then flows through the same queue and safety guardrails as HMS messages. |

The contact + phone you used are auto-added to the address book on
first send, so they autocomplete next time.

## Log

The right-hand panel shows live, colour-coded activity:

* **Blue** — informational (started, queued, sent).
* **Amber** — warning (retry, throttled, recovered).
* **Red** — error (failed, logout, unreachable).

**Clear log** empties the on-screen view only — the file log on disk
keeps growing and rotating.

## Tips

* Keep the Sender screen open on a small monitor at the front desk so
  problems surface quickly — the log spells them out as they happen.
* If the status reads *Stopped* and Pending is growing, the most
  likely cause is the WhatsApp session — press **Start** and watch
  for the QR scan request.

➡ Continue to **[Message Queue](message-queue.md)**.
