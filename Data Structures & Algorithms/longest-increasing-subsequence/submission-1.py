class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state def: index mapped to longest increasing subsequence from that point till the end
        cache = {}

        def dp(i):
            # if i == len(nums):
            #     return 0
            if i in cache:
                return cache[i]
            
            cache[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + dp(j))
            
            return cache[i]
        return max([dp(i) for i in range(len(nums))])


            
            