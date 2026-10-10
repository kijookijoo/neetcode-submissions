class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i, j, prev_height, visited):
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visited:
                return
            if heights[i][j] < prev_height:
                return
            
            visited.add((i,j))
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)

            return
        
        pacific, atlantic = set(), set()

        for j in range(COLS):
            dfs(0, j, heights[0][j], pacific)
            dfs(ROWS - 1, j, heights[ROWS - 1][j], atlantic)
        
        for i in range(ROWS):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, COLS - 1, heights[i][COLS - 1], atlantic)
        
        res = []
        for i,j in pacific:
            if (i,j) in atlantic:
                res.append([i,j])
        
        return res
 

        