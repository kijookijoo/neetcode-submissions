class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(i, j):
            if i == len(word1):
                return len(word2) - j 
            if j == len(word2):
                return len(word1) - i 
            key = (i,j)
            if key in cache:
                return cache[key]
            
            if word1[i] == word2[j]:
                cache[key] = dp(i + 1, j + 1)
            else:
                insert = dp(i, j + 1)
                replace = dp(i + 1, j + 1)
                delete = dp(i + 1, j)
                cache[key] = 1 + min(insert, replace, delete)
            return cache[key]
        
        return dp(0, 0)