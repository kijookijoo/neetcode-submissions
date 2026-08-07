class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # check rotation
            if nums[l] < nums[r]:
                # no rotation
                return nums[l]
            else:
                # rotation
                # TODO: rotation case
                if nums[mid] < nums[r]:
                    r = mid 
                elif nums[mid] > nums[r]:
                    l = mid + 1
        
        return nums[l]
                

        