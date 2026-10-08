class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache ={}

        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            key = (i,j)
            if key in cache:
                return cache[key]

            if text1[i] == text2[j]:
                cache[key] = 1 + dp(i + 1, j + 1)                
            else:
                cache[key] = max(
                    dp(i + 1, j),
                    dp(i, j + 1)
                )
            return cache[key]
        
        return dp(0, 0)
