class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        for char in s[::-1]:
            if char != " ":
                ret += 1
            elif char == " ":
                if ret != 0:
                    break
        return ret
        