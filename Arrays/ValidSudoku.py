from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Valid Sudoku - #36

        Rows, columns, and 3x3 boxes checks, if a digit appears twice in any row, column or box, return False.

        Time complexity: O(1) — board is always 9x9
        Space complexity: O(1) — sets never exceed 9 elements
        """

        # rows
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in check:
                        check.add(board[i][j])
                    else:
                        return False

        # cols
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in check:
                        check.add(board[j][i])
                    else:
                        return False

        # sub-boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                check = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            if board[i][j] not in check:
                                check.add(board[i][j])
                            else:
                                return False
        return True


# test cases
solution = Solution()
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(solution.isValidSudoku(board1))  # True

board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(solution.isValidSudoku(board2))  # False — 8 appears twice in first column

