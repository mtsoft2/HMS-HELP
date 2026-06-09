# Metasoft Communicator

## Introduction

**metasSoft Communicator** is an integrated HMS tool that enables clinics
to send WhatsApp messages, documents, reports, invoices, prescriptions,
and image attachments directly to patients, suppliers, and other
contacts from within HMS.

Unlike traditional WhatsApp Business integrations, Communicator does
not depend on third-party messaging gateways, API configurations, or
template approval processes. This reduces implementation complexity,
lowers operational costs, and simplifies ongoing maintenance.

### Key Benefits

* Send WhatsApp messages directly from HMS.
* Attach documents, reports, images, invoices, and prescriptions.
* Eliminate dependency on third-party WhatsApp gateway providers.
* No template creation, submission, or approval requirements.
* Reduce recurring subscription and messaging fees.
* Faster deployment and easier administration.
* Minimise development and support effort across customer installations.
* Simplify localisation and customisation for different clinics and
  regions.
* Ideal for small and medium-sized clinics seeking a cost-effective
  communication solution.
* Provides a flexible foundation for future SaaS deployments while
  remaining simple to operate in on-premises environments.

By eliminating the need to configure and maintain message templates
for each customer, service provider, appointment reminder, or
localised installation, metasSoft Communicator significantly reduces
implementation and support overhead while delivering a seamless
communication experience directly from HMS.

---

## How it works

The Communicator sends WhatsApp messages on behalf of HMS —
appointment reminders, confirmations, prescriptions, documents, and
ad-hoc messages — by driving WhatsApp Web in the background. It lives
in the Windows system tray on a dedicated PC and runs around the
clock.

## What it does

* **Watches the HMS message queue.** When HMS adds a WhatsApp row
  (status *Pending*), the Communicator picks it up, sends it through
  WhatsApp Web, and writes the result back (*Sent* or *Failed*).
* **Lets staff send by hand** from a small in-app screen — pick a
  contact, type the text, attach a file, send.
* **Lists every message** with its delivery status, lets you resend,
  edit, pause, or delete the ones that haven't gone yet.
* **Protects the WhatsApp account** with safety guardrails — pacing,
  per-number caps, per-day cap, duplicate window, sending hours,
  surge break.
* **Stays alive** — auto-starts with Windows, lives in the tray, a
  watchdog relaunches it, a health monitor restarts the sender if it
  stops, session loss is recovered automatically.

## When you need it

* Your HMS server is **outside the WhatsApp Business API** programme,
  or you want to keep using the personal/business WhatsApp account on
  a phone.
* You want **bulk-friendly pacing** and per-recipient limits without
  paying for an API.
* You want HMS staff to be able to send the **odd manual message**
  through the same path that handles the automated traffic.

## Quick map

* **[Getting Started](getting-started.md)** — install, scan the QR
  once, send your first message.
* **[Features](features.md)** — categorised feature list.
* **Screens** — Sender (Start/Stop + manual send + log) and Message
  Queue (every message with actions).
* **[Everyday Use](everyday-use.md)** — common tasks and quick
  troubleshooting.
* **Settings** — the 7 settings tabs.
* **Administration** — architecture, installation, safety guardrails,
  alerts, reliability internals, logs, uninstall.

➡ Continue to **[Getting Started](getting-started.md)**.
