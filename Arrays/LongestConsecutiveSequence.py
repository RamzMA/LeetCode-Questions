from typing import List


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Longest Consecutive Sequence - #128

        Iterate through the set and only start counting from sequence starts.
        Count upwards while the next number exists in the set, tracking the longest sequence seen.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest


# test cases
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4 → [1,2,3,4]
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 → [0-8]
print(solution.longestConsecutive([]))  # 0
print(solution.longestConsecutive([1]))  # 1
print(solution.longestConsecutive([1, 2, 3, 4, 5]))  # 5
