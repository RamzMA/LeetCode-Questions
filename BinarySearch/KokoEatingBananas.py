import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko Eating Bananas - #875

        Binary search on the answer the eating speed k.
        For each speed, calculate total hours needed using ceiling division.
        If hours fit within h, try a smaller speed.
        Otherwise increase the speed.

        Time complexity: O(n log m)
        Space complexity: O(1)
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


# test cases
solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # 4
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # 23
print(solution.minEatingSpeed([1, 1, 1, 1], 4))  # 1
