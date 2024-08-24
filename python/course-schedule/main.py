from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        cache = set()

        for x, y in prerequisites:
            if x in pre_map:
                pre_map[x].append(y)
            else:
                pre_map[x] = [y]

        visited = set()

        def solve(course: int):
            if course not in pre_map or course in cache:
                return True
            if course in visited:
                return False

            visited.add(course)
            for pre in pre_map[course]:
                if solve(pre) == False:
                    return False
            visited.remove(course)

            cache.add(course)
            return True

        for x, _ in prerequisites:
            if solve(x) == False:
                return False

        return True


s = Solution()

numCourses = 5
pre = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
# pre = [[1,0], [0,1]]

print(s.canFinish(numCourses, pre))
