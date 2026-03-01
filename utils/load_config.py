import json
from pathlib import Path

def load_config(path="config.json"):
    try:
        with open(Path(path), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}