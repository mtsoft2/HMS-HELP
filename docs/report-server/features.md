# Features

Every Report Server V2 feature, grouped by what it lets you do.
Exhaustive but not technical — use it as a training checklist or as a
gap analysis against the legacy V1 catalogue.

---

## 1. Discovery — find a report

* **Welcome page** with a hero block:
    * Title — *Report Catalog*.
    * Helper text — *"Pick a category to see its reports, or use the
      search to find a report by name or description."*
    * Tile-per-category grid (icon + name + report count).
* **Category sidebar** on the left:
    * Two stat tiles at the top — total **Reports**, total
      **Categories**.
    * Category list, each row with an icon, name, and count badge.
    * *All Categories* shortcut at the top of the list.
    * Selected category highlighted.
    * Empty-tree message — *No reports match your search* — when the
      search excludes every category.
* **Live search box** in the header:
    * Searches report **name** *and* **description**.
    * Filters both the sidebar and the main pane as you type.
    * **Clear** (✕) button appears once there's text.
    * Empty-state messages in the pane — *No reports match your search*
      and *No reports match your search in this category*.
* **Filter pills** in the header:
    * **Favorites** — show only reports you've marked as favourite.
    * **All** — show every report (default).
* **Category drill-down**:
    * Big folder icon + category name + total report count.
    * Reports grouped by **sub-category** (defaulting to *General* when
      no sub-category is set).
    * Each report shown as a card with an icon, title, and description.
* **Breadcrumb** in the report view — Catalog › Category ›
  Sub-category › Report Title.

## 2. Navigation

* **Hamburger button** in the header — toggle the sidebar open / closed.
* **Brand button** — *Report Catalog · V2 badge* — click to return to
  the welcome state.
* **Back to Catalog** tooltip on the brand button.
* **Back arrow / Back button**:
    * From a report → back to its category.
    * From a category → back to the welcome state.
* **Breadcrumb links** — click *Catalog* or the category name to jump
  back.
* **Close** (✕) button in the header — returns to the screen the user
  opened the catalogue from. Falls back to the home screen if there
  is no history.
* **RTL support** — back arrow flips direction; sidebar moves to the
  right when the language is Arabic.

## 3. Reports list — cards

Each report card shows:

* File icon.
* **Title** (the report's display name).
* **Description** (when defined).
* A chevron on the right to hint it's clickable.

States:

* Hover effect.
* Click → opens the report.
* Disabled / hidden when the user doesn't have access (driven by
  Security).

## 4. Report parameter panel

When a report is open, its parameters are rendered as a form. Five
control types are supported:

| Type | What you see |
|---|---|
| **Edit (text)** | A plain text input — for free-text filters such as patient name fragment, account number. |
| **Date** | A date picker — for date-from / date-to filters. Default values are decoded from preset tokens (today, first-of-month, etc.). |
| **Dropdown (lookup)** | A searchable dropdown filled from a database lookup — e.g. branches, departments, physicians, payers. |
| **Radio** | Mutually-exclusive options (e.g. *Detailed / Summary*, *Active / Inactive*). |
| **Checkbox** | On/off flags (e.g. *Include cancelled*, *Show inactive*). |
| **Hidden** | Parameters that exist but are not shown — pre-filled from context. |

Every control carries:

* A **caption** (what it filters by).
* A **default value**.
* An **option to disable / hide** based on context.

## 5. Running a report

* **Print Preview** button at the bottom of the parameter pane.
* A loading spinner while the report renders.
* Errors surfaced inline (red banner) with the message and a
  developer trace strip when debug is on.

## 6. Output & sharing

From the preview window the user can:

* **Print** to a connected printer.
* **Save as PDF**.
* **Export to Excel** (when the layout supports it).
* **Export to Word**.
* **Email** the rendered file.
* **Re-render** without leaving the preview after changing a
  parameter.

## 7. Personalisation — per user

Three switches at the top of the report-parameter pane let the user
pin a report to one of three personal surfaces:

* **Favorite** — surfaces under the Favorites pill and the user's
  favourite-reports list.
* **Report List** — surfaces under the module's *Reports* quick list.
* **QuickBar** — surfaces under the QuickBar shortcuts row.

All three are independent; a report can be on any / all / none.

## 8. Security

* Each report has its own access-rights mapping.
* Reports the user can't access don't appear in the catalogue at all.
* Right-click on the report header → **Access Rights** opens the
  per-report security editor for admins.
* The catalogue obeys the session timeout — when the session expires
  the report list re-fetches with the user's current permissions.

## 9. Internationalisation

* All catalogue labels (search, filters, breadcrumb, empty states,
  buttons) are localised — English / Arabic out of the box.
* The report **Title** is localised too.
* **RTL layout** flips the sidebar, the breadcrumb chevrons, and the
  back-arrow icon.
* Number / date formats follow the user's locale.

## 10. Empty / edge states

* Sidebar empty tree — *No reports match your search*.
* Category empty pane — *No reports match your search in this category*.
* Welcome empty pane — *No reports match your search* (when the search
  excludes everything).
* Tabs / cards never render without their counts.

## 11. UI quality-of-life

* Live search — no submit button needed.
* Clear-search button appears only when the box has text.
* Sidebar state (open / closed) persists per session.
* Sticky header — search and filters remain reachable while scrolling
  the catalogue.
* Cards adapt to screen width — phones, tablets, big monitors.
* Light / dark theme follows the HMS app theme.
* Icons throughout: folder tree (brand), folder (category), file
  (report), heart (favourites), printer (preview), magnifying glass
  (search), chevron (drill-down), bars (hamburger), info (description),
  arrow-left/right (back).
* **Stat counters** in the sidebar update live as the search narrows
  the visible set.

## 12. Categories & organisation

* Two-level category hierarchy — **Category** and **Sub-category**.
* Sub-category defaults to *General* when omitted.
* Reports are listed alphabetically inside each sub-category.
* Categories are listed alphabetically inside the sidebar.
* Per-category and per-sub-category headings show the count of
  reports they contain.

## 13. Per-report descriptions

* Each report can carry a **short description** that:
    * Appears under its name on the card in the category view.
    * Appears as an info strip above the parameter pane in the report
      view.
* Searched alongside the title — so a user can find a report by what
  it shows rather than what it's called.

## 14. Direct-launch (deep link)

* Reports can be launched directly by URL (bookmarkable / linkable
  from dashboards and other forms) — the catalogue opens straight on
  the parameter pane, ready to preview.
* Pre-fill parameters via URL query so a dashboard tile can open a
  pre-filtered report.

## 15. V1 ↔ V2 coexistence

* V2 ships alongside the legacy catalogue — the **V2** badge in the
  header is your reminder which one you're in.
* Both versions read the same report definitions, so a report is
  available in both immediately without re-cataloguing.
* The user can choose V1 / V2 as their default catalogue in personal
  preferences.

## 16. Integration points

* **Favourites / Report List / QuickBar** — the same personalisation
  back-end every other HMS surface uses, so favouriting a report here
  surfaces it on the dashboard's quick reports list too.
* **Localisation** — central HMS translation dictionary.
* **Security** — central HMS role / access-rights store.
* **Report engine** — the same Crystal-Reports-based engine for
  output; V2 only replaces the catalogue / launcher.

➡ Back to **[Overview](index.md)** or jump to **[Getting Started](getting-started.md)**.
