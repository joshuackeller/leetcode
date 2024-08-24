from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums[2] = nums[2] + nums[0]
        cur = 3

        while cur < len(nums):
            nums[cur] = nums[cur] + max(nums[cur - 2], nums[cur - 3])
            cur += 1

        return max(nums[-1], nums[-2])


s = Solution()

print(s.rob([1]) == 1)
print(s.rob([2, 1]) == 2)
print(s.rob([1, 2, 3]) == 4)
print(s.rob([1, 5, 3]) == 5)
print(s.rob([1, 2, 3, 1]) == 4)
print(s.rob([1, 14, 2, 15, 3, 4, 16, 0, 1, 18]))
