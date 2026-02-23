from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        
        longest = 0
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen:
                current = num
                count = 1

                while current + 1 in seen:
                    current += 1
                    count += 1
                    longest = max(longest, count)
        return longest

    
# Time Complexity: O(n) where n is the number of elements in the input list.
# Space Complexity: O(n) in the worst case when all elements are unique and stored in the set.

#test cases
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2])) # Output: 4 
print(solution.longestConsecutive([0, -1, 1, 2, -2, -3])) # Output: 5 
print(solution.longestConsecutive([1, 2, 0, 1])) # Output: 3 
print(solution.longestConsecutive([])) # Output: 0 
print(solution.longestConsecutive([1])) # Output: 0 
        