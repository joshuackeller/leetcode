from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st_c = 0
        st_s = 0
        for st in students:
            if st == 0:
                st_c += 1
            else:
                st_s += 1

        for sw in sandwiches:
            if sw == 0:
                if st_c == 0:
                    return st_s
                else:
                    st_c -= 1
            elif sw == 1:
                if st_s == 0:
                    return st_c
                else:
                    st_s -= 1

        return st_c + st_s
