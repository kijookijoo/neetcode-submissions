class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            l,r = i + 1, len(nums) - 1
            target = -num
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            
        return res
