class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = [None for _ in range(len(arr))]
        ret[-1] = -1
        maxSoFar = float("-inf")
        for idx in range(len(arr) - 2, -1, -1):
            if arr[idx + 1] > maxSoFar:
                maxSoFar = arr[idx + 1]
            ret[idx] = maxSoFar
        return ret