class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        First Bad Version - #278

        If mid is a bad version record it and search left for an earlier bad version.
        If mid is good search right.
        The first bad version is the leftmost bad one found.

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        curBad = float("inf")
        l, r = 0, n

        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                curBad = min(curBad, m)
                r = m - 1
            else:
                l = m + 1
        return curBad


# test cases
def isBadVersion(version):
    return version >= 4  # first bad is 4


solution = Solution()
print(solution.firstBadVersion(5))  # 4
print(solution.firstBadVersion(1))  # 1 (if bad)
