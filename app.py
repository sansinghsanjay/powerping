# modules import
from modules.notification_module import show_notification
from modules.sound_module import play_notification_sound

# main function
def main() -> None:
    # show notification
    show_notification()
    # play notification sound
    play_notification_sound()

if __name__ == "__main__":
    # run main function
    main()