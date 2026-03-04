# python-imports
import psutil
import time

# function to read battery charging status and percentage
def battery_status() -> tuple[bool, int]:
    battery = psutil.sensors_battery()
    if battery is not None:
        # returns True if the battery is charging, False otherwise and the battery percentage
        return battery.power_plugged, battery.percent
    else:
        return False, -1