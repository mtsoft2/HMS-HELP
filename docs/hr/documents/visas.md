# Visas

`HR_VISA.FT` records work-visa applications and renewals for expat
staff.

## Fields

| Field | Notes |
|---|---|
| Employee | Picker. |
| Visa Type | `HR_VisaType` (Work / Family / Visit / Re-entry). |
| Status | `HR_VISAStatus` (Requested / Approved / Issued / Cancelled / Used). |
| Validity Start | Visa issue date. |
| Validity End | Expiry. |
| Note | Free text. |

`HR_VISA_BANNER` shows the visa lifecycle at the top of the form.

## Reports

* **Expiring Documents** (`hr_ExpiringDocs.rpt`) — includes visas
  expiring in the next 30/60/90 days.
