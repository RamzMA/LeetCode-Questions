from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search - #704

        Calculate the midpoint each iteration.
        If the midpoint value matches return it.
        If target is greater move left pointer past mid, if smaller move right pointer before mid.
        Return -1 if not found.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1


# test cases
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # 4
print(solution.search([-1, 0, 3, 5, 9, 12], 2))  # -1
print(solution.search([5], 5))  # 0
print(solution.search([1, 3, 5, 7, 9], 7))  # 3
print(solution.search([1, 3, 5, 7, 9], 6))  # -1
