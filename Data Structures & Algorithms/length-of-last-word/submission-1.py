class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newWord = True
        last = 0

        for char in s:
            if char != " ":
                if newWord:
                    last = 1
                    newWord = False
                else:
                    last += 1
            else:
                newWord = True
        
        return last
        