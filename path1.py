class Solution:
    def uniquePaths(self, m=2, n=3, i=0, j=0):
        if i >= m or j >= n:      return 0
        if i == m-1 and j == n-1: return 1
        return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)

sol=Solution()
output=sol.uniquePaths()
print(output)
