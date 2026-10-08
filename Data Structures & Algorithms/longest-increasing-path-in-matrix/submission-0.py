class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dp(i, j):
            if min(i, j) < 0 or i == ROWS or j == COLS:
                return 0
            key = (i, j)
            if key in cache:
                return cache[key]
            curr = matrix[i][j]
            # if ((i == ROWS - 1 or matrix[i + 1][j] >= curr) and
            #     (i == 0 or matrix[i - 1][j] >= curr) and
            #     (j == COLS - 1 or matrix[i][j + 1] >= curr) and
            #     (j == 0 or matrix[i][j - 1] >= curr)):
            #     return 1
            
            down = 1 + dp(i + 1, j) if i != ROWS - 1 and matrix[i + 1][j] > curr else 1
            up = 1 + dp(i - 1, j) if i != 0 and matrix[i - 1][j] > curr else 1
            right = 1 + dp(i, j + 1) if j != COLS - 1 and matrix[i][j + 1] > curr else 1
            left = 1 + dp(i, j - 1) if j != 0 and matrix[i][j - 1] > curr else 1

            cache[key] = max(down, up, right, left)
            return cache[key]
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dp(i, j))
            
        return res



        