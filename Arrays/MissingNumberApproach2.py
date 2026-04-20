from typing import List


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """

        The approach I would take would be a mathmatical approach I would get 2 sets of the sums and divide by 2 shown by the formula
        n*(n+1)//2
        This would give me 30 if n was 5 (n being the length of the array), this being the correct sum of the array.
        The trick would then be to subtract the expected sum from the actual sum and the output would be the missing number.

        Time complexity: O(1)
        Space complexity: O(1)

        """

        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


# Test cases
solution = Solution()
print(solution.missingNumber([1, 2, 3, 4, 5]))  # missing 0
print(solution.missingNumber([0, 1, 2, 4, 5]))  # missing 3
print(solution.missingNumber([0, 1, 2, 3, 4]))  # missing 5
print(solution.missingNumber([1, 2, 3]))  # missing 0
