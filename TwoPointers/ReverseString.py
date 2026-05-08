from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        """
        Reverse String - #344

        Two pointers from both ends swapping characters in place until they meet in the middle.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        i, j = 0, len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return s


# test cases
solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))  # ["o","l","l","e","h"]
print(
    solution.reverseString(["H", "a", "n", "n", "a", "h"])
)  # ["h","a","n","n","a","H"]
print(solution.reverseString(["a"]))  # ["a"]
print(solution.reverseString(["a", "b"]))  # ["b","a"]
