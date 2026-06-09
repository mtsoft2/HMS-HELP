# metasoft NPHIES BridgeProxy

**BridgeProxy** is a small Windows service + tray dashboard that lets
HMS talk to **NPHIES** (Saudi Arabia's national health-information
platform) when the HMS server cannot reach NPHIES directly.

## Why it exists

NPHIES authorises providers by **source IP address**. It accepts FHIR
traffic only from IP addresses that:

* Have been white-listed by NPHIES, **and**
* Are located **inside Saudi Arabia**.

When HMS runs outside KSA (for example, in Lebanon), or from a network
whose public IP is not whitelisted, HMS cannot communicate with
NPHIES directly.

BridgeProxy is installed on a small Windows machine **inside KSA**
with a whitelisted IP. HMS sends its NPHIES traffic to the proxy; the
proxy forwards it to NPHIES from the whitelisted IP and returns the
response verbatim.

## What it does — and what it does not do

| Does | Does not |
|---|---|
| Listens for HMS requests on a TCP port. | Parse the FHIR payload. |
| Forwards bytes to NPHIES. | Modify the request or response. |
| Returns the response verbatim. | Cache, log, or store FHIR data. |
| Counts requests / OK / errors. | Authenticate the HMS caller — it relies on network reach + a shared API key. |
| Tests connectivity to Sandbox / Production. | Replace the NPHIES SSL or certificate handshake — both sides remain end-to-end TLS. |

As a result, **HMS behaviour is unchanged** regardless of its physical
location.

## Two components

| Component | What it is | Runs as |
|---|---|---|
| **BridgeProxy.Service.exe** | The proxy itself. Listens on a TCP port, forwards to NPHIES. | Windows service, auto-start. |
| **BridgeProxy.Tray.exe** | The dashboard — system-tray icon + management window for Start/Stop, configuration, diagnostics. | Per-user, auto-starts at login. |

## Quick map

* **[Getting Started](getting-started.md)** — install, first connection
  test, point HMS at it.
* **[Features](features.md)** — categorised feature list.
* **Dashboard** — one page per tab (Status, Configuration, Send to
  NPHIES).
* **Administration** — installation, uninstall, HMS-side configuration,
  diagnostics.

➡ Continue to **[Getting Started](getting-started.md)**.
