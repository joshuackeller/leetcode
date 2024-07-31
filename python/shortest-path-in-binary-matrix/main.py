from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1]:
            return -1

        visited = set()
        queue = deque()
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        ROWS, COLS = len(grid), len(grid[0])

        queue.append((0, 0))
        visited.add((0, 0))
        length = 1

        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for r_change, c_change in neighbors:
                    r_next, c_next = r + r_change, c + c_change
                    if (
                        min(r_next, c_next) >= 0
                        and r_next < ROWS
                        and c_next < COLS
                        and (r_next, c_next) not in visited
                        and grid[r_next][c_next] == 0
                    ):
                        queue.append((r_next, c_next))
                        visited.add((r_next, c_next))
            length += 1

        return -1


s = Solution()

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

print(s.shortestPathBinaryMatrix(grid))
