class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_i = 0
        t_i = 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1

        return s_i == len(s)


s = Solution()

print(s.isSubsequence("", "abcde") is True)
print(s.isSubsequence("ace", "abcde") is True)
print(s.isSubsequence("aec", "abcde") is False)
print(s.isSubsequence("abcde", "ace") is False)
print(s.isSubsequence("dog", "ddoogg") is True)
print(s.isSubsequence("dog", "adoga") is True)
print(s.isSubsequence("dog", "adoga") is True)
print(s.isSubsequence("dog", "dogggggggggg") is True)
print(s.isSubsequence("dog", "ddddddddddog") is True)
print(s.isSubsequence("dog", "doooooooooog") is True)
