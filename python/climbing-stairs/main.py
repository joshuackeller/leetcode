class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 0, 1

        for _ in range(n):
            temp = n2
            n2 = n2 + n1
            n1 = temp

        return n2
