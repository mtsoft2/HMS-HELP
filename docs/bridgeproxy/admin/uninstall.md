# Uninstall

Run **UNINSTALL.cmd** as Administrator.

It removes:

* The Windows service.
* The inbound Windows Firewall rule.
* The Scheduled Task that auto-starts the tray dashboard.

It **preserves**:

* The configuration file.
* The logs folder.
* The binaries themselves under `C:\BridgeProxy\`.

This makes re-install a drop-in — run `INSTALL.cmd` again on the same
folder and the previous configuration and logs are picked up.

## Fully removing the install

If you need to wipe the host clean:

1. Run **UNINSTALL.cmd** as Administrator.
2. Delete `C:\BridgeProxy\` (folder + everything inside).
3. (Optional) Archive the `logs\` folder first if you need the audit
   trail.

## Reverting HMS to direct mode

Before you stop the bridge, switch HMS back to direct NPHIES:

1. Open **HMS → NPHIES Settings → Bridge**.
2. **Use Bridge** → off.
3. **Test Connection** — confirms HMS can reach NPHIES directly.

Otherwise HMS keeps trying to send through a bridge that no longer
exists.

## Moving the bridge to another host

The cleanest path:

1. Install BridgeProxy on the new host. Verify Test Sandbox /
   Production both go green.
2. Update **HMS → NPHIES Settings → Bridge → Bridge URL** to point at
   the new host.
3. Click **Test Connection** in HMS — confirms it switched.
4. Uninstall BridgeProxy on the old host.

Both hosts can coexist for a few minutes — the old one simply stops
receiving traffic once HMS is repointed.
