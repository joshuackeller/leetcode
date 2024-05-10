class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        n1, n2 = 0, 1

        for _ in range(n - 1):
            temp = n2
            n2 = n2 + n1
            n1 = temp

        return n2
