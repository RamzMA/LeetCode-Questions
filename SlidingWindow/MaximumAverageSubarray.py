from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Maximum Average Subarray I - #643

        Build the first window of size k, then slide it forward one step
        at a time dropping the leftmost element and adding the new right
        element.
        Track the maximum sum seen and return it divided by k.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        cs = sum(nums[:k])
        ms = cs

        for i in range(k, len(nums)):
            cs = cs - nums[i - k] + nums[i]
            ms = max(ms, cs)

        return ms / k


# test cases
solution = Solution()
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(solution.findMaxAverage([5], 1))  # 5.0
print(solution.findMaxAverage([0, 1, 1, 3, 3], 4))  # 2.0
print(solution.findMaxAverage([-1, -2, -3, -4], 2))  # -1.5
