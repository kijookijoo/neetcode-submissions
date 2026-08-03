class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue

                box_num = (i // 3) + (j // 3) * 3 
                
                if curr in rows[i] or curr in cols[j] or curr in boxes[box_num]:
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                boxes[box_num].add(curr)
        
        return True
        