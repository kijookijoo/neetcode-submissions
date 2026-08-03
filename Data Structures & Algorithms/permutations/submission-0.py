class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = [False] * len(nums)

        def backtrack(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True
                backtrack(curr, used)
                curr.pop()
                used[i] = False
        
        backtrack([], used)

        return res

                    

        