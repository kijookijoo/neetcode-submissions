class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_curr = nums[0]
        min_curr = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_curr, min_curr = min_curr, max_curr
                
            max_curr = max(num, max_curr * num)
            min_curr = min(num, min_curr * num)

            res = max(res, max_curr)
        
        return res