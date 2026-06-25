# Features

Everything the NPHIES module can do, in one list.

## Eligibility

- Check a patient's cover in seconds before you treat them.
- See the plan, network, member details, and any limits the insurer returns.

## Pre-authorization

- Request approval for services that need it first — operations, expensive
  items, optical, dental, and so on.
- Get back **Approved**, **Partially Approved**, or **Rejected**, with the reason
  shown on the line.
- Resubmit a rejected request, and link a follow-up request to an earlier one.

## Claims

- Send the bill after the service.
- See, line by line, how much the insurer approved, the patient's share, and the
  reason a line was reduced or refused.
- Handles every claim type: pharmacy, professional (clinic), institutional
  (inpatient), dental, optical, and newborn.

## From approval to bill to claim

- **Create Bill** builds the patient bill straight from an approved
  pre-authorization — items priced, with the patient and insurance shares, each
  line tied back to its pre-authorization item.
- **Import from Pre-auth** pulls every item from a pre-authorization into an
  open bill. Items not in your local price list (pharmacy items, for example)
  come in at the pre-authorization's own price. It's safe to run more than once.
- **Create Claim** turns an approved pre-authorization into a claim, copying the
  patient, visit, diagnosis, and only the approved items at their approved
  quantities, with the approval reference attached.

## Payments

- Follow a claim through to payment and see how much was paid.

## The Overview dashboard

- One page with your headline numbers for any date range you choose, and it
  remembers your choice next time.
- Cards for claims, approved, rejected, pending, the amount requested, and the
  amount approved.
- Charts comparing requested against approved amounts and quantities, plus a
  daily trend.

## The Communication screen

- Organised into **Eligibility**, **Items** (each line's approved-versus-
  requested amount and quantity, with its approval number), **Related Claims**,
  and a **Log**.
- An **Inspect** button shows the full request and reply in plain view.

## The check before sending

- Before any pre-authorization or claim leaves the building, the module checks
  it's complete — patient details, the treating doctor's license number, the
  required information, and that everything links up.
- Anything missing is flagged on the row so you fix it instead of having it
  bounced back.
- An optional stricter setting **blocks** an incomplete request from being sent
  at all.

## Practice mode and Testing

- **Practice mode** sends everything to the NPHIES test system — nothing touches
  real patients or money.
- The **Testing** area runs the standard NPHIES test cases from start to finish,
  so you can prove the whole flow before going live.

**Next:** [The workflow →](workflow/index.md)
