from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, cur = [], []

        def solve(i: int):
            if i >= len(nums):
                ans.append(cur.copy())
                return

            cur.append(nums[i])
            solve(i + 1)

            cur.pop()
            solve(i + 1)

        solve(0)

        return ans


s = Solution()

print(s.subsets([1, 2, 3]))
