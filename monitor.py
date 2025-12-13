import psutil
from datetime import datetime

# Threshold values
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_FILE = "system_health.log"

def log_message(message):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    log_message(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        log_message("ALERT! High CPU usage")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    log_message(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        log_message("ALERT! High Memory usage")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    log_message(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        log_message("ALERT! High Disk usage")

def main():
    log_message("===== System Health Check Started =====")
    check_cpu()
    check_memory()
    check_disk()
    log_message("===== System Health Check Completed =====\n")

if __name__ == "__main__":
    main()

