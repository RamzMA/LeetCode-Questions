from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        Count Pairs Whose Sum is Less than Target - #2824

        Sort the array, then use two pointers from both ends.
        If the sum of nums[left] and nums[right] is less than target, every pair between left and right also works (since the array is sorted), so add right - left to the count and move left forward.
        Otherwise move right pointer in to try a smaller sum.

        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0

        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1

        return res


# test cases
solution = Solution()
print(solution.countPairs([-1, 1, 2, 3, 1], 2))  # 3
print(solution.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))  # 10
print(solution.countPairs([0, 0, 0], 1))  # 3
