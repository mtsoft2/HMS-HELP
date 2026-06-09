# Administration

What the clinic administrator can configure on the Clinic Dashboard.

## Sub-tab visibility per role

Each of the eight sub-tabs (Overview, Schedule, Census, Billing,
Physicians, Inventory, Quality, CRM) can be turned on or off per user
role:

* **Clinical roles** typically see Overview, Schedule, Census,
  Physicians, Quality.
* **Finance / billing roles** typically see Overview, Billing,
  optionally CRM.
* **Front desk** typically see Overview, Schedule.
* **Clinic manager / director** sees everything.

Turn off any sub-tab a role does not need — a smaller dashboard is a
faster, less confusing dashboard.

## Card show / hide

Inside each sub-tab, every card can be hidden by the user via
right-click → *Hide this card*. Preferences are per user and persist
across sessions. The administrator does not need to push these — let
each user tune their own page.

## Currency

The dashboard reads the clinic's configured currency to label every
monetary tile and to format every amount. Set it under
**Clinic Settings → Currency**. If unset, the dashboard falls back
to **SAR**.

## Auto-refresh interval

How often the dashboard re-pulls live numbers. Defaults to a few
minutes. Tune up for high-traffic dashboards (wall displays) or down
for slow networks.

## Demo data

For new installs and training environments, the **Fill Demo Data**
action seeds plausible numbers into the underlying tables so the
dashboard renders meaningfully on day one. Turn it off (and clear
the demo data) before going live.

## Wall-display mode

The dashboard runs full-screen on any modern browser. For a permanent
wall display:

* Open the dashboard URL in full-screen (F11).
* Pin the **Overview** or **Schedule** sub-tab.
* Set the browser to keep the tab awake.
* Auto-refresh keeps the numbers fresh without manual intervention.

## Permissions

Beyond visibility, drill-down clicks respect the user's permission
on the underlying record. A user can see *"23 no-show appointments
today"* without necessarily being able to open one — in that case
the click is suppressed.
