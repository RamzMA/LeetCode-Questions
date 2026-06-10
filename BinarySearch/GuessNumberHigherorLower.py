class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Guess Number Higher or Lower - #374

        Binary search using the guess() API instead of direct comparison.
        If guess returns 0 we found it, -1 means too high so move right pointer down, 1 means too low so move left pointer up.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        l, r = 0, n

        while l <= r:
            m = (r + l) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m - 1
            else:
                l = m + 1


# test cases
# guess() is mocked here
pick = 6


def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


solution = Solution()
print(solution.guessNumber(10))  # 6
print(solution.guessNumber(6))  # 6
