from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[r][c] == target:
                    return True
        return False


solution = Solution()
print(solution.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
