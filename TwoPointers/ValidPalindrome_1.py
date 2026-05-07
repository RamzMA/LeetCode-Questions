import re


class Solution(object):
    def isPalindrome(self, s):
        """
        Valid Palindrome - #125

        Strip non-alphanumeric characters using regex and lowercase the string.
        Then use two pointers from both ends, moving inward comparing characters.
        If any pair doesn't match return False, otherwise return True.

        Time complexity: O(n)
        Space complexity: O(n) — new string created
        """

        nString = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        left, right = 0, len(nString) - 1

        while left < right:
            if nString[left] == nString[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# Test Cases
solution = Solution()
print(solution.isPalindrome("car"))  # returns false as car is not a palindrome
print(solution.isPalindrome("wow"))  # returns true as wow is a palindrome
print(
    solution.isPalindrome("A man, a plan, a canal: Panama")
)  # returns true as it is a palindrome
print(
    solution.isPalindrome("race a car")
)  # returns false as race a car is not a palindrome
