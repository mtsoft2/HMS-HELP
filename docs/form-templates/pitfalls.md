# Pitfalls &amp; Pre-ship Checklist

These are the failures that have actually bitten people building `.FT` forms.
Most produce a blank form or a cryptic exception on open — the cause is almost
always one of the items below.

## Trailing `[Main]` wipes `[MAIN]` { #trailing-main }

**Symptom:** clicking a "New" button throws
`System.FormatException: Input string was not in a correct format`
(around `FT_FormTemp.razor:2291`), or the form opens blank.

**Cause:** the INI parser lower-cases section names and stores them in a
case-insensitive dictionary. `[MAIN]` and a second `[Main]` collapse to the
same key, and the **second one wins** — replacing all your settings with an
empty block. `PKT_Table`, `IDField`, `Table` all come back empty, the SPID
lookup becomes invalid SQL, and the resulting empty string fails to parse.

**Fix:** keep `__CDC=0` **inside** `[MAIN]`. Never add a separate `[Main]`
section.

```ini
[MAIN]
    Title     = Allergy
    …
__CDC=0          ✓ inside [MAIN]

[Banner]
    …
```

```ini
[MAIN]
    Title     = Allergy
    …

[Main]           ✗ WRONG — wipes everything above
__CDC=0
```

This applies to **every** template type — `.FT`, `.ST`, `.GT`, `.BND`,
`.DSH` — they all use the same parser.

## Tab numbering is mixed-base { #tab-off-by-one }

- `[Tabs] count = N` and the `[Tab1]…[TabN]` headers are **1-based**.
- The `tab =` value **inside a field block** is **0-based** (`tab=0` = first
  tab).

Put a field on `tab=1` thinking it's the first tab and it lands on the second
one — or, if you only have one tab, on a tab that doesn't exist, which renders
empty and throws a server exception.

## The selector SP must return `_Hide / _Disable / _Readonly`

`FT_SP_<Entity>` **must** end with the three synthetic columns
`_Hide`, `_Disable`, `_Readonly` (empty strings are fine). The renderer reads
them to drive dynamic hide/disable/lock. Omit them and field binding breaks.

!!! note "Grids are different"
    Inline-grid selectors (`GT_SP_<Entity>`) must **not** return those three
    columns — the grid loader copies the SP's result columns into the real
    table and errors on `_hide` not existing. FT selectors include them; GT
    selectors don't.

## Parent ID arrives as `@Param2`, not `@Param1`

When a form is opened "new" from a list-view toolbar, the parent/visit ID is
passed as **`@Param2`**. `@Param1` is the form's own `New_Param1` (usually
blank). Always declare `@Param1`…`@Param5` on the New SP — some dispatcher
paths pass `@Param3` and `@Param5` too, and a shorter signature throws
"Procedure has too many arguments specified".

## `Radio` values must match the column type

Options render as labels but **store `Value1..7`**. For a numeric column, set
the values to numbers:

```ini
    Option1 = Low
    Value1  = 1
```

Storing the label text into a `TINYINT`/`INT` column throws a conversion
exception on save.

## Save Arabic files as Windows-1256

The parser reads `.FT` files as **CP1256** by default. If you save the file as
UTF-8, Arabic `Caption_a` values become mojibake. Use an editor that can save
CP1256, or set `CodePage=` in `[MAIN]` to match how you saved it.

!!! warning "PowerShell can corrupt these files"
    `Get-Content` / `Set-Content` in Windows PowerShell 5.1 re-encode BOM-less
    files and mangle Arabic. Edit `.FT` files with a proper editor, not a
    PowerShell round-trip.

## Deploying to Assets only does nothing

The app reads templates from the **runtime** `…\FTP\` folder
(`Global.RootPath\FTP` — `D:\hms909_kyan\FTP\` on the current install), not
from `E:\Work\Assets\FTP\`. Copy to the runtime folder and hard-refresh; the
process caches templates on first read, so a navigate-away/back or app restart
may be needed.

## Pre-ship checklist { #pre-ship-checklist }

Run through this before you consider a form done:

- [ ] `[MAIN]` has no duplicate/trailing `[Main]`; `__CDC=0` is inside it.
- [ ] `Table` and `PKT_Table` both exist and the PKT has `SPID` + `_Deleted`.
- [ ] `Procedure` (selector) exists **and** returns the three
      `_Hide/_Disable/_Readonly` trailing columns.
- [ ] `Procedures.New` and `Procedures.Delete` resolve to real SPs.
- [ ] The New SP declares `@Param1`…`@Param5` and reads the parent from
      `@Param2`.
- [ ] Every field's `Field=` is a real column on the table.
- [ ] Every `tab=` value is 0-based and within `[Tabs] count`.
- [ ] `RecordType` uses underscores matching the table name.
- [ ] `IDCounter` column exists on `SYS2`.
- [ ] Any `Radio` on a numeric column stores numeric `Value1..N`.
- [ ] Arabic captions saved in CP1256.
- [ ] File copied to the runtime `…\FTP\` folder, browser hard-refreshed.

---

**Back to:** [Overview](index.md) · [Getting Started](getting-started.md) ·
[Reference](reference.md) · [Field Types](field-types.md)
