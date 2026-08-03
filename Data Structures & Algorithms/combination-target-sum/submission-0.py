class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr, total, i):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(curr.copy())
                return 


            curr.append(nums[i])
            backtrack(curr, total + nums[i], i)
            curr.pop()
            backtrack(curr, total, i + 1)
        
        backtrack([], 0, 0)
        return res