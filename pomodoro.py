from datetime import datetime
from os import system
from sys import platform
from time import sleep


# Default Settings
small_break = 5
large_break = 30
work_duration = 25
period = 4


def notify(title, message):
    # Print notification
    print('[%s] %s: %s' % (datetime.now(), title, message))
    
    if platform == 'linux':  # Ubuntu 16.04 LTS
        # Visual notification
        system('''notify-send --urgency=critical "%s" "%s"''' % (title, message))
        # Audio notification
        system('''canberra-gtk-play --file=/usr/share/sounds/ubuntu/stereo/service-login.ogg''')
    elif platform == 'darwin':  # MacOS
        # Visual notification
        system("""osascript -e 'display notification "%s" with title "%s'""" % (message, title))
    elif platform == 'cygwin':  # Windows/Cygwin
        pass
    else:  # Windows
        pass

def start_pomodoro(duration_work, duration_break_small, duration_break_large, period):
    cycles = 1
    while True:
        notify('Begin Task', 'Work on task for %s minutes' % duration_work)
        sleep(60*duration_work)

        if cycles < period:
            notify('Begin Break', 'Take a small break for %s minutes' % duration_break_small)
            sleep(60*duration_break_small)
            cycles += 1
        else:
            notify('Begin Break', 'Take a large break for %s minutes' % duration_break_large)
            sleep(60*duration_break_large)
            cycles = 1

    
if __name__ == "__main__":
    start_pomodoro(work_duration, small_break, large_break, period)
