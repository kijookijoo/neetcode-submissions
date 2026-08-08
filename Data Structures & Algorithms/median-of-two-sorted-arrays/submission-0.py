class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        total_length = len(nums1) + len(nums2)
        partition_length = (total_length + 1) // 2
        isEven = total_length % 2 == 0
        l, r = 0, len(nums1) 

        while l <= r:
            p1 = (l + r) // 2
            p2 = partition_length - p1
            maxLeftX = nums1[p1 - 1] if p1 != 0 else -math.inf
            minRightX = nums1[p1] if p1 < len(nums1) else math.inf

            maxLeftY = nums2[p2 - 1] if p2 != 0 else -math.inf
            minRightY = nums2[p2] if p2 < len(nums2) else math.inf 

            if maxLeftX <= minRightY and maxLeftY < minRightX:
                if isEven:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # move left
                r = p1 - 1
            else:
                # move right
                l = p1 + 1
            