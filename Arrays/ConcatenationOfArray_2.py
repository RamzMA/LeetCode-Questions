from typing import List

"""
Build the result array by looping through nums twice using a while loop,
appending each element both times to construct the concatenated array.

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j = 0
        array2 = []

        while j < 2:
            for num in nums:
                array2.append(num)
            j += 1
        return array2


# test cases
solution = Solution()
print(solution.getConcatenation([1, 2, 3, 4]))  # 1,2,3,4,1,2,3,4
print(solution.getConcatenation([23, 234, 46, 2]))  # 23,234,46,2,23,234,46,2
print(
    solution.getConcatenation([1546, 324, 564, 234, 253])
)  # 1546,324,564,234,253,1546,324,564,234,253
print(solution.getConcatenation([23, 124, 64, 2]))  # 23,124,64,2,23,124,64,2
