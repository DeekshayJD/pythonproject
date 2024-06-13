def largest_palindrome(s):
    rev=""
    if s=="":
        return ""
    if len(s)==1:
        return s
    rev==s[::-1]
    res=""
    for i in range(len(s)):
        if s[i]==rev[i]:
            res+=s[i]
    return res

s="babad"
print(largest_palindrome(s))
