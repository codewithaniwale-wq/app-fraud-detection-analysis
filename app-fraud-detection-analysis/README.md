# APP Fraud Detection & Financial Crime Intelligence

> **Status:** Phase 1 — Business understanding and project setup. No transaction results have been generated yet.

An end-to-end portfolio project investigating **Authorised Push Payment (APP) fraud** at **Northstar Digital Bank**, a fictional UK digital bank.

## Business problem

APP scams manipulate customers into authorising payments to fraudsters. The bank needs explainable, operationally feasible controls that identify risky payments before execution while limiting disruption to legitimate customers.

## Project objectives

1. Describe fraud prevalence and financial losses by scam type.
2. Investigate beneficiary novelty, unusual payment amounts, and payment velocity.
3. Develop transparent transaction-time fraud risk rules.
4. Evaluate detection effectiveness and alert workload.
5. Analyse recovery and reimbursement outcomes separately from detection.
6. Communicate results through Power BI and documented investigations.

## Technology

- **SQL:** PostgreSQL for transaction investigations and feature queries
- **Python:** pandas, NumPy, matplotlib and scikit-learn for data generation, analysis and rule evaluation
- **Power BI:** interactive fraud monitoring and management dashboards

## Project roadmap

| Phase | Deliverable | Status |
|---|---|---|
| 1. Business understanding | Business brief, KPI definitions, data model | In progress |
| 2. Synthetic data | Reproducible generator and validation | Planned |
| 3. SQL investigations | Documented analytical queries | Planned |
| 4. Exploratory analysis | Python notebooks and findings | Planned |
| 5. Detection evaluation | Risk rules, precision/recall, alert capacity | Planned |
| 6. Dashboard | Power BI report and screenshots | Planned |
| 7. Case studies | Three synthetic investigations | Planned |
| 8. Publication | Final executive report and GitHub polish | Planned |

## Repository structure

- `docs/`: business brief, metrics, fraud taxonomy, and proposed data dictionary
- `data/`: synthetic data documentation (no real customer information)
- `src/`: Python generation, features, and scoring (upcoming)
- `sql/`: SQL schema and investigations (upcoming)
- `notebooks/`: exploratory analysis and evaluation (upcoming)
- `dashboard/`: Power BI file and screenshots (upcoming)
- `investigations/`: synthetic case studies (upcoming)
- `reports/`: executive findings (upcoming)
- `tests/`: validation and automated checks (upcoming)

## Setup

Requires Python 3.11+; PostgreSQL and Power BI Desktop are used in later phases.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

No data generation or analytics are available in Phase 1. Do not interpret the planning documents as observed results.

## Documentation

1. [Business problem](docs/business_problem.md)
2. [Fraud taxonomy](docs/fraud_taxonomy.md)
3. [KPI definitions](docs/kpi_definitions.md)
4. [Proposed data dictionary](docs/data_dictionary.md)
5. [Methodology and limitations](docs/methodology.md)

## Data ethics and limitations

All future customer, beneficiary and transaction records will be **synthetic**. Fraud patterns and performance will be simulated and must not be represented as validated production outcomes. Detection features must be available at the time of scoring; post-event labels, claims and reimbursement fields are reserved for retrospective evaluation.

## Background sources

- [Payment Systems Regulator — APP scams](https://www.psr.org.uk/our-work/app-scams/)
- [UK Finance — Fraud reports](https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications)
- [FCA — Financial crime](https://www.fca.org.uk/firms/financial-crime)

## License

MIT. See [LICENSE](LICENSE).
