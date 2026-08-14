class Solution:
    def rob(self, nums: List[int]) -> int:
        # base cases for bottom up dp approach
        # started from 0th house -> can't rob the (n - 1)th house
        # started from 1st house -> no limitations
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def dp(curr, can_rob_last):
            if curr > len(nums) - 1:
                return 0
            if curr == len(nums) - 1 and not can_rob_last:
                return 0
            if (curr, can_rob_last) in cache:
                return cache[(curr, can_rob_last)]
            
            cache[(curr, can_rob_last)] = max(
                dp(curr + 1, can_rob_last),
                dp(curr + 2, can_rob_last) + nums[curr] 
            )
            return cache[(curr, can_rob_last)]
        
        return max(dp(0, False), dp(1, True))

            
            
        