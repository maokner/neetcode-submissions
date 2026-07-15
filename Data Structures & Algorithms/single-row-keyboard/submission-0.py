class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        board = {char : idx for idx, char in enumerate(keyboard)}

        pos = 0
        time = 0

        for char in word:
            time += abs(board[char] - pos)
            pos = board[char]
        return time
        