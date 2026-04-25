class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Build a frequency hashmap of all numbers, then iterate through it
        tracking the highest frequency seen. Return the key with the highest frequency.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        hs = {}

        for num in nums:
            hs[num] = hs.get(num, 0) + 1

        current = 0
        majority = 0

        for key, value in hs.items():
            if value > current:
                current = value
                majority = key

        return majority


# test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(solution.majorityElement([1]))  # 1
print(solution.majorityElement([6, 6, 6, 1, 2]))  # 6
