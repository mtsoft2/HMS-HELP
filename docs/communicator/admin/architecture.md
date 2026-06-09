# Architecture

A one-page tour of how the Communicator and HMS work together.

## Message flow

```
HMS event (appointment, reminder, prescription, manual click)
                       │
                       ▼
        HMS inserts a row into the message queue
                       │  (status = Pending)
                       ▼
        Communicator polls the queue
                       │
              ┌────────┴────────┐
              ▼                 ▼
   Manual send (Sender)   Auto pickup
              │                 │
              └────────┬────────┘
                       ▼
   Atomically claim the row (status = Sending)
                       │
                       ▼
        Drive WhatsApp Web in background Chrome
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Sent                 Failed
              └────────┬────────┘
                       ▼
        Write result back to the queue row
```

## Components

| Component | What it is | Where it runs |
|---|---|---|
| **HMS** | The hospital application that produces WhatsApp messages. | The HMS web server. |
| **Message queue** | A set of rows in the HMS database. | The HMS SQL Server. |
| **Communicator app** | A tray application that polls the queue and drives WhatsApp Web. | A dedicated Windows PC. |
| **Background Chrome** | The browser instance the Communicator pilots; persistent user-data profile remembers the WhatsApp login. | The same Windows PC. |
| **Watchdog** | A Windows Task Scheduler job that relaunches the Communicator if it isn't running. | The same Windows PC. |
| **WhatsApp Web** | The web client running inside Chrome; speaks to WhatsApp's servers. | Internet. |

## Master switch

HMS only routes WhatsApp to the queue when its master switch is **on**.
When it is off, HMS uses its own legacy WhatsApp path. The
*Install Communicator* / *Uninstall Communicator* buttons flip this
switch for you — no manual config edits.

| Master switch | HMS behaviour |
|---|---|
| **On** | HMS writes new WhatsApp messages to the queue. The Communicator delivers them. |
| **Off** | HMS sends WhatsApp through its legacy code path. The queue is ignored. |

## What the Communicator does *not* do

* It does **not** modify the HMS database schema.
* It does **not** delete data on uninstall.
* It does **not** call WhatsApp's official API — it drives the web
  client of a real WhatsApp account.
* It does **not** parse the HMS payload — text and attachment go to
  WhatsApp as the queue says.

## Why a tray application, not a true Windows service

A real Windows service runs in Session 0 with no interactive desktop
— it cannot drive a browser, scan a QR, or show a tray icon. The
Communicator is therefore a **tray application that auto-starts at
user login** and behaves like a service for every practical purpose
(auto-start, watchdog, hidden window, single instance).

For unattended servers, **[Windows auto-login](install-and-uninstall.md#windows-auto-login)**
plus the watchdog gives true "no human present" operation.

➡ Continue to **[Install & Uninstall](install-and-uninstall.md)**.
