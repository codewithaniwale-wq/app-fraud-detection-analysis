-- PostgreSQL schema; use CSV header imports in this order: customers, beneficiaries, transactions, fraud_cases.
CREATE TABLE IF NOT EXISTS customers (
 customer_id TEXT PRIMARY KEY, account_opened_at DATE NOT NULL, segment TEXT NOT NULL, baseline_payment_gbp NUMERIC(12,2) NOT NULL
);
CREATE TABLE IF NOT EXISTS beneficiaries (
 beneficiary_id TEXT PRIMARY KEY, created_at TIMESTAMP NOT NULL, beneficiary_type TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS transactions (
 transaction_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL REFERENCES customers(customer_id), beneficiary_id TEXT NOT NULL REFERENCES beneficiaries(beneficiary_id), transaction_datetime TIMESTAMP NOT NULL, amount_gbp NUMERIC(12,2) NOT NULL, channel TEXT NOT NULL, beneficiary_age_days INTEGER NOT NULL, is_first_payment INTEGER NOT NULL, cop_result TEXT NOT NULL, device_changed_recently INTEGER NOT NULL, transactions_24h INTEGER NOT NULL, amount_vs_customer_avg NUMERIC(12,2) NOT NULL
);
CREATE TABLE IF NOT EXISTS fraud_cases (
 case_id TEXT PRIMARY KEY, transaction_id TEXT UNIQUE NOT NULL REFERENCES transactions(transaction_id), scam_type TEXT NOT NULL, fraud_reported_at TIMESTAMP NOT NULL, recovered_amount_gbp NUMERIC(12,2) NOT NULL, reimbursed_amount_gbp NUMERIC(12,2) NOT NULL, case_status TEXT NOT NULL
);
