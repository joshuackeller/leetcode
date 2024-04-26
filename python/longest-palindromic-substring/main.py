class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s, start, end) -> bool:
            if (end - start + 1) % 2 == 0:
                mid = ((end - start) // 2) + 1 + start
                return s[start:mid][::-1] == s[mid : end + 1]
            else:
                mid = (end - start) // 2 + start
                return s[start:mid][::-1] == s[mid + 1 : end + 1]

        ans_left, ans_right, left, right, cur = 0, 0, 0, 0, 0

        while left < len(s):
            if (
                left - 1 >= 0
                and right + 1 < len(s)
                and isPalindrome(s, left - 1, right + 1)
            ):
                left -= 1
                right += 1
            elif right + 1 < len(s) and isPalindrome(s, left, right + 1):
                right += 1
            else:
                cur += 1
                left, right = cur, cur

            if right - left > ans_right - ans_left:
                ans_right = right
                ans_left = left

        return s[ans_left : ans_right + 1]
