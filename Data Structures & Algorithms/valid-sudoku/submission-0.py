class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        # (2, 3) -> 3
        # (8, 8) -> 8
        # (0, 3) -> 1
        # (3, 0 ) -> 3
        # (2, 2) -> 1

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                if cur in rows[i] or cur in cols[j] or cur in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    rows[i].add(cur)
                    cols[j].add(cur)
                    boxes[(i // 3) * 3 + (j // 3)].add(cur)
        

        return True
        