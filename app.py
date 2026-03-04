# python imports
import time
import logging
import traceback

# modules import
from modules.battery_module import battery_status
from modules.notification_module import show_app_started_notification, show_battery_full_notification
from modules.sound_module import play_notification_sound

# util imports
from utils.load_config import load_config

# Configure logging
logging.basicConfig(
    filename="powerping_startup.log",   # Log file name
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# main function
def main() -> None:
    # Show startup notification
    show_app_started_notification()
    time.sleep(10)
    # load config
    config = load_config()
    logging.info(f"Configuration loaded: {config}")
    while(True):
        # get battery status
        is_battery_charging, battery_percentage = battery_status()
        # check if battery is charging and battery percentage is greater than or equal to threshold
        if is_battery_charging and battery_percentage >= config["threshold"]:
            # show notification
            show_battery_full_notification()
            # play notification sound
            play_notification_sound()
            # break the loop
            break
        # sleep
        sleep_time = config["threshold"] - battery_percentage
        if sleep_time <= 0:
            sleep_time = 1
        sleep_time = (sleep_time * 60) / 2
        time.sleep(sleep_time)

if __name__ == "__main__":
    logging.info("Application starting...")
    try:
        # run main function
        main()
        logging.info("Application finished successfully.")
    except Exception as e:
        logging.error("Unhandled exception occurred!")
        logging.error(str(e))
        logging.error(traceback.format_exc())