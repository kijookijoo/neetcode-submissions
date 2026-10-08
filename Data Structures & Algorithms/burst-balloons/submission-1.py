class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = {}

        def dp(l, r):
            if l + 1 == r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            res = 0

            for i in range(l + 1, r):
                res = max(
                    res,
                    nums[l] * nums[i] * nums[r]
                    + dp(l, i)
                    + dp(i, r)
                )

            cache[(l, r)] = res
            return res

        return dp(0, n - 1)