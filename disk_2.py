import subprocess

def get_memory_info():
    result = subprocess.run(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize', '/Value'], capture_output=True, text=True)
    output = result.stdout
    lines = output.split('\n')

    memory_info = {}

    for line in lines:
        if '=' in line:
            key, value = line.strip().split('=')
            memory_info[key.strip()] = value.strip()

    return memory_info

# Example usage:
memory_info = get_memory_info()
print(memory_info)
