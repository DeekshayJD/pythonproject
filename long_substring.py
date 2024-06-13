while True:
    s = input("enter string to find longest substring without repetation:-")
    longest_substring = ""
    longest_len_substring = 0
    for i in range(len(s)):
        current_substring = ""
        for j in range(i, len(s)):
            if s[j] not in current_substring:
                current_substring += s[j]

            if len(current_substring) > longest_len_substring:
                longest_len_substring = len(current_substring)
                longest_substring = current_substring
            else:
                break
    print(f"longest substring {longest_substring}")
    print(f"length of longest substring {longest_len_substring}")




