import os

def generate_io_load(file_path, size_in_gb):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_gb * 1024 * 1024 * 1024))

# Generate a 10GB file to stress test the RAID array
generate_io_load('/mnt/raid/largefile.dat', 10)
