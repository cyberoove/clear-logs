#
#THIS SCRIPT WILL DELETE THE SYSTEM LOGS OF THE PAST 24 HOURS
#TO USE APPLY THE FLAG AFTER THE SCRIPT --clear-logs
#
#
import argparse
import os
import datetime

def delete_logs():
    now = datetime.datetime.now()
    one_day_ago = now - datetime.timedelta(days=1)
    log_files = []

    # Find all log files modified within the past 24 hours
    for root, dirs, files in os.walk("/var/log"):
        for file in files:
            full_path = os.path.join(root, file)
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
            if mod_time > one_day_ago:
                log_files.append(full_path)

    # Delete the log files
    for log_file in log_files:
        os.remove(log_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clear-logs", action="store_true", help="Delete log files modified within the past 24 hours")
    args = parser.parse_args()

    if args.clear_logs:
        delete_logs()
        print("Logs are Deleted... Time to go Home")
        exit()
        
    else:
        print("Use the --clear-logs flag after you're done to delete the log files.")
