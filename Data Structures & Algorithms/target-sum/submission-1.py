class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, remaining):
            if i == len(nums):
                return 1 if remaining == 0 else 0
            key = (i, remaining)
            if key in cache:
                return cache[key]
            
            cache[key] = dp(i + 1, remaining + nums[i]) + dp(i + 1, remaining - nums[i])
            return cache[key]
        
        return dp(0, target)
        