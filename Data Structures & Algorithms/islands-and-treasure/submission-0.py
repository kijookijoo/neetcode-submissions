class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = x + dx, y + dy
                    if min(nx,ny) < 0 or nx == ROWS or ny == COLS or (nx,ny) in visited:
                        continue
                    if grid[nx][ny] == -1:
                        continue
                    
                    grid[nx][ny] = min(grid[nx][ny], grid[x][y] + 1)
                    q.append((nx,ny))
                    visited.add((nx,ny))
        
                

