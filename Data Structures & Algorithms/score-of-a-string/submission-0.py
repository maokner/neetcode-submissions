class Solution:
    def scoreOfString(self, s: str) -> int:
        ret = 0

        for R in range(1, len(s)):
            ret += abs(ord(s[R]) - ord(s[R - 1]))
        return ret
        