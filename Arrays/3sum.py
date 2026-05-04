from typing import List


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        3Sum - #15

        Sort the array, then fix each element with index i and use two pointers j and k to find pairs that sum to zero.
        Skip duplicate values of i to avoid duplicate triplets. After finding a triplet, skip duplicate j and k values before advancing both pointers.

        Time complexity: O(n^2)
        Space complexity: O(n)
        """

        sortedNums = sorted(nums)
        res = []

        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            j, k = i + 1, len(sortedNums) - 1

            while j < k:
                if sortedNums[i] + sortedNums[j] + sortedNums[k] == 0:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j < k and sortedNums[j] == sortedNums[j + 1]:
                        j += 1
                    while j < k and sortedNums[k] == sortedNums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sortedNums[i] + sortedNums[j] + sortedNums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res


# test cases
solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0, 0, 0]))  # [[0,0,0]]
print(solution.threeSum([0, 0, 0, 0]))  # [[0,0,0]]
print(solution.threeSum([-2, 0, 0, 2, 2]))  # [[-2,0,2]]
print(solution.threeSum([1, 2, 3]))  # []
