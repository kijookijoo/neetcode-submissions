class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0], [0]

        # [0,0,2,2,2,3]
        # [,3,1,0]
        for i in range(1, len(height)):
            maxLeft.append(max(maxLeft[-1], height[i - 1]))
        
        for i in range(len(height) - 2, -1, -1):
            maxRight.append(max(maxRight[-1], height[i + 1]))
        maxRight.reverse()
        
        res = 0
        for i in range(len(height)):
            res += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return res