# Proposed methodology and limitations

## Workflow

1. Define scenario, taxonomy and KPI formulas.
2. Generate deterministic synthetic customers, beneficiary registrations, payments and case outcomes.
3. Validate uniqueness, timestamps, referential integrity, plausible distributions and nonnegative money fields.
4. Use PostgreSQL to analyse transaction behaviour and fraud outcomes.
5. Use Python to compare groups, visualise risk indicators and build rule-based scores.
6. Evaluate on a chronological holdout period; tune thresholds only on earlier data.
7. Report performance, alert capacity and sensitivity to assumptions.
8. Build Power BI reporting and document synthetic cases.

## Data-generation safeguards

- Use a fixed seed and document scenario parameters.
- Generate legitimate high-value payments and fraudulent low-value payments to prevent trivial separation.
- Avoid making scam category or fraud label a scoring input.
- Simulate reporting delays and pending cases; ensure outcomes occur after the payment.
- Keep reimbursement, recovery and gross fraud amount conceptually separate.

## Key limitations

- Synthetic distributions may not reflect a specific bank's true base rates or attacker adaptation.
- Simulated labels cannot validate real-world precision or prevented losses.
- Observed correlations do not prove causation.
- Actual intervention outcomes depend on customer contact, timing and payment rails.
- Regulatory summaries require current official-source checks and may change.

## References to consult

- https://www.psr.org.uk/our-work/app-scams/
- https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications
- https://www.fca.org.uk/firms/financial-crime
