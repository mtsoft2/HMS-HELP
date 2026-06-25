# Getting started

This is the short path from a fresh setup to your first approved claim. Do it
once in **practice mode** and the rest of the module makes sense.

## Before you start

Ask your IT or implementation team to fill in **Settings** once — your provider
details, the two NPHIES web addresses, and the bridge (only if your system is
outside Saudi Arabia). See [Settings](settings.md). Until that's done, requests
can't reach NPHIES.

## Step by step

1. **Open NPHIES** from the menu. The title bar tells you whether you're in
   practice or live mode.
2. **Make sure you're in practice mode.** On the **Environment** tab, turn
   **Test Mode** on. Everything now goes to the NPHIES test system — safe to
   experiment.
3. **Check a patient's eligibility.** Look up the patient and run the
   eligibility check. In a few seconds you'll see whether the cover is active,
   the plan, the network, and any limits.
4. **Send a pre-authorization** for a service that needs approval first. The
   reply comes back Approved, Partially Approved, or Rejected. When approved, it
   carries an approval number.
5. **Read the result.** Open the record's **Communication** screen to see the
   decision, the approved items, and the reason for anything reduced or refused.
   The **Inspect** button shows the full request and reply in plain view if you
   want the detail.
6. **Turn the approval into a bill.** From the Communication screen, the
   **Create Bill** action builds the patient bill from the pre-authorization —
   it brings in the items, priced, with the patient and insurance shares.
7. **Create the claim.** The **Create Claim** action copies the patient, visit,
   diagnosis, and only the approved items at their approved quantities, and
   attaches the approval reference.
8. **Send the claim.** The insurer reviews it and replies with the approved
   amounts.
9. **Read the claim result.** The claim shows Approved, Partially Approved, or
   Not Approved, and each line shows its approved quantity and amount next to
   what you asked for.
10. **When you're confident, go live.** On the Environment tab, turn Test Mode
    off. From now on, requests go to the real NPHIES.

!!! warning "Live means real"
    With Test Mode off, every request goes to the real NPHIES and affects real
    patients and real money. Double-check the title bar before you send.

## If something is refused

Open **Inspect** on the row and read the reason in plain words. Most refusals
are a missing detail — fix it and send again. See
[the workflow](workflow/index.md) for the common ones.

**Next:** [Features →](features.md) · [The workflow →](workflow/index.md)
