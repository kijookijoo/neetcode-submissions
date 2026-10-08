class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)

        i = 0

        while True:
            if i not in nums:
                return i
            i += 1
        
        
        