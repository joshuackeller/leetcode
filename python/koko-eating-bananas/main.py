from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            k = (low + high) // 2

            total_time = 0

            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                ans = k
                high = k - 1
            else:
                low = k + 1

        return ans


s = Solution()

print(s.minEatingSpeed([312884470], 968709470) == 1)
print(s.minEatingSpeed([3, 6, 7, 11], 8) == 4)
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30)
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23)
print(s.minEatingSpeed([312884470], 312884469) == 2)
