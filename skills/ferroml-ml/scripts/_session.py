"""Session state management — writes .ferroml-session.json for cross-command persistence."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone


SESSION_FILE = ".ferroml-session.json"


def load() -> dict:
    """Load existing session state or return empty dict."""
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE) as f:
            return json.load(f)
    return {"models": [], "data_files": [], "current_best": None}


def save(state: dict) -> None:
    """Write session state to disk."""
    with open(SESSION_FILE, "w") as f:
        json.dump(state, f, indent=2, default=str)


def record_data_profile(path: str, shape: tuple, target: str | None, task: str | None) -> None:
    """Record that a data file was profiled."""
    state = load()
    entry = {
        "path": path,
        "rows": shape[0],
        "columns": shape[1],
        "target": target,
        "task": task,
        "profiled_at": datetime.now(timezone.utc).isoformat(),
    }
    # Deduplicate by path
    state["data_files"] = [d for d in state.get("data_files", []) if d["path"] != path]
    state["data_files"].append(entry)
    save(state)


def record_model(name: str, algorithm: str, metrics: dict, data_path: str | None = None) -> None:
    """Record a trained model and update current best."""
    state = load()
    entry = {
        "name": name,
        "algorithm": algorithm,
        "metrics": metrics,
        "data_path": data_path,
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }
    state.setdefault("models", []).append(entry)
    state["current_best"] = entry
    save(state)


def record_comparison(leaderboard: list, best_model: str | None) -> None:
    """Record a model comparison result."""
    state = load()
    state["last_comparison"] = {
        "leaderboard": leaderboard,
        "best_model": best_model,
        "compared_at": datetime.now(timezone.utc).isoformat(),
    }
    if best_model:
        state["current_best"] = {"name": best_model, "algorithm": best_model}
    save(state)
