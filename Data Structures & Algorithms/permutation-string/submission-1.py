class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = Counter(s1)

        for i,c in enumerate(s2):
            if i < len(s1):
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
                if not freq:
                    return True
                continue
            
            freq[s2[i - len(s1)]] += 1
            if freq[s2[i - len(s1)]] == 0:
                del freq[s2[i - len(s1)]]

            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

            if not freq:
                return True
            
        return False

        
        