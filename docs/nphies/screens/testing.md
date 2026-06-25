# The Testing area

The **Testing** area is a safe place to run the standard NPHIES test cases from
start to finish on the practice system. It's how you prove the whole flow works
before you go live, and it's what NPHIES certification is checked against.

## What you see

A list of test cases grouped by type — eligibility, authorizations, claims, and
payments. Each row shows:

| Column | Meaning |
|---|---|
| **Code / Description** | The test case and what it covers |
| **Record Validation** | Whether the local check passed (and the reason if not) |
| **Payload Check** | Whether the request is structurally complete |
| **NPHIES Response** | What the practice system replied (Approved, error, queued…) |
| **REQS** | How many of the case's requirements are met |

## The buttons on each row

- **Validate** runs the local pre-send checks without sending anything.
- **Inspect** opens the full request and reply in plain view.
- **Demonstrate** shows each requirement proved against the actual request.
- **Run** seeds the data and sends the case to the practice system.

## Running a group

You can run a whole group in one go and read the results down the list. A score
at the top shows how many passed.

!!! tip "Seed first"
    Use **Seed Test Data** before a run so the sample patients, doctors,
    coverage, and provider details are all in place. **Clear Test Data** wipes
    the test results so you can start a clean run.

!!! note "Some cases are meant to fail"
    A few certification cases send a deliberately incomplete request to prove the
    system handles a rejection correctly. A red result on those is expected.

**See also:** [Settings →](../settings.md)
