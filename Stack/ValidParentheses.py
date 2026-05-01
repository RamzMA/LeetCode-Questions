class Solution(object):
    def isValid(self, s):
        """
        Valid Parentheses - #20

        Use a stack and a hashmap mapping opening to closing brackets.
        For each character, if it's an opening bracket push it onto the stack.
        If it's a closing bracket, check the top of the stack matches.
        If the stack is empty at the end, all brackets were matched.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        stack = []

        paren = {"[": "]", "{": "}", "(": ")"}

        for char in s:
            if char in paren:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if paren[top] != char:
                    return False
        if len(stack) == 0:
            return True


# test cases
solution = Solution()
print(solution.isValid("()"))  # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))  # False
print(solution.isValid("([)]"))  # False
print(solution.isValid("{[]}"))  # True
print(solution.isValid("]"))  # False
print(solution.isValid(""))  # True
