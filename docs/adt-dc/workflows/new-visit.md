# New Visit

A **Visit** represents one in-person attendance at the clinic. It is
the container that holds the chart entries, prescriptions, lab
referrals and the bill for that day.

## Open

Click **New Visit** with the patient already in the banner.

## What you fill in

* **Date / time** — defaults to now.
* **Visit type** — Consultation, Follow-up, Emergency, Cleaning, Check-up,
  Cosmetic.
* **Dentist** — the treating doctor.
* **Room** — the chair / operatory.
* **Referred by** — if the patient was sent by another clinic.
* **Chief complaint** — short free-text on why they are there today.

## Save

Saving the visit:

* Creates a bill header against this visit.
* Makes the visit selectable in the Dental Chart's *Visit* dropdown.
* Adds the visit to the dentist's daily roster.

## What happens during the visit

The dentist works in the **Dental Chart** (next page). Every procedure
they tick on a tooth flows into:

* The chart history (visible from now on).
* The visit's bill (price taken from the price-list).
* The treatment plan if it is part of one.

## Closing the visit

When the patient is finished, the receptionist takes payment via **New
Receipt** and (optionally) prints the bill via **New Bill**. There is
no separate *Close Visit* button — the visit is implicitly closed when
no more procedures are added to it.
