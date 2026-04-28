from typing import List


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        Build a frequency hashmap, then sort the keys by their frequency in descending order. 
        Iterate over the first k elements of the sorted result and return them as the output list.

        Time complexity: O(n log n)
        Space complexity: O(n)
        """

        hs = {}

        for num in nums:
            hs[num] = hs.get(num, 0) + 1

        sortedhs = sorted(hs, key=lambda x: hs[x], reverse=True)

        mostFrequent = []

        for key in sortedhs[:k]:
            mostFrequent.append(key)

        return mostFrequent


# test cases
solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
print(solution.topKFrequent([1], 1))  # Output: [1]
print(solution.topKFrequent([1, 2, 3, 4, 5], 3))  # Output: [1, 2, 3]
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 1))  # Output: [1]

