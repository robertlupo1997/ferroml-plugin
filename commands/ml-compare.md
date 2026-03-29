---
name: ml-compare
description: Compare multiple model types on the same data with a ranked leaderboard and significance tests.
arguments:
  - name: data_file
    description: Path to a CSV or Parquet data file. If omitted, Claude will ask.
    required: false
---

The user wants to compare multiple ML models on the same dataset and see which one wins.

## Instructions

1. If `$ARGUMENTS` includes a data file path, use it. Otherwise, ask the user which file to use. Check that the file exists.

2. Ask what they want to predict (target column) unless it's obvious from context.

3. Follow the **ferroml-ml** skill's **Workflow 2: Model Selection**:
   - Explore data (`scripts/explore_data.py`) to understand the dataset
   - Use `ferroml.recommend(X, y, task=...)` to get the top 5 model recommendations
   - Train all recommended models using cross-validation (`scripts/compare_models.py`)
   - Compute statistical significance tests between model pairs

4. Present a ranked leaderboard:
   - Model name, primary metric (with confidence interval), training time
   - Statistical significance: "Random Forest beats Linear Regression with 95% confidence (p=0.003)"
   - Winner recommendation with reasoning

5. For non-technical users: "I tested 5 different approaches. Gradient Boosting is the clear winner — it's 8% more accurate than the runner-up and that difference is statistically significant."

6. For ML engineers: full cross-validation results, per-fold metrics, paired t-test p-values.

7. Write all trained models to `.ferroml-session.json`.
