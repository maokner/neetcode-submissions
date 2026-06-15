class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        set_of_nums = set(nums)
        for num in nums:
            if num - 1 not in set_of_nums:
                length = 1
                while num + length in set_of_nums:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence

        