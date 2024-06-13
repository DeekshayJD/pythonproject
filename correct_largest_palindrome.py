def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def largest_palindrome(s):
    if len(s) == 0:
        return ""
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        # Even length palindromes
        even_palindrome = expand_around_center(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest

s = "deekshay"
print(largest_palindrome(s))
