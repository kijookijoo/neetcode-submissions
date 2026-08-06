class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board), len(board[0])
        global_visited = set()

        def bfs(i, j):
            is_edge = False
            if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                is_edge = True   

            q = deque([(i,j)])
            visited = set([(i,j)])
            points = [(i,j)]
            global_visited.add((i,j))
            

            while q:
                x,y = q.popleft()
            
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x + dx, y + dy
                    if min(nx,ny) < 0 or nx == ROWS or ny == COLS or (nx,ny) in visited:
                        continue
                    if board[nx][ny] == "X":
                        continue

                    global_visited.add((nx,ny))
                    
                    if nx in {0, ROWS - 1} or ny in {0, COLS - 1}:
                        is_edge = True
                    
                    points.append((nx,ny))
                    visited.add((nx,ny))
                    q.append((nx,ny))
            
            return [] if is_edge else points

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in global_visited:
                    continue
                if board[i][j] == "O":
                    toSurround = bfs(i, j)
                    for x,y in toSurround:
                        board[x][y] = "X"


                    
        