class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prevEven = True if nums[0] % 2 == 0 else False
    
        for i in range(1, len(nums)):
            if prevEven:
                if nums[i] % 2 == 0:
                    return False
                prevEven = False
            else:
                if nums[i] % 2 == 1:
                    return False
                prevEven = True
        
        return True
        