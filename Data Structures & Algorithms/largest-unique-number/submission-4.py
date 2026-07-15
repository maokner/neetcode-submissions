class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = [0 for _ in range(1001)]

        for num in nums:
            freq[num] += 1
        
        for num in range(1000, -1, -1):
            if freq[num] == 1:
                return num
        return -1

        