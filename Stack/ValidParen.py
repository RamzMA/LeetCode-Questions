class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        paren = {
            '[':']',
            '{':'}',
            '(':')'
        }

        stack = []

        for char in s:
            if char in paren:
                stack.append(char)
            else:
                if not stack: # check if stack empty
                    return False
                top = stack.pop()
                if paren[top] != char:
                    return False
        return True
    
    # Time Complexity: O(n) where n is the length of the input string.
    # Space Complexity: O(n) in the worst case when all characters in the input string are opening parentheses and stored in the stack.

#test cases
solution = Solution()
print(solution.isValid("()")) # Output: True 
print(solution.isValid("()[]{}")) # Output: True
print(solution.isValid("(]")) # Output: False 
print(solution.isValid("([)]")) # Output: False
