class Solution:
    def isValid(self, s: str) -> bool:
        vals = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []

        for c in s:
            if len(stack) > 0 and c in vals and vals[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
