# python-packages
from winotify import Notification

# function to show notification
def show_notification():
    """
    Show a Windows notification near the bottom-right with a button.
    """
    toast = Notification(
        app_id="PowerPing",
        title="Battery Alert",
        msg="Your laptop battery is almost full. Please unplug the charger.",
        duration="short",
    )
    # Add button - launches powerping://stop so the main app can stop the sound
    toast.add_actions(label="Okay", launch="powerping://stop")
    toast.set_audio()
    toast.show()
