from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D Matrix - #74

        Binary search each row individually.
        Since each row is sorted, binary search finds the target in O(log n) per row, O(m log n) overall.

        Time complexity: O(m log n)
        Space complexity: O(1)
        """
        for row in matrix:
            l, r = 0, len(row) - 1

            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False


# test cases
solution = Solution()
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
)  # True
print(
    solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
)  # False
print(solution.searchMatrix([[1]], 1))  # True
print(solution.searchMatrix([[1, 3]], 3))  # True
