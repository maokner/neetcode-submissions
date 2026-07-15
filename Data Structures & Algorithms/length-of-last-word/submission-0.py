class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newWord = True
        lastWord = None

        for char in s:
            if char != " ":
                if newWord:
                    lastWord = char
                    newWord = False
                else:
                    lastWord += char
            else:
                newWord = True
        
        return len(lastWord)
        