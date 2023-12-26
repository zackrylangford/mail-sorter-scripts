import os
import logging
from datetime import datetime

# Setup basic logging
logging.basicConfig(filename='/home/ec2-user/mail-sorter-scripts/logs/mail_sorter_debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Directory to store the logs
log_directory = "/home/ec2-user/mail-sorter-scripts/logs"

try:
    # Ensure the log directory exists
    os.makedirs(log_directory, exist_ok=True)
    logging.info("Log directory verified/created.")
except Exception as e:
    logging.error("Error creating log directory: %s", e)

# File to store the log
log_file_path = os.path.join(log_directory, "mail_sorter_log.txt")

def main():
    try:
        # Read the last number from the file
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1] if lines else "Hello, Zack 0"
                last_number = int(last_line.split()[-1])
        else:
            last_number = 0

        # Increment the number
        new_number = last_number + 1

        # Append "Hello, Zack" with the new number to the file
        with open(log_file_path, 'a') as file:
            file.write(f"Hello, Zack {new_number}\n")
        logging.info("Logged to file successfully.")
    except Exception as e:
        logging.error("Error during main execution: %s", e)

if __name__ == "__main__":
    logging.info("Script started.")
    main()
    logging.info("Script finished.")
