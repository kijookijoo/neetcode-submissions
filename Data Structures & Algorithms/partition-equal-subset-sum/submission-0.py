class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
    
        cache = {}

        def dp(i, remaining):
            # state def: from index i, is it possible to find a partition that adds up to remaining
            if remaining == 0:
                return True
            if i == len(nums):
                return False
            key = (i, remaining)
            if key in cache:
                return cache[key]
            
            cache[key] = dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)
            
            return cache[key]
        
        return dp(0, half)



