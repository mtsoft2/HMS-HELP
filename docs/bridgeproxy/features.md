# Features

Every BridgeProxy feature, grouped by what it lets you do.

---

## 1. Network bridging

* **Source-IP relay** — every outbound call to NPHIES leaves from the
  bridge's whitelisted IP, regardless of where HMS is located.
* **Verbatim forwarding** — bytes in, bytes out. No payload parsing, no
  rewriting, no caching.
* **TLS pass-through** — end-to-end TLS between HMS and NPHIES is
  preserved.
* **No FHIR coupling** — works for any NPHIES message version without
  upgrades; the proxy is content-agnostic.
* **Allowed-hosts whitelist** — refuses to forward to anywhere other
  than the configured destination hosts.
* **API key** — shared secret between HMS and the bridge; rejects
  unauthorised callers.

## 2. Deployment

* **Single-folder install** — copy `C:\BridgeProxy\`, run
  `INSTALL.cmd`.
* **Auto-installed Windows service** — `BridgeProxy.Service.exe` runs
  on boot as a system service.
* **Auto-installed tray dashboard** — `BridgeProxy.Tray.exe` starts on
  login for every interactive user.
* **Configurable listening port** — chosen during install, changeable
  later from the dashboard.
* **Automatic inbound firewall rule** — installer opens the chosen
  TCP port.
* **Clean uninstall** — `UNINSTALL.cmd` removes the service, firewall
  rules, and scheduled task. Configuration and logs are preserved for
  audit / reinstall.

## 3. Service management (Dashboard → Status)

* **Service state** — Running / Stopped / Starting at a glance.
* **Listening port** — current TCP port.
* **Server IP** — every local IP address of the host (so you know what
  NPHIES sees as your source).
* **Uptime** — time since the service last restarted.
* **Live counters** — Requests / OK / Errors since service start.
* **Start / Stop / Restart** buttons — control the Windows service
  without opening the Services console.

## 4. Connectivity tests

* **Test Sandbox** — TCP + TLS reach to the NPHIES sandbox gateway.
* **Test Production** — same for the production gateway.
* **Diagnostics** — full network diagnostic sweep (DNS, route, TLS
  handshake, gateway reach) in one click.
* **Inbound Check** — verifies HMS can reach the bridge (useful when
  diagnosing whether the issue is HMS-to-bridge or bridge-to-NPHIES).

## 5. Configuration (Dashboard → Configuration)

* **Port** — listening TCP port (changeable; service restarts on save).
* **Timeout** — request timeout in seconds.
* **Allowed Hosts** — comma-separated whitelist of destination hosts
  the proxy will forward to.
* **API Key** — read-only display of the shared secret (rotated via the
  configuration file).
* **Save & Restart Service** — applies any change and restarts the
  service in one click.
* **Open Firewall Port** — re-creates the inbound firewall rule if
  someone has removed it.

## 6. Manual testing (Dashboard → Send to NPHIES)

* **Target selector** — Sandbox / Production / Custom URL.
* **Custom URL** — send a hand-typed request to any whitelisted host
  (useful for testing new endpoints before HMS supports them).
* **Sends from the bridge** — proves the host's NPHIES reach without
  needing HMS to be involved.

## 7. HMS-side configuration (HMS → NPHIES Settings → Bridge)

* **Use Bridge** toggle — switch HMS between *direct* and *bridged*
  NPHIES traffic without restart.
* **Test Connection** — from HMS to the bridge.
* **Configure Firewall (Outbound)** — opens the outbound port from
  the HMS server to the bridge automatically.

## 8. Safety & operations

* **Configuration & logs preserved on uninstall** — re-install is a
  drop-in.
* **No data persistence** — FHIR payloads are not stored anywhere on
  the bridge.
* **Counter-only telemetry** — only Requests / OK / Errors are tracked.

➡ Continue to **[Dashboard → Status](dashboard/status.md)** for
day-to-day operations.
