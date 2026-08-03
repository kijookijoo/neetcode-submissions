class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)

        for i in range(len(strs)):
            sortedWord = sorted(strs[i])
            seen[''.join(sortedWord)].append(strs[i]) 
        
        return list(seen.values())


            
                
                


        