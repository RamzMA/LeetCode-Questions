from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge Sorted Array - #88

        i points to the last real element in nums1,
        j points to the last element in nums2,
        k points to the last position in nums1.
        Compare from the back and place the larger element at k.
        If nums2 has remaining elements copy them in, nums1 elements are already in place.

        Time complexity: O(m + n)
        Space complexity: O(1)
        """

        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j, k = j - 1, k - 1


# test cases
solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # [1, 2, 2, 3, 5, 6]
nums1 = [1]
solution.merge(nums1, 1, [], 0)
print(nums1)  # [1]
nums1 = [0]
solution.merge(nums1, 0, [1], 1)
print(nums1)  # [1]
nums1 = [4, 5, 6, 0, 0, 0]
solution.merge(nums1, 3, [1, 2, 3], 3)
print(nums1)  # [1, 2, 3, 4, 5, 6]
