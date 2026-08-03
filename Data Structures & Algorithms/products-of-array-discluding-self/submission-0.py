class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev = 1
        for i in range(len(nums)):
            prev *= nums[i]
            prefix.append(prev)
        
        postfix = []
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            prev *= nums[i]
            postfix.append(prev)
        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]
        
        return nums
        