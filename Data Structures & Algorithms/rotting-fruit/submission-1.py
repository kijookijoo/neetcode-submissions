class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()
        count = 0
        minutes = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    minutes = -1
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    count += 1
        
        if not q and count > 0:
            return -1
        
        

        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x + dx, y + dy
                    if min(nx,ny) < 0 or nx == ROWS or ny == COLS or (nx,ny) in visited or grid[nx][ny] != 1:
                        continue
                    
                    grid[nx][ny] = 2
                    q.append((nx,ny))
                    visited.add((nx,ny))
                    count -= 1
            minutes += 1

        return minutes if count == 0 else -1
    

                