class Solution:
    def countSubstrings(self, s: str) -> int:

        def count(l, r):
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1   
            return count
            

        res = 0
        for i in range(len(s)):

            res += count(i, i + 1)

            res += count(i, i)
        return res

            