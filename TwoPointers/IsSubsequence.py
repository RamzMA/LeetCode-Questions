from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Is Subsequence - #392

        Two pointers, one for s and one for t.
        When characters match advance both pointers, otherwise only advance the t pointer.
        If i reaches the end of s all characters were found in order.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# test cases
solution = Solution()
print(solution.isSubsequence("ace", "abcde"))  # True
print(solution.isSubsequence("aec", "abcde"))  # False
print(solution.isSubsequence("", "abcde"))  # True
print(solution.isSubsequence("abc", ""))  # False
print(solution.isSubsequence("b", "abc"))  # True
