# Proposed data dictionary — Phase 1 design

**Status:** Schema proposal only. Data generation begins in Phase 2.

## transactions

| Field | Type | Meaning | Available at payment time? |
|---|---|---|---|
| transaction_id | TEXT (PK) | Unique payment | Yes |
| customer_id | TEXT (FK) | Sending customer | Yes |
| beneficiary_id | TEXT (FK) | Recipient | Yes |
| transaction_datetime | TIMESTAMP | Payment initiation time | Yes |
| amount_gbp | DECIMAL(12,2) | Outgoing payment amount | Yes |
| channel | TEXT | Mobile, web or branch | Yes |
| cop_result | TEXT | Confirmation of Payee result | Yes, if checked |
| device_changed_recently | BOOLEAN | Recent device change | Yes, if observed |
| is_app_fraud | BOOLEAN/NULL | Retrospective confirmed fraud label | **No** |
| scam_type | TEXT/NULL | Investigated scam subtype | **No** |
| fraud_reported_at | TIMESTAMP/NULL | Customer/case report time | **No** |
| recovered_amount_gbp | DECIMAL(12,2)/NULL | Funds recovered | **No** |
| reimbursed_amount_gbp | DECIMAL(12,2)/NULL | Customer reimbursement | **No** |

## customers

| Field | Type | Meaning |
|---|---|---|
| customer_id | TEXT (PK) | Synthetic customer key |
| account_opened_at | DATE | Tenure reference |
| segment | TEXT | Simulated customer segment |

## beneficiaries

| Field | Type | Meaning |
|---|---|---|
| beneficiary_id | TEXT (PK) | Synthetic recipient key |
| first_seen_at | TIMESTAMP | First appearance in dataset (not necessarily account opening) |

## fraud_cases

| Field | Type | Meaning |
|---|---|---|
| case_id | TEXT (PK) | Case reference |
| transaction_id | TEXT (FK) | Associated payment |
| reported_at | TIMESTAMP | Report time |
| decision_at | TIMESTAMP/NULL | Case resolution time |
| case_status | TEXT | Pending, confirmed fraud, confirmed legitimate |
| scam_type | TEXT/NULL | Assigned subtype |

## Derived transaction-time features

- `is_first_payment_to_beneficiary`: no earlier payment from this customer to this beneficiary.
- `beneficiary_age_days`: time since this customer first registered beneficiary, **if** beneficiary-add event exists; do not equate with `first_seen_at`.
- `transactions_24h`: count of preceding payments in rolling 24 hours; exclude current transaction unless explicitly defined.
- `amount_vs_customer_avg`: amount divided by prior historical customer average; handle customers without history.

**Leakage prevention:** All historical features must be computed using events strictly before the scored transaction. A beneficiary registration events table may be added in Phase 2 to calculate true beneficiary age.
