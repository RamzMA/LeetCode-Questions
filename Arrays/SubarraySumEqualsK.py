class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        Subarray Sum Equals K - #560 (Brute Force)

        Two loops fixing a start point and expanding right, accumulating a running total. 
        Each time the total equals k, increment the count.

        Time complexity: O(n^2)
        Space complexity: O(1)
        """

        # [1],[1],[1],[1,1],[1,1],[1,1,1]

        count = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1

        return count


# test cases
solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))  # 2
print(solution.subarraySum([1, 2, 3], 3))  # 2 → [3] and [1,2]
print(solution.subarraySum([1, -1, 1], 1))  # 3
print(solution.subarraySum([1], 1))  # 1
print(solution.subarraySum([1, 2, 3, 4, 5], 9))  # 2 → [2,3,4] and [4,5]
