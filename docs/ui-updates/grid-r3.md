# Grid R3 — Enhancements & Usability Improvements

Every data grid in HMS gets a top-to-bottom overhaul in **Grid R3**.
The result is a grid that behaves like a modern spreadsheet —
faster keyboard entry, better visibility for big datasets, flexible
column management, and improved fullscreen usability.

## Layout & Visibility

* **Sticky headers while scrolling** — column headers remain visible
  when scrolling long or maximised grids.
* **Fullscreen / maximise mode** — expand the grid to fill the entire
  screen, then restore it back instantly.
* **Search-as-you-type filtering** — quickly filter rows using the
  built-in search box.
* **Loading & empty states**
    * **Loading spinner** appears while data is being fetched.
    * Empty grids display a clean **“No Records Found”** message
      instead of a blank area.

## Column Features

### Show / hide columns

* **Right-click the grid header** to choose which columns are visible.
* Column visibility preferences are remembered per user.

### Column reordering

* **Drag and drop column headers** to rearrange columns.

### Parent / grouped headers

* Related columns can appear under a shared parent caption such as:
    * **Pricing**
    * **Tax**
    * **Patient Information**

### Column sorting

* **Click once** → Ascending.
* **Click again** → Descending.
* **Click a third time** → Clear sorting.
* Active sort direction is shown with an arrow indicator.

### Footer summaries

* Footer rows can display **totals and sums** for selected numeric
  columns.

## Row Features

### Row number column (#)

* Every grid now includes a fixed **row-number column** on the left
  side.
* The footer of the # column displays the **total number of records**.

### Row density / resize modes

* Switch between:
    * **Compact**
    * **Normal**
    * **Comfortable**
* Preferences are automatically saved and restored.

### Duplicate row

* **Right-click any row** and choose **Duplicate** to insert a new row
  containing the same values as the selected row.

## Editing & Keyboard Navigation

### Single-click editing

* Click any cell and start typing immediately — **no double-click
  required**.
* New typing automatically **replaces** the existing value.

### Spreadsheet-style keyboard navigation

| Key | Action |
|---|---|
| **Tab / →** | Move forward |
| **Shift + Tab / ←** | Move backward |
| **↑ / ↓** | Move vertically |
| **Enter** | Move to the first editable cell in the next row |

### Automatic row creation

Pressing **Enter** on the last row automatically creates a new row and
moves focus into it.

### Selected cell highlighting

The active cell is **visually highlighted** at all times.

### Auto-select existing text

When entering a cell, the **current text is automatically selected**
so typing immediately replaces it.

### Read-only cells

Read-only cells are **skipped automatically** during keyboard
navigation.

## Toolbar Improvements

* **Show / hide toolbar buttons** — right-click the toolbar to choose
  visible buttons.
* **Modern icon toolbar** — toolbar buttons now use cleaner, simplified
  icons for a more modern appearance.

## Overall Experience

The grid now behaves much more like a modern spreadsheet application,
offering:

* **Faster keyboard-based editing**
* **Better visibility for large datasets**
* **Flexible column management**
* **Improved fullscreen usability**
* **Faster navigation and data entry workflows**
