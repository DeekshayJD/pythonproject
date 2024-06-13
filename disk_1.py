import subprocess
import re

def get_memory_info():
    result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')

    headers = re.split(r'\s+', lines[0])
    values = re.split(r'\s+', lines[1])

    memory_info = {}

    for header, value in zip(headers[1:], values[1:]):
        if header == 'available':
            header = 'available (estimate)'  # adjust header name
        memory_info[header] = value

    return memory_info

# Example usage:
memory_info = get_memory_info()
print(memory_info)
