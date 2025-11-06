import shutil
import os
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
# Source folder যা backup করতে হবে
SOURCE_FOLDER = "my_folder"

# Backup folder যেখানে save হবে
BACKUP_ROOT = "backup"

# Maximum number of backups রাখার জন্য (পুরানো গুলো delete হবে)
MAX_BACKUPS = 3

# -----------------------------
# FUNCTIONS
# -----------------------------

def create_backup(src, backup_root):
    """
    Source folder copy করে backup folder এ রাখে।
    Backup folder name timestamp অনুযায়ী বানানো হয়।
    """
    # Ensure backup root folder exists
    os.makedirs(backup_root, exist_ok=True)

    # Backup folder name তৈরি করা timestamp দিয়ে
    timestamp = int(time.time())
    backup_folder = os.path.join(backup_root, f"backup_{timestamp}")

    # Copy পুরো directory
    shutil.copytree(src, backup_folder)

    print(f"Backup created at: {backup_folder}")
    return backup_folder

def cleanup_old_backups(backup_root, max_backups):
    """
    যদি backup folder এ বেশি backup থাকে,
    oldest ones delete করে max_backups রাখে।
    """
    # List all backup folders sorted by creation time
    backups = sorted(
        [os.path.join(backup_root, d) for d in os.listdir(backup_root)],
        key=lambda x: os.path.getctime(x)
    )

    # Delete oldest if more than max_backups
    while len(backups) > max_backups:
        oldest = backups.pop(0)
        shutil.rmtree(oldest)
        print(f"Deleted old backup: {oldest}")

# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():
    # Check if source folder exists
    if not os.path.exists(SOURCE_FOLDER):
        print(f"Error: Source folder '{SOURCE_FOLDER}' does not exist!")
        return

    # Create backup
    create_backup(SOURCE_FOLDER, BACKUP_ROOT)

    # Cleanup old backups
    cleanup_old_backups(BACKUP_ROOT, MAX_BACKUPS)

if __name__ == "__main__":
    main()

