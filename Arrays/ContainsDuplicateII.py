class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Contains Duplicate II - #219

        Store each number and its most recent index in a hashmap.
        If the number is seen again and the distance between indices is <= k return True.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            seen[n] = i
        return False


# test cases
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
