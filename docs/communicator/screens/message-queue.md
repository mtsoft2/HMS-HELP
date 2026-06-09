# Message Queue Screen

Every WhatsApp message — automatic or manual — flows through this
screen. Use it to monitor the queue, act on stuck messages, and answer
"did it actually send?" questions.

## Summary cards

Four cards across the top count the messages in each state:

* **Pending** — waiting to be sent.
* **Sending** — being sent right now.
* **Sent** — delivered to WhatsApp successfully.
* **Failed** — could not be sent.

Click any card to jump the list to that state.

## Filters

| Filter | What it does |
|---|---|
| **Status chips** — *All / Pending / Sending / Sent / Failed / Held* | Narrow the list to one state. |
| **From / To dates** | Limit to a date range. |
| **Clear** | Resets every filter. |

Filters compose — Failed + last 7 days, for example.

## Each message row shows

* A coloured **status badge**.
* The **recipient** — phone number plus name (from the address book if
  known).
* The **message text** (Arabic renders right-to-left).
* A **paperclip chip** if an attachment is included.
* The **failure reason** underneath if the row is Failed (e.g.
  *Invalid number*, *Chat did not open*, *Throttled*).
* The **time** and a **reference number** (e.g. `#16`).

## Per-row actions (on un-sent messages)

| Action | Effect |
|---|---|
| **Send** | Re-queue immediately. The row flips to Sending. |
| **Edit** | Open the editor; change the text; Save. The corrected row is queued. |
| **Pause** | Hold the row — it stays in the queue but is skipped until Send is pressed again. |
| **Delete** | Remove the row from the queue. |

Sent messages are read-only — they cannot be edited or re-sent (HMS
audit assumes Sent rows are immutable).

## Bulk action

**Send all unsent** at the top of the screen re-queues *everything*
that hasn't gone yet — Failed, Paused, Held, plus any rows stuck in
Sending. Useful after fixing the cause of a batch failure (e.g.
WhatsApp logged out for an hour).

## Statuses cheat-sheet

| Status | Meaning | What to do |
|---|---|---|
| Pending | Waiting in the queue. | Nothing — it will send in turn. |
| Sending | Being sent right now. | Nothing — wait a moment. |
| Sent | Delivered to WhatsApp. | Done. |
| Failed | Could not be sent (reason shown). | Fix the issue (e.g. number), press Send. |
| Held / Paused | Held by you, or by a safety rule (throttle, schedule, surge, duplicate). | Releases automatically when the rule clears, or press Send. |

➡ Continue to **[Everyday Use](../everyday-use.md)**.
