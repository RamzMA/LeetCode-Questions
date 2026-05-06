class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        Subarray Sum Equals K - #560

        Track the running sum and store how many times each prefix sum has been seen. 
        At each step check if curSum - k exists in the map if so, a subarray ending here sums to k. 
        Initialise the map with {0: 1} to handle subarrays starting from index 0.

        Time complexity: O(n)
        Space complexity: O(n)
        """

        # [1],[1],[1],[1,1],[1,1],[1,1,1]

        res = 0
        curSum = 0
        prefixSum = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1

        return res


# test cases
solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))  # 2
print(solution.subarraySum([1, 2, 3], 3))  # 2 → [3] and [1,2]
print(solution.subarraySum([1, -1, 1], 1))  # 3
print(solution.subarraySum([1], 1))  # 1
print(solution.subarraySum([1, 2, 3, 4, 5], 9))  # 2 → [2,3,4] and [4,5]
