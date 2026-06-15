class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        return not stack
        