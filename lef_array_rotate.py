def array_left_rotate(arr,n):
    n=n%len(arr)
    rotated=arr[n:]+arr[:n]
    return rotated

arr=[1,2,3,4,5]
n=2
print(array_left_rotate(arr,n))


def rotate_left(arr, n):
    # If the array is empty or n is 0, return the array as is
    if len(arr) == 0 or n == 0:
        return arr

    # Ensure n is within the bounds of the array length
    n = n % len(arr)

    # Rotate the array by slicing
    rotated = arr[n:] + arr[:n]
    return rotated


# Example usage
arr = [1, 2, 3, 4, 5]
n = 2
print("Original array:", arr)

rotated_arr = rotate_left(arr, n)
print(f"Array after rotating to the left by {n} positions:", rotated_arr)
