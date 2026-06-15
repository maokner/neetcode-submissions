class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        L = 0
        for R in range(len(s)):
            if s[R] not in seen:
                seen.add(s[R])
                longest = max(longest, len(seen))
            else:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
                seen.add(s[R])
        return longest

        