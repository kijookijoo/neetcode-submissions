class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        cache = {}

        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
                
            key = (i,j)
            if key in cache:
                return cache[key]
            
            if i <= len(s1) - 1:
                if s1[i] == s3[i + j]:
                    if dp(i + 1, j):
                        cache[key] = True
                        return cache[key]

            if j <= len(s2) - 1:
                if s2[j] == s3[i + j]:
                    if dp(i, j + 1):
                        cache[key] = True
                        return cache[key]

            cache[key] = False
            return cache[key]
        
        return dp(0, 0)

        