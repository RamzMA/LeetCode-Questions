from typing import List


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        My approach would be to loop through all the numbers in the array and add their frequencies to a hashset.
        Then to loop through the hs and check for values (frequencies) equal to 1 for the single digit and return the key (number).

        Time complexity: O(n)
        Space complexity: O(n)
        """

        hs = {}
        for num in nums:
            hs[num] = hs.get(num, 0) + 1

        for key, value in hs.items():
            if value == 1:
                return key

        return -1


# test cases
print(Solution().singleNumber([1, 1, 2, 2, 3]))  # 3
print(Solution().singleNumber([5, 5, 2, 2, 4]))  # 4
print(Solution().singleNumber([9, 9, 7, 7, 5, 44, 44]))  # 5
print(Solution().singleNumber([34, 34, 654, 654, 2]))  # 2
print(Solution().singleNumber([34, 34, 654, 654, 34]))  # -1 false case no singles
