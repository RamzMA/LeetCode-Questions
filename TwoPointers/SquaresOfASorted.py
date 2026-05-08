from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Squares of Sorted Array - #977

        Since the array is sorted, the largest squaresare always at either end.
        Compare absolute values, place the larger square at the current rightmost position of the result array, then move that pointer inward.
        Fill result from right to left.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        res = [0] * len(nums)
        left, right, pos = 0, len(nums) - 1, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return res


# test cases
solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(solution.sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
print(solution.sortedSquares([-1]))  # [1]
print(solution.sortedSquares([0, 1, 2]))  # [0, 1, 4]
