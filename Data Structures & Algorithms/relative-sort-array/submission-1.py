class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ordering = {}
        for i in range(len(arr2)):
            ordering[arr2[i]] = i
        
        freq = Counter(arr1)
        res = []

        for c,idx in ordering.items():
            res.extend([c] * freq[c])
        
        for key,val in sorted(freq.items()):
            if key not in ordering:
                res.extend([key] *  freq[key])
        


        return res