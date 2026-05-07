class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Use a hashmap to track frequency of numbers and return number with highest frequency.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        
        tracker = {}

        for n in nums:
            tracker[n] = tracker.get(n, 0) + 1
        
        return sorted(tracker, key = lambda x: tracker[x], reverse=True)[0


# test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(solution.majorityElement([1]))  # 1
print(solution.majorityElement([6, 6, 6, 1, 2]))  # 6
