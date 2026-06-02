class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Backspace String Compare - #844

        For each character if it's not '#' push it onto the stack, if it is '#' pop the last character if the
        stack is not empty.
        Compare both stacks at the end.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        stacka = []
        stackb = []

        for c in s:
            if c != "#":
                stacka.append(c)
            elif stacka:
                stacka.pop()

        for c in t:
            if c != "#":
                stackb.append(c)
            elif stackb:
                stackb.pop()

        return stacka == stackb


# test cases
solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  # True
print(solution.backspaceCompare("ab##", "c#d#"))  # True
print(solution.backspaceCompare("a#c", "b"))  # False
print(solution.backspaceCompare("a##c", "#a#c"))  # True
print(solution.backspaceCompare("bxj##tw", "bxj##tw"))  # True
