# Personal Info (Tab 1)

The **Personal** tab captures the legal identity of the employee.

## Fields

| Group | Field | Notes |
|---|---|---|
| Name (EN) | First / Father / Grand-Father / Family | Required. Used on contracts, pay slips, certificates. |
| Name (AR) | الاسم / الأب / العائلة | Stored in `HR_EMP_First_A`, `HR_EMP_Father_A`, `HR_EMP_Family_A`. Required for Saudi labour-office filings. |
| Birth | Date of Birth, Place of Birth | |
| Identity | Gender, Nationality, Religion, Marital Status, Blood Group | All come from look-up tables (Data Setup). |
| Impairment | Impaired (yes / no) | Drives the *Disability* line in regulatory reports. |

## Tips

* The **full name** field (`HR_EMP_NAME` / `HR_EMP_NAME_A`) is computed
  automatically from the four name parts on save — never edit it
  directly.
* Use the **photo** placeholder on the right to attach an ID picture
  (drag-and-drop or click *Browse*). Photos are stored under
  `wwwroot/upload/` per the **Imaging** settings.
* The **Saudi Council Certificate** block on the *Qualifications* tab
  uses the *Nationality* set here to enable / disable validation.
