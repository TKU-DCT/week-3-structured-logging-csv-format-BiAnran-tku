import psutil
from datetime import datetime
import csv
import os

# Creste CSV file
LOG_FILE = "log.csv"
HEADER = ["Timestamp", "CPU", "Memory", "Disk"]

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # TODO: Use psutil to get CPU, memory, and disk usage
    cpu = round(psutil.cpu_percent(interval=1), 1)
    memory = round(psutil.virtual_memory().percent, 1)
    disk = round(psutil.disk_usage("/").percent, 1)
    
    return [now, cpu, memory, disk]

def write_log(data):
    # TODO: Check if log.csv exists
    file_exists = os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        # If not, create it and write a header row
        if not file_exists:
            writer.writerow(HEADER)
        # Then append the current data row
        writer.writerow(data)

if __name__ == "__main__":
    row = get_system_info()
    write_log(row)
    print("Logged:", row)
