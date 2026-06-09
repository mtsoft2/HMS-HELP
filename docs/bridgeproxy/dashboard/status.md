# Status Tab

The **Status** tab is the dashboard's home page — live service
information and one-click control of the service.

## Live service information

| Field | What it shows |
|---|---|
| **Service** | Running, Stopped, or Starting. |
| **Port** | The TCP port the service is listening on. |
| **Server IP** | Every local IP address the host has — what NPHIES sees as your source IP. |
| **Uptime** | Time since the service was last restarted. |
| **Requests / OK / Errors** | Live counters since service start. |

The counters give you a real-time pulse — if Requests is climbing but
OK is flat, something downstream is broken; if Requests is flat,
something between HMS and the bridge is broken.

## Action buttons

| Button | What it does |
|---|---|
| **Start** | Starts the Windows service. |
| **Stop** | Stops the Windows service. Use sparingly — HMS NPHIES traffic halts immediately. |
| **Restart** | Stop + Start, useful after a configuration change saved without the *Save & Restart Service* button. |
| **Test Sandbox** | TCP + TLS reach to the NPHIES sandbox gateway. Green = good. |
| **Test Production** | Same as Test Sandbox, against the production NPHIES gateway. |
| **Diagnostics** | Runs a full network diagnostic sweep — DNS resolution, route, TLS handshake, gateway reach. Output appears in a results pane. |
| **Inbound Check** | Verifies HMS can reach the bridge — answers *"is the problem on the HMS side?"* in one click. |

## Reading the test results

* **Green** = success. The bridge has full reach.
* **Yellow / orange** = degraded. Partial reach (TCP fine, TLS fails;
  or one gateway reachable, the other not).
* **Red** = failure. Open **Diagnostics** for the detailed report and
  fix from the bottom up: DNS → route → TLS → gateway.

➡ Continue to **[Configuration](configuration.md)**.
