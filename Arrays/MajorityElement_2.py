class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Track current number and count.
        When the count hits 0, replace the currentNumber with the current number.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        currentNumber = nums[0]
        currentCount = 1

        for i in range(1, len(nums)):
            if nums[i] == currentNumber:
                currentCount += 1
            else:
                currentCount -= 1

            if currentCount == 0:
                currentCount = 1
                currentNumber = nums[i]

        return currentNumber


# test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(solution.majorityElement([1]))  # 1
print(solution.majorityElement([6, 6, 6, 1, 2]))  # 6
