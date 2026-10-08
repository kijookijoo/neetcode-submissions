class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordDict = set(wordDict)

        def dp(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    if dp(j):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        return dp(0)
        