class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for t1 in range(len(text1) - 1, -1, -1):
            for t2 in range(len(text2) - 1, -1, -1):
                if text1[t1] == text2[t2]:
                    grid[t1][t2] = 1 + grid[t1 + 1][t2 + 1]
                else:
                    grid[t1][t2] = max(grid[t1 + 1][t2], grid[t1][t2 + 1])

        return grid[0][0]


s = Solution()

print(s.longestCommonSubsequence("ace", "abcde") == 3)
print(s.longestCommonSubsequence("abcde", "ace") == 3)
print(s.longestCommonSubsequence("abcde", "abcde") == 5)
