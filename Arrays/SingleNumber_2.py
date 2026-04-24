from typing import List


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        My approach would be to loop through all the numbers in the array and use the XOR operator,
        if the values are the same then result should go back to 0 leaving the singleNumber at the end.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        result = 0
        for num in nums:
            result ^= num
        return result


# test cases:
print(Solution().singleNumber([1, 1, 2, 2, 3]))  # 3
print(Solution().singleNumber([5, 5, 2, 2, 4]))  # 4
print(Solution().singleNumber([9, 9, 7, 7, 5, 44, 44]))  # 5
print(Solution().singleNumber([34, 34, 654, 654, 2]))  # 2
print(Solution().singleNumber([34, 34, 654, 654, 34]))  # -1 false case no singles
