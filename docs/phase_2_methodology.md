# Phase 2 — Synthetic data methodology

**Scope:** 2025 calendar year; default 100,000 payments, 8,000 customers, deterministic seed 42.

## Tables

- `customers.csv`: customer_id, account_opened_at, segment, baseline_payment_gbp
- `beneficiaries.csv`: beneficiary_id, created_at, beneficiary_type
- `transactions.csv`: transaction_id, customer_id, beneficiary_id, transaction_datetime, amount_gbp, channel, beneficiary_age_days, is_first_payment, cop_result, device_changed_recently, transactions_24h, amount_vs_customer_avg
- `fraud_cases.csv`: case_id, transaction_id, scam_type, fraud_reported_at, recovered_amount_gbp, reimbursed_amount_gbp, case_status

**Ground truth:** A transaction is retrospectively labelled confirmed fraud **if and only if** its transaction_id occurs in `fraud_cases.csv`. Join this table for retrospective analytics only. Never use scam type, case status, recovery, reimbursement, or reporting timestamp as transaction-time model features.

## Simulation choices and caveats

- Fraud probability is intentionally set at 2.5% for an analysable sample, **not** to represent the UK APP fraud incidence rate.
- Fraud amounts tend to be higher, new beneficiary relationships are more common, and CoP mismatches are more common, but legitimate payments can exhibit the same signals.
- Beneficiary age is simulated as the age of the customer-beneficiary relationship; it is not the age of the beneficiary's bank account. The `created_at` in the beneficiaries table is synthetic metadata and is **not** the customer-specific add timestamp. Do not infer one from the other.
- `transactions_24h` counts prior payments from the same customer within 24 hours, excluding the current payment.
- `amount_vs_customer_avg` uses a simulated customer baseline known at payment time, not a full-year realised average.
- Scam category is sampled independently of behavioural details; this is a teaching simplification.
- Case reporting delays and reimbursement amounts are simulated without modelling actual eligibility or PSR legal requirements. Do not use them to infer real reimbursement rates.
- Cases may be reported after 2025; this is expected and reflects delayed reporting.
- Customer, beneficiary and case identities are entirely fabricated. Do not represent results as actual UK fraud statistics.
- The simulation is **not a calibrated production model**. The synthetic fraud indicators are engineered to differ between classes, so detection performance may be artificially strong. Benchmark on real, governed data before any operational claim.

## Reproduce

```bash
python -m src.generate_data --transactions 100000 --customers 8000 --seed 42
python -m src.validate_data
python -m pytest -q
```

The generator uses only Python's standard library. The generated files are ignored by Git to keep the repository lean. To preview, use `--transactions 500 --customers 70`.
