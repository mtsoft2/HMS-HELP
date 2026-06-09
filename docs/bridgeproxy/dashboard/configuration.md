# Configuration Tab

Settings the bridge service uses. Changes apply on **Save & Restart
Service**.

## Settings

| Setting | What it does |
|---|---|
| **Port** | The listening TCP port. Default 5500. Change if the chosen port is already in use; the firewall rule is updated automatically. |
| **Timeout** | Request timeout in seconds. Increase only if NPHIES is intermittently slow — long timeouts hold connections open and can hide real outages. |
| **Allowed Hosts** | Comma-separated whitelist of destination hosts the proxy will forward to. Requests for anything outside this list are rejected. Pre-populated with the sandbox and production NPHIES hosts. |
| **API Key** | Read-only display of the shared secret between HMS and the bridge. Rotate by editing the configuration file directly on the host. |

## Buttons

| Button | Effect |
|---|---|
| **Save & Restart Service** | Persists changes to the configuration file and restarts the service so the new values take effect. There is a brief window where the proxy is unavailable — schedule for low-traffic times. |
| **Open Firewall Port** | Re-creates the inbound Windows Firewall rule for the current port. Use this if someone manually removed the rule, or after changing the port. |

## Allowed Hosts — what to put in

Only the NPHIES hosts you legitimately need:

* `nphies.sa` and any production sub-domains.
* `sandbox.nphies.sa` for testing.

Do **not** widen the list to include arbitrary internet hosts — the
whitelist is the only place that limits what the proxy can reach.

## Port — picking a safe value

* Default **5500** works for most clinics.
* Avoid common ports (80, 443, 3389, 5432, 1433, 1521) — they
  collide with web servers, RDP, databases.
* Pick from the registered range (1024 – 49151).
* Whatever you pick, the HMS *Bridge URL* on the HMS side has to
  match — change one, change both.

➡ Continue to **[Send to NPHIES](send-to-nphies.md)**.
