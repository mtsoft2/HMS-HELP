# Candidates

A **Candidate** is anyone you are considering for a vacancy. The
record carries 95 % of the data an `HR_Employee` carries — so that on
**Hire** the data simply copies across.

## Candidate form (`HR_Candidate.FT`)

Five tabs: **Personal**, **Employment**, **Contact**, **Notes**, **Note
List**.

### Personal tab

| Field | DB column | Notes |
|---|---|---|
| Number | `Number` | Candidate reference (CV-001…). |
| Name (EN/AR) | `First`, `Father`, `Grand_Father`, `Family`, `First_A`, `Father_A`, `Family_A` | |
| Date / Place of Birth | `Date_of_Birth`, `Place_of_Birth` | |
| Gender / Nationality / Religion | `Gender`, `Nationality`, `Religion` | |
| Marital | `Marital` | |
| Address / Phone / Mobile / Email / PO Box / ZIP | `Address`, `Phone`, `Mobile`, `Email`, `POBOX`, `ZIP` | |
| Origin Country Address / Phone | `Origin_Country_Address`, `Origin_Country_Phone` | |
| Spouse / Children | `Spouse_name`, `Children_number` | |
| Impaired | `Impaired` | |
| Photo | image | |

### Employment tab

| Field | DB column |
|---|---|
| Vacancy | `VACANCY` |
| Position / Department / Branch | `Position`, `Department`, `Branch` |
| Category | `Category` |
| Status | `Status` (`HR_CandidateStatus`) |
| Agency | `Agency` (`HR_Agency`) |
| ETA / PTA | `ETA`, `PTA` (expected / planned travel arrival) |
| Current sponsor name | `Current_sponsor_name` |
| Passport (Number / Place / Expiry / Issue date) | `Passport_*` |
| Residence (Number / Place / Expiry) | `Residence_*` |

## Hire workflow

1. Move the candidate's **Status** to *Offered* and obtain acceptance.
2. Click **Actions → Hire**. The system:
   * Inserts a row into `HR_Employee` (new `Id`, auto Main_Number).
   * Copies all personal/contact/passport/residence fields.
   * Sets `HR_Employee.HR_EMP_Candidate` = source candidate `Id` (audit
     link, also exposed as `EmployeeID` on the candidate row).
   * Closes the **Vacancy** (`HR_Vacancy.HVC_Status` → *Filled*) if the
     vacancy count drops to 0.
3. Open the new employee record and issue the first **Contract**
   (see [Contracts](../employees/contracts.md)).
