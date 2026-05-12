from typing import List


class Solution(object):
    def maxArea(self, height):
        """
        Container With Most Water - #11

        Two pointers from both ends.
        Area is min height times width.
        Always move the pointer with the shorter height inward since the taller wall is already maximising its contribution.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


# test cases
solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(solution.maxArea([1, 1]))  # 1
print(solution.maxArea([4, 3, 2, 1, 4]))  # 16
print(solution.maxArea([1, 2, 1]))  # 2
