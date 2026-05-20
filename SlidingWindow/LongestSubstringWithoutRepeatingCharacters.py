from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Longest Substring Without Repeating Characters - #3

        Sliding window with a set tracking characters in the current window.
        Right pointer expands the window, if a duplicate is found shrink from the left until it's gone.
        Track the longest window seen.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(s) == 1:
            return 1

        left = 0
        seen = set()
        res = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res


# test cases
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3 → "abc"
print(solution.lengthOfLongestSubstring("bbbbb"))  # 1 → "b"
print(solution.lengthOfLongestSubstring("pwwkew"))  # 3 → "wke"
print(solution.lengthOfLongestSubstring(""))  # 0
print(solution.lengthOfLongestSubstring("a"))  # 1
