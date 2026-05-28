from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find All Anagrams in a String - #438

        Fixed sliding window of size len(p).
        Build frequency maps for p and the first window of s.
        Slide forward add new character, remove old one, delete zero counts to keep comparisons clean.
        Append the start index whenever the window matches p's frequency map.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if len(p) > len(s):
            return []

        valids = []
        cS = Counter(s[: len(p)])
        cP = Counter(p)

        if cS == cP:
            valids.append(0)

        for right in range(len(p), len(s)):
            cS[s[right]] += 1
            cS[s[right - len(p)]] -= 1
            if cS[s[right - len(p)]] == 0:
                del cS[s[right - len(p)]]
            if cS == cP:
                valids.append(right - len(p) + 1)
        return list(valids)


# test cases
solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(solution.findAnagrams("abab", "ab"))  # [0, 1, 2]
print(solution.findAnagrams("aa", "bb"))  # []
print(solution.findAnagrams("a", "a"))  # [0]
print(solution.findAnagrams("baa", "aa"))  # [1]
