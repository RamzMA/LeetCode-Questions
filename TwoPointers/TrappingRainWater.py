from typing import List


class Solution(object):
    def trap(self, height):
        """
        Trapping Rain Water - #42

        Two pointers from both ends tracking the max height seen on each side.
        Process whichever side has the smaller max water at that position is
        guaranteed to be maxSide currentHeight since the other side is taller.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        res = 0

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]

        return res


# test cases
solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(solution.trap([4, 2, 0, 3, 2, 5]))  # 9
print(solution.trap([1, 0, 1]))  # 1
print(solution.trap([3, 0, 2, 0, 4]))  # 7
