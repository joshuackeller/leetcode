from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for index, num in enumerate(nums):
            if (target - num) in num_map:
                return [num_map[target - num], index]
            else:
                num_map[num] = index

        return []


s = Solution()

print(s.twoSum([2, 8, 1, 15], 9))
