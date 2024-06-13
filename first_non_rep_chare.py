def first_non_repeating_char(s):
    # Dictionary to store the frequency of each character
    char_count = {}

    # First pass: count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Second pass: find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found
    return None

# Example usage
input_str = "swiss"
result = first_non_repeating_char(input_str)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("There are no non-repeating characters.")
