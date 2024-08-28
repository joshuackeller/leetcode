# Dynamic Programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        len_rows, len_cols = m, n
        grid = [[0 for _ in range(len_cols)] for _ in range(len_rows)]

        for c in range(len_cols):
            grid[-1][c] = 1
        for r in range(len_rows):
            grid[r][-1] = 1

        for r in range(len_rows - 2, -1, -1):
            for c in range(len_cols - 2, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1]

        return grid[0][0]


s = Solution()

print(s.uniquePaths(3, 7) == 28)
print(s.uniquePaths(3, 2) == 3)

# Brute Force w/ Caching
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         cache = {}
#
#         def solve(m: int, n: int) -> int:
#             if m == 1 and n == 1:
#                 return 1
#             if (m, n) in cache:
#                 return cache[(m, n)]
#
#             count = 0
#
#             if m > 1:
#                 count += solve(m - 1, n)
#             if n > 1:
#                 count += solve(m, n - 1)
#
#             cache[(m, n)] = count
#             return count
#
#         return solve(m, n)
#
