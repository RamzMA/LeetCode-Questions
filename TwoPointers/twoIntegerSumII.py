"""
The question states that we must find the 2 numbers that add up to target,
however we are unable to use a hashmap as the space complexity must be o(1).
Therefore the approach I would see fit would be brute force by checking i for all j's,
then increment i and check for all j's again however that would be o(n^2).

The best approach I would apply is 2 pointers to find the numbers in o(n) time,
o(1) space as we check the left and right until we get the numbers.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0 or len(numbers) == 1:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []


solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 3))  # Output should be [1,2] as 1 + 2 = 3
print(solution.twoSum([5, 4, 9, 8], 7))  # Output should be []
print(solution.twoSum([1], 3))  # Output should be []
print(solution.twoSum([2, 3, 9, 11], 13))  # Output should be [1,2] as 1 + 2 = 3

