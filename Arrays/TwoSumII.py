class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Two Sum II - #167

        Start one pointer at the left and one at the right. 
        If the sum is too large decrease from the right,if too small increase from the left. 
        When the sum matches return the 1-indexed positions.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]


# test cases
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # [1, 2]
print(solution.twoSum([2, 3, 4], 6))  # [1, 3]
print(solution.twoSum([-1, 0], -1))  # [1, 2]
print(solution.twoSum([1, 2, 3, 4, 5], 9))  # [4, 5]
