class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_count = 0, 0, 0
        letters = {}

        while right < len(s):
            if s[right] in letters and letters[s[right]] >= left:
                left = letters[s[right]] + 1
                letters[s[right]] = right
                right += 1
            else:
                letters[s[right]] = right
                max_count = max(right - left + 1, max_count)
                right += 1
    
        return max_count

solution = Solution()

print(3, solution.lengthOfLongestSubstring("dvdf"))
print(5, solution.lengthOfLongestSubstring("tmmzuxt"))
print(3, solution.lengthOfLongestSubstring("pwwkew"))
print(3, solution.lengthOfLongestSubstring("abcabcbb"))
print(1, solution.lengthOfLongestSubstring("bbbbb"))
print(2, solution.lengthOfLongestSubstring("aab"))
print(10, solution.lengthOfLongestSubstring("abbccdefghijkrro"))
