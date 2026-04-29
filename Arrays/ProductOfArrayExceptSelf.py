from typing import List


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Product of Array Except Self - #238

        First pass builds prefix products into result array, where each index holds the product of all elements to its left.
        Second pass multiplies in suffix products right to left, giving each index the product of all elements to its right. 
        Combined, each position holds the product of every element except itself.

        Time complexity: O(n)
        Space complexity: O(1) — result array doesn't count as extra space
        """

        res = [1] * len(nums)  # Get length 4 from res array if nums is length 4

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# test cases
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print(solution.productExceptSelf([2, 3]))  # [3, 2]
print(solution.productExceptSelf([1, 0]))  # [0, 1]
