def split_string(s, k):
    # Initialize an empty list to store the modified chunks
    chunks = []

    # Iterate through the string in chunks of length k
    for i in range(0, len(s), k):
        chunk = s[i:i + k]  # Get the current chunk
        unique_chars = []  # List to store distinct characters in the chunk

        # Iterate through each character in the chunk
        for char in chunk:
            # Check if the character is already present in unique_chars
            if char not in unique_chars:
                unique_chars.append(char)  # Add the character if it's not already present

        # Join the unique characters to form the modified chunk
        modified_chunk = ''.join(unique_chars)
        chunks.append(modified_chunk)  # Add the modified chunk to the list

    return chunks


# Test the function with the provided example
s = 'AABCAAADA'
k = 3
result = split_string(s, k)
for chunk in result:
    print(chunk)
