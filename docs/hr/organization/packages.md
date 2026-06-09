# Packages

A **Package** is a re-usable salary template. Instead of typing basic
+ housing + transport on every contract, you create the package once
and pick it on the contract.

## Form (`HR_PACKAGE.FT`)

| Field | DB column |
|---|---|
| Name (EN) | `Name` |
| Name (AR) | `NAME_A` |
| Print Name (AR) | `HRP_PrintName_A` (short label printed on slips when space is tight) |
| Notes | `Note` |

## Allowance breakdown

Each package has child rows in `HR_PKALW` (one row per allowance
type — basic, housing, transportation, mobile, schooling, …):

| Column | Meaning |
|---|---|
| Type | FK to `HR_ALWTYPE`. |
| Amount | Fixed amount, or |
| Percent | % of basic (Type-Married, Type-Single — both possible). |
| Currency | Currency of the package. |

Maintained from the **Allowances** grid on the package form
(`HR_PKALW.GT`).

## Refresh propagation

When you change a package's amounts, **existing contracts are NOT
updated automatically** — the change applies only to new contracts
and to contracts when they are renewed via `HR_Contract_Renew`.

To push a package change to every active contract use the helper SP
`HR_PACKAGE_UPDATE` (run from a SQL prompt with the package ID as
parameter).
