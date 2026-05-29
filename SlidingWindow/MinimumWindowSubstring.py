from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Minimum Window Substring - #76

        Expand right adding characters to the window, increment have when a character's count matches t's.
        When have == need shrink from left recording the minimum window, decrement have when shrinking drops a character below t's required count.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        left = 0
        tCount = Counter(t)
        res, reslen = [-1, -1], float("inf")
        window = {}
        have, need = 0, len(tCount)

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in tCount and window[c] == tCount[c]:
                have += 1

            while need == have:
                if (right - left + 1) < reslen:
                    reslen = right - left + 1
                    res = [left, right]
                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1

        return "" if reslen == float("inf") else s[res[0] : res[1] + 1]


# test cases
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(solution.minWindow("a", "a"))  # "a"
print(solution.minWindow("a", "aa"))  # ""
print(solution.minWindow("bbaa", "aba"))  # "baa"
print(solution.minWindow("aa", "aa"))  # "aa"
