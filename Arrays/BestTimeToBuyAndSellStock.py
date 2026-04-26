from typing import List


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        Track the minimum price seen so far and the maximum profit at each iteration. 
        If current price is a new low, update the minimum.
        Otherwise check if selling today beats the current best profit.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        currentMin = 10000
        currentMax = 0

        for price in prices:
            if currentMin > price:
                currentMin = price
            elif price - currentMin > currentMax:
                currentMax = price - currentMin

        return currentMax


# test cases
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(solution.maxProfit([7, 6, 4, 3, 1]))  # 0
print(solution.maxProfit([1, 2]))  # 1
print(solution.maxProfit([2, 4, 1, 7]))  # 6
