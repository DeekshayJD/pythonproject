def subarray_with_given_sum(arr, desired_sum):
    # Dictionary to store the cumulative sum up to each index
    sum_map = {}
    current_sum = 0

    # Iterate through the array
    for i, num in enumerate(arr):
        # Add the current element to the current_sum
        current_sum += num

        # Check if current_sum is equal to desired_sum
        if current_sum == desired_sum:
            return arr[:i + 1]

        # Check if (current_sum - desired_sum) is in the sum_map
        if (current_sum - desired_sum) in sum_map:
            start_index = sum_map[current_sum - desired_sum] + 1
            return arr[start_index:i + 1]

        # Store the current_sum with its index
        sum_map[current_sum] = i

    # If no subarray is found, return an empty list
    return []

# Example usage
arr = [10, 2, -2, -20, 10]
desired_sum = -10
result = subarray_with_given_sum(arr, desired_sum)

if result:
    print(f"Subarray with the given sum is: {result}")
else:
    print("No subarray with the given sum found.")
