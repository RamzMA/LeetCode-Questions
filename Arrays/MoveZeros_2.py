from typing import List


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        Use a left pointer to track the next position for a non-zero element.
        Right pointer scans the array, whenever a non-zero is found, swap it into the left position and advance left. 

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


# test cases
solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(solution.moveZeroes([0, 0, 1]))  # [1, 0, 0]
print(solution.moveZeroes([0]))  # [0]
print(solution.moveZeroes([1, 2, 3]))  # [1, 2, 3]
