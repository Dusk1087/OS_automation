import os
import shutil
from datetime import datetime

# Location for the log file
log_file = r"C:\Users\reedf\OneDrive - stagrockllc.com\09. Software\Python\New_folder\log.txt"
# function that "a" appends the log with the current date, time and message
def log(message):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")
# runs teh function log with the message "Script started"
log("Script started")


# Define source and destination folders
source_folder = r"C:\Users\reedf\OneDrive - stagrockllc.com\09. Software\Python\Old_folder"
destination_folder = r"C:\Users\reedf\OneDrive - stagrockllc.com\09. Software\Python\New_folder"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in the source folder and move them
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)

    if os.path.isfile(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
