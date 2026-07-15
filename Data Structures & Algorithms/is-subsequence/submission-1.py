class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        P = 0

        for char in t:
            if P == len(s):
                return True
            if char == s[P]:
                P += 1
            
        
        return P == len(s)
            


