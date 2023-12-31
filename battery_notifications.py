import psutil
import subprocess
import time

frequency = int(input('How often would you like to be notified?: '))

battery = psutil.sensors_battery()
percent = battery.percent

while True:
    battery = psutil.sensors_battery()
    current_percent = battery.percent
    change = current_percent - percent
    diff = abs(change)

    if diff >= frequency:
        # Display notification using osascript
        subprocess.run([
            'osascript',
            '-e',
            f'display notification "{current_percent}% Battery Remaining" with title "Current Battery Percentage"'
        ])

        percent = current_percent

    # Sleep for a minute before checking again
    time.sleep(60)
