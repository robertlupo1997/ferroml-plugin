---
name: ml-status
description: Check if a deployed model is still healthy — detect data drift and performance degradation.
arguments:
  - name: prod_data
    description: Path to a file containing recent production data to compare against training data.
    required: false
---

The user wants to check whether a previously trained model is still performing well on new data.

## Instructions

1. Find the model and its training context:
   - Check `.ferroml-session.json` for the model, training data profile, and metrics.
   - If no session state exists, ask the user which model and what data to check.

2. If `$ARGUMENTS` includes a production data file, use it. Otherwise, ask for recent data.

3. Follow the **ferroml-ml** skill's **Workflow 4: Production Readiness**:
   - Run `scripts/detect_drift.py` — compare production data distributions against training data
   - Run `scripts/reproducibility_snapshot.py` — capture current model state
   - If the model can be re-evaluated on the new data, compute fresh metrics and compare against the original baseline

4. Report findings clearly:
   - **Healthy:** "Your model looks good. No significant drift detected. Performance is stable."
   - **Warning:** "Column 'price' has shifted — the average is 15% higher than training data. Monitor closely."
   - **Degraded:** "Model accuracy has dropped from 94% to 81%. Retraining is recommended."

5. If degradation is detected, recommend next steps: retrain, add new features, or investigate the data shift.
