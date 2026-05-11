from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Is Subsequence - #392

        Iterate through t and whenever a character matches the current s pointer advance it.
        If the pointer reaches the end of s all characters were found in order.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        if len(s) == 0:
            return True

        letter = 0

        for i in range(len(t)):
            if t[i] == s[letter]:
                letter += 1
            if letter == len(s):
                return True
        return False


# test cases
solution = Solution()
print(solution.isSubsequence("ace", "abcde"))  # True
print(solution.isSubsequence("aec", "abcde"))  # False
print(solution.isSubsequence("", "abcde"))  # True
print(solution.isSubsequence("abc", ""))  # False
print(solution.isSubsequence("b", "abc"))  # True
