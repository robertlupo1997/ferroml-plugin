# FerroML Plugin for Claude Code

End-to-end machine learning from natural conversation. Say "I have sales data, predict next month's revenue" and Claude handles everything -- data profiling, model selection, training, diagnostics, and a plain-language report.

Powered by [FerroML](https://github.com/robertlupo1997/ferroml), a statistically rigorous ML library written in Rust.

## Install

```bash
claude plugin add github:robertlupo1997/ferroml-plugin
```

FerroML itself must be installed in your Python environment:

```bash
pip install ferroml
```

The plugin's session-start hook will remind you if it's missing.

## Commands

| Command | What it does |
|---------|-------------|
| `/ml [file]` | End-to-end ML project -- profile, train, evaluate, report |
| `/ml-eval [model]` | Full diagnostics on a trained model |
| `/ml-report [audience]` | Plain-language summary for `boss`, `client`, `team`, or `technical` |
| `/ml-status [data]` | Check if a deployed model is still healthy (drift detection) |
| `/ml-compare [file]` | Compare multiple models with statistical significance tests |

All arguments are optional. Claude will ask for what it needs.

## What You Get

Every ML session includes:

- **Model recommendations** based on your data characteristics
- **Statistical diagnostics** -- not just accuracy, but residuals, confidence intervals, feature importance, assumption tests
- **Plain-language explanations** adapted to your technical level
- **Session state** persisted in `.ferroml-session.json` so you can pick up where you left off

## How It Works

The plugin bundles:

- **1 skill** (56 files) -- the core ML intelligence with 6 workflows, 30 template scripts, 14 reference docs
- **5 commands** -- discoverable entry points for common workflows
- **3 hooks** -- session bootstrap, data file validation, diagnostic quality enforcement
- **1 agent** -- autonomous ML engineer for heavy workloads (AutoML, multi-model comparison)

Claude uses FerroML's Python API directly (`import ferroml`). No MCP server, no subprocess calls, no overhead.

## Examples

```
> /ml sales_data.csv
# Claude profiles the data, recommends models, trains the best one,
# runs diagnostics, and explains results in plain language.

> /ml-compare customer_churn.csv
# Trains 5 models, runs cross-validation, computes statistical
# significance tests, returns a ranked leaderboard.

> /ml-report boss
# Generates a one-page executive summary of model performance
# with business impact and recommendations.

> /ml-status new_orders.csv
# Checks for data drift between training and production data,
# flags any degradation.
```

Or just talk naturally:

```
> I have a CSV of patient data. Can you predict readmission risk?
# The skill auto-activates and runs the full workflow.
```

## Requirements

- [Claude Code](https://claude.ai/code) CLI, desktop app, or IDE extension
- Python 3.10+
- `pip install ferroml` (or `pip install ferroml[all]` for Polars/Pandas support)

## License

MIT OR Apache-2.0 (intended; this repo does not include a LICENSE file yet)
