class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        ROW = len(grid)
        COL = len(grid[0])
        neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    for r_diff, c_diff in neighbors:
                        new_r = r + r_diff
                        new_c = c + c_diff
                        if (
                            new_r < 0
                            or new_c < 0
                            or new_r == ROW
                            or new_c == COL
                            or grid[new_r][new_c] == 0
                        ):
                            count += 1

        return count