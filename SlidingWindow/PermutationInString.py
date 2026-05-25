from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Permutation in String - #567

        Slide a fixed window of len(s1) across s2, maintaining a frequency map of the current window.
        At each step add the new character and remove the old one.
        If the window's frequency map matches s1's at any point, a permutation exists.
        Delete zero-count entries to keep comparisons clean.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(s1) > len(s2):
            return False

        hs1 = Counter(s1)
        hs2 = Counter(s2[: len(s1)])

        if hs1 == hs2:
            return True

        for i in range(len(s1), len(s2)):
            hs2[s2[i]] += 1
            hs2[s2[i - len(s1)]] -= 1
            if hs2[s2[i - len(s1)]] == 0:
                del hs2[s2[i - len(s1)]]
            if hs2 == hs1:
                return True
        return False


# test cases
solution = Solution()
print(solution.checkInclusion("ab", "eidbaooo"))  # True
print(solution.checkInclusion("ab", "eidboaoo"))  # False
print(solution.checkInclusion("a", "a"))  # True
print(solution.checkInclusion("abc", "ccccbbbbaaaa"))  # False
print(solution.checkInclusion("adc", "dcda"))  # True
