def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

    # Initialize two pointers
    left = 0
    right = len(cleaned_string) - 1

    # Compare characters from the start and the end
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True


# Test the function
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
