# KPI definitions and calculation rules

All denominators and time windows must be displayed in reporting. The values below are **definitions**, not measured results.

| KPI | Definition | Caution |
|---|---|---|
| Transaction fraud rate | Confirmed fraudulent transactions / all eligible transactions | Distinguish unknown labels from genuine |
| Gross fraud value | Sum of amounts for confirmed APP fraud payments | Not the same as bank net loss |
| Fraud value rate | Gross fraud value / total eligible payment value | Report alongside transaction rate |
| Precision | TP / (TP + FP) | Undefined if no alerts; document convention |
| Recall | TP / (TP + FN) | Depends on label completeness |
| False positive rate | FP / (FP + TN) | Different from false discovery rate |
| Value-weighted recall | Fraud payment value flagged / total confirmed fraud value | Does not establish prevented loss |
| Alert volume | Number of flagged payments per day | Capacity and duplicates matter |
| Recovery rate | Funds recovered / gross fraud value | Avoid counting reimbursement as recovery |
| Reimbursement rate | Customer reimbursement / eligible or confirmed claim value | Define eligible population explicitly |
| Estimated prevented loss | Flagged fraud value × assumed intervention success rate | Scenario estimate only; account for release timing |

## Confusion matrix

- TP: flagged and confirmed fraud.
- FP: flagged and confirmed legitimate.
- FN: not flagged but confirmed fraud.
- TN: not flagged and confirmed legitimate.

Exclude pending/unknown cases from binary classification metrics, and report excluded volume. Do not use final case outcomes to compute payment-time scores.
