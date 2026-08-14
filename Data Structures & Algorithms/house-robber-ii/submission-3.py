class Solution:
    def rob(self, nums: List[int]) -> int:
        # base cases for bottom up dp approach
        # started from 0th house -> can't rob the (n - 1)th house
        # started from 1st house -> no limitations
        if len(nums) == 1:
            return nums[0]
        def dp(curr, nums, cache):
            if curr > len(nums) - 1:
                return 0
            if curr in cache:
                return cache[curr]
            
            cache[curr] = max(dp(curr + 1, nums, cache), dp(curr + 2, nums, cache) + nums[curr])
            return cache[curr]
        
        return max(dp(0, nums[:-1], {}), dp(0, nums[1:], {}))
            
        