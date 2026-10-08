class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = Counter(arr)
        
        for s in arr:
            if seen[s] == 1:
                k -= 1
                if k == 0:
                    return s
        
        return ""
        