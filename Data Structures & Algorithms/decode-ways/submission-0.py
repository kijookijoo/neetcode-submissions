class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up dp, starting from the left going right
        cache = {}
        def dp(i):
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]
            
            cache[i] = 0
            if s[i] != "0":
                cache[i] += dp(i + 1)
            if 10 <= int(s[i:i+2]) <= 26:
                cache[i] += dp(i + 2)
            return cache[i]

        return dp(0)        