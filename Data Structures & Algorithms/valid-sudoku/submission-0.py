class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        squares = {}
        square = 1

        board_t = [list(row) for row in zip(*board)]

        for i in range(0, 9):
            row, col = True, True

            row_val = [x for x in board[i] if x != "."]
            col_val = [x for x in board_t[i] if x != "."]

            row = (len(row_val) == len(set(row_val)))
            col = (len(col_val) == len(set(col_val)))
            if row == False:
                return False
            if col == False:
                return False
            
            for j in range(0, 9):
                box_key = (i // 3, j // 3)
                squares.setdefault(box_key, []).append(board[i][j])
        
        for nums in squares.values():
            vals = [x for x in nums if x != '.']
            if len(vals) != len(set(vals)):
                return False

        return True





                

        