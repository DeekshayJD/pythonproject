#wap to get alert if disk usage is more then 80%

import psutil
import psutil

def check_disk_usage(threshold):
    percent_used = psutil.disk_usage('/').percent
    print(f"Disk usage is {percent_used}%")
    #return percent_used > threshold, percent_used
    if percent_used>threshold:
        return True,percent_used
    else:
        return False,percent_used

def main():
    threshold = 80  # Change this to set your desired threshold
    is_over_threshold, percent_used = check_disk_usage(threshold)
    if is_over_threshold:
        print(f"Alert: Disk usage is {percent_used}% which is over {threshold}%")
    else:
        print("Disk usage is below the threshold.")

if __name__ == "__main__":
    main()


