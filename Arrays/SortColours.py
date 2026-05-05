from typing import List


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        Sort Colors - #75

        Left tracks the boundary of 0s, high tracks the boundary of 2s, mid scans through. 
        Swap 0s to the left, 2s to the right, and leave 1s in place.
        Only advance mid when not swapping with high since the swapped element is unexamined.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left, mid, right = 0, 0, len(nums) - 1
        temp = 0

        while mid <= right:
            if nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            elif nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                mid += 1

        return nums


# test cases
solution = Solution()
print(solution.sortColors([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]
print(solution.sortColors([2, 0, 1]))  # [0, 1, 2]
print(solution.sortColors([0]))  # [0]
print(solution.sortColors([1, 0]))  # [0, 1]
print(solution.sortColors([2, 2, 2, 0, 0, 1]))  # [0, 0, 1, 2, 2, 2]
