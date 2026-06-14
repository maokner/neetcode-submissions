class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in mydict:
                return [mydict[need], idx]
            mydict[num] = idx
        
        