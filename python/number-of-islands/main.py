from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R_MAX = len(grid)
        C_MAX = len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            if c - 1 >= 0 and grid[r][c - 1] == "1":
                dfs(r, c - 1)
            if r - 1 >= 0 and grid[r - 1][c] == "1":
                dfs(r - 1, c)
            if c + 1 < C_MAX and grid[r][c + 1] == "1":
                dfs(r, c + 1)
            if r + 1 < R_MAX and grid[r + 1][c] == "1":
                dfs(r + 1, c)

        count = 0

        for r in range(R_MAX):
            for c in range(C_MAX):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count


# Using set instead of writing over grid
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = set()
#         ROWS, COLS = len(grid), len(grid[0])
#
#         def countIsland(r, c) -> int:
#             if r < ROWS and c < COLS and min(r, c) >= 0 and grid[r][c] == "1":
#                 visited.add((r, c))
#
#                 countIsland(r + 1, c)
#                 countIsland(r - 1, c)
#                 countIsland(r, c + 1)
#                 countIsland(r, c - 1)
#
#         count = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[r])):
#                 if (r, c) not in visited and grid[r][c] == "1":
#                     count += 1
#                     countIsland(r, c)
#
#         return count
#
