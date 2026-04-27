from typing import List


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        Move Zeroes - #283

        Count all zeroes while removing them from the list, iterating over a copy
        to avoid index shifting issues. The append all 0's at the end.

        Time complexity: O(n)
        Space complexity: O(n) — due to the copy made during iteration
        """

        zeroCount = 0

        for num in nums[:]:
            if num == 0:
                nums.remove(num)
                zeroCount += 1

        while zeroCount != 0:
            nums.append(0)
            zeroCount -= 1

        return nums


# test cases
solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(solution.moveZeroes([0, 0, 1]))  # [1, 0, 0]
print(solution.moveZeroes([0]))  # [0]
print(solution.moveZeroes([1, 2, 3]))  # [1, 2, 3]
