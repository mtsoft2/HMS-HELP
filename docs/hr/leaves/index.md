# Leaves & Travel

HMS handles three closely-related leave objects:

| Page | Form | What it is |
|---|---|---|
| [Vacation Requests](vacation.md) | `HR_Vacation.FT` | The day-by-day annual / sick / educational leave request. |
| [Travel Authorisation](travel-auth.md) | `HR_VAUTH.FT` | Authorisation for an employee to travel abroad while on leave (used for ticket entitlement & re-entry visa). |
| [Vacation Extensions](extensions.md) | `HR_Extension.FT` | Extend an in-progress leave. |

## Leave types (`HR_VacationType`)

* **Annual** — counted against `HR_EMP_VacRemain`.
* **Sick** — counted separately; 30 full-pay + 60 half-pay days/year per Saudi labour law.
* **Educational** — exam / study leave.
* **Hajj** — once-in-employment.
* **Compassionate** — bereavement.
* **Unpaid** — does not accrue salary; days >14 reduce service period.
* **Maternity / Paternity**.
