class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = 0
        
        def bfs(i, j):
            q = deque()
            q.append((i,j))
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            visited.add((i,j))
            area = 1
            while q:
                x, y = q.popleft()                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if min(nx, ny) < 0 or (nx, ny) in visited or nx == ROWS or ny == COLS or grid[nx][ny] == 0:
                        continue

                    q.append((nx, ny))
                    visited.add((nx, ny))
                    area += 1
            
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea
        