from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        duplicateCount = 0

        s = set(nums)

        len1 = len(s)
        len2 = len(nums)

        length = len2 - len1

        return [length, len1]


solution = Solution()

print(solution.removeDuplicates([1, 1, 2]))
