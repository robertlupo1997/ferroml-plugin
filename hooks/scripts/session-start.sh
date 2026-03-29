#!/usr/bin/env bash
# FerroML SessionStart hook — check installation + scan for data files
set -euo pipefail

# Check if ferroml is importable
FERROML_STATUS="not_installed"
FERROML_VERSION=""
if python3 -c "import ferroml; print(ferroml.__version__)" 2>/dev/null; then
    FERROML_VERSION=$(python3 -c "import ferroml; print(ferroml.__version__)" 2>/dev/null)
    FERROML_STATUS="installed"
fi

# Scan for data files in working directory
DATA_FILES=""
if [ -d "." ]; then
    DATA_FILES=$(find . -maxdepth 2 \( -name "*.csv" -o -name "*.parquet" -o -name "*.tsv" \) -not -path "./.git/*" -not -path "./node_modules/*" -not -path "./.venv/*" 2>/dev/null | head -20 | tr '\n' ', ' | sed 's/,$//')
fi

# Check for existing session state
SESSION_STATE=""
if [ -f ".ferroml-session.json" ]; then
    SESSION_STATE="found"
fi

# Write to CLAUDE_ENV_FILE for session persistence
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    {
        echo "FERROML_STATUS=$FERROML_STATUS"
        echo "FERROML_VERSION=$FERROML_VERSION"
        echo "FERROML_DATA_FILES=$DATA_FILES"
        echo "FERROML_SESSION_STATE=$SESSION_STATE"
    } >> "$CLAUDE_ENV_FILE"
fi

# Output context for Claude
if [ "$FERROML_STATUS" = "not_installed" ]; then
    echo "FerroML is NOT installed. If the user asks for ML help, install it first:"
    echo "  pip install ferroml"
    echo ""
fi

if [ -n "$DATA_FILES" ]; then
    echo "Available datasets in working directory: $DATA_FILES"
fi

if [ "$SESSION_STATE" = "found" ]; then
    echo "Previous ML session state found (.ferroml-session.json) — use /ml-status or /ml-eval to continue."
fi
