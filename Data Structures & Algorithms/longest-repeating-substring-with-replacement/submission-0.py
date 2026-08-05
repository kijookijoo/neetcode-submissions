class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        res = 0 
        maxFreq = 0
        start = 0

        for i,c in enumerate(s):
            seen[c] += 1
            maxFreq = max(maxFreq, seen[c])
            
            while (i - start + 1) - maxFreq > k:
                seen[s[start]] -= 1
                start += 1

            res = max(res, i - start + 1)
        return res
            
        