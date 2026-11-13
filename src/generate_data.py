"""Reproducible, fully synthetic APP payment dataset. No real customer information."""
import argparse
import csv
import random
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path

START = datetime(2025, 1, 1)
END = datetime(2026, 1, 1)
SCAMS = ['purchase', 'investment', 'romance', 'impersonation', 'invoice_redirection']

def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def generate(output_dir='data/generated', n_transactions=100_000, n_customers=8_000, seed=42):
    if n_transactions < 1 or n_customers < 1:
        raise ValueError('Counts must be positive')
    rng = random.Random(seed)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    customers = []
    for i in range(n_customers):
        opened = START - timedelta(days=rng.randint(30, 2200))
        customers.append(dict(customer_id=f'C{i+1:06d}', account_opened_at=opened.date().isoformat(), segment=rng.choices(['retail','student','business'],[.79,.13,.08])[0], baseline_payment_gbp=round(rng.lognormvariate(4.6,.75),2)))
    # Distinct beneficiary IDs can be shared across customers (potential network signals).
    n_beneficiaries = max(100, int(n_transactions*.22))
    beneficiaries = []
    for i in range(n_beneficiaries):
        added = START - timedelta(days=rng.randint(0,700))
        beneficiaries.append(dict(beneficiary_id=f'B{i+1:06d}', created_at=added.isoformat(timespec='seconds'), beneficiary_type=rng.choices(['individual','business'],[.68,.32])[0]))
    # Fraud is intentionally oversampled to create enough positive examples; not a population estimate.
    fraud_probability = .025
    transactions, cases = [], []
    history = defaultdict(deque)
    seen = set()
    # Chronological ordering makes lookback features strictly historical.
    times = sorted(START + timedelta(seconds=rng.randrange(int((END-START).total_seconds()))) for _ in range(n_transactions))
    for idx, ts in enumerate(times,1):
        cidx = rng.randrange(n_customers)
        customer = customers[cidx]
        customer_id = customer['customer_id']
        is_fraud = rng.random() < fraud_probability
        scam = rng.choice(SCAMS) if is_fraud else ''
        # Some customers pay common recipients, some pay newer recipients.
        if rng.random() < (.80 if is_fraud else .33):
            bidx = rng.randrange(max(1,n_beneficiaries//3),n_beneficiaries)
        else:
            bidx = rng.randrange(n_beneficiaries)
        ben = beneficiaries[bidx]
        # A customer-beneficiary relationship can start only at or before the payment.
        key=(customer_id,ben['beneficiary_id'])
        first = key not in seen
        seen.add(key)
        # Simulated first-added time: 0-5 days for many fraud payments, but not all.
        if first:
            age_days = rng.randint(0,5) if is_fraud and rng.random()<.72 else rng.randint(0,600)
        else:
            age_days = rng.randint(8,600)
        amount = max(1.0, rng.lognormvariate(7.65, .95) if is_fraud else rng.lognormvariate(4.7,1.0))
        amount = round(min(amount,75000),2)
        past = history[customer_id]
        while past and past[0] < ts-timedelta(hours=24):
            past.popleft()
        transactions_24h = len(past)  # prior payments only, excludes current payment
        past.append(ts)
        cop = rng.choices(['match','close_match','no_match','unavailable'], [.52,.13,.29,.06] if is_fraud else [.88,.06,.03,.03])[0]
        device_changed = int(rng.random() < (.24 if is_fraud else .06))
        txid=f'T{idx:08d}'
        transactions.append(dict(transaction_id=txid,customer_id=customer_id,beneficiary_id=ben['beneficiary_id'],transaction_datetime=ts.isoformat(timespec='seconds'),amount_gbp=f'{amount:.2f}',channel=rng.choices(['mobile','web','branch'],[.78,.19,.03])[0],beneficiary_age_days=age_days,is_first_payment=int(first),cop_result=cop,device_changed_recently=device_changed,transactions_24h=transactions_24h,amount_vs_customer_avg=round(amount/max(customer['baseline_payment_gbp'],1),2)))
        if is_fraud:
            delay=timedelta(days=rng.randint(1,45),hours=rng.randint(0,23))
            recovered=round(amount*rng.choice([0,0,0,.15,.4,.8]),2)
            reimbursed=round((amount-recovered)*rng.choice([0,.5,1]),2)
            cases.append(dict(case_id=f'F{len(cases)+1:07d}',transaction_id=txid,scam_type=scam,fraud_reported_at=(ts+delay).isoformat(timespec='seconds'),recovered_amount_gbp=f'{recovered:.2f}',reimbursed_amount_gbp=f'{reimbursed:.2f}',case_status='confirmed'))
    write_csv(out/'customers.csv', list(customers[0]),customers)
    write_csv(out/'beneficiaries.csv',list(beneficiaries[0]),beneficiaries)
    write_csv(out/'transactions.csv',list(transactions[0]),transactions)
    write_csv(out/'fraud_cases.csv',['case_id','transaction_id','scam_type','fraud_reported_at','recovered_amount_gbp','reimbursed_amount_gbp','case_status'],cases)
    print(f'Created {len(transactions):,} payments, {len(customers):,} customers, {len(beneficiaries):,} beneficiaries and {len(cases):,} confirmed synthetic fraud cases in {out}')
    return {'transactions':len(transactions),'customers':len(customers),'beneficiaries':len(beneficiaries),'fraud_cases':len(cases)}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',default='data/generated')
    parser.add_argument('--transactions',type=int,default=100_000)
    parser.add_argument('--customers',type=int,default=8_000)
    parser.add_argument('--seed',type=int,default=42)
    args=parser.parse_args()
    generate(args.output_dir,args.transactions,args.customers,args.seed)
