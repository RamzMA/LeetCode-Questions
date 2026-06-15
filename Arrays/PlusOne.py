class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Plus One - #66

        Traverse from right to left.
        If digit is 9 set to 0 and carry over.
        If digit is not 9 just increment and return.
        If all digits were 9 insert 1 at the front.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        r = len(digits) - 1

        while r >= 0 and digits[r] == 9:
            digits[r] = 0
            r -= 1
        if r >= 0:
            digits[r] += 1
        else:
            digits.insert(0, 1)
        return digits


# test cases
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(solution.plusOne([9]))  # [1, 0]
print(solution.plusOne([9, 9, 9]))  # [1, 0, 0, 0]
