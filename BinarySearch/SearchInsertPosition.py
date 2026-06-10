from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Search Insert Position - #35

        If target is found return its index.
        If not found, return l when the loop exits l is sitting at the first position where nums[l] > target,
        which is exactly where the target should be inserted to keep the array sorted.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


# test cases
solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
print(solution.searchInsert([1, 3, 5, 6], 0))  # 0
print(solution.searchInsert([1], 0))  # 0
