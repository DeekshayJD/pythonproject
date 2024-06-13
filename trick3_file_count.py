import os

# Define a function to parse log file and extract test results
def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        content = file.read()
        pass_count = content.count('PASS')
        fail_count = content.count('FAIL')
        return pass_count, fail_count

# Initialize variables to store total pass and fail counts
total_pass = 0
total_fail = 0


# Iterate over log files and parse each one
for i in range(1, 101):  # Assuming log files are named file1.log, file2.log, ..., file100.log
    filename = f"file{i}.log"
    if os.path.isfile(filename):
        pass_count, fail_count = parse_log_file(filename)
        total_pass += pass_count
        total_fail += fail_count

# Write summary to a summary.txt file
with open("summary.txt", "w") as summary_file:
    summary_file.write(f"Total Pass: {total_pass}\n")
    summary_file.write(f"Total Fail: {total_fail}\n")
