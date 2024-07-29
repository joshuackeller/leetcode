from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], max_val)
            arr[i] = max_val
            max_val = new_max

        return arr


s = Solution()

print(s.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1])
print(s.replaceElements([1]) == [-1])
print(s.replaceElements([5, 4, 3, 2, 1]) == [4, 3, 2, 1, -1])
print(s.replaceElements([1, 2, 3, 4]) == [4, 4, 4, -1])
print(s.replaceElements([1, 2, 3, 4, 3, 2, 1]) == [4, 4, 4, 3, 2, 1, -1])
