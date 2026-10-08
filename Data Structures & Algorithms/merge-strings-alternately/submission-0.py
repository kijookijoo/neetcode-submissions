class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0,0
        p1Turn = True
        res = []
        while p1 < len(word1) and p2 < len(word2):
            if p1Turn:
                res.append(word1[p1])
                p1 += 1
            else:
                res.append(word2[p2])
                p2 += 1
            
            p1Turn = not p1Turn
        
        if p1 < len(word1):
            res.append(word1[p1:])
        if p2 < len(word2):
            res.append(word2[p2:])
    
        return "".join(res)

            
        