# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            m = (low + high) // 2

            isBad = isBadVersion(m)

            if isBad and m == n:
                return m

            if not isBad:
                low = m + 1
            else:
                prevIsBad = isBadVersion(m - 1)
                if prevIsBad:
                    high = m - 1
                else:
                    return m
