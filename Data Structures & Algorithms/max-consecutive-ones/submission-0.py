class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutuve = 0
        ret = 0
        for num in nums:
            if num != 1:
                consecutuve = 0
            else:
                consecutuve += 1
            ret = max(ret, consecutuve)
            
        return ret

        