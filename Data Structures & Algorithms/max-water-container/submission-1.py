class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            currMax = (R - L) * min(heights[R], heights[L])
            ret = max(currMax, ret)
            if heights[R] > heights[L]:
                L += 1
            else:
                R -= 1
        return ret
        