# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        ans = n

        while low <= high:
            m = (low + high) // 2

            isBad = isBadVersion(m)

            if isBad:
                ans = m
                high = m - 1
            else:
                low = m + 1

        return ans
