
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in check:
                        check.add(board[i][j])
                    else:
                        return False
        
        #cols
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in check:
                        check.add(board[j][i])
                    else:
                        return False
                    
        #sub-boxes
        for r in range(0,9,3):
            for c in range(0,9,3):
                check = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] != '.':
                            if board[i][j] not in check:
                                check.add(board[i][j])
                            else:
                                return False
        return True
    
# Time Complexity: O(1) since the board size is fixed at 9x9.
# Space Complexity: O(1) since the sets used for checking duplicates will contain at most 9 elements.
                    

#test cases
solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) # Output: True (valid Sudoku)
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"],[".",".",".",".","8",".",".","7","9"]])) # Output: False (invalid Sudoku)