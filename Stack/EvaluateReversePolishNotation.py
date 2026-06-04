from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate Reverse Polish Notation - #150

        For each token if it's a number push it, if it's an operator pop two numbers, apply the operator and push the result back.
        Pop b first then a for subtraction and division.
        Division truncates towards zero using int().

        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []
        for num in tokens:
            if num in "+-/*":
                b, a = stack.pop(), stack.pop()
                if num == "+":
                    stack.append(a + b)
                elif num == "-":
                    stack.append(a - b)
                elif num == "/":
                    stack.append(int(a / b))
                elif num == "*":
                    stack.append(a * b)
            else:
                stack.append(int(num))
        return stack[0]


# test cases
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # 6
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)  # 22
print(solution.evalRPN(["3", "11", "5", "+", "-"]))  # -13
