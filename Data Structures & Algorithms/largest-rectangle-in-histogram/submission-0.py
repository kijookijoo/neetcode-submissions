class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i,h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx

            stack.append((start, h))
        
        while stack:
            idx, height = stack.pop()
            res = max(res, (len(heights) - idx) * height)
        
        return res
        