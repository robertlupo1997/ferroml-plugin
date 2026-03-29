---
name: ml-report
description: Generate a plain-language summary of model performance for a specific audience.
arguments:
  - name: audience
    description: "Who the report is for: boss, client, team, or technical. Defaults to non-technical."
    required: false
---

The user wants a report summarizing their ML model's results, targeted to a specific audience.

## Instructions

1. Determine the audience from `$ARGUMENTS`. Default to non-technical if not specified.
   - **boss** — Executive summary: business impact, ROI, key metrics, one-paragraph recommendation
   - **client** — What the model does, how reliable it is, what to expect, caveats
   - **team** — Technical summary with methodology, metrics, next steps
   - **technical** — Full statistical report: metrics, diagnostics, assumptions, limitations

2. Find the current model:
   - Check `.ferroml-session.json` for the most recent model and its metrics.
   - If no session state exists, ask the user which model to report on.

3. Follow the **ferroml-ml** skill's **Workflow 6: Explain to Stakeholders**:
   - Use `scripts/explain_model.py` for feature importance narratives
   - Use `scripts/generate_report.py` as a template, adapted to the audience
   - Include confidence intervals — "the model predicts revenue within +/- $12K, 95% of the time"

4. Use `scripts/cost_sensitive_analysis.py` if the model has business-cost implications.

5. Output a clean, formatted report. For boss/client audiences, avoid all jargon. For technical audiences, include full statistical tables.
