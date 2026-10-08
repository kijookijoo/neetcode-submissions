class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        for w in words:
            wordFreq = Counter(w)
            for c,f in wordFreq.items():
                freq[c] += f
        
        for c,f in freq.items():
            if f % len(words) != 0:
                return False
        
        return True
        