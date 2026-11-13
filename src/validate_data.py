"""Validate synthetic data integrity and accounting invariants."""
import argparse
import csv
from datetime import datetime
from pathlib import Path

def read(path):
    with path.open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def validate(directory='data/generated'):
    folder=Path(directory)
    customers=read(folder/'customers.csv')
    beneficiaries=read(folder/'beneficiaries.csv')
    tx=read(folder/'transactions.csv')
    cases=read(folder/'fraud_cases.csv')
    assert len({x['customer_id'] for x in customers})==len(customers)
    assert len({x['beneficiary_id'] for x in beneficiaries})==len(beneficiaries)
    assert len({x['transaction_id'] for x in tx})==len(tx)
    assert len({x['transaction_id'] for x in cases})==len(cases)
    customer_ids={x['customer_id'] for x in customers}
    ben_ids={x['beneficiary_id'] for x in beneficiaries}
    tx_by_id={x['transaction_id']:x for x in tx}
    for t in tx:
        assert t['customer_id'] in customer_ids and t['beneficiary_id'] in ben_ids
        assert float(t['amount_gbp'])>0
        assert t['cop_result'] in {'match','close_match','no_match','unavailable'}
        assert datetime(2025,1,1)<=datetime.fromisoformat(t['transaction_datetime'])<datetime(2026,1,1)
        assert int(t['transactions_24h'])>=0
    for c in cases:
        assert c['transaction_id'] in tx_by_id
        t=tx_by_id[c['transaction_id']]
        assert datetime.fromisoformat(c['fraud_reported_at'])>=datetime.fromisoformat(t['transaction_datetime'])
        assert float(c['recovered_amount_gbp'])+float(c['reimbursed_amount_gbp'])<=float(t['amount_gbp'])+.011
    print(f'PASS: {len(tx):,} transactions; {len(cases):,} confirmed fraud cases; all integrity checks passed')
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--data-dir',default='data/generated'); args=p.parse_args()
    validate(args.data_dir)
