class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            # if i > 1 and curr[i] == curr[i - 1]:
            #     return
            
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res
            
                

        