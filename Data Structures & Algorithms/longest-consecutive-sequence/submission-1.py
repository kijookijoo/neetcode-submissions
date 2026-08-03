class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        currStreak = 1
        maxStreak = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                currStreak += 1
                maxStreak = max(maxStreak, currStreak)
            elif nums[i] == prev:
                continue
            else:
                currStreak = 1
            prev = nums[i]
        
        return maxStreak
