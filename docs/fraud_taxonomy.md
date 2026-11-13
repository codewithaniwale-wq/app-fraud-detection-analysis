# APP fraud taxonomy — initial working definitions

| Scam category | Example social-engineering mechanism | Possible indicators (not proof) |
|---|---|---|
| Purchase scam | Payment for goods or services that do not arrive | New beneficiary, first-time purchase, unusual amount |
| Investment scam | Fake or misrepresented investment opportunity | Large payment, repeated transfers, new recipient |
| Romance scam | Manipulated relationship leading to transfers | Repeat payments to beneficiary, escalating values |
| Impersonation scam | Criminal pretends to be bank, police or another authority | Sudden unusual payment, new beneficiary, urgency reported later |
| Invoice / mandate redirection | Genuine payment instruction replaced with criminal account details | New or changed beneficiary, Confirmation of Payee mismatch |
| Other / unknown | Case not yet classified | Do not assign unsupported subtype |

## Label rules

`is_app_fraud` is a retrospective confirmed-case outcome, not a transaction-time input. `scam_type` is assigned only when a case is classified; unknown and pending cases must remain distinct from confirmed legitimate payments. Indicators suggest investigation, not guilt or certainty. The taxonomy will be reconciled against current UK Finance reporting categories in Phase 2.
