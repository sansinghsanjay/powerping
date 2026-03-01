import json
import os
from pathlib import Path

from playsound3 import playsound


def _load_config() -> dict:
    """Load configuration from config.json located at the project root."""
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "config.json"

    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def play_notification_sound() -> None:
    """Play the notification sound defined in config.json."""
    config = _load_config()
    sound_path = config.get("sound_file")
    if not sound_path:
        return

    project_root = Path(__file__).resolve().parents[1]
    full_path = (project_root / sound_path).resolve()

    if not full_path.exists():
        return

    # playsound blocks until the sound finishes playing.
    playsound(str(full_path))

