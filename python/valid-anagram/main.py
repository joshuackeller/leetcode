from collections import Counter


# Simplest solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Counters = more manual / explicit use
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s, t = Counter(s), Counter(t)
#
#         if len(s) != len(t):
#             return False
#
#         for key in t:
#             if key not in s or s[key] != t[key]:
#                 return False
#
#         return True


# Two maps - more realistic solution for most languages
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_map, t_map = {}, {}
#         for char in s:
#             if char in s_map:
#                 s_map[char] += 1
#             else:
#                 s_map[char] = 1
#         for char in t:
#             if char in t_map:
#                 t_map[char] += 1
#             else:
#                 t_map[char] = 1
#
#         if len(s_map) != len(t_map):
#             return False
#
#         for char in s_map:
#             if char not in t_map or t_map[char] != s_map[char]:
#                 return False
#
#         return True
