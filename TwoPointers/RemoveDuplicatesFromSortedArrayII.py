from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove Duplicates from Sorted Array II - #80

        Left pointer tracks where the next valid element goes.
        Right pointer scans through every element.
        A number is valid if it doesn't match what's two positions behind left meaning it hasn't appeared twice yet.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left = 0

        for right in range(len(nums)):
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        return left


# test cases
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
print(
    solution.removeDuplicates(nums),
    nums[: solution.removeDuplicates([1, 1, 1, 2, 2, 3])],
)  # 5, [1,1,2,2,3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(
    solution.removeDuplicates(nums),
    nums[: solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])],
)  # 7, [0,0,1,1,2,3,3]
nums = [1, 1]
print(solution.removeDuplicates(nums))  # 2
nums = [1]
print(solution.removeDuplicates(nums))  # 1
