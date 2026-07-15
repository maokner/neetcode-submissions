class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = {2, 3, 4, 5, 7}
        valid = {
            0: 0, 
            1:1, 
            6:9, 
            8: 8, 
            9: 6      
                    }
        n = str(n)
        c = n
        p = 0
        confusing = False
        for char in c[::-1]:
            if int(char) in invalid:
                return False
            rev = str(valid[int(char)])
            if rev != n[p]:
                confusing = True 
            p += 1
        return confusing