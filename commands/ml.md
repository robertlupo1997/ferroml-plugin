---
name: ml
description: Start an end-to-end ML project — profile data, train models, evaluate, and get a plain-language report.
arguments:
  - name: data_file
    description: Path to a CSV or Parquet data file. If omitted, Claude will ask.
    required: false
---

The user wants to run an end-to-end machine learning workflow.

## Instructions

1. If `$ARGUMENTS` includes a data file path, use it. Otherwise, ask the user which file to use. Check that the file exists before proceeding.

2. Ask what they want to predict (the target column) unless it's obvious from context.

3. Follow the **ferroml-ml** skill's **Workflow 1: End-to-End ML** exactly:
   - Explore data (`scripts/explore_data.py`)
   - Quality audit (`scripts/data_quality_audit.py`)
   - Leakage check (`scripts/detect_leakage.py`)
   - Feature engineering (`scripts/feature_engineer.py`)
   - Model selection via `ferroml.recommend(X, y, task=...)`
   - Train the top recommended model with a proper train/test split
   - Full diagnostics: residuals, confidence intervals, feature importance
   - Generate a plain-language report of results

4. Adapt explanations to the user's technical level. Non-technical users get business-language summaries. ML engineers get statistical details.

5. Always show diagnostics — never report bare accuracy. This is FerroML's core differentiator.

6. Write session state to `.ferroml-session.json` when training completes.
