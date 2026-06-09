# Certificates

`HR_Certificate.FT` records professional certificates the employee
holds — and most importantly the **Saudi Council Certificate** (SCC)
which is mandatory for licensed clinical staff.

## SCC fields (on the Employee form, Qualifications tab)

| Field | DB column |
|---|---|
| Certificate Number | `HR_EMP_SaudiCouncilCert_NO` |
| Issue Date | `HR_EMP_SaudiCouncilCert_DATE` |
| Exam Date | `HR_EMP_SaudiCouncilCert_ExamDATE` |
| Valid (flag) | `HR_EMP_SaudiCouncilCert_Valid` |
| Expiry Date | `HR_EMP_SaudiCouncilCert_EXPDATE` |
| Profession | `HR_EMP_SaudiCouncilCert_Profession` |
| Status | `HR_EMP_SaudiCouncilCert_Status` |
| Not Applicable | `HR_EMP_SaudiCouncilCert_NA` (set for non-clinical staff) |
| Notes | `HR_EMP_SaudiCouncilCert_Note` |

`HR_CCI_UPDATE` is the SP that refreshes SCC validity for all employees
nightly. `hr_Certificate_ADD` is the helper that inserts a certificate
row from the certificate form into the employee's qualifications.

## Reports

* **Employee Certificates** (`HR_Emp_Certificate.rpt`) — three layouts
  (F1, F2, F3) for different licensing authorities.
* **SaudiCC** (`HR_SaudiCC.ini`) — staff list with current SCC status.
