---
hide:
  - navigation
  - toc
---

# HMS Help

<style>
  .md-typeset h1 { font-size: 2.6rem; margin-bottom: 0.4em; }
  .hms-hero {
    background: linear-gradient(135deg, #3949AB 0%, #1E88E5 100%);
    color: #fff; border-radius: 14px; padding: 40px 36px;
    margin: 0 0 32px 0;
  }
  .hms-hero h1 { color:#fff; margin: 0 0 10px 0; font-size: 2.2rem; }
  .hms-hero p  { color: rgba(255,255,255,0.92); margin: 0; font-size: 1.05rem; max-width: 780px; }
  .hms-hero .repo { display:inline-block; margin-top: 14px; padding: 6px 12px;
    background: rgba(255,255,255,0.18); border-radius: 6px; color:#fff;
    font-size: 0.85rem; text-decoration: none; }
  .hms-hero .repo:hover { background: rgba(255,255,255,0.3); }
  .hms-section-title { margin-top: 36px; margin-bottom: 14px; font-weight: 700; color:#0F172A; font-size: 1.35rem;}
  [data-md-color-scheme="slate"] .hms-section-title { color:#E2E8F0; }
  .grid.cards > ul > li {
    border-radius: 10px; transition: transform 0.12s ease, box-shadow 0.12s ease;
  }
  .grid.cards > ul > li:hover {
    transform: translateY(-2px); box-shadow: 0 6px 20px rgba(15,23,42,0.08);
  }
</style>

<div class="hms-hero" markdown>
# HMS — Hospital Management System
End-user and administrator manual for every module in HMS. Pick a card below to jump in,
or use the search box (top right) to find a feature by name.
</div>

## 🆕 What's New {.hms-section-title}

<div class="grid cards" markdown>

- :material-palette-outline: **UI Updates**

    ---

    Grid R3 spreadsheet-style upgrade, Mini Mode pickers, Patient Avatars on every banner.

    [:octicons-arrow-right-24: Open](ui-updates/index.md)

- :material-tools: **Setup Wizard v2**

    ---

    New installer + patch flow with full patching history and one-click re-apply.

    [:octicons-arrow-right-24: Open](setup-wizard/index.md)

- :material-database-cog-outline: **Maintenance**

    ---

    Database health dashboard — KPIs, scored checklist with one-click fixes, backups, schedules, and Drive-shareable maintenance log.

    [:octicons-arrow-right-24: Open](maintenance/index.md)

- :material-chart-box-outline: **Report Server (V2)**

    ---

    Centralised report runner — browse, run, schedule, export.

    [:octicons-arrow-right-24: Open](report-server/index.md)

</div>

## 📊 Dashboards {.hms-section-title}

<div class="grid cards" markdown>

- :material-hospital-building: **Clinic Dashboard**

    ---

    Manager's home screen for one outpatient clinic — Overview, Schedule, Census, Billing, Physicians, Inventory, Quality, CRM.

    [:octicons-arrow-right-24: Open](clinic-dashboard/index.md)

- :material-account-heart: **Patient Dashboard**

    ---

    The patient's lifetime summary — Profile, Clinical, Care Plan, Appointments, Lab, Imaging, History, Documents, Billing, Insurance.

    [:octicons-arrow-right-24: Open](patient-dashboard/index.md)

</div>

## 🩺 Clinical {.hms-section-title}

<div class="grid cards" markdown>

- :material-tooth-outline: **Dental Chart**

    ---

    Two-arch chairside chart with status / operation / root tools, six clinical overlays (Plan, Perio, Ortho, Caries, Endo/RG, Occlusion), snapshots & compare, demo mode.

    [:octicons-arrow-right-24: Open](dental-chart/index.md)

- :material-calendar-clock: **Scheduler**

    ---

    Day / Week appointment grid with fingerprint find, drag-and-drop reschedule, conflict detection, bulk move.

    [:octicons-arrow-right-24: Open](scheduler/index.md)

- :material-stethoscope: **Clinic Reception**

    ---

    The front desk's one-window workspace — find, book, chart, prescribe, bill in 14 toolbar buttons.

    [:octicons-arrow-right-24: Open](adt-dc/index.md)

- :material-file-image-outline: **Document Manager (DM2)**

    ---

    Unified viewer + gallery for every file type — images, PDF, Office, DICOM. Annotate, measure, compare.

    [:octicons-arrow-right-24: Open](dm2/index.md)

</div>

## 🔌 Integrations {.hms-section-title}

<div class="grid cards" markdown>

- :material-message-text-outline: **Metasoft Communicator**

    ---

    SMS / WhatsApp / e-mail outbound channel with queue, retries, alerts, full audit log.

    [:octicons-arrow-right-24: Open](communicator/index.md)

- :material-shield-check-outline: **NPHIES BridgeProxy**

    ---

    Saudi NPHIES e-claim submissions, status checks, and pre-authorisations.

    [:octicons-arrow-right-24: Open](bridgeproxy/index.md)

</div>

## 👥 Back Office {.hms-section-title}

<div class="grid cards" markdown>

- :material-account-group: **Human Resources**

    ---

    Full employee lifecycle — recruitment, contracts, leaves, appraisals, documents, end of service.

    [:octicons-arrow-right-24: Open](hr/index.md)

- :material-cash-multiple: **Payroll**

    ---

    Pay codes, pay runs, registers, pay slips, staff loans.

    [:octicons-arrow-right-24: Open](hr/payroll/index.md)

</div>

## 🚧 Coming Soon {.hms-section-title}

<div class="grid cards" markdown>

- :material-clipboard-pulse-outline: **Patient / Clinical**

    ---

    Visit forms, vitals, allergies, problem list, medications. *Coming soon.*

- :material-pill: **Pharmacy / Inventory**

    ---

    Stock, dispensing, formulary, expiry tracking. *Coming soon.*

- :material-flask-outline: **Laboratory / Radiology**

    ---

    Orders, sample tracking, results, imaging studies. *Coming soon.*

</div>

---

## How to use this site {.hms-section-title}

* Use the **top navigation tabs** to jump between modules.
* The **left sidebar** lists every page in the current module.
* The **search bar** (top right) searches the entire site.

## Conventions

| Term | Meaning |
|---|---|
| **Form (FT)** | A data-entry window — e.g. the Employee form. |
| **Search pad (ST)** | A list / search window — e.g. the Employees list. |
| **Grid (GT)** | A child table inside a form — e.g. the Salary history grid inside the Employee form. |
| **Binder (BND)** | The full-screen workspace with a toolbar + side menu — e.g. *Patient Affairs*. |
| **Lookup** | A simple reference table (Department, Position, Nationality, …) administered from the **Data Setup** menu. |
