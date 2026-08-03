class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        q = deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = set()

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if min(nx,ny) < 0 or nx == ROWS or ny == COLS or (nx,ny) in visited or board[nx][ny] == "X":
                        continue
                    queue.append((nx,ny))
                    visited.add((nx,ny))

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS -1) and board[i][j] == "O":
                    bfs(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited:
                    board[i][j] = "X"
        
        


        