import os
import re
from collections import defaultdict

# Directory where files are stored
directory = "C:\\Users\\ddevraj"

# Pattern to identify error files
error_pattern = re.compile(r'.*error.*', re.IGNORECASE)

# Dictionary to store the count of error files for each user
user_error_counts = defaultdict(int)

# Dictionary to store all files for each user
user_files = defaultdict(list)

# Function to get the user from the filename
def get_user_from_filename(filename):
    # Assuming the user name is part of the filename, e.g., "user1_error_log.txt"
    return filename.split('_')[0]

# Traverse the directory and count error files for each user
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        user = get_user_from_filename(filename)
        user_files[user].append(filename)
        if error_pattern.match(filename):
            user_error_counts[user] += 1

# Determine the user with the most error files
most_errors_user = max(user_error_counts, key=user_error_counts.get, default=None)
most_errors_count = user_error_counts[most_errors_user] if most_errors_user else 0

# Output results
print("User Files and Number of Error Files:")
for user, files in user_files.items():
    error_count = user_error_counts[user]
    print(f"User: {user}, Total Files: {len(files)}, Error Files: {error_count}")

if most_errors_user:
    print(f"\nUser with the most error files: {most_errors_user} ({most_errors_count} error files)")
else:
    print("\nNo error files found.")

# Save results to a file
output_file = "error_file_report.txt"
with open(output_file, "w") as f:
    f.write("User Files and Number of Error Files:\n")
    for user, files in user_files.items():
        error_count = user_error_counts[user]
        f.write(f"User: {user}, Total Files: {len(files)}, Error Files: {error_count}\n")
    if most_errors_user:
        f.write(f"\nUser with the most error files: {most_errors_user} ({most_errors_count} error files)\n")
    else:
        f.write("\nNo error files found.\n")

print(f"\nReport saved to {output_file}")
