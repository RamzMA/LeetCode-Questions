from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search in Rotated Sorted Array - #33

        At each step one half is always sorted.
        Check if the left half is sorted if target falls in that range search left, otherwise search right.
        Repeat for right half.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


# test cases
solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(solution.search([1], 0))  # -1
print(solution.search([1, 3], 3))  # 1
print(solution.search([3, 1], 1))  # 1
