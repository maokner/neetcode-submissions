class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_groups = {}
        for s in strs:
            counts = self.count_chars(s)
            cc_counts = ".".join(str(counts))
            if cc_counts not in char_groups:
                char_groups[cc_counts] = [s]
            else:
                char_groups[cc_counts].append(s)

        return [s for s in char_groups.values()]




    
    def count_chars(self, mystr):
        counts = [0] * 26
        for c in mystr:
            counts[ord(c) - ord("a")] += 1
        return counts
        