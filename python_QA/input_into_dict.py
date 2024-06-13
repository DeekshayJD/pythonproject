memory_info = {}

input_string = """       total        used        free      shared  buff/cache   available
Mem:        1632788      101996      124792      250352     1404000      904032
Swap:       2097148           0     2097148"""

lines = input_string.split('\n')
headers = lines[0].split()
for line in lines[1:]:
    parts = line.split()
    category = parts[0].rstrip(':')
    memory_info[category] = {header: value for header, value in zip(headers[1:], parts[1:])}

print(memory_info)
