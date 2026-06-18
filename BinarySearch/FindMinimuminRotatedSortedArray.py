from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find Minimum in Rotated Sorted Array - #153

        If mid is greater than right, the minimum is in the right half so move left pointer up.
        Otherwise the minimum is in the left half including mid so move right pointer to mid.
        Track minimum seen at each step.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        res = float("inf")

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            res = min(res, nums[m])
        return min(res, nums[l])


# test cases
solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))  # 1
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(solution.findMin([11, 13, 15, 17]))  # 11
print(solution.findMin([2, 1]))  # 1
print(solution.findMin([1]))  # 1
