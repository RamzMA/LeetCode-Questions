from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Daily Temperatures - #739

        Monotonic stack storing [temperature, index] pairs.
        For each day, pop all days from the stack that are cooler than the current temperature those days have found their warmer day.
        The wait is current index minus the popped index.
        Days with no warmer day stay 0.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackt, stackindex = stack.pop()
                res[stackindex] = i - stackindex
            stack.append([temp, i])
        return res


# test cases
solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([30, 40, 50, 60]))  # [1,1,1,0]
print(solution.dailyTemperatures([30, 60, 90]))  # [1,1,0]
print(solution.dailyTemperatures([90, 80, 70, 60]))  # [0,0,0,0]
