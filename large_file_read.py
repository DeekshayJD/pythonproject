def read_in_chunks(file_path, chunk_size=1024):
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(chunk_size):
                # Process each chunk
                print(chunk)
    except MemoryError:
        print("MemoryError: The file is too large to fit into memory.")

read_in_chunks('large_file.txt', chunk_size=1024*1024)  # 1MB chunks

try:
    with open('large_file.txt', 'r') as file:
        for line in file:
            # Process each line
            print(line)
except MemoryError:
    print("MemoryError: The file is too large to fit into memory.")
