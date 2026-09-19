class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False

                stack.pop()

        return not stack
