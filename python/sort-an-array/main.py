from typing import List


class Solution:
    # merge sort
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(nums: List[int], s, e):
            if e - s <= 1:
                return nums

            m = (e + s) // 2
            sort(nums, s, m)
            sort(nums, m, e)

            merge(nums, s, m, e)

            return nums

        def merge(nums, s, m, e):

            a1 = nums[s:m]
            a2 = nums[m:e]
            p1, l1, p2, l2 = 0, len(a1), 0, len(a2)
            p = s

            while p1 < l1 or p2 < l2:
                if p1 < l1 and p2 < l2:
                    if a1[p1] < a2[p2]:
                        nums[p] = a1[p1]
                        p += 1
                        p1 += 1
                    else:
                        nums[p] = a2[p2]
                        p += 1
                        p2 += 1
                elif p1 < l1:
                    nums[p] = a1[p1]
                    p += 1
                    p1 += 1
                else:
                    nums[p] = a2[p2]
                    p += 1
                    p2 += 1

        return sort(nums, 0, len(nums))
