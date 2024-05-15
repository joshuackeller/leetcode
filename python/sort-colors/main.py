from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for x in nums:
            colors[x] += 1

        p = 0
        for x in range(len(colors)):
            for y in range(colors[x]):
                nums[p] = x
                p += 1
