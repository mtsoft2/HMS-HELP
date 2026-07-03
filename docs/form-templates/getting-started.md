# Getting Started — build a `.FT` from scratch

This walkthrough builds a complete, working form for a fictitious entity
**`Allergy`** (a patient allergy record). Follow the same eight steps for any
new form. Everything ships inside a **patch** — never edit tables or SPs on a
live customer database directly.

!!! tip "Copy from a known-good form"
    The fastest way to a correct `.FT` is to copy an existing simple form and
    rename it. Good starting points: `HR_Candidate.FT` (clean sections + tabs),
    `Account.FT` (small), or any `CRM_*.FT` (modern conventions).

## Step 1 — The two tables

Create the real table and its `PKT_` editing twin. Use idempotent guards so
the script is re-runnable.

```sql
IF OBJECT_ID('Allergy') IS NULL
CREATE TABLE dbo.Allergy (
    ID          INT           NOT NULL PRIMARY KEY,
    CUST_ID     VARCHAR(6)    NULL,      -- patient (Cust.ID)
    Allergen    VARCHAR(100)  NULL,
    Reaction    VARCHAR(200)  NULL,
    Severity    VARCHAR(10)   NULL,
    OnsetDate   SMALLDATETIME NULL,
    Notes       VARCHAR(500)  NULL,
    FT_Locked   BIT           NOT NULL DEFAULT(0)
);

IF OBJECT_ID('PKT_Allergy') IS NULL
CREATE TABLE dbo.PKT_Allergy (
    SPID        INT           NULL,
    _Deleted    BIT           NULL,
    ID          INT           NULL,
    CUST_ID     VARCHAR(6)    NULL,
    Allergen    VARCHAR(100)  NULL,
    Reaction    VARCHAR(200)  NULL,
    Severity    VARCHAR(10)   NULL,
    OnsetDate   SMALLDATETIME NULL,
    Notes       VARCHAR(500)  NULL,
    FT_Locked   BIT           NULL
);

CREATE UNIQUE INDEX UX_PKT_Allergy_ID_SPID ON dbo.PKT_Allergy(ID, SPID);
```

The PKT columns are the same as the real table but **all nullable**, plus
`SPID` and `_Deleted`. See [why this split exists](index.md#the-two-table-pattern-why-pkt_-exists).

## Step 2 — The ID counter column

New IDs come from a counter column on the `SYS2` table. Add it idempotently
(do **not** use `SYS2_CNT_CHECK` to add the column — it only syncs an
existing one):

```sql
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS
               WHERE table_name='SYS2' AND column_name='Allergy')
    ALTER TABLE SYS2 ADD Allergy INT;
```

## Step 3 — The selector SP (`FT_SP_Allergy`)

Loads one record for editing. **Must** return three synthetic trailing
columns `_Hide`, `_Disable`, `_Readonly` — the renderer reads them to
hide/disable/lock fields dynamically. Reads from the **PKT** table.

```sql
CREATE PROCEDURE dbo.FT_SP_Allergy @ID INT = -1
AS
    SET NOCOUNT ON;
    DECLARE @Hide VARCHAR(100) = '';
    DECLARE @Disable VARCHAR(100) = '';
    DECLARE @ReadOnly VARCHAR(100) = '';

    SELECT ID, CUST_ID, Allergen, Reaction, Severity, OnsetDate, Notes, FT_Locked,
           @Hide _Hide, @Disable _Disable, @ReadOnly _Readonly
    FROM   PKT_Allergy
    WHERE  SPID = @@SPID AND ID = @ID;
```

!!! danger "Enumerate columns — never `SELECT *`"
    `FieldsMask` and the field bindings depend on a stable, explicit column
    list. `SELECT *` breaks them.

## Step 4 — The New SP (`FT_SP_Allergy_New`)

Allocates a fresh ID, writes a blank row into the **PKT** table, and returns
the new ID. The parent record ID from the calling toolbar arrives as
**`@Param2`** (not `@Param1`). Always declare all five params.

```sql
CREATE PROCEDURE dbo.FT_SP_Allergy_New
      @Param1 VARCHAR(50) = '',
      @Param2 VARCHAR(50) = '',
      @Param3 VARCHAR(50) = '',
      @Param4 VARCHAR(50) = '',
      @Param5 VARCHAR(50) = ''
AS
    SET NOCOUNT ON;
    DECLARE @ID INT;
    DECLARE @Patient VARCHAR(6) =
        CASE WHEN LTRIM(RTRIM(@Param2)) <> '' THEN @Param2 ELSE @Param1 END;

    SET @ID = ISNULL((SELECT Allergy FROM SYS2), 1) + 1;
    UPDATE SYS2 SET Allergy = @ID;

    INSERT INTO PKT_Allergy (SPID, ID, CUST_ID, Severity, FT_Locked)
    VALUES (@@SPID, @ID, @Patient, 'Low', 0);

    SELECT @ID;
```

## Step 5 — The Delete SP (`FT_SP_Allergy_Delete`)

Deletes from the **real** table, wrapped so failures surface a clean message.

```sql
CREATE PROCEDURE dbo.FT_SP_Allergy_Delete @ID INT
AS
    SET NOCOUNT ON;
    BEGIN TRY
        DELETE FROM Allergy WHERE ID = @ID;
    END TRY
    BEGIN CATCH
        RAISERROR('Cannot delete record.', 16, 1);
    END CATCH;
```

## Step 6 — (Optional) The banner SP

If you want a strip at the top of the form (e.g. the patient's name), write a
banner SP that returns bracketed display columns:

```sql
CREATE PROCEDURE dbo.Allergy_BANNER @ID INT
AS
    SET NOCOUNT ON;
    SELECT c.COMPANY AS [Patient], a.Allergen AS [Allergen], a.Severity AS [Severity]
    FROM   Allergy a
    LEFT JOIN Cust c ON c.ID = a.CUST_ID
    WHERE  a.ID = @ID;
```

Set `[Banner] Show = 0` and delete this SP if you don't want a banner.

## Step 7 — The template file (`Allergy.FT`)

Save as **Windows-1256** if any Arabic is present. Note: `Table`/`PKT_Table`
point at Step 1's tables; every `Procedures` value points at Steps 3–6;
`RecordType` uses underscores matching the entity.

```ini
[MAIN]
    Title        = Allergy
    Width        = 700
    Height       = 600
    Procedure    = FT_SP_Allergy
    Table        = Allergy
    PKT_Table    = PKT_Allergy
    IDField      = ID
    IDCounter    = Allergy
    RecordType   = Allergy
    SingleRecord = 1
    wMinHeight   = 500
__CDC=0

[Banner]
    Show      = 1
    Procedure = Allergy_BANNER
    height    = 60

[Procedures]
    New       = FT_SP_Allergy_New
    Delete    = FT_SP_Allergy_Delete

[Tabs]
    count     = 2
    TabHeight = 40
    TabPos    = Top

[Tab1]
    Caption   = Allergy
    Borderwidth = 2

[Tab2]
    Caption   = Notes
    Borderwidth = 2

[Controls]
    Detail    = section
    Allergen  = edit
    Reaction  = edit
    Severity  = Radio
    OnsetDate = Date
    NoteGroup = section
    Notes     = memo

[Detail]
    Caption   = Allergy Detail
    Type      = section
    tab       = 0

[Allergen]
    Caption      = Allergen
    Field        = Allergen
    Type         = edit
    tab          = 0
    Required     = yes

[Reaction]
    Caption      = Reaction
    Field        = Reaction
    Type         = edit
    tab          = 0

[Severity]
    Caption      = Severity
    Field        = Severity
    Type         = Radio
    tab          = 0
    Option1      = Low
    Option2      = Medium
    Option3      = High

[OnsetDate]
    Caption      = Onset Date
    Field        = OnsetDate
    Type         = Date
    tab          = 0

[NoteGroup]
    Caption      = Notes
    Type         = section
    tab          = 1

[Notes]
    Caption      = Notes
    Field        = Notes
    Type         = memo
    tab          = 1
```

!!! warning "Tab numbering is mixed base"
    `[Tab1]`, `[Tab2]` headers are **1-based**. The `tab =` value inside each
    field block is **0-based** (`tab=0` = first tab). Get this wrong and the
    tab renders empty and the form throws. See [Pitfalls](pitfalls.md#tab-off-by-one).

`__CDC=0` must sit **inside `[MAIN]`** — the runtime recomputes the checksum.
Do **not** add a trailing `[Main]` section for it.

## Step 8 — Deploy & smoke-test

1. Copy `Allergy.FT` into the **runtime** folder: `D:\hms909_kyan\FTP\`
   (and `E:\Work\Assets\FTP\` for the source of truth).
2. Run the SQL from Steps 1–6 against the target DB.
3. Register the form so a toolbar button can open it (a `.ST` view button,
   a binder link, or a menu entry — see the module-building reference).
4. Open the form. If it's blank or throws on open, run the
   [pre-ship checklist](pitfalls.md#pre-ship-checklist).

---

**Next:** [Section & Key Reference →](reference.md) ·
[Field Types →](field-types.md) · [Pitfalls →](pitfalls.md)
