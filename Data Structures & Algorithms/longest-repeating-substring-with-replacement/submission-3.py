class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = [0 for _ in range(26)]
        maxLen = 0
        L = 0
        currMax = 0
        for R, c in enumerate(s):
            charMap[ord(c) - ord('A')] += 1
            currMax = max(currMax, charMap[ord(c) - ord('A')])
            currLen = R - L + 1
            while currLen - currMax > k:
                charMap[ord(s[L]) - ord('A')] -= 1
                L += 1
                currLen -= 1
                #currMax = max(charMap)
            maxLen = max(maxLen, R - L + 1)
        return maxLen

            
        