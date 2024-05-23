from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_matrix, right_matrix = 0, len(matrix) - 1
        arr_index = -1

        while left_matrix <= right_matrix:
            m = (left_matrix + right_matrix) // 2

            if target < matrix[m][0]:
                right_matrix = m - 1
            elif target > matrix[m][-1]:
                left_matrix = m + 1
            else:
                arr_index = m
                break

        if arr_index == -1:
            return False

        arr = matrix[arr_index]
        left, right = 0, len(arr)

        while left <= right:
            m = (left + right) // 2

            if target == arr[m]:
                return True
            elif target < arr[m]:
                right = m - 1
            else:
                left = m + 1

        return False


s = Solution()
