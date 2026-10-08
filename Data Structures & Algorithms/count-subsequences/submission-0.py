class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        # caat
        # cat
        def dp(i, j):
            if i == len(s):
                return 1 if j >= len(t) else 0
            if j >= len(t):
                return 1
            key = (i, j)
            if key in cache:
                return cache[key]

            if s[i] == t[j]:
                cache[key] = dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                cache[key] = dp(i + 1, j)

            return cache[key]
        
        return dp(0, 0)