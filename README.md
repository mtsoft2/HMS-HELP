# HMS Help

End-user and administrator documentation for **HMS (Hospital Management
System)**, published with **MkDocs Material** to GitHub Pages.

## Live site

After the GitHub Action runs, the site is at:
**https://mtsoft2.github.io/HMS-HELP/**

(enable **Pages → Source: GitHub Actions** in the repo settings the
first time).

## Local preview

```bash
pip install mkdocs-material
mkdocs serve
# open http://127.0.0.1:8000
```

## Repo layout

```
mkdocs.yml                 site config + navigation
docs/
  index.md                 site home
  hr/
    index.md               HR module overview
    getting-started.md     end-to-end first-employee walkthrough
    employees/             16-tab employee form, contracts, salary, leaves, EOS
    recruitment/           vacancies, candidates, agencies
    organization/          departments, positions, packages, periodic allowances
    actions/               personnel actions, termination, transfer, promotion, appraisals
    leaves/                vacation requests, travel auth, extensions
    documents/             visas, certificates, sick leave
    payroll/               pay codes, pay runs, registers, loans
    admin/                 lookups, security, alerts
    reports.md             ~30 HR / Payroll reports
    reference/             data model, FT/ST/GT templates, stored procedures, glossary
```

## Contributing

* Edit any `.md` file under `docs/` and commit to `main`.
* The pencil icon on each page links straight to the source file on GitHub.
* CI builds with `--strict`, so broken links / missing pages fail the build.
