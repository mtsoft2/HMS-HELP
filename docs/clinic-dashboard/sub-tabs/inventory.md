# Inventory

Stock visibility for the clinic — what's full, what's empty, what's
about to run out.

## Headline counters

* **In stock** — items above their minimum threshold.
* **Low stock** — items below minimum but above zero.
* **Out of stock** — items at zero on-hand.
* **Total items** in the catalogue.
* **Stock value** — current inventory value in the configured
  currency.
* **Critical alerts** count — items that need attention right now.

## Cards

### Stockout risk

Items currently at zero or trending to zero in the next few days:

| Column | Meaning |
|---|---|
| **Item** | Item / SKU name. |
| **Location** | Where the stock should be. |
| **On hand** | Current quantity. |
| **Min** | Minimum threshold. |
| **Action** | Quick replenishment link. |

### Stock by location

A per-location breakdown — chair, pharmacy, store, fridge, …:

* Counts of items per location.
* **Distribution** view shows the share of stock held at each
  location (useful for asking *"why is so much stock locked in
  the back store?"*).

### Low-stock alerts

A list of every item below its minimum threshold, sorted by severity:

* **Item** name.
* **On hand** vs **Min** with a visual **Stock vs min** bar.
* **Location** of the deficit.
* Click **Open <item>** → opens the item record.

### Top movers · last 90 days

Leaderboard of items by consumption:

* **Volume** — how many units used.
* **Revenue** — money invoiced under this item (when it is also a
  billable service).
* Toggle between Volume and Revenue.
* Click **Open <item>** → opens the item record.

## What you do with it

* **Morning stock check** — In stock + Low stock + Out of stock
  answer "are we safe to open today".
* **Replenishment list** — Stockout risk + Low-stock alerts is the
  buyer's work list for the day.
* **Allocation tuning** — Stock by location shows whether you're
  hoarding in the store while running empty in the chair.
* **Catalog cleanup** — Top movers tells you what to keep stocking
  and what is dead weight.

➡ Continue to **[Quality](quality.md)**.
