# Field Types

Every control on a form has a `Type=`. This page lists the types the
dispatcher supports and the keys each one needs. All of them live in a
`[<FieldName>]` block and are named in `[Controls]` (see
[Reference](reference.md#controls-the-field-list)).

## Data-entry controls

### `edit` — single-line text/number

```ini
[Allergen]
    Caption   = Allergen
    Field     = Allergen
    Type      = edit
    tab       = 0
    Required  = yes
```

Bind numeric columns to `edit` too; use `Format` for display formatting and
`Min`/`Max` if you want spinner bounds.

### `memo` — multi-line text

```ini
[Notes]
    Caption    = Notes
    Field      = Notes
    Type       = memo
    tab        = 1
    HtmlEditor = 0        ; 1 = rich HTML editor instead of plain textarea
```

### `Date` — date (and optional time)

```ini
[OnsetDate]
    Caption    = Onset Date
    Field      = OnsetDate
    Type       = Date
    tab        = 0
    Time       = 0        ; 1 adds a time picker
    NoPastDate = 0        ; 1 blocks dates before today
```

!!! warning "There is no `datetime` type"
    Use `Type=Date` with `Time=1`. A `Type=DateTime` renders an empty slot —
    the dispatcher has no branch for it.

### `Radio` — fixed choice

Options are `Option1..7`; the stored value is `Value1..7` (defaults to the
option text). **Match the column type** — a numeric column needs numeric
values.

```ini
[Severity]
    Caption  = Severity
    Field    = Severity
    Type     = Radio
    tab      = 0
    Option1  = Low
    Option2  = Medium
    Option3  = High
```

For a `TINYINT` column store numbers, not labels:

```ini
    Option1 = Resuscitation
    Value1  = 1
    Option2 = Emergent
    Value2  = 2
```

Storing a label into a numeric column throws `FormatException: Failed to
convert String to Byte`.

### `Checkbox` — boolean

Binds to a `BIT` column. Give it a `Default Value` of `0` (not NULL) so a new
record saves cleanly.

### `dblookup` — pick from a query

```ini
[Nationality]
    Caption      = Nationality
    Field        = Nationality
    Type         = dblookup
    tab          = 0
    Lookup Query = SELECT Code, Name FROM Nationality ORDER BY Name
    Key          = Code       ; the value stored in the column
    Result1      = Name       ; the text shown to the user
    Size1        = 200
```

!!! tip "Case-sensitive matching"
    The dropdown matches the stored value against the lookup's key with
    case-sensitive equality. If records save `new` but the lookup returns
    `New`, the control shows blank. Keep stored casing consistent with the
    lookup.

## Layout controls (not stored in the DB)

### `section` — a group divider

A labelled horizontal divider that groups the fields listed **after** it in
`[Controls]`. Not a DB column — never put it in a SP, `FieldsMask`, or the
PKT table.

```ini
[Detail]
    Caption  = Allergy Detail
    Type     = section
    tab      = 0
    height   = 2          ; divider thickness
    Color2   = $0080BFFF  ; divider colour (BGR hex $00BBGGRR)
```

### `section2` — a boxed panel

A panel with a background colour and fixed geometry, used by dashboard-style
tabs that lay out fixed regions side by side (e.g. the ER vitals tab). Keys:
`backcolor`, `backcolor2`, `TopMargin`, `height`, `height2`, `width2`.

!!! info "Ordering"
    A section's position is set by where its name appears in `[Controls]`,
    **not** by where the `[<SectionName>]` block sits in the file. A section's
    `tab=` must match the `tab=` of the fields beneath it.

## Action controls

### `button` — run a dispatcher action

```ini
[OpenLabs]
    Caption  = Open Lab Results
    Type     = button
    tab      = 0
    Object   = searchpad          ; formtemp | searchpad | dashboard | …
    Command  = open               ; new | edit | open | find | …
    Param1   = Lab_Results.ST
    Param2   = [CUST_ID]          ; [Col] = current record's column value
```

Placeholders resolved before the action runs:

| Token | Resolves to |
|---|---|
| `[ColumnName]` | The current record's column value. |
| `**LAST_PATIENT_ID`, `**UserID`, `**site` | Session values, substituted client-side. |
| `^^NAME` | Passed **literally**; the target SP must detect and resolve it. |

### `grid` — an inline detail grid

Registers a `.GT` grid as a child of the form. Register it as a control of
`Type=grid`, then give it a matching block:

```ini
[Controls]
    …
    GT_Activities = grid

[GT_Activities]
    Template = CRM_Activity.GT
    Type     = grid
    Tab      = 1          ; 0-based, same as fields
    Height   = 280
```

!!! danger "Do not add `MasterID = ID`"
    The framework already passes the form's record ID as the grid master.
    Writing `MasterID = ID` sends the literal string `"id"`. Omit it, or use
    `MasterID = **ID` (double asterisk) if you must be explicit.

Other supported types you'll see in existing forms: `picker`, `sign`
(signature with `Sign_Procedure` + `SecCode`), `chart`, and the numeric
spinner variants. Grep the `[Controls]` blocks of a similar shipped form for a
working example before inventing a new pattern.

---

**Next:** [Pitfalls & pre-ship checklist →](pitfalls.md)
