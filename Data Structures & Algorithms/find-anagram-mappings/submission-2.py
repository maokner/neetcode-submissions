class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {}
        out = [0 for _ in range(len(nums1))]

        for idx, number in enumerate(nums1):
            if number not in indices:
                indices[number] = []
            indices[number].append(idx)
        
        for idx, num in enumerate(nums2):
            for index in indices[num]:
                out[index] = idx
        
        return out
        