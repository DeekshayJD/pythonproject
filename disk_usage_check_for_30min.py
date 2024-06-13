import schedule
import time
import psutil

def check_disk_usage(threshold):
    disk_usage = psutil.disk_usage('/')
    percent_used = disk_usage.percent
    if percent_used > threshold:
        return True, percent_used
    else:
        return False, percent_used

def job():
    threshold = 80  # Change this to set your desired threshold
    is_over_threshold, percent_used = check_disk_usage(threshold)
    if is_over_threshold:
        print(f"Alert: Disk usage is {percent_used}% which is over {threshold}%")

def main():
    # Schedule the job to run every 30 minutes
    schedule.every(30).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
