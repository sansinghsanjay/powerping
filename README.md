## PowerPing

PowerPing is a lightweight Windows background utility that monitors your laptop battery and proactively alerts you when the charge level reaches a configurable threshold (default: **98%**). It helps you avoid overcharging, extend battery health, and maintain better charging habits.

---

### Features

- **Automatic background startup**  
  - Runs automatically after Windows boot completes (via Task Scheduler or service setup).
- **Battery status monitoring**  
  - Detects whether the battery is **charging** or **on battery**.  
  - Tracks current **battery charge percentage** in real time.
- **Smart notifications**  
  - Shows a **desktop notification** near the bottom-right corner (system tray area) when the battery crosses a set threshold (e.g. 98%).  
  - Plays a **customizable sound** along with the notification.
- **Configurable behavior**  
  - Adjustable charge threshold (e.g. 90%, 95%, 98%).  
  - Optional cool‑down / reminder interval to avoid spamming notifications.  
  - Option to enable/disable sound.
- **Optimized for laptops**  
  - Designed specifically for Windows laptops running **Python 3.12.8**.  
  - Low CPU and memory footprint suitable for long‑running background use.

---

## Requirements

- **Operating system**: Windows 10 or later (laptop form factor recommended)  
- **Python**: **3.12.8** (64‑bit recommended)  
- **Recommended Python packages** (subject to change during implementation):
  - `psutil` – battery and power information
  - `plyer` or `win10toast` – system notifications
  - `playsound` or similar – audio playback

---

## Installation

### Install PowerPing

- **Option 1 – Clone the repository**

  ```bash
  git clone https://github.com/<your-username>/PowerPing.git
  cd PowerPing
  ```

- **Option 2 – Download the source**

  - Download the project archive (e.g. from GitHub) and extract it.
  - Open a terminal in the extracted `PowerPing` directory.

### Install dependencies

Once a `requirements.txt` is available, install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run PowerPing in the background at startup

There are multiple ways to run PowerPing automatically after boot:

- **Using Task Scheduler (recommended for most users)**:
  - Create a new Task:
    - **Trigger**: At log on (or at startup).
    - **Action**: Start a program → `python.exe`
    - **Arguments**: `C:\path\to\PowerPing\app.py`
    - **Start in**: `C:\path\to\PowerPing\`
  - Enable "Run whether user is logged on or not" if desired.
- **Alternative**: Add a shortcut to `app.py` (or a `.bat` wrapper) in the **Startup** folder.

> Exact step‑by‑step instructions can be refined once the script structure is finalized.

---

## Configuration

Configuration options will be exposed via a simple config file (e.g. `config.json` / `.ini`). Planned settings include:

- **Battery threshold**:  
  - Default: `98`  
  - Description: Percentage at which to trigger notification and sound.  
- **Sound file path**:  
  - Custom path to a `.wav` or `.mp3` file to play.

Example configuration file:

```json
{
  "threshold": 98,
  "sound_file": "assets/alert.wav"
}
```

---

## Architecture & File Structure

The current implementation mirrors the originally planned design. Key files and modules in the repository are:

- **`app.py`**
  - Main entry point. Loads configuration, initializes components, and starts the monitor loop.
- **`config.json`**
  - Default configuration file shipped with the project. See the **Configuration** section below for format.
- **`modules/battery_module.py`**
  - Encapsulates battery status access using `psutil`.
- **`modules/notification_module.py`**
  - Handles Windows toast notifications via `win10toast` or similar.
- **`modules/sound_module.py`**
  - Plays alert sounds (configurable file path).
- **`utils/load_config.py`**
  - Helper for reading and validating the JSON configuration.

The monitoring loop in `app.py`:

1. Reads battery percentage and charging state from `battery_module`.
2. Compares against the configured threshold.
3. Enforces the reminder interval to avoid repeated alerts.
4. Dispatches a notification (and optional sound) via the notification and sound modules.

This structure keeps concerns separated and makes the code easier to maintain or extend.

---

## License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for full license text.

---

## Contributing

Contributions, ideas, and bug reports are welcome.

Once this repository is initialized, you can:

1. Fork the project.
2. Create a feature branch.
3. Submit a pull request with a clear description of the changes and rationale.

