import time
from datetime import datetime
import os
import winsound  # Windows sound notification
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# -----------------------------
# Configuration
# -----------------------------
reminders = {
    "Water": 60*60,       # 1 hour
    "Stretch": 2*60*60,   # 2 hours
    "Eye Break": 1.5*60*60 # 1.5 hours
}

LOG_FILE = "health_log.txt"
SOUND_DURATION = 1000  # milliseconds
SOUND_FREQ = 1000      # Hz

# Track last time reminder was given
last_reminder = {key: time.time() for key in reminders.keys()}

# -----------------------------
# Helper Functions
# -----------------------------
def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {event}\n")

def notify(event):
    # Console message
    colors = {
        "Water": Fore.CYAN,
        "Stretch": Fore.MAGENTA,
        "Eye Break": Fore.YELLOW
    }
    print(colors.get(event, Fore.WHITE) + f"\n🔔 Reminder: {event}! 🔔\n" + Style.RESET_ALL)

    # Play beep sound
    winsound.Beep(SOUND_FREQ, SOUND_DURATION)

    # Log
    log_event(event)

# -----------------------------
# Main Program
# -----------------------------
def main():
    print(Fore.GREEN + "💡 Creative Health Reminder Started!" + Style.RESET_ALL)
    print("Press Ctrl+C to stop the program.\n")

    try:
        while True:
            current_time = time.time()
            for event, interval in reminders.items():
                if current_time - last_reminder[event] >= interval:
                    notify(event)
                    last_reminder[event] = current_time
            time.sleep(30)  # Check every 30 seconds

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram stopped. Stay healthy and hydrated! 💦" + Style.RESET_ALL)

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    main()
