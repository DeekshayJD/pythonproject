import subprocess




memory_info={
    "memory":{
        "total":192890,
        "used":348,
        "remaining":5680
    },
    "swap":{"total":192890,
        "used":348,
        "free":5680

    }
}
print(memory_info["memory"]["used"])



def get_memory_info():
    result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split('\n')
    headers = output[0].split()
    values = output[1].split()
    memory_info = {}

    for header, value in zip(headers, values):
        if header == 'available':
            header = 'available (estimate)'  # adjust header name
        memory_info[header] = value

    return memory_info

# Example usage:
memory_info = get_memory_info()
print(memory_info)
