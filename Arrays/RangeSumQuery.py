from typing import List


class NumArray:
    """
    Range Sum Query - Immutable - #303

    Build a prefix sum array where prefix[i] is the sum of all elements from index 0 to i-1.
    sumRange is then just prefix[right+1] - prefix[left], making each query O(1) after O(n) preprocessing.

    Time complexity: O(1)
    Space complexity: O(n)
    """

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# test cases
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3
