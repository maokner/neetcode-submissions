class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for idx, num in enumerate(nums):
            if idx != 0:
                pre[idx] = pre[idx - 1] * nums[idx - 1]
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            if idx != (len(nums) - 1):
                post[idx] = post[idx + 1] * nums[idx +1]
        return [post[i] * pre[i] for i in range(len(nums))]

        