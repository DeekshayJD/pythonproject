import threading


# Function to print even numbers
def print_even():
    for i in range(2, 11, 2):
        print(i, end=", ")


# Function to print odd numbers
def print_odd():
    for i in range(1, 10, 2):
        print(i, end=", ")


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
