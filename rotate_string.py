def rotate_left(s, n):
    # Ensure n is within the bounds of the string length
    n = n % len(s)

    # Rotate the string by slicing
    rotated = s[n:] + s[:n]
    return rotated


# Example usage
s = "hello"
n = 5

result = rotate_left(s, n)
print(result)  # Output: "llohe"
