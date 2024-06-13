import threading

# Create a lock for synchronization
lock = threading.Lock()

# Shared variable to track the next number to be printed
next_number = 1

# Function to print even numbers
def print_even():
    global next_number
    while next_number <= 10:
        if next_number % 2 == 0:
            with lock:
                print(next_number, end=", ")
                next_number += 1

# Function to print odd numbers
def print_odd():
    global next_number
    while next_number <= 10:
        if next_number % 2 != 0:
            with lock:
                print(next_number, end=", ")
                next_number += 1

# Create two threads for printing even and odd numbers
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

# Start both threads
even_thread.start()
odd_thread.start()

# Wait for both threads to finish
even_thread.join()
odd_thread.join()

print()  # Print a newline after all numbers are printed
