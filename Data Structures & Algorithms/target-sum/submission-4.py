class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            key = (i, curr)
            if key in cache:
                return cache[key]
            
            cache[key] = dp(i + 1, curr + nums[i]) + dp(i + 1, curr - nums[i])
            return cache[key]
        
        return dp(0, 0)
        