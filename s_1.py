def find_peak_elements(nums):
    n = len(nums)
    peaks = []

    for i in range(n):
        # Check if the current element is a peak
        if (i == 0 or nums[i] >= nums[i - 1]) and (i == n - 1 or nums[i] >= nums[i + 1]):
            peaks.append(nums[i])

    return peaks

# Example usage
nums = [10, 20, 15, 2, 23, 90, 67]
result = find_peak_elements(nums)
print("Peak elements:", result)
