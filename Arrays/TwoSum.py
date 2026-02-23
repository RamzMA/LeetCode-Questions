from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return []
        
        seen = {}

        for i in range(len(nums)):
            looking = target - nums[i] # for example 7 -3 = 4 we want to see if 4 is in seen
            if looking in seen:
                return [seen[looking], i]
            else:
                seen[nums[i]] = i
            
        return []

# Time Complexity: O(n) where n is the number of elements in the input list.
# Space Complexity: O(n) in the worst case when all elements are unique and stored in the hash map.

#test cases
solution = Solution()
print(solution.twoSum([1,2,3,4,5,6,7], 7)) # Output: [0, 6] (nums[0] + nums[6] = 1 + 7 = 8)
print(solution.twoSum([1,2,3,4,5,6,7], 10)) # Output: [3, 6] (nums[3] + nums[6] = 4 + 7 = 11)
print(solution.twoSum([1,2,3,4,5,6,7], 13)) # Output: [5, 6] (nums[5] + nums[6] = 6 + 7 = 13)
print(solution.twoSum([1,2,3,4,5,6,7], 1)) # Output: []
print(solution.twoSum([1,2,3,4,5,6,7], 14)) # Output: []
            