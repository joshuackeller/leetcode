from typing import List
import random
import sys

sys.setrecursionlimit(100000)


# Quick Select w/ Random Pivot and removes equal values
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums: List[int], k: int) -> int:
            small, large = [], []
            pivot = random.choice(nums)

            for num in nums:
                if num < pivot:
                    small.append(num)
                elif num > pivot:
                    large.append(num)

            if len(nums) - k < len(small):
                return quickSelect(small, k - (len(nums) - len(small)))
            elif len(nums) - k >= len(nums) - len(large):
                return quickSelect(large, k)
            else:
                return pivot

        return quickSelect(nums, k)
