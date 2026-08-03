class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, curr = [], []

        def helper(i, curset):
            if i > len(nums) - 1:
                subset.append(curset.copy())
                return
            
            curset.append(nums[i])
            helper(i + 1, curset)
            curset.pop()
            helper(i + 1, curset)
        
        helper(0, curr)
        return subset
        