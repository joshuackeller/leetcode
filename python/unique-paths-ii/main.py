from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        rHasPath = True
        for r in range(rows - 1, -1, -1):
            if obstacleGrid[r][-1] == 1 or not rHasPath:
                obstacleGrid[r][-1] = 0
                rHasPath = False
            else:
                obstacleGrid[r][-1] = 1

        cHasPath = True
        for c in range(cols - 2, -1, -1):
            if obstacleGrid[-1][c] == 1 or not cHasPath:
                obstacleGrid[-1][c] = 0
                cHasPath = False
            else:
                obstacleGrid[-1][c] = 1

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r + 1][c] + obstacleGrid[r][c + 1]

        return obstacleGrid[0][0]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]) == 0)
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2)
print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1)
