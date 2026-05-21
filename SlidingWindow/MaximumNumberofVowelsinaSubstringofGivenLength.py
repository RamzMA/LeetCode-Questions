class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Maximum Number of Vowels in Substring - #1456

        Build the first window counting vowels, then slide forward adding the new character if it's a vowel and removing the old character if it was a vowel.
        Track the maximum count.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        vowels = set(["a", "e", "i", "o", "u"])
        c = 0

        for i in range(k):
            if s[i] in vowels:
                c += 1
        m = c

        for i in range(k, len(s)):
            if s[i] in vowels:
                c += 1
            if s[i - k] in vowels:
                c -= 1
            m = max(m, c)
        return m


# test cases
solution = Solution()
print(solution.maxVowels("abciiidef", 3))  # 3 → "iii"
print(solution.maxVowels("aeiou", 2))  # 2
print(solution.maxVowels("leetcode", 3))  # 2
print(solution.maxVowels("rhythms", 4))  # 0
print(solution.maxVowels("a", 1))  # 1
