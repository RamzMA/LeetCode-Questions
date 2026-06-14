from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        #27 Remove Elements

        Two points swapping all numbers == val to the end and return r+1 which is the position of valid numbers 0 indexed + 1.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return r + 1


solution = Solution()
print(solution.removeElement([1, 2, 3, 4], 2))  # 3
print(solution.removeElement([1, 2, 3, 3, 3, 4], 2))  # 5
print(solution.removeElement([1, 2, 5, 7, 3, 4], 2))  # 5
print(solution.removeElement([1], 1))  # 0
