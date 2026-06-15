class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        res = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            res[counts[num]].append(num)
        ret = []
        for idx in range(len(nums), -1, -1):
            if len(ret) < k:
                ret += res[idx]
            else:
                break
        return ret
        
        