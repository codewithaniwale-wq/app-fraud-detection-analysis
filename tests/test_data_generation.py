import csv
from src.generate_data import generate
from src.validate_data import validate

def test_small_dataset(tmp_path):
    output=tmp_path/'synthetic'
    result=generate(output, n_transactions=500,n_customers=70,seed=42)
    assert result['transactions']==500
    assert validate(output)
    with (output/'transactions.csv').open(newline='') as f:
        assert len(list(csv.DictReader(f)))==500

def test_reproducible(tmp_path):
    a,b=tmp_path/'a',tmp_path/'b'
    generate(a,500,70,42)
    generate(b,500,70,42)
    for name in ['customers.csv','beneficiaries.csv','transactions.csv','fraud_cases.csv']:
        assert (a/name).read_bytes()==(b/name).read_bytes()
