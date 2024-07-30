from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def countIsland(r, c):
            sum = 0
            if r < ROWS and c < COLS and min(r, c) >= 0 and grid[r][c] == 1:
                grid[r][c] = 0
                sum += 1
                sum += countIsland(r + 1, c)
                sum += countIsland(r - 1, c)
                sum += countIsland(r, c + 1)
                sum += countIsland(r, c - 1)

            return sum

        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_size = max(max_size, countIsland(r, c))

        return max_size


grid = [
    [0],
]

s = Solution()

print(s.maxAreaOfIsland(grid))
