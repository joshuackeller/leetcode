from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for x in range(1, n + 1):
            ans.append(ans[x // 2] + (x & 1))

        return ans
