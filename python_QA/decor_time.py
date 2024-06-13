
import time
from functools import wraps

def calculate_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # Record the start time
        result = func(*args, **kwargs) # Call the original function
        end_time = time.time() # Record the end time
        execution_time = end_time - start_time # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.2f} seconds")
        return result
    return wrapper

# Example usage:
@calculate_execution_time
def square(x):
    return x ** 2

print(square(5)) # Example function call