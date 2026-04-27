from typing import List

"""
Return a new array that is nums concatenated with itself.
Python's + operator on lists handles this in one line.

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        array2 = nums + nums

        return array2


# test cases
solution = Solution()
print(solution.getConcatenation([1, 2, 3, 4]))  # 1,2,3,4,1,2,3,4
print(solution.getConcatenation([23, 234, 46, 2]))  # 23,234,46,2,23,234,46,2
print(
    solution.getConcatenation([1546, 324, 564, 234, 253])
)  # 1546,324,564,234,253,1546,324,564,234,253
print(solution.getConcatenation([23, 124, 64, 2]))  # 23,124,64,2,23,124,64,2
