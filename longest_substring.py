s = "pwwkew"
longest_substring = ""
longest_length = 0

for i in range(len(s)):
    current_substring = ""
    for j in range(i, len(s)):
        if s[j] not in current_substring:
            current_substring += s[j]
            # Update the longest substring and length if current length is greater
            if len(current_substring) > longest_length:
                longest_length = len(current_substring)
                longest_substring = current_substring
        else:
            # Break the inner loop if a repeating character is found
            break

print("Longest substring without repeating characters:", longest_substring)
print("Length of the longest substring:", longest_length)
