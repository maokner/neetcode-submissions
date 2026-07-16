class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        k = 0
        for direction, ammt in shift:
            if direction == 0:
                k -= ammt
            else:
                k += ammt
        k = k % len(s)
        return s[-1 * k:] + s[:-1 * k]
        