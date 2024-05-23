from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while e >= s:
            m = (e + s) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                e = m - 1
            else:
                s = m + 1

        return -1
