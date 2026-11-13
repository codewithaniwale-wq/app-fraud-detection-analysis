# Business problem and investigation brief

## 1. Scenario

**Organisation:** Northstar Digital Bank (fictional). **Jurisdiction:** United Kingdom. **Role:** Fraud Analyst. **Scope:** Outbound retail authorised push payments, initially focused on domestic GBP account-to-account transfers.

The bank suspects that social engineering scams are causing losses among customers who authorise payments themselves. Transaction authentication alone cannot establish whether the payer was deceived. The fraud team needs risk indicators that are explainable, usable at payment time, and manageable within analyst capacity.

## 2. Decision to support

**Which outgoing payments should be allowed, warned, stepped up, or referred for urgent review, given expected fraud losses and the cost of false alarms?**

The project is an analytical simulation, not a deployable banking control.

## 3. Stakeholders

- Fraud operations: actionable alerts and supporting evidence.
- Fraud strategy: thresholds, trade-offs and intervention effectiveness.
- Financial crime leadership: fraud trends and operational capacity.
- Customer protection: friction, reporting, recovery and reimbursement.

## 4. Research questions

1. What share of transactions and total value are confirmed APP fraud?
2. Which scam types account for the most cases and gross loss?
3. How does fraud incidence differ for new versus established beneficiaries?
4. How does payment size relative to customer history relate to fraud?
5. Do recent payment frequency and sudden behaviour changes improve detection?
6. How do risk thresholds trade off precision, recall and false positives?
7. How much *potential* fraud value could a feasible intervention capture, under explicitly stated assumptions?
8. How do funds recovery and customer reimbursement change the financial outcomes, without double-counting?

## 5. Scope

**In scope:** Synthetic retail payment records; beneficiary and customer histories; retrospective case labels; transparent rule-based scoring; SQL and Python investigations; Power BI management reporting.

**Out of scope:** Real customer data; production payment blocking; live case-management integrations; definitive regulatory eligibility determinations; claims of proven loss prevention; causal attribution of fraud to any single feature.

## 6. Success criteria

- Reproducible synthetic dataset with documented generation assumptions.
- No label leakage or future information in transaction-time features.
- At least 10 interpretable SQL investigations.
- Clearly defined precision, recall, false positive rate, value recall and alerts per day.
- Transparent comparison of candidate thresholds against a simple baseline.
- Four-page Power BI report and three synthetic investigation narratives.
- GitHub repository runnable by a reviewer with clear instructions.

## 7. Initial hypotheses (not findings)

H1: New beneficiaries may be associated with higher APP fraud incidence.

H2: Unusually large payments relative to a customer's historical behaviour may carry higher risk.

H3: Combining multiple indicators may improve detection compared with single-indicator rules.

H4: Increasing sensitivity may increase alert volume and false positives.

## 8. Research and regulatory context

Consult the PSR, UK Finance and FCA primary sources for current UK definitions and relevant requirements. Reimbursement eligibility and limits must be dated and scoped to the relevant payment system and claim; they should not be inferred from a synthetic dataset.
