class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        islands = 0

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(x, y):
            q = deque()
            q.append((x,y))
            while q:
                r, c = q.popleft()
                for dx, dy in directions:
                    nx, ny = r + dx, c + dy
                    if ((nx,ny) in visited or 
                        min(nx,ny) < 0 or 
                        nx >= ROWS or 
                        ny >= COLS or 
                        grid[nx][ny] == "0"):
                        continue
                    q.append((nx,ny))
                    visited.add((nx,ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        
        return islands
        