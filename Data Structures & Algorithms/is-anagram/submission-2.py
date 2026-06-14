class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            counts[idx] += 1
        for c in t:
            idx = ord(c) - ord('a')
            counts[idx] -= 1
        return counts == [0] * 26
        