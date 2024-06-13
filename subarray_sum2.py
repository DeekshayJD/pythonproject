def subarray_with_given_sum(arr, n, desired_sum):
    current_sum = 0
    start = 0

    # Iterate through the array
    for end in range(n):
        # Add the current element to the current_sum
        current_sum += arr[end]

        # While current_sum is greater than the desired_sum, remove elements from the start of the current window
        while current_sum > desired_sum and start <= end:
            current_sum -= arr[start]
            start += 1

        # Check if the current_sum equals the desired_sum
        if current_sum == desired_sum:
            return arr[start:end + 1]

    # If no subarray is found, return an empty list
    return []

# Example usage
arr = [1, 2, 3, 7, 5]
n = len(arr)
desired_sum = 12
result = subarray_with_given_sum(arr, n, desired_sum)

if result:
    print(f"Subarray with the given sum is: {result}")
else:
    print("No subarray with the given sum found.")
