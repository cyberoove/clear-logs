#Disclaimer
The author is not responsible for any misuse of the code. Do not use this code for any illegal activities.

#Log File Deletion Script
This script searches for log files in the /var/log directory and its subdirectories, and deletes the log files that have been modified within the past 24 hours.

#Prerequisites
Python 3

#How to use
Download or clone the script.
Run the script with the --clear-logs flag: python delete_logs.py --clear-logs
What the script does
Finds all log files modified within the past 24 hours.
Deletes the log files.

#Notes
Use the --clear-logs flag after you're done to delete the log files.
The script does not prompt for confirmation before deleting the log files. Be careful when using it.
