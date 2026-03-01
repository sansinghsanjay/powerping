import time

from modules.notification_module import show_notification
from modules.sound_module import play_notification_sound


def main() -> None:
    # Wait 3 seconds after script start, then show notification + sound.
    time.sleep(3)
    show_notification()
    play_notification_sound()


if __name__ == "__main__":
    main()

