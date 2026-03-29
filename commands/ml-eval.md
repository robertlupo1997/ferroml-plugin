---
name: ml-eval
description: Run full diagnostics on a trained model — residuals, calibration, learning curves, assumption tests.
arguments:
  - name: model
    description: Path to a saved model file, or "last" to use the most recent model from this session.
    required: false
---

The user wants to evaluate an existing trained model with full diagnostics.

## Instructions

1. Find the model to evaluate:
   - If `$ARGUMENTS` specifies a model path, load it.
   - If `$ARGUMENTS` is "last" or empty, check `.ferroml-session.json` for the most recently trained model.
   - If no model is found, ask the user.

2. Follow the **ferroml-ml** skill's **Workflow 3: Evaluation & Diagnostics**:
   - Error analysis (`scripts/error_analysis.py`) — where the model struggles
   - Learning curves (`scripts/learning_curves.py`) — over/underfitting diagnosis
   - Calibration (`scripts/calibrate_probabilities.py`) — for classifiers
   - Assumption tests (`scripts/validate_assumptions.py`) — residual normality, homoscedasticity
   - Feature importance (`scripts/explain_model.py`)

3. Present a structured diagnostic report:
   - Overall performance metrics with confidence intervals
   - Key diagnostic findings (what's good, what's concerning)
   - Actionable recommendations (e.g., "model underfits — try a more complex model or engineer more features")

4. Adapt depth to the user's technical level. Non-technical users get "your model is 92% accurate and most reliable for customers aged 25-45." ML engineers get residual plots and p-values.
