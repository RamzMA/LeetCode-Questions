from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove Duplicates from Sorted Array - #26

        Right pointer scans through every element.
        A number is valid if it doesn't match the element directly behind left meaning it hasn't appeared yet.
        First element is always valid.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left = 0

        for right in range(len(nums)):
            if left < 1 or nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
        return left


# test cases
solution = Solution()
nums = [1, 1, 2]
print(solution.removeDuplicates(nums))  # 2
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))  # 5
nums = [1]
print(solution.removeDuplicates(nums))  # 1
nums = [1, 2, 3]
print(solution.removeDuplicates(nums))  # 3
