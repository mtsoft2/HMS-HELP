# Recruitment

The Recruitment pipeline turns an **open vacancy** into a **hired
employee** in three stages:

```
Vacancy  →  Candidate  →  Hire (Employee)
```

Optionally backed by a **Recruitment Agency**.

## Pages

* **[Vacancies](vacancies.md)** — define what you are hiring for.
* **[Candidates](candidates.md)** — track applicants from CV to arrival.
* **[Agencies](agencies.md)** — manage external recruiters and their
  commissions.

## Related lookups

| Table | Purpose |
|---|---|
| `HR_CandidateStatus` | New / Screened / Interviewed / Offered / Rejected / Hired |
| `HR_Vacancy_Status` | Open / On Hold / Filled / Cancelled |
| `HR_RecSource` | LinkedIn, Bayt, Walk-in, Agency, Referral, … |
| `HR_VACClass` | Vacancy classification (Critical / Standard / Replacement) |
| `HR_POSCATEG` | Position category — used for headcount budget reporting |
