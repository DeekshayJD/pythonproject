class LargestPal:
    def largest_palindrome(self, s):
        self.res = ""

        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i + 1)
            self.res = max(odd, even, self.res, key=len)

        return self.res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


large = LargestPal()
s = "babad"
res = large.largest_palindrome(s)
print(res)
