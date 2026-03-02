# python-packages
from winotify import Notification

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
    #toast.add_actions(label="Dismiss", launch="stop_sound")
    toast.show()

