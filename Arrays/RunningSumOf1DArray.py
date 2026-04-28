from typing import List


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Iterate through the array starting at index 1, adding the previous
        element to the current one in-place. Each element becomes the sum of all elements before it plus itself.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums


# test cases
solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(solution.runningSum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]
print(solution.runningSum([3, 1, 2, 10, 1]))  # [3, 4, 6, 16, 17]
print(solution.runningSum([1]))  # [1]
