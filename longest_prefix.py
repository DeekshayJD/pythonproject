def longest_common_prefix(strings):
    if not strings:
        return ""

    # Sort the list of strings
    strings.sort()

    # Compare the first and the last string in the sorted list
    first = strings[0]
    last = strings[-1]
    common_prefix_length = min(len(first), len(last))

    # Find the common prefix between the first and the last string
    for i in range(common_prefix_length):
        if first[i] != last[i]:
            return first[:i]

    return first[:common_prefix_length]

# Example usage
strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(f"The longest common prefix is: '{result}'")
