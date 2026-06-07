class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decode String - #394

        Push everything except ']'. When ']' is hit, pop characters to build the substring until '[' is found.
        Then pop digits to build the repeat count.
        Push the repeated substring back.
        Multi-digit numbers are reconstructed by prepending each popped digit.

        Time complexity: O(n * k) where k is the max repeat count
        Space complexity: O(n)
        """
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)
        return "".join(stack)


# test cases
solution = Solution()
print(solution.decodeString("3[a]2[bc]"))  # "aaabcbc"
print(solution.decodeString("3[a2[c]]"))  # "accaccacc"
print(solution.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
print(solution.decodeString("2[a2[b]]"))  # "abbabb"
print(solution.decodeString("10[a]"))  # "aaaaaaaaaa"
