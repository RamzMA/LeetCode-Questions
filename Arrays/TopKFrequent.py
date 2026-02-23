from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or len(nums) == 1: # if the list is empty or has only one element, return the list itself as the top k frequent elements
            return nums
        
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1 

        return sorted(seen.keys(), key=lambda k: seen[k], reverse=True)[:k] # sort by keys and return top k frequent elements
    
# Time Complexity: O(n log n) where n is the number of elements in the input list due to sorting.
# Space Complexity: O(n) in the worst case when all elements are unique and stored in

#test cases
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2)) # Output: [1, 2] 
print(solution.topKFrequent([1], 1)) # Output: [1] 
print(solution.topKFrequent([1,2,3,4,5], 3)) # Output: [1, 2, 3] 
print(solution.topKFrequent([1,1,1,2,2,3], 1)) # Output: [1] 
            