class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for i in range(len(nums)):
            if seen[nums[i]] == 1:
                return True
            else:
                seen[nums[i]] += 1
            
        
        return False
                
        