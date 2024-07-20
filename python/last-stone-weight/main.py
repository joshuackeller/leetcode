from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -(x - y))

        if len(max_heap) == 0:
            return 0

        return -max_heap[0]


s = Solution()

print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
