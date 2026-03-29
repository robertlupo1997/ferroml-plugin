#!/usr/bin/env python3
"""FerroML PreToolUse(Bash) hook — validate data file references and catch sklearn installs."""

import json
import os
import re
import sys


def main():
    # Read tool input from stdin
    try:
        tool_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # Can't parse input — allow through
        sys.exit(0)

    command = tool_input.get("input", {}).get("command", "")
    if not command:
        sys.exit(0)

    # Check 1: Catch attempts to pip install sklearn/scikit-learn when ferroml covers the use case
    sklearn_pattern = r"pip\s+install\s+[^\n]*(?:scikit-learn|sklearn|xgboost|lightgbm)"
    match = re.search(sklearn_pattern, command)
    if match:
        print(
            f"WARN: This command installs {match.group(0).split()[-1]}. "
            "FerroML already provides equivalent functionality. "
            "Use `import ferroml` instead. If the user specifically requested this package, proceed."
        )
        # Warn but don't block — user may have a legitimate reason
        sys.exit(0)

    # Check 2: Detect ML scripts referencing data files and verify they exist
    # Look for common patterns: read_csv("file.csv"), pd.read_csv, pl.read_csv, open("file.csv")
    file_patterns = [
        r'read_csv\(["\']([^"\']+\.(?:csv|tsv))["\']',
        r'read_parquet\(["\']([^"\']+\.parquet)["\']',
        r'open\(["\']([^"\']+\.(?:csv|tsv|parquet))["\']',
        r'python3?\s+\S+\.py\s+["\']?(\S+\.(?:csv|tsv|parquet))',
    ]

    for pattern in file_patterns:
        matches = re.findall(pattern, command)
        for filepath in matches:
            # Resolve relative to working directory
            if not os.path.isabs(filepath):
                filepath_abs = os.path.join(os.getcwd(), filepath)
            else:
                filepath_abs = filepath

            if not os.path.exists(filepath_abs):
                # Block — missing data file is the #1 failure for non-technical users
                result = {
                    "decision": "block",
                    "reason": (
                        f"Data file not found: {filepath}\n"
                        "Ask the user to confirm the correct filename. "
                        "Check for typos or look in subdirectories."
                    ),
                }
                json.dump(result, sys.stdout)
                sys.exit(0)

    # All checks passed
    sys.exit(0)


if __name__ == "__main__":
    main()
