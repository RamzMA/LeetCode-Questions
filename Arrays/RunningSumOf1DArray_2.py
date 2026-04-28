from typing import List


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Two pointers, Left and right start at 0 and 1. At each step, add the left value to the right value in-place, then advance both pointers.
        Each element accumulates the sum of all previous elements.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left, right = 0, 1

        while right < len(nums):
            nums[right] = nums[left] + nums[right]
            right += 1
            left += 1

        return nums


# test cases
solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(solution.runningSum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]
print(solution.runningSum([3, 1, 2, 10, 1]))  # [3, 4, 6, 16, 17]
print(solution.runningSum([1]))  # [1]
