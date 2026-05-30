from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Baseball Game - #682

        For each operation: integers get pushed, C pops the last score, D doubles the last score and pushes it,
        and + pushes the sum of the last two scores.
        Return the sum of all scores.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []

        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)


# test cases
solution = Solution()
print(solution.calPoints(["5", "2", "C", "D", "+"]))  # 30
print(solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(solution.calPoints(["1"]))  # 1
print(solution.calPoints(["5", "2", "C", "D", "+"]))  # 30
