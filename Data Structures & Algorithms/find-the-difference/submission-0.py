class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1, freq2 = Counter(s), Counter(t)

        for c,f in freq2.items():
            if freq2[c] != freq1[c]:
                return c
        
        