class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        trips = []
        used = set()
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if num not in used:
                target = -1 * num
                pairs = self.twoSum(nums[idx + 1:], target)
                trips.extend([num] + pairs[i] for i in range(len(pairs)))
                used.add(num)
            
        return trips
    
    def twoSum(self, nums : List[int], target) -> List[int]:
        #target = 2
        #[1, 1, 1]
        ret = []
        used = set()
        L = 0
        R = len(nums) - 1
        while L < R:
            currSum = nums[L] + nums[R]
            if currSum == target:
                if nums[L] not in used and nums[R] not in used:
                    ret.append([nums[L], nums[R]])
                used.add(nums[L])
                used.add(nums[R])
                L += 1
                R -= 1
            elif currSum >= target:
                R -= 1
            else:
                L += 1
        return ret
