from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = -1
        queue = deque()
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        print(fresh_count)

        if fresh_count == 0:
            return 0
        elif fresh_count > 0 and len(queue) == 0:
            return -1

        while len(queue) > 0:
            minutes += 1
            print(queue)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for r_change, c_change in neighbors:
                    r_next, c_next = r + r_change, c + c_change
                    if (
                        r_next < ROWS
                        and c_next < COLS
                        and min(r_next, c_next) >= 0
                        and grid[r_next][c_next] == 1
                    ):
                        grid[r_next][c_next] = 2
                        fresh_count -= 1
                        queue.append((r_next, c_next))

        print(fresh_count)

        if fresh_count > 0:
            return -1

        return minutes


s = Solution()

# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# print(s.orangesRotting(grid)) # 4

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(s.orangesRotting(grid))  # -1

# grid = [[0]]
# print(s.orangesRotting(grid)) # 0
