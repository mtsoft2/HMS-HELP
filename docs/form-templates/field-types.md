# Field Types

Every control on a form has a `Type=`. At render time
[`FormTemp/FT_Control.razor`](https://github.com/mtsoft2/HMS-HELP) lower-cases
that value and dispatches to a concrete Blazor component. **This page lists
every type that dispatcher actually handles** — if a `Type=` isn't in the
table below, the control renders nothing (an empty slot).

Each control lives in a `[<FieldName>]` block and is named in `[Controls]`
(see [Reference](reference.md#controls-the-field-list)). The keys shared by
all controls (`Field`, `Type`, `tab`, `Caption`, `Caption_a`, `Required`,
`wHidden`, `ReadOnly`, `Hint`, `Newline`, `NoLabel`, `Default Value`) are on
the reference page; this page focuses on the **type-specific** keys.

## The complete type list

| `Type=` | Renders | Purpose |
|---|---|---|
| `edit` | `FT_Edit` | Single-line text / number input |
| `memo` / `memo2` | `FT_Memo` | Multi-line text (optionally rich HTML) |
| `richmemo` | `FT_Memo` | Multi-line text (rich variant) |
| `date` | `FT_Date` | Date (with optional time) |
| `checkbox` | `FT_Checkbox` | Boolean, with optional check/uncheck prompts |
| `radio` | `FT_Radio` | Fixed choice, up to 7 options |
| `spinner` | `FT_Spinner` | Numeric up/down within `Min`..`Max` |
| `colorpicker` | `FT_ColorPicker` | Colour picker |
| `dblookup` | `FT_DropDown` | Searchable dropdown from a SQL query |
| `dblookuplong` | `FT_DropDown` | Dropdown variant (no child/edit wiring) |
| `dblist` | `FT_List` | List box from a SQL query |
| `picker` | `FT_Picker` | Multi-column lookup that opens a search dialog |
| `sign` | `FT_Sign` | Electronic signature (stamps date + user) |
| `section` / `wsection` | `FT_Section` | Full-width group divider with a caption |
| `section2` | `FT_Section` (boxed) | Panel-style group (background + fixed region) |
| `sectionend` | *(raw `</div>`)* | Explicitly closes an open section container |
| `panel` | `FT_Panel` | Layout panel |
| `blank` | `FT_Blank` | Empty spacer cell |
| `box` | *(nothing)* | **Suppressed** — the whole control is skipped |
| `label` / `wlabel` | `FT_Text` | Static caption text |
| `label_f` | `FT_Label_C` | Static caption (field style) |
| `image` | `FT_Image` | Static / bound image |
| `chart` | `FT_Chart` | Rendered chart image |
| `grid` | `FT_Grid` | Inline detail grid (a `.GT` template) |
| `searchpad` | `SC_Searchpad` | Embedded list view (a `.ST` template) |
| `report` | `RP_Report` | Embedded report |
| `digest` | `FT_Digest` | Compact record digest that opens a form on click |
| `plate` | `FT_Plate` | Info plate driven by a `Procedure` |
| `dmgallery` | `DM2_Gallery` / `DM_Gallery` | Document/image gallery for the record |
| `document` | `FT_Document` | Single-document upload field |
| `dynamicfields` | `DN_Fields` | User-defined dynamic fields for the record type |
| `notepad` | `NPD_Notepad` | Embedded notes pad |

!!! note "Dead / duplicate branches"
    In the current dispatcher a second `blank` and a second `memo2` branch sit
    after the ones above and never execute — the first match wins. Use `blank`
    and `memo` / `memo2` as documented; the duplicates have no effect.

---

## Data-entry controls

### `edit` — single-line text / number

```ini
[Allergen]
    Caption   = Allergen
    Field     = Allergen
    Type      = edit
    tab       = 0
    Required  = yes
    Units     = mg          ; optional suffix shown after the input
    History   = 0           ; 1 = right-click to pick a previous value
    Refocus   = 0           ; 1 = keep focus after save (rapid entry)
    AutoSelect= 0           ; 1 = select-all on focus
    Format    =             ; display format for numeric columns
    Min       = 0
    Max       = 1000000
```

`DataSize` / `DataType` are read from the **SQL column schema**, not the INI —
you don't set them. Bind numeric columns to `edit` too.

### `memo` / `memo2` / `richmemo` — multi-line text

```ini
[Notes]
    Caption    = Notes
    Field      = Notes
    Type       = memo
    tab        = 1
    HtmlEditor = 0          ; 1 = rich HTML editor instead of a textarea
    Snippet    = 1          ; 1 = allow inserting saved text snippets
    AIPrompts  = memo.aip   ; prompt set for the AI-assist button
    AIContext  =            ; extra context passed to AI-assist
    Width      =
    Height     =
```

`memo` defaults to full width (`col-md-12`). `richmemo` is the rich variant.

### `date` — date (and optional time)

```ini
[OnsetDate]
    Caption    = Onset Date
    Field      = OnsetDate
    Type       = date
    tab        = 0
    Time       = 0          ; 1 adds a time picker
    NoPastDate = 0          ; 1 blocks dates before today
    Format     =            ; e.g. dd/MM/yyyy
```

!!! warning "There is no `datetime` type"
    Use `date` with `Time=1`. A `Type=datetime` isn't in the dispatcher and
    renders an empty slot.

### `checkbox` — boolean

```ini
[IsChronic]
    Caption       = Chronic
    Field         = IsChronic
    Type          = checkbox
    tab           = 0
    CheckPrompt   = Mark as chronic?      ; optional confirm on check
    UnCheckPrompt =                       ; optional confirm on uncheck
    DateField     = ChronicOn             ; stamp this column when checked
```

Binds to a `BIT` column. Give it `Default Value = 0` (not NULL).

### `radio` — fixed choice (up to 7 options)

Options are `Option1..7`; the **stored value** is `Value1..7` (defaults to the
option text). `OptionClass1..7` add a CSS class per option (`wOptionClass1..7`
in the file). Match the column type — a numeric column needs numeric values.

```ini
[Severity]
    Caption  = Severity
    Field    = Severity
    Type     = radio
    tab      = 0
    Option1  = Low
    Option2  = Medium
    Option3  = High
```

For a `TINYINT` column, store numbers:

```ini
    Option1 = Resuscitation
    Value1  = 1
    Option2 = Emergent
    Value2  = 2
```

Storing a label into a numeric column throws
`FormatException: Failed to convert String to Byte`. The control's width grows
with the number of options (3/12 for ≤3, up to 7/12 for 7).

### `spinner` — numeric up/down

```ini
[Quantity]
    Caption = Quantity
    Field   = Quantity
    Type    = spinner
    tab     = 0
    Min     = 0
    Max     = 100
```

### `colorpicker` — colour value

```ini
[TagColor]
    Caption = Tag Colour
    Field   = TagColor
    Type    = colorpicker
    tab     = 0
```

## Lookups

### `dblookup` — searchable dropdown from a query

```ini
[Nationality]
    Caption      = Nationality
    Field        = Nationality
    Type         = dblookup
    tab          = 0
    Lookup Query = SELECT Code, Name FROM Nationality ORDER BY Name
    Key          = Code       ; value stored in the column
    Result1      = Name       ; text shown to the user
    Result2      =            ; optional second display column
    Size1        = 200
    ForceSearch  = 0          ; 1 = require a search before selection
    ChildList    =            ; child dropdowns to refresh on change
    EditObject   =            ; dispatcher action for an inline "edit" button
    EditCommand  =
    EditParam1   =
    SettingObject=            ; dispatcher action for a "settings" button
    SettingCommand =
```

!!! tip "Case-sensitive matching"
    The dropdown matches the stored value against the key with case-sensitive
    equality. If records save `new` but the lookup returns `New`, the control
    shows blank. Keep stored casing consistent with the lookup.

### `dblookuplong` — plain dropdown

A lighter `dblookup` (`Lookup Query`, `Key`, `Result1` only) with no child /
edit / setting wiring.

### `dblist` — list box

Same data keys as `dblookup` (`Lookup Query`, `Key`, `Result1`) but rendered as
a list box rather than a dropdown.

### `picker` — multi-column search dialog

Opens a dialog and returns several columns into `Field`..`Field5`:

```ini
[Physician]
    Caption       = Physician
    Field         = ATTEND_PHY       ; primary value
    Field2        = PhysicianName    ; extra columns filled from the pick
    Field3        =
    Type          = picker
    tab           = 0
    Template      = Physician.ST      ; the search view to open
    InfoProcedure =                   ; optional info SP
    Object        = searchpad
    Command       = find
    Param1        =
    Param2        =
```

## Signature

### `sign` — electronic signature

Stamps the signing user and date, gated by a security code. Can run an SP and
save/close the form on sign.

```ini
[Approval]
    Field          = ApprovedBy
    Type           = sign
    tab            = 0
    Sign_Caption   = Approve
    Date_field     = ApprovedOn       ; column that gets the timestamp
    User_field     = ApprovedBy       ; column that gets the user
    SecCode        = ALLERGY_APPROVE  ; permission required to sign
    Unsign_SecCode = ALLERGY_UNSIGN   ; permission required to un-sign
    Prompt         = Sign this record?
    Unsign_Prompt  = Remove signature?
    Sign_Procedure =                  ; optional SP run on sign
    UnSign_Procedure =
```

## Layout &amp; static controls

### `section` / `wsection` — group divider

A full-width labelled divider that groups the fields listed **after** it in
`[Controls]`. Not a DB column — never put it in a SP, `FieldsMask`, or the PKT
table.

```ini
[Detail]
    Caption = Allergy Detail
    Type    = section
    tab     = 0
    height  = 2           ; divider thickness (px)
    Color2  = $0080BFFF   ; divider colour (BGR hex $00BBGGRR)
```

### `section2` — boxed panel

A panel with a background colour and fixed geometry, used by dashboard-style
tabs that lay out regions side by side (e.g. the ER vitals tab). Keys:
`backcolor`, `backcolor2`, `TopMargin`, `height`, `height2`, `width2`.

### `sectionend` — close a section

Emits a raw closing `</div>`. Only needed when you must explicitly end a
section container before the next one; normal vertical-stack tabs don't need
it (the next `section` starts a new group on its own).

### `panel` / `blank` / `box`

- `panel` — a layout panel (`FT_Panel`).
- `blank` — an empty spacer cell to push the next field onto a new column.
- `box` — **suppressed**: a control with `Type=box` is skipped entirely
  (the outer render guard is `if (Type != "box")`). Use it to keep a field in
  the SP/data but off the screen.

### `label` / `wlabel` / `label_f` — static text

```ini
[Divider]
    Caption = Contact Information
    Type    = label       ; wlabel = same; label_f = field-style label
    tab      = 0
```

`label` is full-width; it shows `Caption` only and binds to no column.

### `image` — picture

```ini
[Logo]
    Caption = Logo
    Field   = Logo
    Type    = image
    tab     = 0
    Image   = logo.png    ; static file, or bound via Field
    Height  = 120
    Width   = 120
```

With `wPosition = absolute` you can also set `Top` / `Left` for absolute
placement.

### `chart` — chart image

```ini
[Trend]
    Caption   = Trend
    Field     = Trend
    Type      = chart
    tab       = 0
    ChartFile = vitals.chart
    Height    = 200
    Width     = 400
```

## Embedded / composite controls

### `grid` — inline detail grid

Registers a `.GT` grid as a child of the form. Register it as a control of
`Type=grid`, then give it a matching block:

```ini
[Controls]
    …
    GT_Activities = grid

[GT_Activities]
    Template = CRM_Activity.GT
    Type     = grid
    Tab      = 1          ; 0-based, same base as fields
    Height   = 280
```

!!! danger "Do not add `MasterID = ID`"
    The framework already passes the form's record ID as the grid master.
    Writing `MasterID = ID` sends the literal string `"id"`. Omit it, or use
    `MasterID = **ID` (double asterisk) if you must be explicit.

### `searchpad` — embedded list view

Embeds a `.ST` view inside the form, scoped to the record.

```ini
[Visits]
    Type     = searchpad
    tab      = 1
    Template = Patient_Visits.ST
    Key1     = [CUST_ID]     ; keys passed to the view's SP
    Key2     =
```

### `digest` — compact record digest

A small multi-row summary; clicking a row opens the target form.

```ini
[LatestLabs]
    Caption       = Latest Labs
    Type          = digest
    tab           = 1
    InfoProcedure = DGS_Labs
    Object        = formtemp
    Command       = edit
    Param1        = Lab_Result.FT
    New           = 0
```

### `plate` — info plate

```ini
[Summary]
    Caption   = Summary
    Type      = plate
    tab       = 0
    Procedure = Allergy_PLATE
```

### `report` — embedded report

```ini
[Statement]
    Type     = report
    tab      = 1
    Template = Patient_Statement
    Key1     = [CUST_ID]     ; Param1 to the report
    Key2     =               ; Param2
```

### `dmgallery` / `document` — attachments

- `dmgallery` — the full document/image gallery for the record (`RecordType` +
  the record ID). Uses the DM2 gallery when imaging version ≥ 2, else the
  legacy gallery.
- `document` — a single-file upload bound to a `Field` plus an `ImageField`
  that holds the bytes.

```ini
[Scan]
    Caption    = Scanned Form
    Field      = ScanName
    ImageField = ScanBytes
    Type       = document
    tab        = 1
```

### `dynamicfields` — user-defined fields

```ini
[Extra]
    Caption    = Additional Fields
    Type       = dynamicfields
    tab        = 1
    RecordType = Allergy
```

### `notepad` — embedded notes

```ini
[Notes]
    Caption    = Notes
    Type       = notepad
    tab        = 1
    RecordType = Allergy
```

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
    Param2   = [CUST_ID]
    Prompt   =                    ; optional confirm before running
    Save     = 0                  ; 1 = save the form first
    Savebuffer = 0
    Close    = 0                  ; 1 = close the form after
    Reload   = 0
    State_Field       =           ; colour the button by a record value
    State_Code_1      =
    State_Color_1     =
    State_Color_Else  =
```

Placeholders resolved before the action runs:

| Token | Resolves to |
|---|---|
| `[ColumnName]` | The current record's column value. |
| `**LAST_PATIENT_ID`, `**UserID`, `**site` | Session values, substituted client-side. |
| `^^NAME` | Passed **literally**; the target SP must detect and resolve it. |

## Automatic column widths

If you don't set a `wClass`, `FT_Control` picks a Bootstrap width by type:

| Type | Default width |
|---|---|
| `section`, `section2`, `wsection`, `notepad`, `grid`, `searchpad`, `memo`, `memo2`, `label` | `col-md-12` (full) |
| `radio` | `col-md-3` … `col-md-7` (grows with option count) |
| `document` | `col-md-6` |
| `button`, `checkbox`, `date`, everything else | `col-md-3` |

An admin can override any field's width at runtime by **right-clicking** it and
choosing `1/12`…`12/12 Screen` (also Hide / New Line / Required) — those
choices are saved as per-user, per-template preferences.

---

**Back to:** [Overview](index.md) · [Getting Started](getting-started.md) ·
[Reference](reference.md) · [Pitfalls](pitfalls.md)
