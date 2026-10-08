class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i == m or j == n:
                return 0
            key = (i,j)
            if key in cache:
                return cache[key]
            
            cache[key] = dp(i + 1, j) + dp(i, j + 1)
            return cache[key]
        
        return dp(0, 0)

        