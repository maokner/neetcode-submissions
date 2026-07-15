class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for x in range(len(words)):
            for y in range(len(words[x])):
                if len(words) <= y:
                    return False
                if len(words[y]) <= x:
                    return False
                
                if words[x][y] != words[y][x]:
                    return False
        return True
        