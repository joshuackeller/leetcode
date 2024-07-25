from typing import List
import heapq


# klogn
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append((p[0] ** 2 + p[1] ** 2, p))

        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            _, p = heapq.heappop(heap)
            ans.append(p)

        return ans


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

# nlogn
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
