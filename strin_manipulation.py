
import re
str="this is log file corrupted at 10:30 am with process id [1239578]"
exp=r"\[(\d+)\]"

result=re.findall(exp,str)
print(result[0])

import re

'''
# Input string
input_str = "this is log file corrupted at 10:30 am with process id [1239578]"

# Regular expression pattern to match process id
pattern = r"\[(\d+)\]"

# Find all matches in the input string
matches = re.findall(pattern, input_str)

# Print the process id (assuming there's only one match)
if matches:
    print("Process ID:", matches[0])
'''
