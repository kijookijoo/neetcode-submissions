class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            seen = {}
            for j in range(min(i + 1, len(nums)), len(nums)):
                if nums[j] in seen:
                    toAdd = [nums[i], nums[seen[nums[j]]], nums[j]]
                    toAdd.sort()
                    if toAdd not in res:
                        res.append(toAdd)
                else:
                    seen[target - nums[j]] = j
        
        return res
        

