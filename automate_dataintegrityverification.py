import hashlib

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Calculate checksum of a file before and after transfer
original_checksum = calculate_checksum('/path/to/original/file')
transferred_checksum = calculate_checksum('/mnt/raid/file')
assert original_checksum == transferred_checksum
