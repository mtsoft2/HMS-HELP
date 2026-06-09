# Getting Started

Install BridgeProxy, verify it reaches NPHIES, and point HMS at it.

## 1. Pick the host machine

* It must be **inside Saudi Arabia**.
* Its **public IP** must be one of the IPs already whitelisted with
  NPHIES (or about to be whitelisted).
* **Windows Server** or Windows 10/11 with admin rights.
* Always-on — the HMS server depends on it for every NPHIES call.

## 2. Install

1. Copy the BridgeProxy folder to `C:\BridgeProxy\`.
2. Run **INSTALL.cmd** and accept the UAC prompt.

During first launch the installer:

* Asks for the listening port (default: **5500**).
* Installs and starts the Windows service.
* Creates an inbound Windows Firewall rule.
* Configures the tray application to start automatically at login.
* Displays the tray icon (a shield).

## 3. Open the dashboard

Double-click the shield tray icon. The dashboard window opens on the
**Status** tab.

Confirm:

* **Service** shows *Running*.
* **Port** shows the port you chose.
* **Server IP** lists the host's local IP addresses.

## 4. Test connectivity to NPHIES

Click **Test Sandbox** — verifies the host can reach the NPHIES
sandbox gateway. Should turn green.

Click **Test Production** — same for the production gateway.

If either fails:

* Open **Diagnostics** (next button) for a full network report.
* Confirm the host's **public IP** is whitelisted with NPHIES.

## 5. Configure HMS to use the bridge

On the HMS application server:

1. Open **NPHIES Settings → Bridge**.
2. **Use Bridge** → enable. (Enable this when HMS runs outside KSA or
   its IP is not static / whitelisted.)
3. Set the **Bridge URL** to the BridgeProxy host
   (e.g. `http://203.0.113.10:5500`).
4. Click **Test Connection** — HMS should be able to reach the proxy.
5. (Optional) Click **Configure Firewall (Outbound)** to open the
   outbound port from HMS to the bridge automatically.

## 6. First real submission

Send any normal NPHIES message from HMS — eligibility check,
pre-authorization, claim. The proxy forwards it; HMS gets the same
response it would have received talking to NPHIES directly.

On the dashboard, the **Requests / OK / Errors** counters tick up.

## 7. Verify from the bridge side

Click **Inbound Check** in the dashboard — confirms HMS can still
reach the bridge.

Use **Send to NPHIES** (third dashboard tab) to send a manual test
request from the bridge itself — handy when troubleshooting whether
the issue is HMS or the bridge.

➡ Continue to **[Features](features.md)** for the complete catalogue,
or **[Dashboard → Status](dashboard/status.md)** for day-to-day use.
