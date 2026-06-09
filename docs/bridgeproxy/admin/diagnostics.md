# Diagnostics

When connectivity isn't green, **Diagnostics** is the one-click sweep
that tells you which layer is broken.

## How to run it

Dashboard → **Status** tab → click **Diagnostics**. The results pane
fills with a tiered report.

## What it tests, in order

The sweep walks the network stack bottom-up so you can fix from the
root.

| Tier | Checks | Failure means |
|---|---|---|
| **DNS** | Can the host resolve `nphies.sa` and the sandbox host name? | DNS server unreachable or misconfigured — fix `ipconfig /all` first. |
| **Route** | Is there an IP route to the gateway? | Default gateway or routing table problem. |
| **TCP** | Three-way handshake to port 443 on the NPHIES host. | Firewall (host or network) blocking outbound 443. |
| **TLS** | Successful TLS 1.2/1.3 handshake. | Outdated TLS stack on the host, or a TLS-intercepting proxy in the way. |
| **Gateway** | Sends a no-op probe to the NPHIES gateway and gets a response. | NPHIES side is up but rejecting — most often, the host's public IP is not whitelisted. |

## Reading the output

* Every tier ends in **OK** or a specific error line.
* Stop at the first failure — fixing it usually clears the ones below.
* The report is plain text — copy it into a support ticket if you
  escalate.

## Adjacent buttons

* **Inbound Check** — separate sweep that verifies HMS can reach
  *this* host (i.e. the bridge from HMS's point of view). Useful when
  bridge → NPHIES is green but HMS still can't submit.
* **Test Sandbox** / **Test Production** — quick green / red on the
  gateway specifically, without running the full DNS/route/TCP/TLS
  walk. Use these for the fast pulse; use Diagnostics when something
  is actually broken.

## Common failures and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| DNS fails. | Wrong DNS server on the host. | Set a working DNS server (Cloudflare 1.1.1.1, Google 8.8.8.8, or your ISP's). |
| Route fails. | Default gateway missing. | Check NIC configuration. |
| TCP fails. | Outbound 443 blocked. | Open the firewall — host AND network. |
| TLS fails. | Old Windows / TLS-intercepting proxy. | Update Windows; bypass the corporate proxy for NPHIES hosts. |
| Gateway fails. | Source IP not whitelisted with NPHIES. | Confirm the host's public IP, contact NPHIES to whitelist. |
| Inbound Check fails. | HMS server can't reach the bridge. | Check the path *from HMS to the bridge*: firewall on bridge, network route, HMS *Bridge URL* value. |
