class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(curr):
            if curr < 0:
                return 0
            if curr in cache:
                return cache[curr]

            cache[curr] = max(dp(curr - 1), nums[curr] + dp(curr - 2))

            return cache[curr]
        
        return max(dp(len(nums) - 1), dp(len(nums) - 2))