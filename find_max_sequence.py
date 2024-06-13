s = "pwwkew"
#s="abcdefabcdefgh"
l = ""  # Initialize an empty string to store the current substring
l1 = []  # Initialize an empty list to store the lengths of valid substrings

# Loop through each character in the string
for i in range(len(s)):
    # Inner loop to check for substrings starting from the current character
    for j in range(i, len(s)):
        if s[j] not in l:  # Check if the current character is not in the current substring
            l += s[j]  # Add the current character to the substring
        else:
            l1 += [len(l)]  # Append the length of the current substring to the list
            l = ""  # Reset the substring to an empty string
            break  # Break the inner loop if a repeating character is found

print(max(l1))  # Print the maximum length of valid substrings
