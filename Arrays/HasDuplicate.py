from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return False
        return True

# Time Complexity: O(n) where n is the number of elements in the input list.
# Space Complexity: O(n) in the worst case when all elements are unique and stored in the set.

#test cases
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 4, 5])) # Output: True (no duplicates)
print(solution.hasDuplicate([1, 2, 3, 4, 5, 1])) # Output: False (duplicate '1')
print(solution.hasDuplicate([])) # Output: True (empty list, no duplicates)
print(solution.hasDuplicate([1])) # Output: True (single element, no duplicates)
print(solution.hasDuplicate([1, 2, 3, 4, 5, 2])) # Output: False (duplicate '2')