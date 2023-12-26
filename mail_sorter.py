import os

# Directory to store the logs
log_directory = "/home/ec2-user/mail-sorter-scripts/logs"

# Ensure the log directory exists
os.makedirs(log_directory, exist_ok=True)

# File to store the log
log_file_path = os.path.join(log_directory, "mail_sorter_log.txt")

def main():
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

if __name__ == "__main__":
    main()
