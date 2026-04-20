from typing import List


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        The first approach I would use is to make a set with the numbers, with that I would then make a for loop from (i...n) and check which number (i) is not in the set.
        This approach would have to loop through all numbers i...n so that would result in a o(n) and the space complexity is a o(n) as we are using a set.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        s = set(nums)

        for i in range(len(nums) + 1):
            if i not in s:
                return i
        return 0


# Test cases
solution = Solution()
print(solution.missingNumber([1, 2, 3, 4, 5]))  # missing 0
print(solution.missingNumber([0, 1, 2, 4, 5]))  # missing 3
print(solution.missingNumber([0, 1, 2, 3, 4]))  # missing 5
print(solution.missingNumber([1, 2, 3]))  # missing 0
