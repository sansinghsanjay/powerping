import time

from winotify import Notification, audio


def show_notification():
    """
    Show a Windows notification near the bottom-right with a button.
    """
    toast = Notification(
        app_id="Python App",
        title="Hello!",
        msg="This is a Windows 11 notification.",
        duration="short",
    )

    # Add button
    toast.add_actions(label="Okay", launch="close")

    toast.set_audio(audio.Default, loop=False)

    toast.show()


if __name__ == "__main__":
    # Simple manual test: wait 3 seconds, then show the notification.
    time.sleep(3)
    show_notification()
