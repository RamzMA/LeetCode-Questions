from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Squares of Sorted Array - #977

        Times each number by the power of 2 and then return sorted array

        Time complexity: O(nlogn)
        Space complexity: O(n)
        """

        return sorted(x**2 for x in nums)


# test cases
solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(solution.sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
print(solution.sortedSquares([-1]))  # [1]
print(solution.sortedSquares([0, 1, 2]))  # [0, 1, 4]
