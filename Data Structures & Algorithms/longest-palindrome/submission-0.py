class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        res = 0
        used = False

        for key,val in freq.items():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                if not used:
                    res += 1
                    used = True

        
        return res
