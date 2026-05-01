from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encode and Decode Strings - #271

        Encode by prefixing each word with its length and a '#'.
        Decode by using two pointers, i starts at the length number, j scans forward to find '#' finding the length.
        Slice the word, then jump i forward to the next encoded word.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        newString = ""

        for word in strs:
            newString += str(len(word)) + "#" + word
        return newString

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# test cases
solution = Solution()
print(solution.encode(["hello", "bye", "world"]))  # 5#hello3#bye5#world
print(solution.decode("5#hello3#bye5#world"))  # ['hello', 'bye', 'world']
print(solution.decode(solution.encode(["hello", "world"])))  # ['hello', 'world']
print(solution.decode(solution.encode(["#", "##", "###"])))  # ['#', '##', '###']
print(solution.decode(solution.encode([""])))  # ['']
