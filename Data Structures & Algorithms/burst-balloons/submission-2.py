class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dp(l, r):
            if l + 1 == r:
                return 0
            key = (l, r)
            if key in cache:
                return cache[key]
            
            cache[key] = 0
            for i in range(l + 1, r):
                cache[key] = max(
                    cache[key], 
                    nums[l] * nums[i] * nums[r] + dp(l, i) + dp(i, r)
                    )
            return cache[key]

        return dp(0, len(nums) - 1)
        