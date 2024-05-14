from typing import List


# quick sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def helper(nums: List[int], s: int, e: int) -> List[int]:
            if e - s + 1 <= 1:
                return nums

            p1, p2 = s, s

            while p2 < e:
                if nums[p2] < nums[e]:
                    nums[p2], nums[p1] = nums[p1], nums[p2]
                    p1 += 1
                p2 += 1

            nums[e], nums[p1] = nums[p1], nums[e]

            helper(nums, s, p1 - 1)
            helper(nums, p1 + 1, e)

            return nums

        return helper(nums, 0, len(nums) - 1)


s = Solution()
a = [2, 1]

print(s.sortArray(a))

# merge sort
# def sortArray(self, nums: List[int]) -> List[int]:

#     def sort(nums: List[int], s, e):
#         if e - s <= 1:
#             return nums

#         m = (e + s) // 2
#         sort(nums, s, m)
#         sort(nums, m, e)

#         merge(nums, s, m, e)

#         return nums

#     def merge(nums, s, m, e):

#         a1 = nums[s:m]
#         a2 = nums[m:e]
#         p1, l1, p2, l2 = 0, len(a1), 0, len(a2)
#         p = s

#         while p1 < l1 or p2 < l2:
#             if p1 < l1 and p2 < l2:
#                 if a1[p1] < a2[p2]:
#                     nums[p] = a1[p1]
#                     p += 1
#                     p1 += 1
#                 else:
#                     nums[p] = a2[p2]
#                     p += 1
#                     p2 += 1
#             elif p1 < l1:
#                 nums[p] = a1[p1]
#                 p += 1
#                 p1 += 1
#             else:
#                 nums[p] = a2[p2]
#                 p += 1
#                 p2 += 1

#     return sort(nums, 0, len(nums))
