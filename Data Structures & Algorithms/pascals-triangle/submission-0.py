class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        if numRows == 1:
            return ret
        # for i will have i items
        for row in range(2, numRows + 1):
            newRow = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    newRow.append(1)
                else:
                    newVal = ret[row - 2][i-1] + ret[row - 2][i]
                    newRow.append(newVal)
            ret.append(newRow)

        return ret
        