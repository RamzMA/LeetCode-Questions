class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Longest Repeating Character Replacement - #424

        Sliding window tracking character frequencies.
        A window is valid if window size minus the most frequent character count is <= k,
        meaning we only need k replacements to make it uniform.
        Shrink from left when invalid, track the longest valid window.

        Time complexity: O(n)
        Space complexity: O(1) — at most 26 characters in the map
        """
        left = 0
        count = {}
        maxCount = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])

            while (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res


# test cases
solution = Solution()
print(solution.characterReplacement("ABAB", 2))  # 4
print(solution.characterReplacement("AABABBA", 1))  # 4
print(solution.characterReplacement("AAAA", 2))  # 4
print(solution.characterReplacement("ABCD", 0))  # 1
print(solution.characterReplacement("AABB", 0))  # 2
