class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)

        freq2 = Counter(t)
        if len(freq) != len(freq2):
            return False
        
        for c in freq2:
            if freq2[c] != freq[c]:
                return False
        return True
        