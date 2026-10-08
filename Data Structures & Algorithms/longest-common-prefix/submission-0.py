class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for i in range(min(len(w) for w in strs)):
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return strs[0][:i]
            i += 1
        
        return strs[0][:i]
        
        
            

        