# Send to NPHIES Tab

A manual-testing utility — send a request straight from the bridge to
NPHIES without HMS being involved. Useful when you need to isolate
whether a failure is on the HMS side or the bridge side.

## Target options

| Target | What it does |
|---|---|
| **Sandbox** | Sends the request to the NPHIES sandbox gateway. Safe — no real claims are created. |
| **Production** | Sends to the production gateway. Use with care — real submissions count. |
| **Custom URL** | Send to any URL within the **Allowed Hosts** whitelist. Useful for testing new endpoints before HMS supports them. |

## When to use this tab

* **HMS reports a NPHIES failure** — replay the same payload from
  here. If the bridge succeeds, the issue is on the HMS side; if it
  fails the same way, the issue is bridge or NPHIES.
* **A new NPHIES endpoint** — verify the bridge can reach it before
  upgrading HMS to use it.
* **Connectivity drill** — quick check from a fresh install before
  pointing HMS at the bridge.

## What does *not* belong here

* **Real clinical submissions** — those should always come from HMS so
  the response is captured against the right patient / claim record.
* **Load tests** — the manual tool sends one request at a time and is
  not designed for performance work.
