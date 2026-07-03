# Form Templates (`.FT`) — Developer Guide

!!! info "Audience"
    This is a **technical / developer** guide, not an end-user manual. It
    explains how HMS forms are actually built — from the metadata file on
    disk to the stored procedures behind them. If you only want to *use* a
    module, see that module's own section in the left nav.

## What a `.FT` file is

HMS is **metadata-driven**. Almost no screen in the system is hand-written
Blazor. Instead, each "edit one record" form is described by a plain-text
**INI file with a `.FT` extension** — a *Form Template*. At runtime a single
generic Blazor component, `FT_FormTemp.razor`, reads that file, asks the
database for the record, and renders the tabs, sections, fields, banner and
toolbar the file describes.

That means to add a new form you **do not write C# or Razor**. You write:

1. A `.FT` text file (the layout).
2. A handful of **stored procedures** (the data).
3. Two SQL tables — a real table and its `PKT_` editing twin.

```
      ┌────────────────────┐        reads        ┌──────────────────────┐
      │   MyEntity.FT      │  ─────────────────▶  │  FT_FormTemp.razor   │
      │  (INI on disk)     │                      │  (generic renderer)  │
      └────────────────────┘                      └──────────┬───────────┘
                                                             │ EXEC
                                                             ▼
      ┌────────────────────┐                      ┌──────────────────────┐
      │  FT_SP_MyEntity     │◀────── selects ─────│  SQL Server          │
      │  FT_SP_MyEntity_New │                      │  MyEntity            │
      │  FT_SP_MyEntity_Del │                      │  PKT_MyEntity (ghost)│
      └────────────────────┘                      └──────────────────────┘
```

## The file is a strict INI

The parser is [`Models/Ini.cs`](https://github.com/mtsoft2/HMS-HELP). A few
rules fall directly out of how it reads the file — memorise them, because
most "my form is blank / crashes on open" bugs trace back here:

- **Sections** are `[Name]` on their own line. Section names are stored
  **lower-cased and case-insensitively**, so `[MAIN]`, `[Main]` and `[main]`
  are *the same section*. Declaring the same section twice makes the second
  one **overwrite** the first with an empty block — see
  [Pitfalls](pitfalls.md#trailing-main).
- **Entries** are `Key = Value`. Everything before the first `=` is the key
  (trimmed); everything after is the value (trimmed).
- **Comments** start with `;`. Dashed separator lines like
  `-----------------` that you see in existing files are *not* comments —
  they survive as junk keys but are harmless because nothing reads them.
- **Encoding** defaults to **Windows-1256** (Arabic code page). Arabic
  captions (`Caption_a`) must be saved in CP1256, *not* UTF-8, or they turn
  into mojibake. The `CodePage=` key in `[MAIN]` can override this.
- Keys are **case-insensitive** too, so `Title`, `title` and `TITLE` all work.

## Anatomy of a `.FT`

A form template is read section by section by `FT_FormTemp.razor`. The
sections, in the order they usually appear:

| Section | Purpose | Read by |
|---|---|---|
| `[MAIN]` | Title, size, the record table + its PKT twin, the selector SP, the record type | `OpenTemplate()` |
| `[Banner]` | Optional patient/record banner strip at the top | `FT_Banner` |
| `[Procedures]` | The New / Delete / Validate / Save SPs **and** the security codes | `SEC_Code_*` |
| `[Reports]` | Optional `Print=<file>.rpt` | print handler |
| `[Tabs]` | How many tabs, their height/position | `FT_Tabs.razor` |
| `[Tab1]…[TabN]` | One block per tab: its caption + icon | `FT_Tabs.razor` |
| `[Controls]` | The **ordered list** of every field/section/grid on the form | `InitControls()` |
| `[<FieldName>]` | One block per control: its caption, type, tab, lookup, etc. | `InitControls()` |
| `[GT_*]` | Optional inline detail grids | `FT_Grid.razor` |

Each of these is documented, key by key, in the
[Section & Key Reference](reference.md).

## The two-table pattern (why `PKT_` exists)

Every editable entity has **two** tables:

- **`MyEntity`** — the real, persistent table. This is the only place data
  actually lives.
- **`PKT_MyEntity`** — a *ghost* / editing buffer. Same columns, all
  nullable, plus `SPID INT` and `_Deleted BIT`. While a user has the form
  open, their in-progress edits live here, scoped to their SQL session
  (`@@SPID`). On save, the row is copied into the real table.

The generic renderer relies on this split for dirty-tracking, so **you must
ship both tables**. The [Getting Started](getting-started.md) walkthrough
creates them together.

## Where the files live

| Path | Role |
|---|---|
| `…\FTP\MyEntity.FT` | The **runtime** template folder the app reads (`Global.RootPath\FTP`). On the current install that is `D:\hms909_kyan\FTP\`. |
| `E:\Work\Assets\FTP\MyEntity.FT` | The source-of-truth copy that patches deploy from. |
| `E:\Work\Assets\HMS23-PatchA<NNN>\copy\FTP\` | The per-patch copy that the installer deploys to every customer. |

!!! warning "Deploy to the runtime folder, not just Assets"
    Editing the file under `E:\Work\Assets\FTP\` alone does nothing to the
    running app — that folder is the deploy *source*, not what the app loads.
    Copy the file into the `…\FTP\` runtime folder too, then hard-refresh
    the browser. The Blazor process caches templates on first read, so a
    navigate-away/back (or app restart) is sometimes needed.

---

**Next:** [Getting Started — build a `.FT` from scratch →](getting-started.md)
