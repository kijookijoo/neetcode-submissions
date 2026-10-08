class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for key,val in Counter(arr).items():
            if val == 1:
                k -= 1
                if k == 0:
                    return key
        
        return ""