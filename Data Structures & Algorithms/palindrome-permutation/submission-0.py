class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        evens = set(s)
        odds = set()
        for char in s:
            if char in evens:
                evens.remove(char)
                odds.add(char)
            else:
                evens.add(char)
                odds.remove(char)
        return len(odds) <= 1
        