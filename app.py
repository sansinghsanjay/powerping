# python imports
import time
from winotify import Notification
import winsound
import psutil



# constants
config = {
  "threshold": 97,
  "sound": "DeviceConnect"
}



# function to show application started notification
def show_app_started_notification():
    """
    Show a Windows notification near the bottom-right with a button.
    """
    toast = Notification(
        app_id="PowerPing",
        title="PowerPing Started",
        msg="PowerPing is now running in the background. You'll receive a notification when your battery is almost full.",
        duration="short",
    )
    toast.show()



# function to show notification
def show_battery_full_notification():
    """
    Show a Windows notification near the bottom-right with a button.
    """
    toast = Notification(
        app_id="PowerPing",
        title="Battery Alert",
        msg="Your laptop battery is almost full. Please unplug the charger.",
        duration="long",
    )
    # Add button - launches powerping://stop so the main app can stop the sound
    toast.add_actions(label="Dismiss", launch="stop_sound")
    toast.show()



def play_notification_sound():
    """Play the Windows system sound for battery full (Device Connect sound)."""
    winsound.PlaySound(config["sound"], winsound.SND_ALIAS)



# function to read battery charging status and percentage
def battery_status() -> tuple[bool, int]:
    battery = psutil.sensors_battery()
    if battery is not None:
        # returns True if the battery is charging, False otherwise and the battery percentage
        return battery.power_plugged, battery.percent
    else:
        return False, -1



if __name__ == "__main__":
    # Show startup notification
    show_app_started_notification()
    time.sleep(10)
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