# python-packages
import json
from pathlib import Path
import pygame

# function to load configuration
def _load_config() -> dict:
    """Load configuration from config.json located at the project root."""
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "config.json"
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)

# function to get sound path
def get_sound_path() -> Path | None:
    """Return the full path to the notification sound from config, or None if not set."""
    config = _load_config()
    sound_path = config.get("sound_file")
    if not sound_path:
        return None
    project_root = Path(__file__).resolve().parents[1]
    full_path = (project_root / sound_path).resolve()
    return full_path if full_path.exists() else None

# function to play notification sound
def play_notification_sound() -> None:
    """Play the notification sound once (blocking)."""
    path = get_sound_path()
    if not path:
        return
    pygame.mixer.init()
    pygame.mixer.music.load(str(path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()