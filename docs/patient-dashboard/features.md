# Features

Every feature of the Patient Dashboard, grouped by what it lets you
do. Exhaustive but not technical — use it as a training checklist or
a gap analysis against another system.

---

## 1. Identity & Demographics

* Patient photo (avatar with fallback initials).
* Full name.
* Salutation (Mr / Mrs / Dr / …).
* File / MRN number.
* Gender.
* Date of birth — Gregorian.
* Date of birth — Hijri.
* Computed age (years / months / days as appropriate).
* Blood group.
* Marital status.
* Nationality.
* Religion.
* National ID — type and number.
* Passport — number, issue place, issue / expiry dates.
* Visa number.
* VIP flag.

## 2. Contact

* Mobile phone.
* Landline / phone.
* E-mail address.
* Address (home).
* P.O. Box.
* Employer.

## 3. Emergency / Next-of-kin

* Salutation.
* Name.
* Relation.
* Phone.
* Mobile.
* Address.

## 4. Insurance & Guarantors

* Primary guarantor — name, contract, network, class.
* Secondary guarantor — same set of fields.
* Self-insured flag.
* Coverage tier / class.
* Currency.
* Latest admission coverage card.
* Edit primary coverage shortcut.
* Edit secondary coverage shortcut.
* Click-to-set-up coverage when none is on file.
* Claims history list — Pending, Sent, Accepted, Rejected, with counts and totals.
* Open the latest admission to add / edit a claim.

## 5. Vitals

* Last *N* readings of each vital sign.
* Per-reading badge — Normal / Borderline / Low / High / Markedly high.
* Date and time of each reading.
* Free-text note on each reading.
* + Vital — record a new reading.
* Visual sparkline / trend bar per vital.
* Height, Weight, BMI (computed), Area (BSA, computed).

## 6. Allergies

* Known allergies list.
* Severity & type (drug / non-drug).
* Reaction description.
* Source (chart / by whom).
* Last-reviewed date.

## 7. Active Problems

* Problem list with diagnosis codes.
* Onset date.
* Status (Active / Resolved / Recurrent).
* Priority.
* Diagnosing physician.
* Free-text notes per problem.

## 8. Prescriptions / Active Medications

* Active medications list.
* Past prescriptions list (with show-more toggle).
* Drug name, dose, frequency, duration.
* Prescribing physician.
* Start / end date.
* Source visit / encounter.
* Refill flag.
* + Prescription — write a new one.

## 9. Visit / Encounter History

* Chronological list of every visit.
* Visit date, physician, department, type (OP / IP / ER / dental / …).
* Chief complaint / reason.
* Diagnosis from the visit.
* Click a visit to open its full record.

## 10. Care Plan (Treatment Plans)

* List of all treatment plans for the patient.
* Plan name, status, total estimated cost, total paid.
* Per-plan progress bar.
* Per-procedure list — tooth, treatment, dentist, planned date.
* Procedure stages — Planned / Existing / Pre-existing / Done /
  Cancelled.
* Status badges: **Planned**, **Existing**, **Procedures already
  completed**, **Procedures still to be performed**, **Existing
  procedures (pre-existing condition records)**.
* + Treatment Plan — create a new plan.
* Open the full Treatment Plans panel.
* Mini dental chart embedded inline.
* Click a tooth to open the full dental chart.

## 11. Dental Chart Snapshot

* Read-only thumbnail of the patient's current chart state.
* Per-tooth marks (caries / fracture / treated / missing / …).
* Click any tooth → open the full dental chart for that tooth.
* "Open full" button → full-page chart.

## 12. Appointments

* Upcoming appointments list with status.
* Past appointments list (collapsible).
* Next-upcoming highlight at the top.
* "No upcoming appointment" empty state.
* Per-appointment actions: Attend, Reschedule, Set status, Remind.
* Set status — No-show, Confirmed, Arrived, In-Service, Completed.
* WhatsApp / SMS reminder.
* Book an appointment dialog:
    * Pick a physician.
    * Pick a speciality.
    * Filter by day shift / window / duration.
    * Mini calendar — green days have availability.
    * Available-slots list (Find available slots).
    * Confirm to commit.
* Show more / show fewer toggle.
* "Past" and "Upcoming" segmented filter.

## 13. Lab Tests

* List of lab orders + results.
* Sample-collection workflow indicators (Q = request closed, C = sample
  collected, R = sample received, P = reply closed).
* Latest results panel.
* Per-test serial number.
* Click row to open the lab request.
* + Lab test — order a new test.

## 14. Imaging / Radiology

* Latest imaging study with thumbnail.
* Click thumbnail to view in the document viewer.
* Imaging requests list (open / in progress / completed).
* Imaging results list.
* Open the radiology request the image belongs to.
* + Imaging — order a new study.
* Per-image description / physician.
* Direct link into the source admission for context.

## 15. History — Immunisations

* Vaccine dose list.
* Date of administration.
* Vaccine name.
* Site (left arm, right arm, …).
* Lot / batch number.
* Administrator (nurse / physician).
* Notes per dose.
* + Vaccine dose.
* Edit this vaccine dose.

## 16. History — Family

* Family member list with relation.
* Per-member health background (genetic, chronic conditions).
* Edit family + add a member.
* Edit this family member.

## 17. History — Social

* Smoking status.
* Alcohol consumption.
* Substance use.
* Occupation / risk exposure.
* Marital / living arrangement notes.
* Edit social history.

## 18. History — Referrals

* Referrals to / from other practitioners.
* Reason for referral.
* Referring / receiving clinician.
* Date.
* Status.
* + Referral.
* Edit this referral.

## 19. Documents

* Embedded **Document Manager (DM2)** gallery scoped to the patient.
* Upload by drag-and-drop or file picker.
* View any file type (PDF, Word, Excel, images, videos, DICOM, …) in
  the unified viewer.
* Annotate, measure, compare images.
* Categories, tags, keywords on every document.
* Search across the patient's library.
* + Document — add a new file.
* Open Patient Documents header link to the full DM2 view.

## 20. Billing

* List of bills with status badge.
* Bill total, patient share, insurer share.
* Per-bill physician / diagnosis label.
* Per-bill date.
* Payments list.
* Per-payment number, date, method, amount.
* Patient balance — current outstanding.
* Counts strip — number of bills / payments / refunds.
* + Bill — create a new bill.
* + Payment — record a new payment.
* Refund — record a refund.
* Click a bill to open it in the bill editor.
* Click a payment to open it in the payment editor.

## 21. Statement & Communication

* Open statement (printable).
* Email the patient statement.
* Send statement via WhatsApp.
* Statement totals — total submitted, total estimated, grand total.

## 22. Insurance Coverage (panel)

* Primary coverage card — insurer, network, plan, validity, copay.
* Secondary coverage card — same.
* Add primary coverage CTA (when missing).
* Add secondary coverage CTA (when missing).
* Edit patient coverage shortcut.
* Latest admission coverage with policy + class.

## 23. Claims

* Claims history list (all claims for this patient).
* Per-claim status — Pending, Claim sent, Accepted, Rejected.
* Per-claim totals — submitted, accepted, rejected, net.
* Click to open the originating admission.
* Open the latest admission to add or edit a claim.

## 24. Cross-tab Quick Actions (+ buttons)

A consistent **+** button on every list lets you create:

* New vital reading.
* New prescription.
* New lab order.
* New imaging order.
* New treatment plan.
* New bill.
* New payment.
* New appointment.
* New vaccine dose.
* New referral.
* New family member.
* New document.

## 25. Drill-down Links

Every row in every list is clickable and opens the originating record
in its native screen:

* Visit row → visit form.
* Prescription row → prescription form.
* Lab row → lab request.
* Imaging row → radiology request / admission.
* Bill row → bill editor.
* Payment row → payment editor.
* Treatment plan row → plan editor.
* Tooth click → full dental chart.
* Document tile → DM2 viewer.
* Claim row → admission with claim panel.

## 26. UI Quality-of-life

* Per-list **Show all / Show fewer** toggle.
* Per-list **Search** filter.
* Tooltip on every status badge.
* Tooltip on every micro-icon (alerts, flags).
* Tooltip on every clickable row explaining what will open.
* Esc closes any opened drill-down dialog.
* Mobile-friendly — the dashboard re-flows to a single column on small
  screens.
* Empty-state messages on every list ("No appointments on this day.",
  "No upcoming appointment", "No diagnosis", "No description", "Not
  done", …).
* Per-tab last-position memory.
* Avatar fallback when no photo is uploaded.

## 27. Permissions & Read-only Mode

* Sensitive sections (insurance, billing) hide their + buttons for
  users without the right role.
* Read-only mode hides every Edit / Create control.
* Cashiers see Billing & Insurance + read-only Clinical / History.
* Physicians see everything except + on bills (depends on clinic
  policy).

## 28. Integration Points

The Patient Dashboard is a single page but every section delegates to
another HMS module:

| Section | Powered by |
|---|---|
| Documents | Document Manager (DM2) |
| Appointments | Scheduler V2 |
| Vitals / Allergies / Problems / Meds | Clinical EMR |
| Care plans + chart | Dental / Treatment-plan engine |
| Lab tests | Laboratory module |
| Imaging | Radiology / PACS module |
| Billing & Payments | Billing engine |
| Insurance & claims | Insurance / NPHIES module |
| History (immunisations, family, social, referrals) | EMR longitudinal record |

Every embedded section keeps the look of the dashboard — you don't
notice you're crossing module boundaries.

➡ Continue to the **[Profile tab](tabs/profile.md)**.
