class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        if nums[L] < nums[R]:
            return nums[L]
        while nums[L] >= nums[R] and ((R - L) > 1):
            mid = (L + R) // 2
            if nums[mid] > nums[L]:
                L = mid
            else:
                R = mid
        
            
        return nums[R]
