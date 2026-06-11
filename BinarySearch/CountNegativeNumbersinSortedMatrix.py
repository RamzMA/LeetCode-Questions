from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Count Negative Numbers in Sorted Matrix - #1351

        Binary search each row to find the first negative number.
        Since each row is sorted in non-increasing order, everything from that index to the end is negative.
        Add len(row) - l to the count for each row.

        Time complexity: O(m log n)
        Space complexity: O(1)
        """
        c = 0

        for row in grid:
            l, r = 0, len(row)
            while l < r:
                m = (r + l) // 2
                if row[m] < 0:
                    r = m
                else:
                    l = m + 1
            c += len(row) - l
        return c


# test cases
solution = Solution()
print(
    solution.countNegatives(
        [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    )
)  # 8
print(solution.countNegatives([[3, 2], [1, 0]]))  # 0
print(solution.countNegatives([[-1]]))  # 1
print(solution.countNegatives([[5, 1, 0, -5]]))  # 1
