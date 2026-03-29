"""
My apprach would be to use binary seach in order to check the middle value, if the middle value is over the target number then I would check numbers before the middle.
Otherwise if the middle number is less than the target check for numbers after middle numbers in the list. Each time repeating the binary search until a target is found, or thereappears to be no target found where I would return -1.

The brute force approach would be to set a for loop in order to check each number in the list, however that would be o(n) and we are looking for o(logn) which binary searching  can provide
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


solution = Solution()

print(solution.search([-1, 0, 2, 4, 6, 8], 4))
