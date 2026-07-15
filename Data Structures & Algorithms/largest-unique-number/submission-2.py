class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set()
        seen_once = set()
        currMax = -1
        for num in nums:
            if num in seen:
                if num in seen_once:
                    seen_once.remove(num)
                if num == currMax:
                    if len(seen_once) > 0:
                        currMax = max(seen_once)
                    else:
                        currMax = -1
            else:
                seen.add(num)
                seen_once.add(num)
                currMax = max(currMax, num)
        return currMax

        