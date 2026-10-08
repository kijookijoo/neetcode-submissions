class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        n = len(matrix[0]) - 1

        while t < b:
            mid = (t + b) // 2
            if matrix[mid][n] == target:
                return True
            elif target > matrix[mid][n]:
                t = mid + 1
            else:
                b =mid 
                
        mid = (t + b) // 2
        row = mid

        l, r = 0, len(matrix[0]) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:        
                r = mid - 1
        
        return False