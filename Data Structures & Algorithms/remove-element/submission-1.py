class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        for slow in range(len(nums)):
            curr = nums[slow]
            if curr == val:
                if fast <= slow:
                    fast = slow + 1
                while fast < len(nums):
                    if nums[fast] != val:
                        nums[slow], nums[fast] = nums[fast], nums[slow]
                        break
                    else:
                        fast += 1
                if fast == len(nums):
                    return slow
        return len(nums)
