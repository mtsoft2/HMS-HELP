# HMS Configuration

The bridge does nothing useful until HMS is told to route NPHIES
traffic through it.

## Where

In HMS, open **NPHIES Settings → Bridge**.

## Settings

| Setting | Meaning |
|---|---|
| **Use Bridge** | The master switch. Enable when HMS runs outside KSA or its IP is not static / whitelisted. Disable to send NPHIES traffic directly. |
| **Bridge URL** | The TCP endpoint of the bridge — e.g. `http://203.0.113.10:5500`. Must match the bridge host's reachable IP and listening port. |
| **API Key** | The shared secret. Must match the **API Key** shown on the bridge's *Configuration* tab. |
| **Timeout** | Optional override for the request timeout. |

## Buttons

| Button | What it does |
|---|---|
| **Test Connection** | Sends a no-op to the bridge and verifies the round-trip. Use after any change. |
| **Configure Firewall (Outbound)** | Asks Windows to open the outbound port from the HMS server to the bridge — saves a trip to IT. |

## When to enable

| Situation | Enable Bridge? |
|---|---|
| HMS server inside KSA on a whitelisted static IP. | No — use direct. |
| HMS server outside KSA. | **Yes**. |
| HMS server inside KSA on a dynamic / consumer IP. | **Yes** — until the IP is whitelisted. |
| HMS server inside KSA on a static IP awaiting whitelisting. | **Yes** as a temporary bridge. |
| Multi-site HMS where some sites need bridging and some don't. | Per-site setting — toggle at the right tenant. |

## After enabling

* All existing NPHIES configuration (provider IDs, payer codes,
  eligibility forms) keeps working. The bridge is transparent.
* Response times can go up by a few hundred milliseconds (extra
  network hop). If you see seconds of added latency, the bridge host
  may be on a slow link.

## Switching back to direct

Disable **Use Bridge** and click **Test Connection**. HMS connects to
NPHIES directly again. Any pending submissions in the HMS queue
re-try on the new path.

## Verifying the round-trip

After **Use Bridge** is on:

1. **HMS → Test Connection** turns green.
2. Submit any real NPHIES check (eligibility for any patient).
3. On the bridge **Dashboard → Status**, the **Requests** counter
   ticks up by one and **OK** ticks up by one shortly after.

If Requests ticks but OK does not, the bridge reached HMS but NPHIES
rejected the call — open Diagnostics on the bridge.
