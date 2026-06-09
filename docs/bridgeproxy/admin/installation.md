# Installation

The installer is a single command. It registers the Windows service,
opens the firewall, configures auto-start, and shows the tray icon.

## Prerequisites

* **Windows Server / Windows 10 / 11** with administrator rights.
* The host is **inside Saudi Arabia**.
* The host's **public IP is whitelisted with NPHIES** (or will be).
* The chosen TCP port is **free**.

## Install

1. Copy the BridgeProxy folder to `C:\BridgeProxy\`.
2. Right-click **INSTALL.cmd** → **Run as administrator** (or simply
   double-click and accept the UAC prompt).
3. When asked, enter the listening port. The default **5500** is fine
   for most clinics.
4. Wait for the installer to finish — the tray icon (a shield) appears
   when it's done.

The installer:

* Registers `BridgeProxy.Service.exe` as a Windows service set to
  auto-start at boot.
* Creates an inbound Windows Firewall rule for the listening port.
* Sets `BridgeProxy.Tray.exe` to auto-start at login (Scheduled Task).
* Launches the tray application.

## Post-install checklist

| Step | Where |
|---|---|
| Confirm **Service = Running** | Dashboard → Status |
| Confirm **Test Sandbox** is green | Dashboard → Status |
| Confirm **Test Production** is green | Dashboard → Status |
| Confirm **Allowed Hosts** lists the right NPHIES hosts | Dashboard → Configuration |
| Configure HMS to use the bridge | HMS → NPHIES Settings → Bridge |
| Send a test eligibility check from HMS | HMS |
| Verify counters tick up | Dashboard → Status |

## Where things go

| Item | Location |
|---|---|
| Service binary | `C:\BridgeProxy\BridgeProxy.Service.exe` |
| Tray binary | `C:\BridgeProxy\BridgeProxy.Tray.exe` |
| Configuration file | `C:\BridgeProxy\` (alongside the binaries) |
| Logs | `C:\BridgeProxy\logs\` |
| Firewall rule | Windows Firewall → Inbound Rules → *BridgeProxy* |
| Scheduled Task | Task Scheduler → *BridgeProxy Tray* |

## Multi-user host

The tray dashboard auto-starts at login **per user**. The service is
shared. If several Windows users sign in to the host, each sees their
own tray icon; clicking either opens the same dashboard pointing at
the same service.
