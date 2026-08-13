class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            if curr in cache:
                return cache[curr]
            
            cache[curr] = dp(curr + 1) + dp(curr + 2)
            
            return cache[curr]
        
        return dp(0)
        