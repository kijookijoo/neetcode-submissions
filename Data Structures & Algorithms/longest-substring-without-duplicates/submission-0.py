class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        res = 0
        # ababcd
        for i,c in enumerate(s):
            if c in window:
                # get to the repeating character
                while s[start] != c:
                    window.remove(s[start])
                    start += 1
                # then remove the repeating character
                start += 1
                window.add(c)
            else:
                window.add(c)
            
            res = max(res, i - start + 1)
        
        return res
        