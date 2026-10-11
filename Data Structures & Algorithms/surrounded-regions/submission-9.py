class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        visited = set()
        def capture(i, j):
            if min(i, j) < 0 or i == ROWS or j == COLS or (i,j) in visited:
                return
            if board[i][j] != "O":
                return
            visited.add((i,j))
            board[i][j] = "C"
            capture(i + 1, j)
            capture(i - 1, j)
            capture(i, j + 1)
            capture(i, j - 1)

        for i in range(ROWS):
            if board[i][0] == "O":
                capture(i, 0)
            if board[i][COLS - 1] == "O":
                capture(i, COLS - 1)
            
        for j in range(COLS):
            if board[0][j] == "O":
                capture(0, j)
            if board[ROWS - 1][j] == "O":
                capture(ROWS - 1, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "C":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            

        