from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur, ans = [], []

        def solve(i: int, runningTotal: int):
            if i > len(candidates) - 1 or runningTotal > target:
                return

            if runningTotal == target:
                ans.append(cur.copy())
                return

            cur.append(candidates[i])
            solve(i, runningTotal + candidates[i])

            cur.pop()
            solve(i + 1, runningTotal)

        solve(0, 0)

        return ans
