# Section &amp; Key Reference

Every key below is one the runtime **actually reads** — the list is taken
from the `ini.GetValue(...)` calls in `FT_FormTemp.razor`, `FT_Tabs.razor`
and `FT_Banner`. Defaults shown are the runtime defaults (what you get if the
key is absent). Keys are case-insensitive.

## `[MAIN]`

The form's identity and data binding.

| Key | Default | Meaning |
|---|---|---|
| `Title` | *(empty)* | Window title. Passed through translation + `FT_Decode`. |
| `Procedure` | *(empty)* | **Selector SP** — loads one record (`FT_SP_<Entity>`). |
| `Table` | *(empty)* | Real table name. |
| `PKT_Table` | *(empty)* | Editing-buffer table (`PKT_<Entity>`). |
| `IDField` | *(empty)* | Primary-key column. |
| `IDField2` | *(empty)* | Secondary key column (composite keys). |
| `IdentityField` | *(empty)* | Column that is a SQL IDENTITY, if any. |
| `IDCounter` | *(empty)* | `SYS2` counter column the `_New` SP increments. *(By convention; the runtime keys off `IDField`.)* |
| `IDisString` | `0` | Treat the ID as a string. **Auto-forced true when `Table = admision`.** |
| `RecordType` | *(empty)* | Binder record type; drives banner + document routing. Use underscores (`ER_Consult`). |
| `SingleRecord` | `0` | `1` hides the record-ID navigator (one-record-per-form). |
| `wClass` | *(empty)* | Extra CSS class on the form root. |
| `wMinHeight` | `500` | Minimum body height in px. |
| `idTagField` | `id` | Field used as the DOM id tag. |
| `CodePage` | `1256` | File encoding. `1256` = Arabic (Windows-1256); set `65001`-style only if the file is UTF-8. |
| `wLanguage` | *(unset)* | `1` forces bilingual on; `0` forces off. |
| `Version` | `0` | Form version stamp. |
| `SaveConfirmation` | `1` | `0` saves without the confirm prompt. |
| `ShowLogo` | `0` | Show the corporate logo on the form. |
| `External` | `0` | Marks the form as opened from an external context (affects locking). |
| `InitAutoSave` | `0` | Auto-save a new record immediately on open. |
| `DataManagement` / `DM` | `1` | `0` hides the document-gallery side button. |
| `Notes` | `1` | `0` hides the Notes side panel. |
| `History` | `1` | `0` hides the record-history toggle. |
| `ImageFields` | *(empty)* | Fields rendered as images. |
| `Notepad_RecordType` | *(empty)* | Record type used by the Notes panel, if different. |
| `ReadOnly_Exclude` | *(empty)* | Fields that stay editable even when the form is read-only. |
| `ServerCode` | *(empty)* | `imaging` switches to imaging-server plumbing. |

!!! note "`__CDC=0`"
    Put the checksum key `__CDC=0` on its own line **inside `[MAIN]`**. The
    runtime recomputes it. A separate `[Main]` section for it silently wipes
    every `[MAIN]` setting — see [Pitfalls](pitfalls.md#trailing-main).

## `[Banner]`

Optional strip at the top of the form.

| Key | Default | Meaning |
|---|---|---|
| `Show` | `0` | `1` renders the banner. |
| `Procedure` | *(empty)* | Banner SP returning bracketed display columns. |
| `ID` | *(empty)* | Override the ID passed to the banner SP. |
| `height` | *(FT_Banner)* | Banner height in px. |
| `EnableColor` | *(off)* | `1` lets the banner SP drive its background colour. |
| `EnableBorderColor` | *(off)* | `1` lets the banner SP drive its border colour. |

## `[Procedures]`

The action SPs **and** the security codes. If a security code key is absent,
the runtime falls back to `FT_<RecordType>_<ACTION>`.

| Key | Meaning |
|---|---|
| `New` | New-record SP (`FT_SP_<Entity>_New`). Its absence disables the New button. |
| `New_Param1` | Value passed as `@Param1` to the New SP (usually blank; parent id arrives as `@Param2`). |
| `Delete` | Delete SP. **Presence of this key is what enables the Delete button.** |
| `validate` | Optional pre-save validation SP. |
| `process` | Optional post-load / recompute SP. |
| `PostSave` | SP run after a successful save. |
| `PostClose` | SP run after the form closes. |
| `SaveClick` | SP run on the Save click. |
| `New_code` | Security code for New *(default `FT_<RecordType>_NEW`)*. |
| `Edit_code` | Security code for Edit *(default `FT_<RecordType>_EDIT`)*. |
| `Delete_Code` | Security code for Delete *(default `FT_<RecordType>_DEL`)*. |
| `Lock_code` | Security code for Lock *(default `FT_<RecordType>_LOCK`)*. |
| `UnLock_code` | Security code for Unlock *(default `FT_<RecordType>_UNLOCK`)*. |
| `Access_code` | Security code for view access *(default `FT_<RecordType>_ACCESS`)*. |

## `[Reports]`

| Key | Meaning |
|---|---|
| `Print` | Crystal report file (`Rp_<Name>.rpt`) fired by the print button. |

## `[Tabs]`

| Key | Default | Meaning |
|---|---|---|
| `count` | `1` | Number of tab blocks (`[Tab1]…[TabN]`). |
| `ActiveTab` | `0` | Which tab is selected on open (**0-based**). |
| `Dynamic` | `0` | `1` = tabs render on demand (deferred). |
| `TabHeight` | *(theme)* | Tab bar height. |
| `TabWidth` | *(theme)* | Per-tab width. |
| `TabPos` | *(theme)* | `Top` / `Left` etc. |

## `[Tab1] … [TabN]` — one per tab

Blocks are **1-based** (`[Tab1]` is the first tab).

| Key | Meaning |
|---|---|
| `Caption` | Tab label. Existing files pack the Arabic after the English in the same value; new work should use `Caption` + `Caption_A`. |
| `Borderwidth` | Tab panel border width. |
| `Icon` | Optional tab icon. |

## `[Controls]` — the field list { #controls-the-field-list }

The **order** of keys in `[Controls]` is the **render order** of the form.
Each key is a control name; the value is its type (a convenience — the
authoritative type is `Type=` inside the control's own block).

```ini
[Controls]
    Detail    = section     ← group divider
    Allergen  = edit        ← renders under "Detail"
    Reaction  = edit
    Severity  = Radio
    NoteGroup = section     ← next group
    Notes     = memo
```

To reorder fields on screen, reorder them here — **not** by moving the
`[<FieldName>]` blocks.

## `[<FieldName>]` — one per control

Each control named in `[Controls]` gets its own block. The full list of types
and their type-specific keys is on the [Field Types](field-types.md) page.
The keys common to most controls:

| Key | Default | Meaning |
|---|---|---|
| `Field` | *(empty)* | The **DB column** this control binds to. |
| `Type` | *(empty)* | Control type — `edit`, `memo`, `dblookup`, `Date`, `Radio`, `Checkbox`, `section`, `button`, … |
| `tab` | `0` | Which tab (**0-based**). |
| `Caption` / `Caption_a` | *(empty)* | English / Arabic label. |
| `Required` | *(no)* | `yes` makes the field mandatory. |
| `Default Value` | *(empty)* | Value for a new record. |
| `wHidden` | `0` | `1` hides the control. |
| `ReadOnly` | `0` | `1` renders it read-only. |
| `Hint` | *(empty)* | Tooltip. |
| `Format` | *(empty)* | Display format (e.g. numeric). |
| `Newline` | `0` | `1` forces the field onto a new row. |
| `NoLabel` | `0` | `1` hides the label. |
| `Lookup Query` | *(empty)* | SQL for `dblookup` list. |
| `Key` / `Result1` / `Result2` | *(empty)* | Value column / display column(s) for a lookup. |
| `Option1..7` (+ `_a`) | *(empty)* | Options for `Radio`. |
| `Value1..7` | *(= Option)* | Stored value per option (defaults to the option text). |
| `Min` / `Max` / `Increment` | `0` / `10000` / `1` | Numeric-spinner bounds. |
| `Time` | `0` | `1` adds a time picker to a `Date` field. |
| `Object` / `Command` / `Param1..6` | *(empty)* | Dispatcher action for a `button`. |

---

**Next:** [Field Types →](field-types.md) · [Pitfalls →](pitfalls.md)
