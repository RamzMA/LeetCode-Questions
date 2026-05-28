from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        """
        Diet Plan Performance - #1176

        Fixed sliding window of size k.
        Build the first window sum, then slide forward.
        At each position check if the sum is below lower (-1), above upper (+1), or in range (0).
        Accumulate the total score.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        total = 0
        score = 0

        for i in range(k):
            total += calories[i]

        if total > upper:
            score += 1
        elif total < lower:
            score -= 1

        for i in range(k, len(calories)):
            total = total - calories[i - k] + calories[i]

            if total > upper:
                score += 1
            elif total < lower:
                score -= 1
        return score


# test cases
solution = Solution()
print(solution.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3))  # 0
print(solution.dietPlanPerformance([3, 2], 2, 0, 1))  # 1
print(
    solution.dietPlanPerformance([6, 5, 0, 4, 2, 6, 1, 6], 4, 5, 6)
)  # 0 — check manually
