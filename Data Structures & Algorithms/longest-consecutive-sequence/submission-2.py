class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxStreak, curStreak = 0, 0
        seen = set(nums)

        for curr in seen:

            if curr - 1 not in seen:
                curStreak = 1
                while curr + 1 in seen:
                    curStreak += 1
                    curr += 1
            else:
                curStreak = 1
            maxStreak = max(maxStreak, curStreak)
        
        return maxStreak
        