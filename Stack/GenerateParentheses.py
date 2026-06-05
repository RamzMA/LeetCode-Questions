from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate Parentheses - #22

        Backtracking, build combinations by adding '(' when open count is less than n, and ')' when close count is less than open count.
        Push before recursing, pop after to restore state.
        When both counts equal n a valid combination is complete.

        Time complexity: O(4^n / sqrt(n))
        Space complexity: O(n)
        """
        stack = []
        res = []

        def backtrack(openn, closee):
            if openn == closee == n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append("(")
                backtrack(openn + 1, closee)
                stack.pop()

            if closee < openn:
                stack.append(")")
                backtrack(openn, closee + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# test cases
solution = Solution()
print(solution.generateParenthesis(1))  # ["()"]
print(solution.generateParenthesis(2))  # ["(())", "()()"]
print(solution.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
