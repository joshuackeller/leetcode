import time


# Recursive (Brute Force)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 1:
#             return 1
#
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Recursive With Cache
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = {}
#
#         def solve(n: int) -> int:
#             if n <= 1:
#                 return 1
#
#             if n in cache:
#                 return cache[n]
#
#             cache[n] = solve(n - 1) + solve(n - 2)
#
#             return cache[n]
#
#         return solve(n)


# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        n1, n2 = 0, 1

        while count < n:
            tmp = n2
            n2 = n2 + n1
            n1 = tmp
            count += 1

        return n2


s = Solution()

start = time.time()
print(s.climbStairs(1) == 1)
print(s.climbStairs(2) == 2)
print(s.climbStairs(3) == 3)
print(s.climbStairs(4) == 5)
print(s.climbStairs(5) == 8)
print(s.climbStairs(6) == 13)
print(s.climbStairs(39) == 102334155)
end = time.time()

print(end - start)
